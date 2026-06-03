#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCREENS = ROOT / "screens"

DARK = "0xf172a"
BG = "0xf4f7fb"
CARD = "0xffffff"
BORDER = "0xd7dee8"
TEXT = "0xf172a"
MUTED = "0x64748b"
SUBTLE = "0xcbd5e1"
GREEN = "0x22c55e"
RED = "0xef4444"
SKY = "0x0ea5e9"
AMBER = "0xf59e0b"
INDIGO = "0x6366f1"
GRAY = "0x94a3b8"


def read_screen(name: str) -> str:
    raw = (SCREENS / name).read_bytes()
    encoding = "gb18030" if b"gb2312" in raw.lower() else "utf-8"
    text = raw.decode(encoding, errors="replace").replace("\x02", " ")
    return re.sub(r'/\s+([^<>]*?)>', r' \1/>', text)


def script_block(src: str) -> str:
    match = re.search(r"\s*<Script>.*?</Script>", src, re.S)
    return f"{match.group(0).strip()}\n" if match else ""


def part_by_name(src: str, name: str) -> str:
    pattern = rf'<PartInfo\b(?=[^>]*\bPartName="{re.escape(name)}")[^>]*>.*?</PartInfo>'
    match = re.search(pattern, src, re.S)
    if not match:
        raise ValueError(f"Part not found: {name}")
    return match.group(0)


def parts_by_type(src: str, part_type: str) -> list[str]:
    pattern = rf'<PartInfo\b(?=[^>]*\bPartType="{re.escape(part_type)}")[^>]*>.*?</PartInfo>'
    return re.findall(pattern, src, re.S)


def first_part_by_type(src: str, part_type: str) -> str:
    pattern = rf'<PartInfo\b(?=[^>]*\bPartType="{re.escape(part_type)}")[^>]*>.*?</PartInfo>'
    match = re.search(pattern, src, re.S)
    if not match:
        raise ValueError(f"Part type not found: {part_type}")
    return match.group(0)


def screen_no(src: str) -> str:
    match = re.search(r'<ScrInfo\b[^>]*\bScreenNo="([^"]+)"', src)
    if not match:
        raise ValueError("ScreenNo not found")
    return match.group(1)


def xml_attr(xml: str, attr: str) -> str:
    match = re.search(rf'\b{re.escape(attr)}="([^"]*)"', xml)
    return match.group(1) if match else ""


def set_attr(xml: str, tag: str, attr: str, value: str, status: str | None = None) -> str:
    if status is None:
        tag_pattern = rf"<{tag}\b[^>]*"
    else:
        tag_pattern = rf'<{tag}\b(?=[^>]*\bStatus="{re.escape(status)}")[^>]*'

    match = re.search(tag_pattern, xml)
    if not match:
        return xml

    start, end = match.span()
    tag_text = match.group(0)
    if re.search(rf'\b{re.escape(attr)}="[^"]*"', tag_text):
        tag_text = re.sub(rf'\b{re.escape(attr)}="[^"]*"', lambda _m: f'{attr}="{value}"', tag_text, count=1)
    else:
        if tag_text.endswith("/"):
            tag_text = f'{tag_text[:-1]} {attr}="{value}"/'
        else:
            tag_text = f'{tag_text} {attr}="{value}"'
    return xml[:start] + tag_text + xml[end:]


def set_attrs(xml: str, tag: str, attrs: dict[str, str], status: str | None = None) -> str:
    for key, value in attrs.items():
        xml = set_attr(xml, tag, key, value, status)
    return xml


def style_numeric(part: str, area: str, char_size: str = "304") -> str:
    part = set_attrs(
        part,
        "General",
        {
            "Area": area,
            "KbdScreen": "1000",
            "FigureFile": "",
            "BorderColor": f"{BORDER} 0",
            "FrnColor": f"{TEXT} -1",
            "BgColor": f"{CARD} -1",
            "BmpIndex": "-1",
            "Transparent": "0",
        },
    )
    return set_attrs(part, "DispFormat", {"CharSize": char_size})


def style_readout(part: str, area: str, char_size: str = "304") -> str:
    part = style_numeric(part, area, char_size)
    return set_attrs(
        part,
        "General",
        {
            "BorderColor": f"{CARD} 0",
            "BgColor": f"{CARD} -1",
            "Transparent": "0",
            "IsInput": "0",
        },
    )


def style_string(part: str, area: str, char_size: str = "233") -> str:
    return set_attrs(
        part,
        "General",
        {
            "Area": area,
            "FigureFile": "",
            "BorderColor": f"{BORDER} 0",
            "FrnColor": f"{TEXT} -1",
            "BgColor": f"{CARD} -1",
            "CharSize": char_size,
            "Transparent": "0",
        },
    )


def style_string_readout(part: str, area: str, char_size: str = "233") -> str:
    part = style_string(part, area, char_size)
    return set_attrs(
        part,
        "General",
        {
            "BorderColor": f"{CARD} 0",
            "BgColor": f"{CARD} -1",
            "Transparent": "0",
            "IsInput": "0",
        },
    )


def remove_readonly_field_border(part: str) -> str:
    general = re.search(r"<General\b[^>]*", part)
    if not general or 'IsInput="0"' not in general.group(0):
        return part

    background = xml_attr(general.group(0), "BgColor")
    background_color = background.split()[0] if background else CARD
    return set_attr(part, "General", "BorderColor", f"{background_color} 0")


def remove_all_readonly_field_borders() -> None:
    pattern = r'<PartInfo\b(?=[^>]*\bPartType="(?:Numeric|String)")[^>]*>.*?</PartInfo>'
    for path in sorted(SCREENS.glob("*.hsc")):
        src = read_screen(path.name)
        updated = re.sub(pattern, lambda match: remove_readonly_field_border(match.group(0)), src, flags=re.S)
        if updated != src:
            path.write_text(updated, encoding="utf-8")


def style_recipe_name(part: str, area: str, char_size: str = "233") -> str:
    part = style_string(part, area, char_size)
    return set_attrs(
        part,
        "General",
        {
            "BorderColor": f"{CARD} 0",
            "BgColor": f"{CARD} -1",
            "Transparent": "1",
        },
    )


def style_downlist(part: str, area: str, char_size: str = "233") -> str:
    return set_attrs(
        part,
        "General",
        {
            "Area": area,
            "FigureFile": "",
            "BorderColor": f"{BORDER} 0",
            "FrnColor": f"{TEXT} -1",
            "BgColor": f"{CARD} -1",
            "CharSize": char_size,
            "Transparent": "0",
        },
    )


def style_time(part: str, area: str, char_size: str = "233") -> str:
    return set_attrs(
        part,
        "General",
        {
            "Area": area,
            "FigureFile": "",
            "BorderColor": f"{BORDER} 0",
            "FrnColor": f"{TEXT} -1",
            "BgColor": f"{CARD} -1",
            "CharSize": char_size,
            "Transparent": "0",
        },
    )


def style_function_icon(part: str, area: str, bmp_index: str, start: str = "24 24") -> str:
    part = set_attrs(
        part,
        "General",
        {
            "Area": area,
            "FigureFile": "TFT-type style\\TFT001.pvg",
            "BorderColor": f"{CARD} 16777215",
            "FrnColor": "0x0 0",
            "BgColor": "0x0 0",
            "BmpIndex": bmp_index,
            "LaStartPt": start,
        },
    )
    return set_attrs(part, "Label", {"CharSize": "6 12", "LaFrnColor": f"{CARD} -1"}, status="0")


def style_bit_icon(part: str, area: str, bmp_index: str, start: str = "24 24") -> str:
    part = set_attrs(
        part,
        "General",
        {
            "Area": area,
            "FigureFile": "TFT-type style\\TFT001.pvg",
            "BorderColor": f"{CARD} 0",
            "BmpIndex": bmp_index,
            "LaStartPt": start,
        },
    )
    part = set_attrs(part, "Label", {"CharSize": "6 12", "LaFrnColor": f"{CARD} -1"}, status="0")
    return set_attrs(part, "Label", {"CharSize": "6 12", "LaFrnColor": f"{CARD} -1"}, status="1")


def style_bit_touch(part: str, area: str) -> str:
    part = set_attrs(
        part,
        "General",
        {
            "Area": area,
            "FigureFile": "",
            "BorderColor": f"{CARD} 0",
            "FrnColor": f"{CARD} -1",
            "BgColor": f"{CARD} -1",
            "BmpIndex": "-1",
            "Transparent": "1",
        },
    )
    part = set_attrs(part, "Label", {"CharSize": "6 12", "LaFrnColor": f"{CARD} -1"}, status="0")
    return set_attrs(part, "Label", {"CharSize": "6 12", "LaFrnColor": f"{CARD} -1"}, status="1")


def style_bit_button(part: str, area: str, color: str, off_label: str, on_label: str | None = None) -> str:
    part = set_attrs(
        part,
        "General",
        {
            "Area": area,
            "FigureFile": "TFT-type style\\TFT010.pvg",
            "BorderColor": f"{color} -1",
            "FrnColor": f"{color} -1",
            "BgColor": f"{color} -1",
            "BmpIndex": "-1",
            "LaStartPt": "36 13",
            "Align": "3",
        },
    )
    part = set_attrs(
        part,
        "Label",
        {"Pattern": "1", "FrnColor": f"{color} 1", "BgColor": f"{color} 0", "LaIndexID": off_label, "CharSize": "14", "LaFrnColor": f"{CARD} -1"},
        status="0",
    )
    if on_label is not None:
        part = set_attrs(
            part,
            "Label",
            {"Pattern": "1", "FrnColor": f"{GREEN} 0", "BgColor": f"{GREEN} 0", "LaIndexID": on_label, "CharSize": "14", "LaFrnColor": f"{CARD} -1"},
            status="1",
        )
    return part


