#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import binascii
import html
import json
import mimetypes
import re
import socketserver
import struct
import sys
import zlib
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
SCREEN_DIR = ROOT / "screens"
PICTURE_XML = ROOT / "G_Picture" / "G_Picture.xml"
PICTURE_DIR = ROOT / "G_Picture" / "G_bmplib"
INVALID_XML = re.compile(r"[\x00-\x08\x0B\x0C\x0E-\x1F]")


@dataclass(frozen=True)
class Screen:
    file: str
    number: str
    title: str
    part_count: int
    html: str
    addresses: list[str]


@dataclass(frozen=True)
class PictureAsset:
    path: Path
    transparent: bool
    transparent_color: int
    status_paths: dict[str, Path]


def decode_project_xml(path: Path) -> ET.Element:
    data = path.read_bytes().replace(b"\x02", b"&#10;")
    encoding = "gb18030" if b'encoding="gb2312"' in data.lower() else "utf-8"
    text = data.decode(encoding, errors="replace")
    text = re.sub(r"<\?xml[^>]*\?>", '<?xml version="1.0"?>', text, count=1)
    text = INVALID_XML.sub("", text)
    return ET.fromstring(text)


def clean_text(value: str | None) -> str:
    if not value:
        return ""
    lines = [line.strip() for line in value.replace("\r", "").split("\n") if line.strip()]
    if not lines:
        return " ".join(value.split())
    deduped: list[str] = []
    for line in lines:
        if line not in deduped:
            deduped.append(line)
    return " ".join(deduped)


def clean_multiline(value: str | None) -> str:
    if not value:
        return ""
    lines = [line.rstrip() for line in value.replace("\r", "").split("\n")]
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines)


def labels_by_status(part: ET.Element) -> dict[str, str]:
    labels: dict[str, str] = {}
    for label in part.findall("Label"):
        status = label.get("Status") or "0"
        text = clean_multiline(label.get("LaIndexID"))
        if text:
            labels[status] = text
    return labels


def color(value: str | None, fallback: str = "transparent") -> str:
    if not value:
        return fallback
    token = value.split()[0]
    if not token.startswith("0x"):
        return fallback
    try:
        return f"#{int(token, 16) & 0xFFFFFF:06x}"
    except ValueError:
        return fallback


def area(value: str | None) -> tuple[int, int, int, int]:
    if not value:
        return 0, 0, 80, 32
    try:
        x1, y1, x2, y2 = [int(float(part)) for part in value.split()[:4]]
        return x1, y1, max(1, x2 - x1), max(1, y2 - y1)
    except (ValueError, IndexError):
        return 0, 0, 80, 32


def point(value: str | None) -> tuple[int, int]:
    if not value:
        return 0, 0
    try:
        x, y = [int(float(part)) for part in value.split()[:2]]
        return x, y
    except (ValueError, IndexError):
        return 0, 0


def font_size(value: str | None, box_height: int | None = None) -> int:
    if box_height:
        return max(12, min(42, int(box_height * 0.42)))
    if not value:
        return 16
    try:
        first = int(str(value).split()[0])
    except (ValueError, IndexError):
        return 16
    if first >= 298:
        return 22
    if first >= 230:
        return 17
    if first >= 100:
        return 14
    return 16


def load_image_map() -> dict[str, PictureAsset]:
    root = ET.parse(PICTURE_XML).getroot()
    images: dict[str, PictureAsset] = {}
    for item in root.findall(".//G_bmp"):
        image_id = item.get("nId")
        if not image_id:
            continue
        transparent = item.get("bTransparent") == "1"
        try:
            transparent_color = int(item.get("cTransColor") or "0") & 0xFFFFFF
        except ValueError:
            transparent_color = 0
        status_paths: dict[str, Path] = {}
        for status in item.findall("MulStatus"):
            status_name = status.get("szFilename") or ""
            status_id = status.get("dwMID") or ""
            for candidate_name in (status_name, status_name.strip()):
                if not candidate_name:
                    continue
                candidate = PICTURE_DIR / candidate_name
                if candidate.is_file():
                    status_paths[status_id] = candidate
                    break

        filenames = [item.get("szFilename") or ""]
        filenames.extend(status.get("szFilename") or "" for status in item.findall("MulStatus"))
        primary_path: Path | None = None
        for filename in filenames:
            for candidate_name in (filename, filename.strip()):
                if not candidate_name:
                    continue
                candidate = PICTURE_DIR / candidate_name
                if candidate.is_file():
                    primary_path = candidate
                    break
            if primary_path is not None:
                break

        if primary_path is not None:
            images[image_id] = PictureAsset(primary_path, transparent, transparent_color, status_paths)
    return images


IMAGE_MAP = load_image_map()


def png_chunk(kind: bytes, data: bytes) -> bytes:
    return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", binascii.crc32(kind + data) & 0xFFFFFFFF)