def style_bit_switch(part: str, area: str) -> str:
    part = set_attrs(
        part,
        "General",
        {
            "Area": area,
            "FigureFile": "TFT-type style\\TFT001.pvg",
            "BorderColor": f"{CARD} 0",
            "FrnColor": f"{CARD} -1",
            "BgColor": f"{CARD} -1",
            "BmpIndex": "143",
            "LaStartPt": "0 0",
            "Align": "3",
        },
    )
    part = set_attrs(
        part,
        "Label",
        {"Pattern": "1", "FrnColor": f"{CARD} 0", "BgColor": f"{CARD} 0", "LaIndexID": "", "CharSize": "6 12", "LaFrnColor": f"{CARD} -1"},
        status="0",
    )
    return set_attrs(
        part,
        "Label",
        {"Pattern": "1", "FrnColor": f"{CARD} 0", "BgColor": f"{CARD} 0", "LaIndexID": "", "CharSize": "6 12", "LaFrnColor": f"{CARD} -1"},
        status="1",
    )


def style_word_button(part: str, area: str, color: str, start: str) -> str:
    part = set_attrs(
        part,
        "General",
        {
            "Area": area,
            "FigureFile": "TFT-type style\\TFT010.pvg",
            "BorderColor": f"{color} -1",
            "FrnColor": f"{color} -1",
            "BgColor": f"{color} -1",
            "BmpIndex": "-1",
            "Align": "3",
            "LaStartPt": start,
        },
    )
    return set_attrs(
        part,
        "Label",
        {"Pattern": "1", "FrnColor": f"{color} 0", "BgColor": f"{color} 0", "CharSize": "12 24", "LaFrnColor": f"{CARD} -1"},
        status="0",
    )


def style_word_button_label(part: str, area: str, color: str, label: str) -> str:
    part = style_word_button(part, area, color, "0 0")
    return set_attrs(
        part,
        "Label",
        {"LaIndexID": label, "CharSize": "14", "LaFrnColor": f"{CARD} -1"},
        status="0",
    )


def style_word_icon(part: str, area: str, icon: str) -> str:
    part = set_attrs(
        part,
        "General",
        {
            "Area": area,
            "FigureFile": "TFT-type style\\TFT001.pvg",
            "BorderColor": f"{BORDER} 0",
            "FrnColor": f"{CARD} -1",
            "BgColor": f"{CARD} -1",
            "BmpIndex": icon,
            "Align": "3",
            "LaStartPt": "0 0",
        },
    )
    return set_attrs(
        part,
        "Label",
        {"LaIndexID": "", "CharSize": "6 12", "LaFrnColor": f"{CARD} -1"},
        status="0",
    )


def style_key(
    part: str,
    area: str | None = None,
    label: str | None = None,
    color: str = CARD,
    text_color: str = TEXT,
    icon: str | None = None,
) -> str:
    attrs = {
        "FigureFile": "TFT-type style\\TFT001.pvg" if icon else "",
        "BorderColor": f"{BORDER} 0",
        "FrnColor": f"{color} -1",
        "BgColor": f"{color} -1",
        "BmpIndex": icon or "-1",
        "Transparent": "0",
        "Align": "3",
        "LaStartPt": "0 0",
    }
    if area is not None:
        attrs["Area"] = area
    part = set_attrs(part, "General", attrs)
    label_attrs = {
        "Pattern": "1",
        "FrnColor": f"{color} 0",
        "BgColor": f"{color} 0",
        "CharSize": "14",
        "LaFrnColor": f"{text_color} -1",
    }
    if label is not None:
        label_attrs["LaIndexID"] = label
    return set_attrs(part, "Label", label_attrs, status="0")


def style_key_icon(part: str, area: str, icon: str) -> str:
    return style_key(part, area, "", CARD, CARD, icon)


def style_header_key_icon(part: str, area: str, icon: str) -> str:
    part = style_key(part, area, "", DARK, DARK, icon)
    return set_attrs(
        part,
        "General",
        {
            "BorderColor": f"{DARK} 0",
            "FrnColor": f"{DARK} -1",
            "BgColor": f"{DARK} -1",
        },
    )


def key_parts(src: str) -> list[str]:
    return parts_by_type(src, "keystoke")


def key_by_ascii(keys: list[str], ascii_key: str) -> str:
    for key in keys:
        if 'IsCtrlKey="0"' in key and xml_attr(key, "ASCIIKey") == ascii_key:
            return key
    raise ValueError(f"Key not found: {ascii_key!r}")


def key_by_ctrl(keys: list[str], ctrl_key: str) -> str:
    for key in keys:
        if xml_attr(key, "CtrlKey") == ctrl_key:
            return key
    raise ValueError(f"Control key not found: {ctrl_key}")


def enter_key(keys: list[str]) -> str:
    for key in keys:
        if xml_attr(key, "IsCtrlKey") == "1" and not xml_attr(key, "CtrlKey"):
            return key
    raise ValueError("Enter key not found")


def style_hidden(part: str) -> str:
    part = set_attrs(
        part,
        "General",
        {
            "Area": "0 0 1 1",
            "BorderColor": f"{BG} 0",
            "FrnColor": f"{BG} 0",
            "BgColor": f"{BG} 0",
            "FigureFile": "",
            "BmpIndex": "-1",
            "Transparent": "1",
        },
    )
    for status in ("0", "1", "2", "3", "4", "5", "6"):
        part = set_attrs(
            part,
            "Label",
            {
                "LaIndexID": "",
                "FrnColor": f"{BG} 0",
                "BgColor": f"{BG} 0",
                "LaFrnColor": f"{BG} 0",
                "CharSize": "6 12",
            },
            status=status,
        )
    return part


def move_general(part: str, area: str) -> str:
    return set_attr(part, "General", "Area", area)


def rect(name: str, area: str, fill: str, border: str | None = None) -> str:
    border = border or fill
    return f'''<PartInfo PartType="Rect" PartName="{name}">
<General Area="{area}" BorderColor="{border} 0" Pattern="1" FrnColor="{fill} -1" BgColor="{fill} -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>'''


def line(name: str, start: str, end: str, color: str = BORDER) -> str:
    return f'''<PartInfo PartType="Line" PartName="{name}">
<General BorderColor="{color} 0" StartPt="{start}" EndPt="{end}" AutoAdsorption="20"/></PartInfo>'''


def bitmap(name: str, start: str, width: str, height: str, bmp_index: str) -> str:
    return f'''<PartInfo PartType="Bitmap" PartName="{name}">
<General StartPt="{start}" Width="{width}" Height="{height}" BmpIndex="{bmp_index}"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>'''


def text(name: str, content: str, point: str, size: str = "233", color: str = TEXT, bold: str = "0", bg: str = CARD) -> str:
    return f'''<PartInfo PartType="Text" PartName="{name}">
<General TextContent="{content}" LaFrnColor="{color} -1" IsBackColor="0" BgColor="{bg} 0" CharSize="{size}" Bold="{bold}" StartPt="{point}"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>'''


def function_switch(
    name: str,
    area: str,
    *,
    screen_no: str | None = None,
    popup_no: str | None = None,
    func_func: str | None = None,
    bmp_index: str = "-1",
    start: str = "0 0",
    transparent: bool = False,
    part_password: bool = False,
    lower_level: bool = False,
) -> str:
    scr_switch = "1" if screen_no is not None else "0"
    target_screen = screen_no or "-1"
    target_popup = popup_no or "-1"
    func = func_func or ("2" if popup_no is not None else "")
    func_attr = f' FuncFunc="{func}"' if func else ""
    popup_type = "1" if popup_no is not None else "0"
    popup_close_parent = "1" if popup_no is not None else "0"
    figure = "TFT-type style\\TFT001.pvg" if bmp_index != "-1" else ""
    transparent_value = "1" if transparent else "0"
    password_value = "1" if part_password else "0"
    level_value = "1" if lower_level else "0"
    level_attr = ' PartPasswordLev="1"' if lower_level or part_password else ""
    label_color = f"{CARD} -1"
    return f'''<PartInfo PartType="FunctionSwitch" PartName="{name}">
<General Desc="{name}" Area="{area}" ScrSwitch="{scr_switch}"{func_attr} ScreenNo="{target_screen}" ScreenNo2="{target_popup}" PointPos="0 0" PopupScreenType="{popup_type}" PopupCloseWithParent="{popup_close_parent}" FigureFile="{figure}" BorderColor="{CARD} 16777215" FrnColor="0x0 0" BgColor="0x0 0" BmpIndex="{bmp_index}" LaStartPt="{start}" Transparent="{transparent_value}" UseShowHide="0" HideType="0" IsHideAllTime="0"/>
<Extension Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="{password_value}" IsSetLowerLev="{level_value}"{level_attr} IsUseUserAuthority="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/>
<Label Status="0" Bold="0" CharSize="6 12" LaFrnColor="{label_color}"/></PartInfo>'''


def menu_button(area: str = "24 28 80 84", name: str = "FS_MENU_OPEN") -> str:
    return function_switch(name, area, popup_no="1003", bmp_index="140", start="12 12")


def close_popup_button(area: str = "204 20 260 76", name: str = "FS_MENU_CLOSE") -> str:
    return function_switch(name, area, func_func="8", bmp_index="128", start="12 12")


def transparent_nav(name: str, area: str, screen_no: str, *, part_password: bool = False, lower_level: bool = False) -> str:
    return function_switch(
        name,
        area,
        screen_no=screen_no,
        transparent=True,
        part_password=part_password,
        lower_level=lower_level,
    )


def header(title: str, subtitle: str, accent: str, left: str | None = None, right: str | None = None) -> list[str]:
    text_x = "92" if left else "28"
    accent_end = "204" if left else "140"
    return [
        rect("BG_0", "0 0 480 800", BG),
        rect("HEADER_BG", "0 0 480 112", DARK),
        text("TITLE_0", title, f"{text_x} 22", "304", "0xffffff", "1", DARK),
        text("SUBTITLE_0", subtitle, f"{text_x} 60", "233", SUBTLE, "0", DARK),
        rect("HEADER_ACCENT", f"{text_x} 92 {accent_end} 97", accent),
        *([left] if left else []),
        *([right] if right else []),
    ]


def footer(*parts: str) -> list[str]:
    return [
        rect("FOOTER_BG", "24 688 456 776", CARD, BORDER),
        *parts,
    ]


def drawer_item(
    index: int,
    label: str,
    subtitle: str,
    screen_no_value: str,
    icon: str,
    accent: str,
    *,
    lower_level: bool = False,
    part_password: bool = False,
) -> list[str]:
    top = 104 + index * 62
    bottom = top + 56
    slug = re.sub(r"[^A-Z0-9]+", "_", label.upper()).strip("_")
    return [
        rect(f"DRAWER_ITEM_BG_{index}", f"12 {top} 268 {bottom}", CARD, BORDER),
        rect(f"DRAWER_ITEM_ACCENT_{index}", f"12 {top} 18 {bottom}", accent),
        bitmap(f"DRAWER_ITEM_ICON_{index}", f"28 {top + 12}", "32", "32", icon),
        text(f"DRAWER_ITEM_TEXT_{index}", label, f"72 {top + 9}", "14", TEXT, "1"),
        text(f"DRAWER_ITEM_SUB_{index}", subtitle, f"72 {top + 33}", "8 16", MUTED),
        transparent_nav(
            f"FS_DRAWER_{slug}",
            f"12 {top} 268 {bottom}",
            screen_no_value,
            lower_level=lower_level,
            part_password=part_password,
        ),
    ]


def normalize_block(block: str) -> str:
    return block.replace("\r\n", "\n").replace("\r", "\n")


def write_screen(name: str, screen_no: str, blocks: list[str], script: str = "", screen_size: str = "0") -> None:
    content = "\n".join(blocks)
    (SCREENS / name).write_text(
        f'''<?xml version="1.0" encoding="UTF-8"?>
<ScrInfo ScreenNo="{screen_no}" ScreenType="" ScreenSize="{screen_size}">
{script}{content}</ScrInfo>
''',
        encoding="utf-8",
    )


def modernize_screen_1003() -> None:
    items = [
        ("Home", "Tela principal", "0", "125", GREEN, False, False),
        ("Economico", "Modo eco", "2", "142", GREEN, False, False),
        ("Temperatura", "Delta chama", "4", "141", RED, False, False),
        ("Esteira", "Calibracao", "6", "145", SKY, False, False),
        ("Receitas", "Perfis", "8", "30", AMBER, False, False),
        ("Data e Hora", "Relogio", "3", "149", INDIGO, True, False),
        ("Sistema", "Reset", "5", "150", GRAY, True, True),
        ("Offset", "Calibracao", "7", "144", GRAY, True, False),
        ("Diagnostico", "Variaveis", "30", "32", SKY, True, False),
        ("Login", "Usuario", "1011", "32", INDIGO, True, False),
        ("Manutencao", "Validade", "1009", "146", AMBER, True, True),
    ]
    blocks: list[str] = [
        rect("DRAWER_BG", "0 0 280 800", "0xe9eef6", BORDER),
        rect("DRAWER_PANEL", "0 0 280 800", CARD, BORDER),
        rect("DRAWER_HEADER", "0 0 280 96", DARK),
        text("DRAWER_TITLE", "Menu", "20 20", "304", "0xffffff", "1", DARK),
        text("DRAWER_SUBTITLE", "Navegacao", "20 58", "12 24", SUBTLE, "0", DARK),
        rect("DRAWER_ACCENT", "20 82 120 88", GREEN),
        close_popup_button(),
    ]
    for index, item in enumerate(items):
        label, subtitle, target, icon, accent, lower_level, part_password = item
        blocks.extend(
            drawer_item(
                index,
                label,
                subtitle,
                target,
                icon,
                accent,
                lower_level=lower_level,
                part_password=part_password,
            )
        )
    write_screen("1003.hsc", "1003", blocks, screen_size="1")


def modernize_screen_0() -> None:
    src = read_screen("0.hsc")
    popup_edit = part_by_name(src, "DIW_2")
    popup_eco = part_by_name(src, "DIW_1")
    recipe_name = style_string_readout(part_by_name(src, "STR_0"), "48 180 432 226", "233")
    current_temp = style_readout(part_by_name(src, "NUM_0"), "44 342 180 426", "304")
    current_temp = set_attr(current_temp, "General", "FrnColor", f"{RED} -1")
    desired_temp = style_readout(part_by_name(src, "NUM_1"), "272 342 408 426", "304")
    desired_temp = set_attr(desired_temp, "General", "FrnColor", f"{GREEN} -1")
    min_speed = style_readout(part_by_name(src, "NUM_3"), "298 570 412 642", "262")
    bake_time = style_readout(part_by_name(src, "NUM_2"), "48 570 166 642", "262")
    clock = style_time(part_by_name(src, "TIME_0"), "312 42 448 84", "304")
    clock = set_attrs(
        clock,
        "General",
        {
            "BorderColor": "0x10213a 0",
            "FrnColor": "0xffffff -1",
            "BgColor": "0x10213a -1",
        },
    )
    edit = style_bit_icon(part_by_name(src, "BS_3"), "52 696 116 760", "144", "16 16")
    eco = style_bit_icon(part_by_name(src, "BS_0"), "208 696 272 760", "123", "32 32")
    footer_recipe = function_switch("FS_FOOT_RECIPE", "364 696 428 760", screen_no="8", bmp_index="30", start="8 8")
    diagnostic = style_numeric(part_by_name(src, "Numeric Input/Display0"), "470 4 476 10", "6 12")
    diagnostic = set_attrs(
        diagnostic,
        "General",
        {
            "BorderColor": f"{DARK} 0",
            "FrnColor": f"{DARK} 0",
            "BgColor": f"{DARK} 0",
            "Transparent": "1",
        },
    )

    write_screen(
        "0.hsc",
        "0",
        [
            popup_edit,
            popup_eco,
            rect("BG_0", "0 0 480 800", BG),
            rect("HEADER_BG", "0 0 480 116", DARK),
            menu_button(),
            text("TITLE_0", "Forno Gazal", "92 22", "304", "0xffffff", "1", DARK),
            text("SUBTITLE_0", "Painel principal", "92 60", "233", SUBTLE, "0", DARK),
            rect("HEADER_ACCENT", "92 94 204 100", GREEN),
            rect("HEADER_CLOCK", "292 20 456 88", "0x10213a", "0x22324c"),
            text("TXT_CLOCK_HEAD", "Horario", "316 28", "8 16", SUBTLE, "0", "0x10213a"),
            clock,
            rect("CARD_RECIPE", "24 128 456 242", CARD, BORDER),
            rect("ACCENT_RECIPE", "24 128 30 242", AMBER),
            text("TXT_RECIPE", "Receita ativa", "48 150", "233", TEXT, "1"),
            recipe_name,
            rect("CARD_CURRENT", "24 258 228 450", CARD, BORDER),
            rect("ACCENT_CURRENT", "24 258 30 450", RED),
            bitmap("ICO_CURRENT", "48 278", "46", "46", "141"),
            text("TXT_CURRENT", "Atual", "104 278", "233", TEXT, "1"),
            text("TXT_CURRENT_SUB", "Temperatura", "104 312", "8 16", MUTED),
            current_temp,
            text("TXT_CURRENT_UNIT", "C", "184 372", "233", MUTED),
            rect("CARD_DESIRED", "252 258 456 450", CARD, BORDER),
            rect("ACCENT_DESIRED", "252 258 258 450", GREEN),
            bitmap("ICO_DESIRED", "276 278", "46", "46", "141"),
            text("TXT_DESIRED", "Desejada", "332 278", "233", TEXT, "1"),
            text("TXT_DESIRED_SUB", "Setpoint", "332 312", "8 16", MUTED),
            desired_temp,
            text("TXT_DESIRED_UNIT", "C", "412 372", "233", MUTED),
            rect("CARD_TIME", "24 470 228 676", CARD, BORDER),
            rect("ACCENT_TIME", "24 470 30 676", INDIGO),
            bitmap("ICO_TIME", "48 498", "42", "42", "139"),
            text("TXT_TIME", "Tempo", "104 498", "233", TEXT, "1"),
            bake_time,
            text("TXT_TIME_UNIT", "min", "170 595", "8 16", MUTED),
            rect("CARD_MIN", "252 470 456 676", CARD, BORDER),
            rect("ACCENT_MIN", "252 470 258 676", SKY),
            bitmap("ICO_MIN", "276 498", "42", "42", "145"),
            text("TXT_MIN", "Min. esteira", "322 498", "233", TEXT, "1"),
            min_speed,
            rect("FOOTER_BG", "24 688 456 792", CARD, BORDER),
            edit,
            text("TXT_FOOT_EDIT", "Aj. Manual", "44 764", "8 16", MUTED),
            eco,
            text("TXT_FOOT_ECO", "Eco", "226 764", "8 16", MUTED),
            footer_recipe,
            text("TXT_FOOT_RECIPE", "Receitas", "368 764", "8 16", MUTED),
            part_by_name(src, "Timer_0"),
            part_by_name(src, "Timer_1"),
            diagnostic,
        ],
        script_block(src),
    )