def bmp_with_transparency_to_png(body: bytes, transparent_color: int) -> bytes:
    if body[:2] != b"BM":
        return body
    pixel_offset = struct.unpack_from("<I", body, 10)[0]
    dib_size = struct.unpack_from("<I", body, 14)[0]
    if dib_size < 40:
        return body
    width = struct.unpack_from("<i", body, 18)[0]
    height_raw = struct.unpack_from("<i", body, 22)[0]
    planes = struct.unpack_from("<H", body, 26)[0]
    bits_per_pixel = struct.unpack_from("<H", body, 28)[0]
    compression = struct.unpack_from("<I", body, 30)[0]
    if planes != 1 or bits_per_pixel != 24 or compression != 0 or width <= 0 or height_raw == 0:
        return body

    top_down = height_raw < 0
    height = abs(height_raw)
    row_stride = ((width * 3 + 3) // 4) * 4
    trans_r = transparent_color & 0xFF
    trans_g = (transparent_color >> 8) & 0xFF
    trans_b = (transparent_color >> 16) & 0xFF
    rows: list[bytes] = []

    for y in range(height):
        source_y = y if top_down else height - 1 - y
        row_start = pixel_offset + source_y * row_stride
        row = bytearray()
        row.append(0)
        for x in range(width):
            offset = row_start + x * 3
            blue = body[offset]
            green = body[offset + 1]
            red = body[offset + 2]
            alpha = 0 if (red, green, blue) == (trans_r, trans_g, trans_b) else 255
            row.extend((red, green, blue, alpha))
        rows.append(bytes(row))

    png_body = b"".join(
        [
            b"\x89PNG\r\n\x1a\n",
            png_chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 6, 0, 0, 0)),
            png_chunk(b"IDAT", zlib.compress(b"".join(rows), 9)),
            png_chunk(b"IEND", b""),
        ]
    )
    return png_body


def style_from_box(x: int, y: int, width: int, height: int, extra: str = "") -> str:
    return (
        f"left:{x}px;top:{y}px;width:{width}px;height:{height}px;"
        f"{extra}"
    )


def attrs(**items: str | int | None) -> str:
    result = []
    for key, value in items.items():
        if value is None:
            continue
        result.append(f'{key.replace("_", "-")}="{html.escape(str(value), quote=True)}"')
    return " ".join(result)


def collect_dir_show_targets(root: ET.Element, screen_number_map: dict[str, str]) -> dict[str, str]:
    targets: dict[str, str] = {}
    for part in root.iter("PartInfo"):
        if part.get("PartType") != "DirShow":
            continue
        general = part.find("General")
        if general is None:
            continue
        trigger = general.get("TriggAddr")
        screen_number = general.get("ScreenNo")
        target = screen_number_map.get(screen_number or "")
        if trigger and target:
            targets[trigger] = target
    return targets