def modernize_screen_2() -> None:
    src = read_screen("2.hsc")
    temp = style_numeric(part_by_name(src, "Numeric Input/Display0"), "286 166 410 246", "304")
    speed = style_numeric(part_by_name(src, "NUM_0"), "286 386 410 466", "304")
    write_screen(
        "2.hsc",
        "2",
        [
            *header("Modo Economico", "Parametros de temperatura e tempo", GREEN, left=menu_button()),
            rect("CARD_TEMP", "24 132 456 300", CARD, BORDER),
            rect("ACCENT_TEMP", "24 132 30 300", GREEN),
            text("TXT_TEMP", "Temperatura eco", "48 154", "233", TEXT, "1"),
            text("TXT_TEMP_MIN", "Min: 180 C", "48 190", "8 16", MUTED),
            text("TXT_TEMP_MAX", "Max: 400 C", "48 222", "8 16", MUTED),
            temp,
            text("TXT_TEMP_UNIT", "C", "420 196", "233", MUTED),
            rect("CARD_TIME", "24 344 456 512", CARD, BORDER),
            rect("ACCENT_TIME", "24 344 30 512", SKY),
            text("TXT_TIME", "Tempo economico", "48 366", "233", TEXT, "1"),
            text("TXT_TIME_MIN", "Min: 1.30 min", "48 402", "8 16", MUTED),
            text("TXT_TIME_MAX", "Max: 9.59 min", "48 434", "8 16", MUTED),
            speed,
            text("TXT_TIME_UNIT", "min", "418 416", "12 24", MUTED),
            rect("INFO_CARD", "24 540 456 640", CARD, BORDER),
            text("TXT_INFO", "Modo eco", "48 562", "233", TEXT, "1"),
            text("TXT_INFO_SUB", "Temperatura e tempo usados no modo economico.", "48 598", "8 16", MUTED),
        ],
        script_block(src),
    )


def modernize_screen_3() -> None:
    src = read_screen("3.hsc")
    close = style_function_icon(part_by_name(src, "FS_0"), "400 28 456 84", "128", "16 16")
    message = part_by_name(src, "WL_0")
    message = set_attrs(
        message,
        "General",
        {
            "Area": "48 184 432 390",
            "FigureFile": "",
            "BorderColor": f"{CARD} 0",
            "FrnColor": f"{TEXT} -1",
            "BgColor": f"{CARD} -1",
            "BmpIndex": "-1",
            "Align": "0",
            "LaStartPt": "22 22",
        },
    )
    for status in ("0", "1", "2", "3"):
        message = set_attrs(
            message,
            "Label",
            {
                "Pattern": "1",
                "FrnColor": f"{CARD} 0",
                "BgColor": f"{CARD} 0",
                "CharSize": "8 16",
                "LaFrnColor": f"{TEXT} -1",
                "Bold": "0",
            },
            status=status,
        )
    message = set_attrs(
        message,
        "Label",
        {
            "LaIndexID": "PASSO 1 DE 4&#10;Preparar&#10;&#10;O ajuste pode ser feito com o forno quente ou frio.&#10;&#10;Deixe a esteira livre e toque em Avancar."
        },
        status="0",
    )
    message = set_attrs(
        message,
        "Label",
        {
            "LaIndexID": "PASSO 2 DE 4&#10;Posicionar objeto&#10;&#10;Coloque um objeto pequeno no inicio do tunel, no lado oposto ao painel.&#10;&#10;Depois toque em Avancar."
        },
        status="1",
    )
    message = set_attrs(
        message,
        "Label",
        {"LaIndexID": "PASSO 3 DE 4&#10;Medir percurso&#10;&#10;A esteira esta em teste.&#10;&#10;Quando o objeto sair do tunel, toque em Avancar."},
        status="2",
    )
    message = set_attrs(
        message,
        "Label",
        {"LaIndexID": "PASSO 4 DE 4&#10;Concluido&#10;&#10;Calibracao salva no parametro SPd.r.&#10;&#10;Use a seta do topo para fechar."},
        status="3",
    )
    message = set_attrs(message, "Label", {"LaFrnColor": f"{GREEN} -1", "Bold": "1"}, status="3")
    restart = style_word_button_label(part_by_name(src, "WS_1"), "48 488 210 548", GRAY, "Reiniciar")
    advance = style_word_button_label(part_by_name(src, "WS_0"), "270 488 432 548", GREEN, "Avancar")
    write_screen(
        "3.hsc",
        "31",
        [
            rect("BG_0", "0 0 480 600", BG),
            rect("HEADER_BG", "0 0 480 112", DARK),
            text("TITLE_0", "Calibrar Esteira", "92 22", "304", "0xffffff", "1", DARK),
            text("SUBTITLE_0", "Assistente de calibracao", "92 60", "12 24", SUBTLE, "0", DARK),
            rect("HEADER_ACCENT", "92 92 222 98", SKY),
            menu_button(),
            close,
            rect("CARD_STEP", "24 128 456 424", CARD, BORDER),
            rect("ACCENT_STEP", "24 128 30 424", SKY),
            text("TXT_STEP", "Assistente em 4 passos", "48 150", "233", TEXT, "1"),
            text("TXT_STEP_SUB", "Siga uma acao por vez.", "48 428", "8 16", MUTED),
            message,
            rect("FOOTER_INFO", "24 462 456 572", CARD, BORDER),
            restart,
            advance,
        ],
    )


def modernize_screen_4() -> None:
    src = read_screen("4.hsc")
    delta = style_numeric(part_by_name(src, "NUM_0"), "302 206 436 286", "304")
    write_screen(
        "4.hsc",
        "4",
        [
            *header("Temperatura", "Delta para religar a chama alta", RED, left=menu_button()),
            rect("CARD_DELTA", "24 140 456 340", CARD, BORDER),
            rect("ACCENT_DELTA", "24 140 30 340", RED),
            text("TXT_DELTA", "Delta temperatura", "48 166", "233", TEXT, "1"),
            text("TXT_DELTA_MIN", "Min: 1", "48 202", "8 16", MUTED),
            text("TXT_DELTA_MAX", "Max: 10", "48 232", "8 16", MUTED),
            text("TXT_DELTA_SUB", "Religa a chama alta.", "48 262", "8 16", MUTED),
            delta,
            rect("INFO_CARD", "24 376 456 512", CARD, BORDER),
            text("TXT_INFO", "Ajuste de chama", "48 402", "233", TEXT, "1"),
            text("TXT_INFO_SUB", "Delta menor antecipa a recuperacao.", "48 438", "8 16", MUTED),
        ],
    )


def modernize_screen_5() -> None:
    src = read_screen("5.hsc")
    alarm = style_bit_switch(part_by_name(src, "BS_1"), "336 162 432 214")
    password = style_string_readout(part_by_name(src, "STR_0"), "260 324 432 370", "233")
    reset = style_bit_button(part_by_name(src, "BS_0"), "264 520 432 580", RED, "RESET", "RESET")
    write_screen(
        "5.hsc",
        "5",
        [
            *header("Sistema", "Reset e seguranca", GRAY, left=menu_button()),
            rect("CARD_ALARM", "24 128 456 258", CARD, BORDER),
            rect("ACCENT_ALARM", "24 128 30 258", GREEN),
            text("TXT_ALARM", "Alarme do gas", "48 158", "233", TEXT, "1"),
            text("TXT_ALARM_SUB", "Liga/desliga saida.", "48 194", "8 16", MUTED),
            alarm,
            rect("CARD_PASS", "24 288 456 394", CARD, BORDER),
            rect("ACCENT_PASS", "24 288 30 394", GRAY),
            text("TXT_PASS", "Senha", "48 324", "233", TEXT, "1"),
            password,
            rect("CARD_RESET", "24 424 456 626", CARD, BORDER),
            rect("ACCENT_RESET", "24 424 30 626", RED),
            text("TXT_CAUTION", "CUIDADO", "48 450", "304", RED, "1"),
            text("TXT_RESET", "Reset de fabrica", "48 494", "233", TEXT, "1"),
            text("TXT_RESET_SUB", "Segure para resetar.", "48 530", "8 16", MUTED),
            reset,
        ],
        script_block(src),
    )


def modernize_screen_6() -> None:
    src = read_screen("6.hsc")
    start = part_by_name(src, "FS_2")
    start = set_attrs(
        start,
        "General",
        {
            "Area": "304 220 432 280",
            "FigureFile": "",
            "BorderColor": f"{GREEN} 0",
            "FrnColor": f"{GREEN} -1",
            "BgColor": f"{GREEN} -1",
            "BmpIndex": "-1",
            "LaStartPt": "0 0",
            "Align": "3",
            "Transparent": "1",
        },
    )
    start = set_attrs(start, "Label", {"LaIndexID": "", "CharSize": "6 12", "LaFrnColor": f"{CARD} -1"}, status="0")
    speed = style_numeric(part_by_name(src, "Numeric Input/Display0"), "286 420 410 500", "304")
    write_screen(
        "6.hsc",
        "6",
        [
            *header("Calibrar Esteira", "Referencia de velocidade", SKY, left=menu_button()),
            rect("CARD_START", "24 132 456 316", CARD, BORDER),
            rect("ACCENT_START", "24 132 30 316", SKY),
            text("TXT_START", "Calibracao guiada", "48 156", "233", TEXT, "1"),
            text("TXT_START_SUB", "Mede referencia da esteira.", "48 192", "8 16", MUTED),
            text("TXT_START_FLOW", "4 passos simples.", "48 246", "8 16", MUTED),
            rect("BTN_START_BG", "304 220 432 280", GREEN),
            text("TXT_START_BTN", "Iniciar", "344 238", "14", "0xffffff", "1", GREEN),
            start,
            rect("CARD_SPEED", "24 360 456 548", CARD, BORDER),
            rect("ACCENT_SPEED", "24 360 30 548", SKY),
            text("TXT_SPEED", "Referencia de velocidade", "48 388", "233", TEXT, "1"),
            text("TXT_SPEED_MIN", "Min: 0.30 min", "48 424", "8 16", MUTED),
            text("TXT_SPEED_MAX", "Max: 9.56 min", "48 454", "8 16", MUTED),
            text("TXT_SPEED_SUB", "Valor salvo no painel.", "48 496", "8 16", MUTED),
            speed,
            text("TXT_SPEED_UNIT", "min", "418 450", "12 24", MUTED),
        ],
        script_block(src),
    )


def modernize_screen_7() -> None:
    src = read_screen("7.hsc")
    save = style_bit_touch(part_by_name(src, "BS_1"), "24 586 456 746")
    timers = [
        move_general(part_by_name(src, "Timer_0"), "0 0 1 1"),
        move_general(part_by_name(src, "BS_2"), "0 0 1 1"),
    ]
    rows: list[str] = []
    row_specs = [
        (1, "WL_3", "STR_3", "WS_1", "126 190", "80 129 374 187", "27 126 378 190", "390 134 438 182"),
        (2, "WL_2", "STR_2", "WS_3", "194 258", "80 197 374 255", "27 194 378 258", "390 202 438 250"),
        (3, "WL_1", "STR_1", "WS_2", "262 326", "80 265 374 323", "27 262 378 326", "390 270 438 318"),
        (4, "WL_0", "STR_0", "WS_4", "330 394", "80 333 374 391", "27 330 378 394", "390 338 438 386"),
        (5, "WL_4", "STR_4", "WS_5", "398 462", "80 401 374 459", "27 398 378 462", "390 406 438 454"),
        (6, "WL_5", "STR_5", "WS_6", "466 530", "80 469 374 527", "27 466 378 530", "390 474 438 522"),
    ]
    for recipe_no, word_show, string, word_switch, word_area, str_area, switch_area, edit_area in row_specs:
        wl = move_general(part_by_name(src, word_show), f"27 {word_area.split()[0]} 457 {word_area.split()[1]}")
        st = style_recipe_name(part_by_name(src, string), str_area, "233")
        ws = move_general(part_by_name(src, word_switch), switch_area)
        ws = set_attrs(ws, "General", {"WordAddr": "recipe", "WriteAddr": "recipe", "Const": str(recipe_no)})
        edit_x1, edit_y1, edit_x2, edit_y2 = edit_area.split()
        ed_icon = bitmap(f"BMP_EDIT_{recipe_no}", f"{edit_x1} {edit_y1}", str(int(edit_x2) - int(edit_x1)), str(int(edit_y2) - int(edit_y1)), "127")
        ed_touch = function_switch(f"FS_EDIT_{recipe_no}", edit_area, screen_no=str(9 + recipe_no), transparent=True)
        rows.extend([normalize_block(wl), normalize_block(st), normalize_block(ws), ed_icon, ed_touch])
    write_screen(
        "7.hsc",
        "8",
        [
            *header("Receitas", "Selecionar receita ativa", AMBER, left=menu_button()),
            rect("LIST_BG", "24 120 456 546", CARD, BORDER),
            *rows,
            rect("SAVE_INFO", "24 586 456 746", CARD, BORDER),
            rect("ACCENT_SAVE", "24 586 30 746", GREEN),
            text("TXT_SAVE", "Aplicar receita", "48 620", "233", TEXT, "1"),
            text("TXT_SAVE_SUB", "Ativa o perfil selecionado no forno.", "48 654", "8 16", MUTED),
            bitmap("BMP_SAVE_ACTION", "374 634", "64", "64", "126"),
            save,
            *timers,
        ],
        script_block(src),
    )


def modernize_screen_8() -> None:
    src = read_screen("8.hsc")
    alarm = style_readout(part_by_name(src, "Numeric Input/Display0"), "302 180 426 260", "304")
    alarm = set_attr(alarm, "General", "FrnColor", "0x15803d -1")
    target = style_readout(part_by_name(src, "Numeric Input/Display1"), "302 404 426 484", "304")
    target = set_attr(target, "General", "FrnColor", "0x15803d -1")
    write_screen(
        "8.hsc",
        "30",
        [
            *header("Variaveis Teste", "Diagnostico de sinais", SKY, left=menu_button()),
            rect("CARD_ALARM", "24 132 456 308", CARD, BORDER),
            rect("ACCENT_ALARM", "24 132 30 308", SKY),
            text("TXT_ALARM", "Alarme gas", "48 162", "233", TEXT, "1"),
            text("TXT_ALARM_SUB", "Sinal de alarme acionado.", "48 198", "8 16", MUTED),
            alarm,
            rect("CARD_TARGET", "24 356 456 532", CARD, BORDER),
            rect("ACCENT_TARGET", "24 356 30 532", GREEN),
            text("TXT_TARGET", "Temperatura desejada", "48 386", "233", TEXT, "1"),
            text("TXT_TARGET_SUB", "Sinal de temperatura atingida.", "48 422", "8 16", MUTED),
            target,
            rect("INFO_CARD", "24 570 456 652", CARD, BORDER),
            text("TXT_INFO", "Tela de diagnostico", "48 590", "233", TEXT, "1"),
            text("TXT_INFO_SUB", "Somente leitura dos sinais internos.", "48 626", "8 16", MUTED),
        ],
    )


def modernize_screen_20() -> None:
    src = read_screen("20.hsc")
    password = style_string(part_by_name(src, "STR_0"), "76 318 404 394", "304")
    write_screen(
        "20.hsc",
        "20",
        [
            *header("Senha", "Codigo de acesso", GRAY, left=menu_button()),
            rect("CARD_PASSWORD", "24 176 456 464", CARD, BORDER),
            rect("ACCENT_PASSWORD", "24 176 30 464", GRAY),
            text("TXT_PASSWORD", "Sua senha", "48 208", "233", TEXT, "1"),
            text("TXT_PASSWORD_SUB", "Informe o codigo solicitado.", "48 244", "8 16", MUTED),
            password,
        ],
    )


def modernize_screen_21() -> None:
    src = read_screen("21.hsc")
    temp = style_numeric(part_by_name(src, "NUM_1"), "282 156 416 236", "304")
    temp = set_attr(temp, "General", "FrnColor", "0x0000ff -1")
    speed = style_numeric(part_by_name(src, "NUM_0"), "282 336 416 416", "304")
    minimum = style_readout(part_by_name(src, "NUM_2"), "282 524 390 586", "262")
    save = style_bit_icon(part_by_name(src, "BS_0"), "400 28 456 84", "126", "12 12")
    close = style_hidden(part_by_name(src, "Bit Switch0"))
    background = move_general(part_by_name(src, "WL_0"), "0 0 1 1")
    write_screen(
        "21.hsc",
        "21",
        [
            background,
            *header("Ajuste Manual", "Temperatura e tempo ativos", GREEN, left=menu_button(), right=save),
            rect("CARD_TEMP", "24 132 456 280", CARD, BORDER),
            rect("ACCENT_TEMP", "24 132 30 280", RED),
            text("TXT_TEMP", "Nova temperatura", "48 154", "233", TEXT, "1"),
            text("TXT_TEMP_MIN", "Min: 150 C", "48 190", "8 16", MUTED),
            text("TXT_TEMP_MAX", "Max: 400 C", "48 222", "8 16", MUTED),
            temp,
            text("TXT_TEMP_UNIT", "C", "424 186", "233", MUTED),
            rect("CARD_SPEED", "24 312 456 460", CARD, BORDER),
            rect("ACCENT_SPEED", "24 312 30 460", SKY),
            text("TXT_SPEED", "Novo tempo", "48 334", "233", TEXT, "1"),
            text("TXT_SPEED_MIN", "Min: 0.00 min", "48 370", "8 16", MUTED),
            text("TXT_SPEED_MAX", "Max: 9.99 min", "48 402", "8 16", MUTED),
            speed,
            text("TXT_SPEED_UNIT", "min", "420 366", "12 24", MUTED),
            rect("CARD_MIN", "24 492 456 620", CARD, BORDER),
            rect("ACCENT_MIN", "24 492 30 620", GRAY),
            text("TXT_MIN", "Minimo da esteira", "48 516", "233", TEXT, "1"),
            text("TXT_MIN_SUB", "Referencia atual para ajuste.", "48 552", "8 16", MUTED),
            minimum,
            text("TXT_MIN_UNIT", "min", "398 552", "12 24", MUTED, "1"),
            close,
        ],
        script_block(src),
    )