def render_screen(root: ET.Element, screen_file: str, screen_number_map: dict[str, str]) -> tuple[str, list[str], str]:
    output: list[str] = []
    addresses: list[str] = []
    texts: list[str] = []
    bit_targets = collect_dir_show_targets(root, screen_number_map)
    z_index = 1

    def add_address(value: str | None) -> None:
        if value and value not in addresses:
            addresses.append(value)

    def emit(markup: str) -> None:
        output.append(markup)

    def walk(node: ET.Element) -> None:
        nonlocal z_index
        for part in node.findall("PartInfo"):
            part_type = part.get("PartType") or ""
            general = part.find("General")
            if general is not None:
                for key in ("WordAddr", "WriteAddr", "OperateAddr", "MonitorAddr", "TriggAddr", "BitAddr", "SetAddr"):
                    add_address(general.get(key))

                if part_type in {"Rect", "Circle"} and general.get("Area"):
                    x, y, width, height = area(general.get("Area"))
                    radius = "50%" if part_type == "Circle" else "0"
                    emit(
                        '<div class="shape" '
                        + attrs(
                            style=style_from_box(
                                x,
                                y,
                                width,
                                height,
                                (
                                    f"background:{color(general.get('BgColor') or general.get('FrnColor'), 'transparent')};"
                                    f"border:1px solid {color(general.get('BorderColor'), '#888')};"
                                    f"border-radius:{radius};z-index:{z_index};"
                                ),
                            )
                        )
                        + "></div>"
                    )
                    z_index += 1

                if part_type == "Line" and general.get("Area"):
                    x, y, width, height = area(general.get("Area"))
                    emit(
                        '<div class="line" '
                        + attrs(
                            style=style_from_box(
                                x,
                                y,
                                width,
                                max(2, height),
                                f"background:{color(general.get('BorderColor'), '#666')};z-index:{z_index};",
                            )
                        )
                        + "></div>"
                    )
                    z_index += 1

                if part_type == "Bitmap":
                    image_id = general.get("BmpIndex")
                    if image_id in IMAGE_MAP:
                        x, y = point(general.get("StartPt"))
                        width = int(float(general.get("Width") or 50))
                        height = int(float(general.get("Height") or 50))
                        emit(
                            '<img class="bitmap" '
                            + attrs(
                                src=f"/asset/{image_id}",
                                style=style_from_box(x, y, width, height, f"z-index:{z_index};"),
                                alt="",
                            )
                            + ">"
                        )
                        z_index += 1

                if part_type in {"WordShow", "FunctionSwitch", "BitSwitch", "WordSwitch"} and general.get("Area"):
                    x, y, width, height = area(general.get("Area"))
                    image_id = general.get("BmpIndex")
                    labels = labels_by_status(part)
                    did_emit_control = False
                    if image_id in IMAGE_MAP:
                        emit(
                            '<img class="bitmap control-image' + (" word-show-image" if part_type == "WordShow" else "") + '" '
                            + attrs(
                                src=f"/asset/{image_id}",
                                style=style_from_box(x, y, width, height, f"z-index:{z_index};"),
                                data_addr=general.get("WordAddr") if part_type == "WordShow" else None,
                                data_const=general.get("Const") if part_type == "WordShow" else None,
                                data_image_id=image_id if part_type == "WordShow" else None,
                                alt="",
                            )
                            + ">"
                        )
                        did_emit_control = True
                    elif part_type == "WordShow" and labels:
                        label = part.find("Label")
                        emit(
                            '<div class="word-show" '
                            + attrs(
                                style=style_from_box(
                                    x,
                                    y,
                                    width,
                                    height,
                                    (
                                        f"border:1px solid {color(general.get('BorderColor'), '#ccd0d5')};"
                                        f"color:{color(general.get('FrnColor'), '#111')};"
                                        f"background:{color(general.get('BgColor'), '#fff')};"
                                        f"font-size:{font_size(label.get('CharSize') if label is not None else general.get('CharSize'))}px;"
                                        f"z-index:{z_index};"
                                    ),
                                ),
                                data_addr=general.get("WordAddr") or "",
                                data_labels=json.dumps(labels, ensure_ascii=False),
                                title=f"WordShow: {general.get('WordAddr') or ''}",
                            )
                            + f">{html.escape(labels.get('0') or next(iter(labels.values())))}</div>"
                        )
                        did_emit_control = True
                    elif part_type in {"WordSwitch", "BitSwitch"} and labels:
                        label_text = labels.get("0") or next(iter(labels.values()))
                        label = part.find("Label")
                        emit(
                            '<button class="switch-button" '
                            + attrs(
                                style=style_from_box(
                                    x,
                                    y,
                                    width,
                                    height,
                                    (
                                        f"border:1px solid {color(general.get('BorderColor'), '#ccd0d5')};"
                                        f"color:{color(label.get('LaFrnColor') if label is not None else None, '#fff')};"
                                        f"background:{color(general.get('BgColor') or general.get('FrnColor'), '#fff')};"
                                        f"font-size:{font_size(label.get('CharSize') if label is not None else general.get('CharSize'))}px;"
                                        f"z-index:{z_index};"
                                    ),
                                ),
                                type="button",
                                title=f"{part_type}: {general.get('WriteAddr') or general.get('WordAddr') or general.get('OperateAddr') or ''}",
                            )
                            + f">{html.escape(label_text)}</button>"
                        )
                        did_emit_control = True
                    elif part_type == "FunctionSwitch" and general.get("Transparent") != "1":
                        emit(
                            '<div class="control-placeholder" '
                            + attrs(style=style_from_box(x, y, width, height, f"z-index:{z_index};"))
                            + "></div>"
                        )
                        did_emit_control = True
                    if did_emit_control:
                        z_index += 1

                if part_type == "keystoke" and general.get("Area"):
                    x, y, width, height = area(general.get("Area"))
                    if general.get("Transparent") == "1" and width <= 1 and height <= 1:
                        continue
                    image_id = general.get("BmpIndex")
                    labels = labels_by_status(part)
                    label_text = labels.get("0") or ""
                    key = part.find("Key")
                    if not label_text and key is not None:
                        ctrl = key.get("CtrlKey")
                        if ctrl == "1":
                            label_text = "Apagar caractere"
                        elif ctrl == "2":
                            label_text = "Limpar tudo"
                        elif ctrl == "3":
                            label_text = "Voltar"
                        elif key.get("ASCIIKey") == " ":
                            label_text = "Espaco"
                        else:
                            label_text = key.get("ASCIIKey") or "Tecla"
                    label = part.find("Label")
                    if image_id in IMAGE_MAP:
                        content = f'<img src="/asset/{html.escape(image_id, quote=True)}" alt="{html.escape(label_text, quote=True)}">'
                    else:
                        content = html.escape(label_text)
                    emit(
                        '<button class="key-button' + (" icon-key" if image_id in IMAGE_MAP else "") + '" '
                        + attrs(
                            style=style_from_box(
                                x,
                                y,
                                width,
                                height,
                                (
                                    f"border:1px solid {color(general.get('BorderColor'), '#ccd0d5')};"
                                    f"color:{color(label.get('LaFrnColor') if label is not None else None, '#111')};"
                                    f"background:{color(general.get('BgColor') or general.get('FrnColor'), '#fff')};"
                                    f"font-size:{font_size(label.get('CharSize') if label is not None else general.get('CharSize'), height)}px;"
                                    f"z-index:{z_index};"
                                ),
                            ),
                            type="button",
                            title=f"Tecla: {label_text}",
                        )
                        + f">{content}</button>"
                    )
                    z_index += 1

                if part_type in {"Numeric", "String", "DownList"} and general.get("Area"):
                    x, y, width, height = area(general.get("Area"))
                    read_addr = general.get("WordAddr") or ""
                    write_addr = general.get("WriteAddr") or read_addr
                    field_type = "String" if part_type == "DownList" else part_type
                    initial = "000" if part_type == "Numeric" else clean_text(general.get("Remark")) or write_addr or "Texto"
                    class_name = "field numeric-field" if part_type == "Numeric" else "field string-field"
                    is_transparent = general.get("Transparent") == "1"
                    emit(
                        f'<button class="{class_name}" '
                        + attrs(
                            style=style_from_box(
                                x,
                                y,
                                width,
                                height,
                                (
                                    f"border:1px solid {'transparent' if is_transparent else color(general.get('BorderColor'), '#ccd0d5')};"
                                    f"color:{color(general.get('FrnColor'), '#111')};"
                                    f"background:{'transparent' if is_transparent else color(general.get('BgColor'), '#fff')};"
                                    f"font-size:{font_size(general.get('CharSize'), height)}px;"
                                    f"z-index:{z_index};"
                                ),
                            ),
                            data_addr=write_addr,
                            data_type=field_type,
                            title=f"{part_type}: {write_addr}",
                        )
                        + f"><span>{html.escape(initial)}</span></button>"
                    )
                    z_index += 1

                if part_type == "TimeDisplay" and general.get("Area"):
                    x, y, width, height = area(general.get("Area"))
                    emit(
                        '<div class="field time-field" '
                        + attrs(
                            style=style_from_box(
                                x,
                                y,
                                width,
                                height,
                                (
                                    f"border:1px solid {color(general.get('BorderColor'), '#ccd0d5')};"
                                    f"color:{color(general.get('FrnColor'), '#111')};"
                                    f"background:{color(general.get('BgColor'), '#fff')};"
                                    f"font-size:{font_size(general.get('CharSize'), height)}px;"
                                    f"z-index:{z_index};"
                                ),
                            ),
                            data_type="TimeDisplay",
                            title="TimeDisplay",
                        )
                        + "><span>00:00</span></div>"
                    )
                    z_index += 1

                text = clean_text(general.get("TextContent"))
                if part_type == "Text" and text:
                    texts.append(text)
                    x, y = point(general.get("StartPt"))
                    emit(
                        '<div class="text" '
                        + attrs(
                            style=(
                                f"left:{x}px;top:{y}px;color:{color(general.get('LaFrnColor'), '#111')};"
                                f"font-size:{font_size(general.get('CharSize'))}px;z-index:{z_index};"
                            )
                        )
                        + f">{html.escape(text)}</div>"
                    )
                    z_index += 1

                target_file = None
                title = ""
                action = None
                if part_type == "FunctionSwitch":
                    if general.get("FuncFunc") == "2":
                        target_file = screen_number_map.get(general.get("ScreenNo2") or "")
                        title = f"Abrir popup {general.get('ScreenNo2')}"
                        if target_file:
                            action = f"openPopup({json.dumps(target_file)})"
                    elif general.get("FuncFunc") == "8":
                        title = "Fechar popup"
                        action = "closePopup()"
                    else:
                        target_file = screen_number_map.get(general.get("ScreenNo") or "")
                        title = f"Ir para tela {general.get('ScreenNo')}"
                elif part_type == "BitSwitch":
                    addr = general.get("OperateAddr") or general.get("MonitorAddr") or ""
                    target_file = bit_targets.get(addr)
                    title = f"{addr} -> {target_file}" if target_file else f"Alternar {addr}"
                elif part_type == "WordSwitch":
                    addr = general.get("WriteAddr") or general.get("WordAddr") or ""
                    title = f"WordSwitch {addr}"

                if part_type in {"FunctionSwitch", "BitSwitch", "WordSwitch"} and general.get("Area"):
                    x, y, width, height = area(general.get("Area"))
                    if action:
                        pass
                    elif target_file:
                        action = f"goToScreen({json.dumps(target_file)})"
                    elif part_type == "WordSwitch":
                        action = "wordSwitch(" + ",".join(
                            [
                                json.dumps(general.get("WriteAddr") or general.get("WordAddr") or ""),
                                json.dumps(general.get("WordFunc") or ""),
                                json.dumps(general.get("Const") or ""),
                                json.dumps(general.get("Limit") or ""),
                            ]
                        ) + ")"
                    else:
                        action = f"toggleBit({json.dumps(general.get('OperateAddr') or general.get('MonitorAddr') or '')})"
                    emit(
                        '<button class="hotspot" '
                        + attrs(
                            style=style_from_box(x, y, width, height, "z-index:1000;"),
                            title=title,
                            onclick=action,
                        )
                        + "></button>"
                    )

            walk(part)

    walk(root)
    title = next((text for text in texts if len(text) <= 60), "") or f"Tela {root.get('ScreenNo') or screen_file}"
    return "\n".join(output), addresses, title