def modernize_screen_22() -> None:
    src = read_screen("22.hsc")
    temperature = style_readout(part_by_name(src, "Numeric Input/Display0"), "160 262 320 350", "304")
    temperature = set_attr(temperature, "General", "FrnColor", "0x0000ff -1")
    acknowledge = style_bit_button(part_by_name(src, "BS_0"), "292 626 432 704", RED, "Reconhecer", "Reconhecer")
    write_screen(
        "22.hsc",
        "32",
        [
            rect("BG_0", "0 0 480 800", BG),
            rect("HEADER_BG", "0 0 480 112", RED),
            menu_button(),
            text("TITLE_0", "Alerta", "92 22", "304", "0xffffff", "1", RED),
            text("SUBTITLE_0", "Queda de temperatura", "92 60", "233", "0xffffff", "0", RED),
            rect("HEADER_ACCENT", "92 92 214 97", "0xffffff"),
            bitmap("ICO_ALERT", "348 18", "72", "72", "78"),
            rect("CARD_TEMP", "24 150 456 398", CARD, BORDER),
            rect("ACCENT_TEMP", "24 150 30 398", RED),
            text("TXT_TEMP", "Temperatura atual", "48 184", "233", TEXT, "1"),
            text("TXT_TEMP_SUB", "Leitura atual do forno.", "48 220", "8 16", MUTED),
            temperature,
            text("TXT_TEMP_UNIT", "C", "330 292", "233", MUTED),
            rect("CARD_MSG", "24 430 456 548", CARD, BORDER),
            rect("ACCENT_MSG", "24 430 30 548", AMBER),
            text("TXT_MSG", "Verifique o gas", "48 462", "233", TEXT, "1"),
            text("TXT_MSG_SUB", "Corrija a causa antes de reconhecer.", "48 498", "8 16", MUTED),
            rect("CARD_ACK", "24 590 456 746", CARD, BORDER),
            rect("ACCENT_ACK", "24 590 30 746", RED),
            text("TXT_ACK", "Reconhecer alarme", "48 616", "233", TEXT, "1"),
            text("TXT_ACK_SUB", "Confirme apos verificar.", "48 652", "8 16", MUTED),
            acknowledge,
        ],
    )


def modernize_screen_23() -> None:
    src = read_screen("23.hsc")
    current = style_readout(part_by_name(src, "Numeric Input/Display0"), "282 206 416 286", "304")
    current = set_attr(current, "General", "FrnColor", "0x0000ff -1")
    desired = style_readout(part_by_name(src, "Numeric Input/Display1"), "282 430 416 510", "304")
    desired = set_attr(desired, "General", "FrnColor", "0x15803d -1")
    disable = style_bit_touch(part_by_name(src, "BS_0"), "400 28 456 84")
    for status in ("0", "1"):
        disable = set_attrs(
            disable,
            "Label",
            {
                "LaIndexID": "",
                "FrnColor": f"{DARK} 0",
                "BgColor": f"{DARK} 0",
                "LaFrnColor": f"{DARK} -1",
            },
            status=status,
        )
    header_icon = f'{bitmap("ICO_ECO_HEADER", "405 33", "46", "46", "142")}\n{disable}'
    write_screen(
        "23.hsc",
        "33",
        [
            *header("Modo Economico", "Eco ativado", GREEN, left=menu_button(), right=header_icon),
            rect("CARD_CURRENT", "24 146 456 330", CARD, BORDER),
            rect("ACCENT_CURRENT", "24 146 30 330", SKY),
            bitmap("ICO_CURRENT", "48 202", "46", "46", "123"),
            text("TXT_CURRENT", "Temperatura atual", "110 188", "233", TEXT, "1"),
            text("TXT_CURRENT_SUB", "Leitura do forno.", "110 224", "8 16", MUTED),
            current,
            text("TXT_CURRENT_UNIT", "C", "424 236", "233", MUTED),
            rect("CARD_DESIRED", "24 382 456 554", CARD, BORDER),
            rect("ACCENT_DESIRED", "24 382 30 554", GREEN),
            bitmap("ICO_DESIRED", "48 426", "46", "46", "141"),
            text("TXT_DESIRED", "Desejada", "110 410", "233", TEXT, "1"),
            text("TXT_DESIRED_SUB", "Setpoint ativo.", "110 446", "8 16", MUTED),
            desired,
            text("TXT_DESIRED_UNIT", "C", "424 460", "233", MUTED),
        ],
    )


def modernize_screen_1000() -> None:
    src = read_screen("1000.hsc")
    keys = key_parts(src)
    display = style_string(part_by_name(src, "STR_0"), "36 138 444 208", "304")
    display = set_attr(display, "General", "Align", "3")
    min_value = style_string(part_by_name(src, "STR_2"), "112 250 220 278", "14")
    min_value = set_attrs(
        min_value,
        "General",
        {
            "Align": "0",
            "BorderColor": f"{CARD} 0",
            "FrnColor": f"{RED} -1",
            "BgColor": f"{CARD} -1",
        },
    )
    max_value = style_string(part_by_name(src, "STR_1"), "322 250 430 278", "14")
    max_value = set_attrs(
        max_value,
        "General",
        {
            "Align": "0",
            "BorderColor": f"{CARD} 0",
            "FrnColor": f"{RED} -1",
            "BgColor": f"{CARD} -1",
        },
    )

    number_keys = [
        ("7", "36 318 126 392"),
        ("8", "144 318 234 392"),
        ("9", "252 318 342 392"),
        ("4", "36 408 126 482"),
        ("5", "144 408 234 482"),
        ("6", "252 408 342 482"),
        ("1", "36 498 126 572"),
        ("2", "144 498 234 572"),
        ("3", "252 498 342 572"),
        ("0", "36 588 234 662"),
        (".", "252 588 342 662"),
    ]
    back = style_header_key_icon(key_by_ctrl(keys, "3"), "24 28 80 84", "128")
    blocks = [
        *header("Teclado Numerico", "Digite o valor do parametro", SKY, left=back),
        rect("DISPLAY_CARD", "24 124 456 222", CARD, BORDER),
        display,
        rect("RANGE_CARD", "24 238 456 294", CARD, BORDER),
        text("TXT_MIN", "Min", "70 256", "8 16", MUTED, "1"),
        min_value,
        text("TXT_MAX", "Max", "280 256", "8 16", MUTED, "1"),
        max_value,
    ]
    for label, area in number_keys:
        blocks.append(style_key(key_by_ascii(keys, label), area, label))
    blocks.extend(
        [
            style_hidden(key_by_ctrl(keys, "2")),
            style_hidden(key_by_ascii(keys, "-")),
            style_key_icon(key_by_ctrl(keys, "1"), "360 318 444 392", "121"),
            style_key_icon(enter_key(keys), "360 588 444 662", "126"),
        ]
    )
    write_screen("1000.hsc", "1000", blocks, script_block(src), screen_size="1")


def text_keyboard_blocks(src: str, title: str, subtitle: str, input_name: str) -> list[str]:
    keys = key_parts(src)
    display = style_string(part_by_name(src, input_name), "24 134 456 196", "304")
    display = set_attr(display, "General", "Align", "3")
    back = style_header_key_icon(key_by_ctrl(keys, "3"), "24 28 80 84", "128")
    blocks = [
        *header(title, subtitle, INDIGO, left=back),
        rect("DISPLAY_CARD", "12 124 468 206", CARD, BORDER),
        display,
        rect("KEY_PANEL", "8 222 472 718", "0xe9eef6", BORDER),
    ]

    def add_row(chars: str, y: int, x: int, width: int, gap: int) -> None:
        for index, char in enumerate(chars):
            left = x + index * (width + gap)
            blocks.append(style_key(key_by_ascii(keys, char), f"{left} {y} {left + width} {y + 56}", char))

    add_row("1234567890", 236, 14, 40, 6)
    add_row("QWERTYUIOP", 306, 14, 40, 6)
    add_row("ASDFGHJKL", 376, 24, 42, 7)
    add_row("ZXCVBNM", 446, 58, 44, 9)
    try:
        space = key_by_ascii(keys, " ")
    except ValueError:
        space = ""
    if space:
        blocks.extend(
            [
                style_key_icon(key_by_ctrl(keys, "1"), "24 530 116 586", "121"),
                style_key_icon(space, "128 530 352 586", "129"),
                style_key_icon(enter_key(keys), "364 530 456 586", "126"),
                style_key(key_by_ctrl(keys, "2"), "80 646 400 698", "Limpar tudo"),
                bitmap("ICO_CLEAR_ALL", "104 658", "28", "28", "130"),
            ]
        )
    else:
        blocks.extend(
            [
                style_key_icon(key_by_ctrl(keys, "1"), "24 530 116 586", "121"),
                style_key_icon(enter_key(keys), "364 530 456 586", "126"),
                style_key(key_by_ctrl(keys, "2"), "80 646 400 698", "Limpar tudo"),
                bitmap("ICO_CLEAR_ALL", "104 658", "28", "28", "130"),
            ]
        )
    return blocks


def modernize_screen_1001() -> None:
    src = read_screen("1001.hsc")
    write_screen(
        "1001.hsc",
        "1001",
        text_keyboard_blocks(src, "Teclado de Texto", "Edicao de nomes e textos", "STR_0"),
    )


def modernize_screen_1002() -> None:
    src = read_screen("1002.hsc")
    timer = style_hidden(part_by_name(src, "Timer_0_Comm"))
    write_screen(
        "1002.hsc",
        "1002",
        [
            *header("Timer Interno", "Controle do alarme de gas", GRAY, left=menu_button()),
            rect("CARD_TIMER", "24 180 456 380", CARD, BORDER),
            rect("ACCENT_TIMER", "24 180 30 380", GRAY),
            text("TXT_TIMER", "Tela tecnica", "48 220", "304", TEXT, "1"),
            text("TXT_TIMER_SUB", "Timer preservado para a logica do alarme.", "48 266", "8 16", MUTED),
            text("TXT_TIMER_NOTE", "Nao possui comando manual.", "48 306", "8 16", MUTED),
            timer,
        ],
    )


def modernize_screen_1004() -> None:
    src = read_screen("1004.hsc")
    write_screen(
        "1004.hsc",
        "1004",
        text_keyboard_blocks(src, "Senha do Sistema", "Digite a senha de manutencao", "STR_0"),
    )


def modernize_screen_1006() -> None:
    src = read_screen("1006.hsc")
    ok = style_function_icon(part_by_name(src, "FS_0"), "400 28 456 84", "126", "12 12")
    rows = [
        ("NUM_0", "Ano", 126),
        ("NUM_1", "Mes", 204),
        ("NUM_2", "Dia", 282),
        ("NUM_6", "Dia da semana", 360),
        ("NUM_3", "Hora", 438),
        ("NUM_4", "Minuto", 516),
        ("NUM_5", "Segundo", 594),
    ]
    blocks = [*header("Data e Hora", "Ajuste interno do painel", INDIGO, left=menu_button(), right=ok)]
    for index, (part_name, label, top) in enumerate(rows):
        bottom = top + 62
        field = style_numeric(part_by_name(src, part_name), f"286 {top + 10} 424 {bottom - 10}", "233")
        blocks.extend(
            [
                rect(f"CARD_DT_{index}", f"24 {top} 456 {bottom}", CARD, BORDER),
                rect(f"ACCENT_DT_{index}", f"24 {top} 30 {bottom}", INDIGO),
                text(f"TXT_DT_{index}", label, f"48 {top + 19}", "233", TEXT, "1"),
                field,
            ]
        )
    blocks.append(style_hidden(part_by_name(src, "WS_0")))
    write_screen("1006.hsc", "1006", blocks)


def modernize_screen_1007() -> None:
    src = read_screen("1007.hsc")
    up = style_numeric(part_by_name(src, "Numeric Input/Display1"), "248 170 420 232", "233")
    down = style_numeric(part_by_name(src, "Numeric Input/Display0"), "248 270 420 332", "233")
    cancel = style_hidden(part_by_name(src, "Word Switch0"))
    enter = style_word_icon(part_by_name(src, "Word Switch1"), "400 28 456 84", "126")
    line_switches = [
        ("Bit Switch0", "Linha 1", "134 458 218 504", "48 470"),
        ("Bit Switch2", "Linha 3", "344 458 428 504", "246 470"),
        ("Bit Switch1", "Linha 2", "134 556 218 602", "48 568"),
        ("Bit Switch3", "Linha 4", "344 556 428 602", "246 568"),
    ]
    blocks = [
        *header("Faixa de Dados", "Periodo das tendencias", INDIGO, left=menu_button(), right=enter),
        rect("CARD_RANGE", "24 148 456 356", CARD, BORDER),
        rect("ACCENT_RANGE", "24 148 30 356", INDIGO),
        text("TXT_UP", "Inicio", "48 174", "233", TEXT, "1"),
        text("TXT_UP_SUB", "Valor superior", "48 208", "8 16", MUTED),
        up,
        text("TXT_DOWN", "Fim", "48 274", "233", TEXT, "1"),
        text("TXT_DOWN_SUB", "Valor inferior", "48 308", "8 16", MUTED),
        down,
        rect("CARD_LINES", "24 390 456 632", CARD, BORDER),
        rect("ACCENT_LINES", "24 390 30 632", SKY),
        text("TXT_LINES", "Linhas do grafico", "48 408", "233", TEXT, "1"),
    ]
    blocks.append(cancel)
    for index, (part_name, label, area, point) in enumerate(line_switches):
        blocks.extend(
            [
                text(f"TXT_LINE_{index}", label, point, "14", TEXT, "1"),
                style_bit_switch(part_by_name(src, part_name), area),
            ]
        )
    write_screen("1007.hsc", "1007", blocks, script_block(src), screen_size="1")


def modernize_screen_1008() -> None:
    src = read_screen("1008.hsc")
    keys = key_parts(src)
    display = style_string(part_by_name(src, "STR_0"), "24 134 456 196", "304")
    display = set_attr(display, "General", "Align", "3")
    caps = style_hidden(part_by_name(src, "BS_0"))

    back = style_header_key_icon(key_by_ctrl(keys, "3"), "24 28 80 84", "128")
    blocks = [
        *header("Teclado Alfanumerico", "Digite letras e numeros", INDIGO, left=back),
        rect("DISPLAY_CARD", "12 124 468 206", CARD, BORDER),
        display,
        rect("KEY_PANEL", "8 222 472 718", "0xe9eef6", BORDER),
    ]

    def add_row(chars: str, y: int, x: int, width: int, gap: int) -> None:
        for index, char in enumerate(chars):
            left = x + index * (width + gap)
            blocks.append(style_key(key_by_ascii(keys, char), f"{left} {y} {left + width} {y + 54}", char))

    add_row("1234567890", 236, 14, 40, 6)
    add_row("QWERTYUIOP", 302, 14, 40, 6)
    add_row("ASDFGHJKL", 368, 24, 42, 7)
    add_row("ZXCVBNM", 434, 58, 44, 9)
    blocks.extend(
        [
            style_key_icon(key_by_ctrl(keys, "1"), "24 530 116 586", "121"),
            style_key_icon(key_by_ascii(keys, " "), "128 530 352 586", "129"),
            style_key_icon(enter_key(keys), "364 530 456 586", "126"),
            caps,
            style_key(key_by_ctrl(keys, "2"), "80 646 400 698", "Limpar tudo"),
            bitmap("ICO_CLEAR_ALL", "104 658", "28", "28", "130"),
        ]
    )
    write_screen("1008.hsc", "1008", blocks, script_block(src))


def modernize_screen_1009() -> None:
    src = read_screen("1009.hsc")
    total = style_numeric(part_by_name(src, "NUM_1"), "290 150 420 202", "233")
    start = style_numeric(part_by_name(src, "NUM_5"), "290 220 420 272", "233")
    current = style_readout(part_by_name(src, "NUM_0"), "266 290 362 342", "233")
    admin_password = style_string(part_by_name(src, "STR_0"), "220 402 420 452", "233")
    password = style_string(part_by_name(src, "STR_1"), "220 466 420 516", "233")
    day = style_numeric(part_by_name(src, "NUM_6"), "58 610 154 662", "233")
    month = style_numeric(part_by_name(src, "NUM_4"), "192 610 288 662", "233")
    year = style_numeric(part_by_name(src, "NUM_2"), "326 610 422 662", "233")
    previous_period = style_word_icon(part_by_name(src, "WS_0"), "208 290 256 342", "128")
    next_period = style_word_icon(part_by_name(src, "WS_1"), "372 290 420 342", "151")
    save = style_word_icon(part_by_name(src, "WS_2"), "400 28 456 84", "126")
    cancel = style_hidden(part_by_name(src, "WS_3"))
    exit_button = style_hidden(part_by_name(src, "WS_4"))

    write_screen(
        "1009.hsc",
        "1009",
        [
            *header("Periodo Manutencao", "Configuracao de validade", AMBER, left=menu_button(), right=save),
            rect("CARD_PERIOD", "24 132 456 360", CARD, BORDER),
            rect("ACCENT_PERIOD", "24 132 30 360", AMBER),
            text("TXT_TOTAL", "Total de periodos", "48 160", "233", TEXT, "1"),
            total,
            text("TXT_START", "Periodo inicial", "48 230", "233", TEXT, "1"),
            start,
            text("TXT_CURRENT", "Periodo atual", "48 300", "233", TEXT, "1"),
            current,
            previous_period,
            next_period,
            rect("CARD_PASS", "24 384 456 532", CARD, BORDER),
            rect("ACCENT_PASS", "24 384 30 532", GRAY),
            text("TXT_ADMIN_PASS", "Senha superior", "48 414", "233", TEXT, "1"),
            admin_password,
            text("TXT_PASS", "Senha", "48 478", "233", TEXT, "1"),
            password,
            rect("CARD_DATE", "24 548 456 704", CARD, BORDER),
            rect("ACCENT_DATE", "24 548 30 704", SKY),
            text("TXT_DATE", "Validade", "48 572", "233", TEXT, "1"),
            day,
            month,
            year,
            text("TXT_DAY", "Dia", "58 670", "8 16", MUTED, "1"),
            text("TXT_MONTH", "Mes", "192 670", "8 16", MUTED, "1"),
            text("TXT_YEAR", "Ano", "326 670", "8 16", MUTED, "1"),
            cancel,
            exit_button,
        ],
        script_block(src),
    )


def modernize_screen_1010() -> None:
    src = read_screen("1010.hsc")
    current = style_readout(part_by_name(src, "NUM_0"), "286 168 420 230", "304")
    password = style_string(part_by_name(src, "STR_0"), "164 366 420 428", "304")
    enter = style_word_icon(part_by_name(src, "WS_0"), "400 28 456 84", "126")

    write_screen(
        "1010.hsc",
        "1010",
        [
            *header("Periodo Atual", "Validacao de manutencao", AMBER, left=menu_button(), right=enter),
            rect("CARD_PERIOD", "24 140 456 270", CARD, BORDER),
            rect("ACCENT_PERIOD", "24 140 30 270", AMBER),
            text("TXT_PERIOD", "Periodo atual", "48 174", "233", TEXT, "1"),
            current,
            rect("CARD_PASSWORD", "24 330 456 470", CARD, BORDER),
            rect("ACCENT_PASSWORD", "24 330 30 470", GRAY),
            text("TXT_PASSWORD", "Senha", "48 386", "233", TEXT, "1"),
            password,
            rect("INFO_CARD", "24 510 456 594", CARD, BORDER),
            text("TXT_INFO", "Acesso tecnico", "48 532", "233", TEXT, "1"),
            text("TXT_INFO_SUB", "Informe a senha para abrir as configuracoes.", "48 566", "8 16", MUTED),
        ],
        script_block(src),
        screen_size="1",
    )