def load_screens() -> list[Screen]:
    parsed: list[tuple[str, ET.Element, int]] = []
    for path in sorted(SCREEN_DIR.glob("*.hsc"), key=lambda item: int(item.stem) if item.stem.isdigit() else item.stem):
        root = decode_project_xml(path)
        parsed.append((path.name, root, sum(1 for _ in root.iter("PartInfo"))))

    screen_number_map: dict[str, str] = {}
    for filename, root, part_count in parsed:
        number = root.get("ScreenNo") or Path(filename).stem
        current = screen_number_map.get(number)
        if current is None:
            screen_number_map[number] = filename
            continue
        current_parts = next(count for name, _, count in parsed if name == current)
        if part_count > current_parts:
            screen_number_map[number] = filename

    screens: list[Screen] = []
    for filename, root, part_count in parsed:
        body, addresses, title = render_screen(root, filename, screen_number_map)
        screens.append(
            Screen(
                file=filename,
                number=root.get("ScreenNo") or Path(filename).stem,
                title=title,
                part_count=part_count,
                html=body,
                addresses=addresses,
            )
        )
    return screens


def render_app() -> bytes:
    screens = load_screens()
    data = {
        screen.file: {
            "file": screen.file,
            "number": screen.number,
            "title": screen.title,
            "partCount": screen.part_count,
            "html": screen.html,
            "addresses": screen.addresses,
        }
        for screen in screens
    }
    first = "0.hsc" if "0.hsc" in data else screens[0].file
    payload = json.dumps(data, ensure_ascii=False)
    markup = f"""<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>IHM Gazal Preview</title>
  <style>
    :root {{
      color-scheme: light;
      --bg: #202124;
      --panel: #f7f7f7;
      --line: #d0d3d7;
      --text: #1f2328;
      --muted: #667085;
      --active: #0b77d5;
    }}
    * {{ box-sizing: border-box; }}
    html {{
      height: 100%;
      overflow: hidden;
    }}
    body {{
      margin: 0;
      height: 100vh;
      min-height: 0;
      overflow: hidden;
      background: var(--bg);
      color: var(--text);
      font-family: Arial, Helvetica, sans-serif;
      display: grid;
      grid-template-columns: 280px minmax(520px, 1fr) 280px;
    }}
    aside, .inspector {{
      background: #ffffff;
      border-right: 1px solid var(--line);
      height: 100vh;
      min-height: 0;
    }}
    aside {{
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }}
    .inspector {{
      border-left: 1px solid var(--line);
      border-right: 0;
      overflow: auto;
    }}
    .panel-header {{
      padding: 14px 16px;
      border-bottom: 1px solid var(--line);
      position: sticky;
      top: 0;
      background: #fff;
      z-index: 20;
      flex: 0 0 auto;
    }}
    h1, h2 {{
      margin: 0;
      font-size: 16px;
      line-height: 1.2;
    }}
    .panel-header p {{
      margin: 4px 0 0;
      color: var(--muted);
      font-size: 12px;
    }}
    .screen-list {{
      display: flex;
      flex-direction: column;
      flex: 1 1 auto;
      min-height: 0;
      overflow-y: auto;
      overscroll-behavior: contain;
      padding: 8px;
      gap: 4px;
    }}
    .screen-button {{
      appearance: none;
      border: 1px solid transparent;
      background: transparent;
      color: var(--text);
      text-align: left;
      border-radius: 6px;
      padding: 8px;
      cursor: pointer;
      display: grid;
      gap: 2px;
    }}
    .screen-button:hover {{ background: #eef6ff; }}
    .screen-button.active {{
      border-color: #7ab7f5;
      background: #e8f3ff;
    }}
    .screen-button strong {{
      font-size: 13px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}
    .screen-button span {{
      color: var(--muted);
      font-size: 11px;
    }}
    main {{
      min-width: 0;
      height: 100vh;
      min-height: 0;
      padding: 16px;
      overflow: auto;
    }}
    .toolbar {{
      max-width: 520px;
      margin: 0 auto 12px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      color: #fff;
      gap: 8px;
    }}
    .toolbar-title {{
      min-width: 0;
    }}
    .toolbar-title strong {{
      display: block;
      font-size: 15px;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }}
    .toolbar-title span {{
      color: #c9d1d9;
      font-size: 12px;
    }}
    .toolbar-actions {{
      display: flex;
      gap: 8px;
      flex-shrink: 0;
    }}
    .toolbar button, .inspector button {{
      border: 1px solid #bec7d2;
      background: #fff;
      color: #111;
      border-radius: 6px;
      padding: 7px 10px;
      font-weight: 700;
      cursor: pointer;
    }}
    .screen-frame {{
      margin: 0 auto;
      position: relative;
    }}
    .screen-shell {{
      width: 480px;
      height: 800px;
      background: #f4f4f4;
      position: relative;
      overflow: hidden;
      transform-origin: top left;
      box-shadow: 0 18px 48px rgba(0,0,0,.45);
    }}
    .popup-layer {{
      position: absolute;
      inset: 0;
      width: 480px;
      height: 800px;
      pointer-events: none;
      z-index: 3000;
    }}
    .popup-layer.active {{
      pointer-events: auto;
    }}
    .popup-layer .hotspot {{
      z-index: 5000 !important;
    }}
    .shape, .line, .text, .field, .bitmap, .control-placeholder, .word-show, .switch-button, .key-button, .hotspot {{
      position: absolute;
      box-sizing: border-box;
    }}
    .bitmap {{
      object-fit: fill;
      pointer-events: none;
    }}
    .word-show-image.selected-word-show {{
      outline: 2px solid #0ea5e9;
      outline-offset: -2px;
    }}
    .text {{
      font-weight: 700;
      white-space: nowrap;
      pointer-events: none;
    }}
    .field {{
      border: 1px solid #ccd0d5;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      line-height: 1;
      cursor: pointer;
      overflow: hidden;
    }}
    .control-placeholder {{
      border: 1px dashed #8a8f98;
      background: rgba(255,255,255,.2);
    }}
    .word-show {{
      padding: 18px 22px;
      line-height: 1.24;
      white-space: pre-line;
      overflow: hidden;
      font-weight: 700;
      display: flex;
      align-items: flex-start;
      justify-content: flex-start;
    }}
    .switch-button {{
      padding: 0 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      line-height: 1;
      font-weight: 800;
      cursor: pointer;
      overflow: hidden;
    }}
    .key-button {{
      padding: 0 4px;
      display: flex;
      align-items: center;
      justify-content: center;
      line-height: 1;
      font-weight: 800;
      cursor: default;
      overflow: hidden;
      border-radius: 4px;
    }}
    .key-button img {{
      width: auto;
      height: 72%;
      max-width: 72%;
      object-fit: contain;
      pointer-events: none;
    }}
    .hotspot {{
      opacity: 0;
      border: 2px solid transparent;
      background: rgba(11, 119, 213, .1);
      cursor: pointer;
      padding: 0;
    }}
    body.show-hotspots .hotspot {{
      opacity: 1;
      border-color: rgba(11,119,213,.75);
    }}
    .hotspot:hover {{
      opacity: 1;
      border-color: #0b77d5;
      background: rgba(11,119,213,.18);
    }}
    .inspector-section {{
      padding: 12px 16px;
      border-bottom: 1px solid var(--line);
    }}
    .inspector-section h2 {{
      font-size: 13px;
      margin-bottom: 8px;
    }}
    .register-list {{
      list-style: none;
      padding: 0;
      margin: 0;
      display: grid;
      gap: 4px;
      font-size: 12px;
    }}
    .register-list li {{
      display: flex;
      justify-content: space-between;
      gap: 8px;
      border: 1px solid #e1e4e8;
      padding: 5px 6px;
      border-radius: 4px;
    }}
    .register-list code {{
      color: #475467;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }}
    .register-list span {{
      font-weight: 700;
    }}
    @media (max-width: 1100px) {{
      body {{ grid-template-columns: 210px minmax(0, 1fr); }}
      .inspector {{ display: none; }}
      main {{ padding: 10px; }}
      .toolbar {{ max-width: 100%; }}
    }}
    @media (max-width: 720px) {{
      body {{ grid-template-columns: 160px minmax(0, 1fr); }}
      .screen-list {{ padding: 6px; }}
      .screen-button {{ padding: 7px 6px; }}
      .screen-button strong {{ font-size: 12px; }}
      .screen-button span {{ font-size: 10px; }}
      .toolbar {{ align-items: flex-start; flex-direction: column; }}
    }}
  </style>
</head>
<body>
  <aside>
    <div class="panel-header">
      <h1>IHM Gazal</h1>
      <p>{len(screens)} telas carregadas</p>
    </div>
    <div class="screen-list" id="screenList"></div>
  </aside>
  <main>
    <div class="toolbar">
      <div class="toolbar-title">
        <strong id="activeTitle"></strong>
        <span id="activeMeta"></span>
      </div>
      <div class="toolbar-actions">
        <button type="button" id="hotspotButton">Hotspots</button>
        <button type="button" onclick="window.print()">Print</button>
      </div>
    </div>
    <div class="screen-frame" id="screenFrame">
      <div class="screen-shell" id="screenShell"></div>
    </div>
  </main>
  <section class="inspector">
    <div class="panel-header">
      <h1>Estado</h1>
      <p>Valores simulados no navegador</p>
    </div>
    <div class="inspector-section">
      <h2>Registradores da tela</h2>
      <ul class="register-list" id="registerList"></ul>
    </div>
    <div class="inspector-section">
      <button type="button" onclick="resetRegisters()">Resetar valores</button>
    </div>
  </section>
  <script>
    const SCREENS = {payload};
    const FIRST_SCREEN = {json.dumps(first)};
    const registers = Object.create(null);
    let activePopup = null;

    function initialValue(addr, type) {{
      if (!addr) return type === 'String' ? '' : '0';
      if (addr === 'recipe' && registers[addr] === undefined) registers[addr] = '1';
      if (registers[addr] === undefined) registers[addr] = type === 'String' ? addr : '0';
      return registers[addr];
    }}

    function currentScreenFromHash() {{
      const raw = decodeURIComponent(location.hash.replace(/^#/, ''));
      return SCREENS[raw] ? raw : FIRST_SCREEN;
    }}

    function goToScreen(file) {{
      if (!SCREENS[file]) return;
      activePopup = null;
      location.hash = encodeURIComponent(file);
      renderScreen(file);
    }}

    function openPopup(file) {{
      if (!SCREENS[file]) return;
      activePopup = file;
      renderPopup();
    }}

    function closePopup() {{
      activePopup = null;
      renderPopup();
    }}

    function editValue(event, addr, type) {{
      event.stopPropagation();
      if (!addr) return;
      const current = initialValue(addr, type);
      const next = prompt(addr, current);
      if (next === null) return;
      registers[addr] = next;
      renderScreen(currentScreenFromHash());
    }}

    function toggleBit(addr) {{
      if (!addr) return;
      registers[addr] = registers[addr] === '1' ? '0' : '1';
      renderInspector(currentScreenFromHash());
    }}

    function wordSwitch(addr, func, constant, limit) {{
      if (!addr) return;
      const current = Number(registers[addr] ?? '0') || 0;
      const step = Number(constant || '1') || 1;
      const max = Number(limit || '');
      let next = func === '1' ? current + step : Number(constant || '0') || 0;
      if (Number.isFinite(max) && max > 0) next = Math.min(next, max);
      registers[addr] = String(next);
      if (addr === 'HDW100') {{
        const recipeByMask = {{ '1': '1', '2': '2', '4': '3', '8': '4', '16': '5', '32': '6' }};
        if (recipeByMask[String(next)]) registers.recipe = recipeByMask[String(next)];
      }}
      renderScreen(currentScreenFromHash());
    }}

    function resetRegisters() {{
      for (const key of Object.keys(registers)) delete registers[key];
      renderScreen(currentScreenFromHash());
    }}

    window.goToScreen = goToScreen;
    window.openPopup = openPopup;
    window.closePopup = closePopup;
    window.toggleBit = toggleBit;
    window.wordSwitch = wordSwitch;
    window.resetRegisters = resetRegisters;

    function renderScreenList(active) {{
      const list = document.getElementById('screenList');
      list.innerHTML = '';
      for (const screen of Object.values(SCREENS)) {{
        const button = document.createElement('button');
        button.type = 'button';
        button.className = 'screen-button' + (screen.file === active ? ' active' : '');
        button.onclick = () => goToScreen(screen.file);
        button.innerHTML = `<strong>${{screen.file}} - ${{screen.title}}</strong><span>ScreenNo ${{screen.number}} / ${{screen.partCount}} partes</span>`;
        list.appendChild(button);
      }}
    }}

    function bindFields(shell) {{
      for (const field of shell.querySelectorAll('.field')) {{
        const addr = field.dataset.addr || '';
        const type = field.dataset.type || 'Numeric';
        if (type === 'TimeDisplay') {{
          field.querySelector('span').textContent = new Date().toLocaleTimeString('pt-BR', {{ hour: '2-digit', minute: '2-digit' }});
          field.onclick = null;
          continue;
        }}
        const value = initialValue(addr, type);
        field.querySelector('span').textContent = type === 'String' ? value : String(value).padStart(3, '0').slice(-6);
        field.onclick = event => editValue(event, addr, type);
      }}
    }}

    function bindWordShows(shell) {{
      for (const wordShow of shell.querySelectorAll('.word-show')) {{
        const addr = wordShow.dataset.addr || '';
        let labels = {{}};
        try {{
          labels = JSON.parse(wordShow.dataset.labels || '{{}}');
        }} catch {{
          labels = {{}};
        }}
        const value = initialValue(addr, 'Numeric');
        wordShow.textContent = labels[value] || labels[String(Number(value) || 0)] || labels['0'] || wordShow.textContent;
      }}
      for (const wordShow of shell.querySelectorAll('.word-show-image')) {{
        const addr = wordShow.dataset.addr || '';
        const imageId = wordShow.dataset.imageId || '';
        if (!addr || !imageId) continue;
        const value = String(Number(initialValue(addr, 'Numeric')) || 0);
        wordShow.src = `/asset/${{encodeURIComponent(imageId)}}?status=${{encodeURIComponent(value)}}`;
        wordShow.classList.toggle('selected-word-show', wordShow.dataset.const === value);
      }}
    }}

    function renderInspector(file) {{
      const screen = SCREENS[file];
      const list = document.getElementById('registerList');
      list.innerHTML = '';
      if (!screen.addresses.length) {{
        list.innerHTML = '<li><code>Nenhum endereco</code><span>-</span></li>';
        return;
      }}
      for (const addr of screen.addresses) {{
        const li = document.createElement('li');
        li.innerHTML = `<code>${{addr}}</code><span>${{registers[addr] ?? '-'}}</span>`;
        list.appendChild(li);
      }}
    }}

    function renderScreen(file) {{
      const screen = SCREENS[file] || SCREENS[FIRST_SCREEN];
      document.getElementById('activeTitle').textContent = `${{screen.file}} - ${{screen.title}}`;
      document.getElementById('activeMeta').textContent = `ScreenNo ${{screen.number}} / ${{screen.partCount}} partes`;
      const shell = document.getElementById('screenShell');
      shell.innerHTML = screen.html + '<div class="popup-layer" id="popupLayer"></div>';
      bindFields(shell);
      bindWordShows(shell);
      renderPopup();
      renderScreenList(screen.file);
      renderInspector(screen.file);
      fitScreen();
    }}

    function renderPopup() {{
      const layer = document.getElementById('popupLayer');
      if (!layer) return;
      if (!activePopup || !SCREENS[activePopup]) {{
        layer.classList.remove('active');
        layer.innerHTML = '';
        return;
      }}
      layer.classList.add('active');
      layer.innerHTML = SCREENS[activePopup].html;
      bindFields(layer);
      bindWordShows(layer);
    }}

    function fitScreen() {{
      const main = document.querySelector('main');
      const frame = document.getElementById('screenFrame');
      const shell = document.getElementById('screenShell');
      const available = Math.max(240, main.clientWidth - 20);
      const scale = Math.min(1, Math.max(0.42, available / 500));
      frame.style.width = `${{480 * scale}}px`;
      frame.style.height = `${{800 * scale}}px`;
      shell.style.transform = `scale(${{scale}})`;
    }}

    document.getElementById('hotspotButton').onclick = () => {{
      document.body.classList.toggle('show-hotspots');
    }};
    window.addEventListener('resize', fitScreen);
    window.addEventListener('hashchange', () => renderScreen(currentScreenFromHash()));
    renderScreen(currentScreenFromHash());
  </script>
</body>
</html>
"""
    return markup.encode("utf-8")


class PreviewHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path in {"/", "/index.html"}:
            body = render_app()
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        if parsed.path == "/favicon.ico":
            self.send_response(HTTPStatus.NO_CONTENT)
            self.end_headers()
            return

        if parsed.path.startswith("/asset/"):
            image_id = unquote(parsed.path.removeprefix("/asset/"))
            asset = IMAGE_MAP.get(image_id)
            if not asset or not asset.path.is_file():
                self.send_error(HTTPStatus.NOT_FOUND)
                return
            params = parse_qs(parsed.query)
            status = (params.get("status") or [""])[0]
            image_path = asset.status_paths.get(status, asset.path)
            body = image_path.read_bytes()
            if asset.transparent:
                body = bmp_with_transparency_to_png(body, asset.transparent_color)
                content_type = "image/png"
            else:
                content_type = mimetypes.guess_type(image_path.name)[0] or "image/bmp"
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", content_type)
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        self.send_error(HTTPStatus.NOT_FOUND)

    def log_message(self, format: str, *args: object) -> None:
        sys.stderr.write("%s - %s\n" % (self.address_string(), format % args))


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a local browser preview for the WECON HMI project.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", default=8123, type=int)
    args = parser.parse_args()

    class ReusableTCPServer(socketserver.TCPServer):
        allow_reuse_address = True

    with ReusableTCPServer((args.host, args.port), PreviewHandler) as httpd:
        print(f"Serving HMI preview on http://{args.host}:{args.port}/", flush=True)
        httpd.serve_forever()


if __name__ == "__main__":
    main()