def modernize_screen_1011() -> None:
    src = read_screen("1011.hsc")
    user_list = style_downlist(part_by_name(src, "DL_1"), "190 212 420 274", "233")
    password = style_string(part_by_name(src, "STR_0"), "190 368 420 430", "304")
    cancel = style_hidden(part_by_name(src, "FS_1"))
    ok = style_bit_icon(part_by_name(src, "BS_1"), "400 28 456 84", "126", "12 12")

    write_screen(
        "1011.hsc",
        "1011",
        [
            *header("Login", "Acesso de usuario", INDIGO, left=menu_button(), right=ok),
            rect("CARD_USER", "24 166 456 308", CARD, BORDER),
            rect("ACCENT_USER", "24 166 30 308", INDIGO),
            text("TXT_USER", "Usuario", "48 230", "233", TEXT, "1"),
            user_list,
            rect("CARD_PASSWORD", "24 338 456 470", CARD, BORDER),
            rect("ACCENT_PASSWORD", "24 338 30 470", GRAY),
            text("TXT_PASSWORD", "Senha", "48 386", "233", TEXT, "1"),
            password,
            cancel,
        ],
    )


def modernize_screen_1012() -> None:
    src = read_screen("1012.hsc")
    user = style_string_readout(part_by_name(src, "STR_1"), "210 152 420 204", "233")
    current_password = style_string(part_by_name(src, "STR_0"), "210 256 420 308", "233")
    new_password = style_string(part_by_name(src, "STR_2"), "210 360 420 412", "233")
    confirm_password = style_string(part_by_name(src, "STR_3"), "210 464 420 516", "233")
    cancel = style_hidden(part_by_name(src, "FS_0"))
    ok = style_bit_icon(part_by_name(src, "BS_1"), "400 28 456 84", "126", "12 12")

    write_screen(
        "1012.hsc",
        "1012",
        [
            *header("Alterar Senha", "Atualize o acesso do usuario", INDIGO, left=menu_button(), right=ok),
            rect("CARD_USER", "24 128 456 224", CARD, BORDER),
            rect("ACCENT_USER", "24 128 30 224", INDIGO),
            text("TXT_USER", "Usuario", "48 166", "233", TEXT, "1"),
            user,
            rect("CARD_CURRENT_PASS", "24 232 456 328", CARD, BORDER),
            rect("ACCENT_CURRENT_PASS", "24 232 30 328", GRAY),
            text("TXT_CURRENT_PASS", "Senha atual", "48 270", "233", TEXT, "1"),
            current_password,
            rect("CARD_NEW_PASS", "24 336 456 432", CARD, BORDER),
            rect("ACCENT_NEW_PASS", "24 336 30 432", GREEN),
            text("TXT_NEW_PASS", "Nova senha", "48 374", "233", TEXT, "1"),
            new_password,
            rect("CARD_CONFIRM_PASS", "24 440 456 536", CARD, BORDER),
            rect("ACCENT_CONFIRM_PASS", "24 440 30 536", GREEN),
            text("TXT_CONFIRM_PASS", "Confirmar", "48 478", "233", TEXT, "1"),
            confirm_password,
            cancel,
        ],
    )


def modernize_screen_17() -> None:
    src = read_screen("17.hsc")
    day = style_numeric(part_by_name(src, "Numeric Input/Display0"), "184 176 238 238", "262")
    month = style_numeric(part_by_name(src, "Numeric Input/Display1"), "270 176 324 238", "262")
    year = style_numeric(part_by_name(src, "Numeric Input/Display2"), "356 176 434 238", "262")
    hour = style_numeric(part_by_name(src, "Numeric Input/Display4"), "244 354 304 416", "262")
    minute = style_numeric(part_by_name(src, "Numeric Input/Display3"), "338 354 398 416", "262")
    write_screen(
        "17.hsc",
        "3",
        [
            *header("Data e Hora", "Ajuste do relogio interno", INDIGO, left=menu_button()),
            rect("CARD_DATE", "24 138 456 282", CARD, BORDER),
            rect("ACCENT_DATE", "24 138 30 282", INDIGO),
            text("TXT_DATE", "Data", "48 180", "233", TEXT, "1"),
            day,
            text("TXT_DATE_SEP1", "/", "252 194", "304", MUTED),
            month,
            text("TXT_DATE_SEP2", "/", "340 194", "304", MUTED),
            year,
            rect("CARD_TIME", "24 324 456 468", CARD, BORDER),
            rect("ACCENT_TIME", "24 324 30 468", INDIGO),
            text("TXT_TIME", "Hora", "48 366", "233", TEXT, "1"),
            hour,
            text("TXT_TIME_SEP", ":", "318 372", "304", MUTED),
            minute,
            rect("INFO_CARD", "24 506 456 606", CARD, BORDER),
            text("TXT_INFO", "Formato", "48 528", "233", TEXT, "1"),
            text("TXT_INFO_SUB", "Ajuste data e hora do relogio interno.", "48 564", "8 16", MUTED),
        ],
    )


def modernize_recipe_editor(file_name: str, recipe_no: int) -> None:
    src = read_screen(file_name)
    name = style_string(part_by_name(src, "STR_0"), "48 174 432 238", "233")
    temperature = style_numeric(part_by_name(src, "NUM_0"), "284 336 418 416", "304")
    time_value = style_numeric(part_by_name(src, "NUM_1"), "284 504 418 584", "304")
    write_screen(
        file_name,
        screen_no(src),
        [
            *header(f"Receita {recipe_no}", "Nome, temperatura e tempo", AMBER, left=menu_button()),
            rect("CARD_NAME", "24 132 456 266", CARD, BORDER),
            rect("ACCENT_NAME", "24 132 30 266", AMBER),
            text("TXT_NAME", "Nome", "48 150", "233", TEXT, "1"),
            name,
            rect("CARD_TEMP", "24 300 456 444", CARD, BORDER),
            rect("ACCENT_TEMP", "24 300 30 444", RED),
            text("TXT_TEMP", "Temperatura", "48 326", "233", TEXT, "1"),
            text("TXT_TEMP_MIN", "Min: 180 C", "48 362", "8 16", MUTED),
            text("TXT_TEMP_MAX", "Max: 400 C", "48 392", "8 16", MUTED),
            temperature,
            text("TXT_TEMP_UNIT", "C", "422 366", "233", MUTED),
            rect("CARD_TIME", "24 476 456 620", CARD, BORDER),
            rect("ACCENT_TIME", "24 476 30 620", SKY),
            text("TXT_TIME", "Tempo", "48 502", "233", TEXT, "1"),
            text("TXT_TIME_MIN", "Min: 1.00 min", "48 538", "8 16", MUTED),
            text("TXT_TIME_MAX", "Max: 9.99 min", "48 568", "8 16", MUTED),
            time_value,
            text("TXT_TIME_UNIT", "min", "420 536", "12 24", MUTED),
        ],
    )


def modernize_screen_16() -> None:
    src = read_screen("16.hsc")
    fields = [
        ("NUM_0", "Low Point", "Min: 0", "Max: 40", "124 232", "286 148 436 212"),
        ("Numeric Input/Display0", "Low Offset", "Min: -50", "Max: 50", "258 366", "286 282 436 346"),
        ("Numeric Input/Display1", "High Point", "Min: 200", "Max: 400", "392 500", "286 416 436 480"),
        ("Numeric Input/Display2", "High Offset", "Min: -500", "Max: 500", "526 634", "286 550 436 614"),
    ]
    blocks = [*header("Ajustes Offset", "Calibracao de pontos", GRAY, left=menu_button())]
    for index, (part_name, label, min_hint, max_hint, y_area, input_area) in enumerate(fields):
        top, bottom = y_area.split()
        accent = SKY if index < 2 else RED
        blocks.extend(
            [
                rect(f"CARD_OFFSET_{index}", f"24 {top} 456 {bottom}", CARD, BORDER),
                rect(f"ACCENT_OFFSET_{index}", f"24 {top} 30 {bottom}", accent),
                text(f"TXT_OFFSET_{index}", label, f"48 {int(top) + 24}", "233", TEXT, "1"),
                text(f"TXT_OFFSET_MIN_{index}", min_hint, f"48 {int(top) + 60}", "8 16", MUTED),
                text(f"TXT_OFFSET_MAX_{index}", max_hint, f"48 {int(top) + 88}", "8 16", MUTED),
                style_numeric(part_by_name(src, part_name), input_area, "304"),
            ]
        )
    write_screen("16.hsc", screen_no(src), blocks)


def main() -> None:
    modernize_screen_1003()
    modernize_screen_0()
    modernize_screen_2()
    modernize_screen_3()
    modernize_screen_4()
    modernize_screen_5()
    modernize_screen_6()
    modernize_screen_7()
    modernize_screen_8()
    modernize_screen_17()
    modernize_screen_20()
    modernize_screen_21()
    modernize_screen_22()
    modernize_screen_23()
    modernize_screen_1000()
    modernize_screen_1001()
    modernize_screen_1002()
    modernize_screen_1004()
    modernize_screen_1006()
    modernize_screen_1007()
    modernize_screen_1008()
    modernize_screen_1009()
    modernize_screen_1010()
    modernize_screen_1011()
    modernize_screen_1012()
    for recipe_no, file_name in enumerate(["10.hsc", "11.hsc", "12.hsc", "13.hsc", "14.hsc", "15.hsc"], start=1):
        modernize_recipe_editor(file_name, recipe_no)
    modernize_screen_16()
    remove_all_readonly_field_borders()


if __name__ == "__main__":
    main()
