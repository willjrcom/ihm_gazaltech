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
            "FigureFile": "",
            "BorderColor": f"{BORDER} 0",
            "FrnColor": f"{TEXT} -1",
            "BgColor": f"{CARD} -1",
            "BmpIndex": "-1",
            "Transparent": "0",
        },
    )
    return set_attrs(part, "DispFormat", {"CharSize": char_size})


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
    return set_attrs(
        part,
        "General",
        {
            "Area": "0 0 1 1",
            "BorderColor": f"{BG} 0",
            "FrnColor": f"{BG} 0",
            "BgColor": f"{BG} 0",
            "Transparent": "1",
        },
    )


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


def header(title: str, subtitle: str, accent: str) -> list[str]:
    return [
        rect("BG_0", "0 0 480 800", BG),
        rect("HEADER_BG", "0 0 480 112", DARK),
        text("TITLE_0", title, "28 22", "304", "0xffffff", "1", DARK),
        text("SUBTITLE_0", subtitle, "28 60", "233", SUBTLE, "0", DARK),
        rect("HEADER_ACCENT", "28 92 140 97", accent),
    ]


def footer(*parts: str) -> list[str]:
    return [
        rect("FOOTER_BG", "24 688 456 776", CARD, BORDER),
        *parts,
    ]


def write_screen(name: str, screen_no: str, blocks: list[str], script: str = "", screen_size: str = "0") -> None:
    content = "\n".join(blocks)
    (SCREENS / name).write_text(
        f'''<?xml version="1.0" encoding="UTF-8"?>
<ScrInfo ScreenNo="{screen_no}" ScreenType="" ScreenSize="{screen_size}">
{script}{content}</ScrInfo>
''',
        encoding="utf-8",
    )


def modernize_screen_0() -> None:
    src = read_screen("0.hsc")
    popup_edit = part_by_name(src, "DIW_2")
    popup_eco = part_by_name(src, "DIW_1")
    recipe = style_function_icon(part_by_name(src, "FS_0"), "384 158 444 218", "30", "30 30")
    recipe_name = style_string(part_by_name(src, "STR_0"), "48 180 360 226", "233")
    current_temp = style_numeric(part_by_name(src, "NUM_0"), "44 342 180 426", "304")
    current_temp = set_attr(current_temp, "General", "FrnColor", f"{RED} -1")
    desired_temp = style_numeric(part_by_name(src, "NUM_1"), "272 342 408 426", "304")
    desired_temp = set_attr(desired_temp, "General", "FrnColor", f"{GREEN} -1")
    min_speed = style_numeric(part_by_name(src, "NUM_3"), "298 570 412 642", "262")
    bake_time = style_numeric(part_by_name(src, "NUM_2"), "48 570 166 642", "262")
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
    edit = style_bit_icon(part_by_name(src, "BS_3"), "52 704 116 768", "127", "24 24")
    eco = style_bit_icon(part_by_name(src, "BS_0"), "208 704 272 768", "123", "32 32")
    menu = style_function_icon(part_by_name(src, "FS_1"), "364 704 428 768", "140", "32 32")
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
            text("TITLE_0", "Forno Gazal", "28 22", "304", "0xffffff", "1", DARK),
            text("SUBTITLE_0", "Painel principal", "28 60", "233", SUBTLE, "0", DARK),
            rect("HEADER_ACCENT", "28 94 166 100", GREEN),
            rect("HEADER_CLOCK", "292 20 456 88", "0x10213a", "0x22324c"),
            text("TXT_CLOCK_HEAD", "Horario", "316 28", "8 16", SUBTLE, "0", "0x10213a"),
            clock,
            rect("CARD_RECIPE", "24 128 456 242", CARD, BORDER),
            rect("ACCENT_RECIPE", "24 128 30 242", AMBER),
            text("TXT_RECIPE", "Receita ativa", "48 150", "233", TEXT, "1"),
            recipe_name,
            recipe,
            text("TXT_RECIPE_BTN", "Receitas", "382 222", "8 16", MUTED),
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
            text("TXT_MIN", "Minimo", "332 498", "233", TEXT, "1"),
            min_speed,
            rect("FOOTER_BG", "24 688 456 784", CARD, BORDER),
            edit,
            text("TXT_FOOT_EDIT", "Editar", "58 766", "8 16", MUTED),
            eco,
            text("TXT_FOOT_ECO", "Eco", "226 766", "8 16", MUTED),
            menu,
            text("TXT_FOOT_MENU", "Menu", "380 766", "8 16", MUTED),
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
    home = style_function_icon(part_by_name(src, "FS_0"), "208 704 272 768", "125", "32 32")
    back = style_function_icon(part_by_name(src, "FS_2"), "48 704 112 768", "128", "24 24")
    write_screen(
        "2.hsc",
        "2",
        [
            *header("Modo Economico", "Parametros de temperatura e tempo", GREEN),
            rect("CARD_TEMP", "24 132 456 300", CARD, BORDER),
            rect("ACCENT_TEMP", "24 132 30 300", GREEN),
            text("TXT_TEMP", "Temperatura eco", "48 154", "233", TEXT, "1"),
            text("TXT_TEMP_HINT", "Valores entre 180 e 400", "48 190", "12 24", MUTED),
            temp,
            text("TXT_TEMP_UNIT", "C", "420 196", "233", MUTED),
            rect("CARD_TIME", "24 344 456 512", CARD, BORDER),
            rect("ACCENT_TIME", "24 344 30 512", SKY),
            text("TXT_TIME", "Tempo economico", "48 366", "233", TEXT, "1"),
            text("TXT_TIME_HINT", "Valores entre 1.30 e 9.59 min", "48 402", "12 24", MUTED),
            speed,
            text("TXT_TIME_UNIT", "min", "418 416", "12 24", MUTED),
            rect("INFO_CARD", "24 540 456 640", CARD, BORDER),
            text("TXT_INFO", "Modo eco", "48 562", "233", TEXT, "1"),
            text("TXT_INFO_SUB", "Temperatura e tempo usados no modo economico.", "48 598", "8 16", MUTED),
            *footer(back, home),
        ],
        script_block(src),
    )


def modernize_screen_3() -> None:
    src = read_screen("3.hsc")
    close = style_function_icon(part_by_name(src, "FS_0"), "392 20 448 76", "128", "28 28")
    message = part_by_name(src, "WL_0")
    message = set_attrs(
        message,
        "General",
        {
            "Area": "58 170 422 418",
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
            {"Pattern": "1", "FrnColor": f"{CARD} 0", "BgColor": f"{CARD} 0", "CharSize": "12 24", "LaFrnColor": f"{TEXT} -1"},
            status=status,
        )
    message = set_attrs(
        message,
        "Label",
        {"LaIndexID": "OBSERVACAO&#10;&#10;O ajuste do tempo da esteira pode ser feito com o forno quente ou frio.&#10;&#10;Pressione Avancar para iniciar o teste."},
        status="0",
    )
    message = set_attrs(
        message,
        "Label",
        {"LaIndexID": "ETAPA 1&#10;&#10;Coloque um objeto pequeno no inicio do tunel, no lado oposto ao painel.&#10;&#10;Pressione Avancar."},
        status="1",
    )
    message = set_attrs(
        message,
        "Label",
        {"LaIndexID": "ETAPA 2&#10;&#10;A esteira esta em teste.&#10;&#10;Quando o objeto atravessar todo o tunel, pressione Avancar."},
        status="2",
    )
    message = set_attrs(
        message,
        "Label",
        {"LaIndexID": "ETAPA 3&#10;&#10;Calibracao realizada com sucesso.&#10;&#10;O valor foi salvo no parametro SPd.r. Pode fechar a tela."},
        status="3",
    )
    message = set_attrs(message, "Label", {"LaFrnColor": f"{GREEN} -1"}, status="3")
    restart = style_word_button(part_by_name(src, "WS_1"), "58 476 214 546", GRAY, "36 22")
    advance = style_word_button(part_by_name(src, "WS_0"), "266 476 422 546", GREEN, "42 22")
    write_screen(
        "3.hsc",
        "31",
        [
            rect("BG_0", "0 0 480 600", BG),
            rect("PANEL", "10 8 470 590", CARD, BORDER),
            rect("HEADER_BG", "10 8 470 96", DARK),
            text("TITLE_0", "Calibrar Esteira", "34 28", "304", "0xffffff", "1", DARK),
            text("SUBTITLE_0", "Assistente de calibracao", "34 64", "12 24", SUBTLE, "0", DARK),
            rect("HEADER_ACCENT", "34 84 164 90", SKY),
            close,
            rect("CARD_STEP", "34 116 446 434", CARD, BORDER),
            rect("ACCENT_STEP", "34 116 40 434", SKY),
            text("TXT_STEP", "Etapas do assistente", "58 136", "233", TEXT, "1"),
            message,
            rect("FOOTER_INFO", "34 448 446 564", CARD, BORDER),
            restart,
            advance,
        ],
    )


def modernize_screen_4() -> None:
    src = read_screen("4.hsc")
    delta = style_numeric(part_by_name(src, "NUM_0"), "302 206 436 286", "304")
    home = style_function_icon(part_by_name(src, "FS_0"), "208 704 272 768", "125", "32 32")
    back = style_function_icon(part_by_name(src, "FS_1"), "48 704 112 768", "128", "24 24")
    write_screen(
        "4.hsc",
        "4",
        [
            *header("Temperatura", "Delta para religar a chama alta", RED),
            rect("CARD_DELTA", "24 140 456 340", CARD, BORDER),
            rect("ACCENT_DELTA", "24 140 30 340", RED),
            text("TXT_DELTA", "Delta temperatura", "48 166", "233", TEXT, "1"),
            text("TXT_DELTA_HINT", "Valores entre 1 e 10", "48 202", "12 24", MUTED),
            text("TXT_DELTA_SUB", "Religa a chama alta.", "48 228", "8 16", MUTED),
            delta,
            rect("INFO_CARD", "24 376 456 512", CARD, BORDER),
            text("TXT_INFO", "Ajuste de chama", "48 402", "233", TEXT, "1"),
            text("TXT_INFO_SUB", "Delta menor antecipa a recuperacao.", "48 438", "8 16", MUTED),
            *footer(back, home),
        ],
    )


def modernize_screen_5() -> None:
    src = read_screen("5.hsc")
    back = style_function_icon(part_by_name(src, "FS_1"), "48 704 112 768", "128", "24 24")
    home = style_function_icon(part_by_name(src, "Function Switch1"), "208 704 272 768", "125", "32 32")
    reset = style_bit_button(part_by_name(src, "BS_0"), "264 226 432 286", RED, "RESET", "RESET")
    password = style_string(part_by_name(src, "STR_0"), "260 384 432 430", "233")
    alarm = style_bit_button(part_by_name(src, "BS_1"), "264 516 432 576", GREEN, "ON/OFF", "ON/OFF")
    write_screen(
        "5.hsc",
        "5",
        [
            *header("Sistema", "Reset e seguranca", GRAY),
            rect("CARD_RESET", "24 128 456 320", CARD, BORDER),
            rect("ACCENT_RESET", "24 128 30 320", RED),
            text("TXT_CAUTION", "CUIDADO", "48 154", "304", RED, "1"),
            text("TXT_RESET", "Reset de fabrica", "48 198", "233", TEXT, "1"),
            text("TXT_RESET_SUB", "Segure para resetar.", "48 234", "8 16", MUTED),
            reset,
            rect("CARD_PASS", "24 350 456 456", CARD, BORDER),
            rect("ACCENT_PASS", "24 350 30 456", GRAY),
            text("TXT_PASS", "Senha", "48 386", "233", TEXT, "1"),
            password,
            rect("CARD_ALARM", "24 486 456 606", CARD, BORDER),
            rect("ACCENT_ALARM", "24 486 30 606", GREEN),
            text("TXT_ALARM", "Alarme do gas", "48 516", "233", TEXT, "1"),
            text("TXT_ALARM_SUB", "Liga/desliga saida.", "48 552", "8 16", MUTED),
            alarm,
            *footer(back, home),
        ],
        script_block(src),
    )


def modernize_screen_6() -> None:
    src = read_screen("6.hsc")
    back = style_function_icon(part_by_name(src, "Function Switch2"), "48 704 112 768", "128", "24 24")
    home = style_function_icon(part_by_name(src, "Function Switch3"), "208 704 272 768", "125", "32 32")
    start = part_by_name(src, "FS_2")
    start = set_attrs(
        start,
        "General",
        {
            "Area": "48 154 198 216",
            "FigureFile": "TFT-type style\\TFT010.pvg",
            "BorderColor": f"{SKY} -1",
            "Pattern": "1",
            "FrnColor": f"{SKY} -1",
            "BgColor": f"{SKY} -1",
            "BmpIndex": "-1",
            "LaStartPt": "42 18",
            "Align": "3",
        },
    )
    start = set_attrs(start, "Label", {"LaIndexID": "Iniciar", "CharSize": "12 24", "LaFrnColor": "0xffffff -1"}, status="0")
    speed = style_numeric(part_by_name(src, "Numeric Input/Display0"), "286 330 410 410", "304")
    write_screen(
        "6.hsc",
        "6",
        [
            *header("Calibrar Esteira", "Referencia de velocidade", SKY),
            rect("CARD_START", "24 132 456 250", CARD, BORDER),
            rect("ACCENT_START", "24 132 30 250", SKY),
            text("TXT_START", "Assistente de calibracao", "220 156", "233", TEXT, "1"),
            text("TXT_START_SUB", "Abra o popup de ajuste.", "220 192", "8 16", MUTED),
            start,
            rect("CARD_SPEED", "24 292 456 460", CARD, BORDER),
            rect("ACCENT_SPEED", "24 292 30 460", SKY),
            text("TXT_SPEED", "Referencia de velocidade", "48 318", "233", TEXT, "1"),
            text("TXT_SPEED_HINT", "Valores entre 0.30 e 9.56", "48 354", "12 24", MUTED),
            speed,
            text("TXT_SPEED_UNIT", "min", "418 360", "12 24", MUTED),
            *footer(back, home),
        ],
        script_block(src),
    )


def modernize_screen_7() -> None:
    src = read_screen("7.hsc")
    home = style_function_icon(part_by_name(src, "Function Switch0"), "208 704 272 768", "125", "32 32")
    save = style_bit_icon(part_by_name(src, "BS_1"), "368 704 432 768", "126", "24 24")
    timers = [part_by_name(src, "Timer_0"), move_general(part_by_name(src, "BS_2"), "0 0 1 1")]
    rows: list[str] = []
    row_specs = [
        ("WL_3", "STR_3", "WS_1", "BS_0", 1, "126 190", "80 129 374 187", "25 126 455 190", "390 134 438 182"),
        ("WL_2", "STR_2", "WS_3", "BS_3", 2, "194 258", "80 197 374 255", "27 194 457 258", "390 202 438 250"),
        ("WL_1", "STR_1", "WS_2", "BS_4", 3, "262 326", "80 265 374 323", "27 262 457 326", "390 270 438 318"),
        ("WL_0", "STR_0", "WS_4", "BS_5", 4, "330 394", "80 333 374 391", "27 330 457 394", "390 338 438 386"),
        ("WL_4", "STR_4", "WS_5", "BS_6", 5, "398 462", "80 401 374 459", "27 398 457 462", "390 406 438 454"),
        ("WL_5", "STR_5", "WS_6", "BS_7", 6, "466 530", "80 469 374 527", "27 466 457 530", "390 474 438 522"),
    ]
    for word_show, string, word_switch, edit, _row, word_area, str_area, switch_area, edit_area in row_specs:
        wl = move_general(part_by_name(src, word_show), f"27 {word_area.split()[0]} 457 {word_area.split()[1]}")
        st = style_string(part_by_name(src, string), str_area, "233")
        ws = move_general(part_by_name(src, word_switch), switch_area)
        ed = style_bit_icon(part_by_name(src, edit), edit_area, "127", "24 24")
        rows.extend([wl, st, ws, ed])
    write_screen(
        "7.hsc",
        "7",
        [
            *header("Receitas", "Selecionar e editar perfis", AMBER),
            rect("LIST_BG", "24 120 456 556", CARD, BORDER),
            *rows,
            rect("SAVE_INFO", "24 596 456 674", CARD, BORDER),
            rect("ACCENT_SAVE", "24 596 30 674", GREEN),
            text("TXT_SAVE", "Salvar alteracoes", "48 614", "233", TEXT, "1"),
            text("TXT_SAVE_SUB", "Botao verde grava os nomes.", "48 648", "8 16", MUTED),
            *timers,
            *footer(home, save),
        ],
        script_block(src),
    )


def modernize_screen_8() -> None:
    src = read_screen("8.hsc")
    home = style_function_icon(part_by_name(src, "Function Switch0"), "208 704 272 768", "125", "32 32")
    back = style_function_icon(part_by_name(src, "Function Switch1"), "48 704 112 768", "128", "24 24")
    alarm = style_numeric(part_by_name(src, "Numeric Input/Display0"), "302 180 426 260", "304")
    alarm = set_attr(alarm, "General", "FrnColor", "0x15803d -1")
    target = style_numeric(part_by_name(src, "Numeric Input/Display1"), "302 404 426 484", "304")
    target = set_attr(target, "General", "FrnColor", "0x15803d -1")
    write_screen(
        "8.hsc",
        "8",
        [
            *header("Variaveis Teste", "Diagnostico de sinais", SKY),
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
            *footer(back, home),
        ],
    )


def modernize_screen_20() -> None:
    src = read_screen("20.hsc")
    home = style_function_icon(part_by_name(src, "FS_0"), "208 704 272 768", "125", "32 32")
    password = style_string(part_by_name(src, "STR_0"), "76 318 404 394", "304")
    write_screen(
        "20.hsc",
        "20",
        [
            *header("Senha", "Codigo de acesso", GRAY),
            rect("CARD_PASSWORD", "24 176 456 464", CARD, BORDER),
            rect("ACCENT_PASSWORD", "24 176 30 464", GRAY),
            text("TXT_PASSWORD", "Sua senha", "48 208", "233", TEXT, "1"),
            text("TXT_PASSWORD_SUB", "Informe o codigo solicitado.", "48 244", "8 16", MUTED),
            password,
            *footer(home),
        ],
    )


def modernize_screen_21() -> None:
    src = read_screen("21.hsc")
    temp = style_numeric(part_by_name(src, "NUM_1"), "282 156 416 236", "304")
    temp = set_attr(temp, "General", "FrnColor", "0x0000ff -1")
    speed = style_numeric(part_by_name(src, "NUM_0"), "282 336 416 416", "304")
    minimum = style_numeric(part_by_name(src, "NUM_2"), "300 492 388 544", "233")
    save = style_bit_button(part_by_name(src, "BS_0"), "278 608 432 672", GREEN, "Confirmar", "Aguarde")
    close = style_bit_icon(part_by_name(src, "Bit Switch0"), "392 24 448 80", "128", "28 28")
    background = move_general(part_by_name(src, "WL_0"), "0 0 1 1")
    write_screen(
        "21.hsc",
        "21",
        [
            background,
            rect("BG_0", "0 0 480 800", BG),
            rect("HEADER_BG", "0 0 480 112", DARK),
            text("TITLE_0", "Editar Setpoint", "28 22", "304", "0xffffff", "1", DARK),
            text("SUBTITLE_0", "Temperatura e tempo ativos", "28 60", "233", SUBTLE, "0", DARK),
            rect("HEADER_ACCENT", "28 92 150 97", GREEN),
            close,
            rect("CARD_TEMP", "24 132 456 280", CARD, BORDER),
            rect("ACCENT_TEMP", "24 132 30 280", RED),
            text("TXT_TEMP", "Nova temperatura", "48 154", "233", TEXT, "1"),
            text("TXT_TEMP_SUB", "Setpoint atual do forno.", "48 190", "8 16", MUTED),
            temp,
            text("TXT_TEMP_UNIT", "C", "424 186", "233", MUTED),
            rect("CARD_SPEED", "24 312 456 460", CARD, BORDER),
            rect("ACCENT_SPEED", "24 312 30 460", SKY),
            text("TXT_SPEED", "Novo tempo", "48 334", "233", TEXT, "1"),
            text("TXT_SPEED_SUB", "Velocidade da esteira.", "48 370", "8 16", MUTED),
            speed,
            text("TXT_SPEED_UNIT", "min", "420 366", "12 24", MUTED),
            rect("CARD_MIN", "24 492 456 564", CARD, BORDER),
            rect("ACCENT_MIN", "24 492 30 564", GRAY),
            text("TXT_MIN", "Minimo", "48 514", "233", TEXT, "1"),
            minimum,
            rect("ACTION_CARD", "24 588 456 700", CARD, BORDER),
            text("TXT_ACTION", "Gravar ajuste", "48 616", "233", TEXT, "1"),
            text("TXT_ACTION_SUB", "Confirma os valores ativos.", "48 650", "8 16", MUTED),
            save,
        ],
        script_block(src),
    )


def modernize_screen_22() -> None:
    src = read_screen("22.hsc")
    temperature = style_numeric(part_by_name(src, "Numeric Input/Display0"), "156 276 318 364", "304")
    temperature = set_attr(temperature, "General", "FrnColor", "0x0000ff -1")
    close = style_bit_button(part_by_name(src, "BS_0"), "158 626 322 690", RED, "Fechar", "Fechar")
    write_screen(
        "22.hsc",
        "9",
        [
            rect("BG_0", "0 0 480 800", BG),
            rect("HEADER_BG", "0 0 480 112", RED),
            text("TITLE_0", "Alerta", "28 22", "304", "0xffffff", "1", RED),
            text("SUBTITLE_0", "Queda de temperatura", "28 60", "233", "0xffffff", "0", RED),
            rect("HEADER_ACCENT", "28 92 150 97", "0xffffff"),
            bitmap("ICO_ALERT", "360 26", "56", "56", "124"),
            rect("CARD_TEMP", "24 164 456 428", CARD, BORDER),
            rect("ACCENT_TEMP", "24 164 30 428", RED),
            text("TXT_TEMP", "Temperatura atual", "48 194", "233", TEXT, "1"),
            temperature,
            text("TXT_TEMP_UNIT", "C", "326 306", "233", MUTED),
            rect("CARD_MSG", "24 468 456 574", CARD, BORDER),
            rect("ACCENT_MSG", "24 468 30 574", GREEN),
            text("TXT_MSG", "Verifique o gas", "48 496", "233", TEXT, "1"),
            text("TXT_MSG_SUB", "Reconheca o alarme para fechar.", "48 532", "8 16", MUTED),
            close,
        ],
    )


def modernize_screen_23() -> None:
    src = read_screen("23.hsc")
    current = style_numeric(part_by_name(src, "Numeric Input/Display0"), "282 206 416 286", "304")
    current = set_attr(current, "General", "FrnColor", "0x0000ff -1")
    desired = style_numeric(part_by_name(src, "Numeric Input/Display1"), "282 430 416 510", "304")
    desired = set_attr(desired, "General", "FrnColor", "0x15803d -1")
    disable = style_bit_button(part_by_name(src, "BS_0"), "154 650 326 714", GREEN, "Desativar", "Desativar")
    write_screen(
        "23.hsc",
        "33",
        [
            rect("BG_0", "0 0 480 800", BG),
            rect("HEADER_BG", "0 0 480 112", DARK),
            text("TITLE_0", "Modo Economico", "28 22", "304", "0xffffff", "1", DARK),
            text("SUBTITLE_0", "Eco ativado", "28 60", "233", SUBTLE, "0", DARK),
            rect("HEADER_ACCENT", "28 92 150 97", GREEN),
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
            rect("ACTION_CARD", "24 622 456 742", CARD, BORDER),
            disable,
        ],
    )


def modernize_screen_1000() -> None:
    src = read_screen("1000.hsc")
    keys = key_parts(src)
    display = style_string(part_by_name(src, "STR_0"), "36 124 444 194", "304")
    display = set_attr(display, "General", "Align", "3")
    min_value = style_string(part_by_name(src, "STR_2"), "112 714 220 742", "14")
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
    max_value = style_string(part_by_name(src, "STR_1"), "322 714 430 742", "14")
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
        ("7", "36 228 126 302"),
        ("8", "144 228 234 302"),
        ("9", "252 228 342 302"),
        ("4", "36 318 126 392"),
        ("5", "144 318 234 392"),
        ("6", "252 318 342 392"),
        ("1", "36 408 126 482"),
        ("2", "144 408 234 482"),
        ("3", "252 408 342 482"),
        ("0", "36 498 234 572"),
        (".", "252 498 342 572"),
    ]
    blocks = [
        *header("Teclado Numerico", "Digite o valor do parametro", SKY),
        rect("DISPLAY_CARD", "24 112 456 210", CARD, BORDER),
        display,
    ]
    for label, area in number_keys:
        blocks.append(style_key(key_by_ascii(keys, label), area, label))
    blocks.extend(
        [
            style_key_icon(key_by_ctrl(keys, "1"), "360 228 444 302", "121"),
            style_key_icon(key_by_ctrl(keys, "2"), "360 318 444 392", "130"),
            style_hidden(key_by_ascii(keys, "-")),
            style_key_icon(enter_key(keys), "360 498 444 572", "126"),
            style_key_icon(key_by_ctrl(keys, "3"), "368 30 444 86", "128"),
            rect("RANGE_CARD", "24 700 456 760", CARD, BORDER),
            text("TXT_MIN", "Min", "70 718", "8 16", MUTED, "1"),
            min_value,
            text("TXT_MAX", "Max", "280 718", "8 16", MUTED, "1"),
            max_value,
        ]
    )
    write_screen("1000.hsc", "1000", blocks, script_block(src), screen_size="1")


def text_keyboard_blocks(src: str, title: str, subtitle: str, input_name: str) -> list[str]:
    keys = key_parts(src)
    display = style_string(part_by_name(src, input_name), "24 116 456 178", "304")
    display = set_attr(display, "General", "Align", "3")
    blocks = [
        *header(title, subtitle, INDIGO),
        rect("DISPLAY_CARD", "12 106 468 188", CARD, BORDER),
        display,
        style_key_icon(key_by_ctrl(keys, "3"), "368 30 444 86", "128"),
        rect("KEY_PANEL", "8 198 472 678", "0xe9eef6", BORDER),
    ]

    def add_row(chars: str, y: int, x: int, width: int, gap: int) -> None:
        for index, char in enumerate(chars):
            left = x + index * (width + gap)
            blocks.append(style_key(key_by_ascii(keys, char), f"{left} {y} {left + width} {y + 56}", char))

    add_row("1234567890", 212, 14, 40, 6)
    add_row("QWERTYUIOP", 282, 14, 40, 6)
    add_row("ASDFGHJKL", 352, 24, 42, 7)
    add_row("ZXCVBNM", 422, 58, 44, 9)
    try:
        space = key_by_ascii(keys, " ")
    except ValueError:
        space = ""
    if space:
        blocks.extend(
            [
                style_key_icon(key_by_ctrl(keys, "1"), "24 506 116 562", "121"),
                style_key_icon(space, "128 506 352 562", "129"),
                style_key_icon(enter_key(keys), "364 506 456 562", "126"),
                style_key(key_by_ctrl(keys, "2"), "80 600 400 652", "Limpar tudo"),
                bitmap("ICO_CLEAR_ALL", "104 612", "28", "28", "130"),
            ]
        )
    else:
        blocks.extend(
            [
                style_key_icon(key_by_ctrl(keys, "1"), "24 510 116 570", "121"),
                style_key(key_by_ctrl(keys, "2"), "128 510 240 570", "Limpar"),
                bitmap("ICO_CLEAR_ALL", "138 526", "28", "28", "130"),
                style_key_icon(enter_key(keys), "252 510 344 570", "126"),
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
            *header("Timer Interno", "Controle do alarme de gas", GRAY),
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
    ok = style_function_icon(part_by_name(src, "FS_0"), "208 704 272 768", "126", "8 8")
    rows = [
        ("NUM_0", "Ano", 126),
        ("NUM_1", "Mes", 204),
        ("NUM_2", "Dia", 282),
        ("NUM_6", "Dia da semana", 360),
        ("NUM_3", "Hora", 438),
        ("NUM_4", "Minuto", 516),
        ("NUM_5", "Segundo", 594),
    ]
    blocks = [*header("Data e Hora", "Ajuste interno do painel", INDIGO)]
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
    blocks.extend([style_hidden(part_by_name(src, "WS_0")), ok])
    write_screen("1006.hsc", "0", blocks)


def modernize_screen_1007() -> None:
    src = read_screen("1007.hsc")
    up = style_numeric(part_by_name(src, "Numeric Input/Display1"), "248 154 420 216", "233")
    down = style_numeric(part_by_name(src, "Numeric Input/Display0"), "248 254 420 316", "233")
    cancel = style_word_icon(part_by_name(src, "Word Switch0"), "90 682 154 746", "128")
    enter = style_word_icon(part_by_name(src, "Word Switch1"), "326 682 390 746", "126")
    line_switches = [
        ("Bit Switch0", "Linha 1", "142 410 222 462", "48 426"),
        ("Bit Switch2", "Linha 3", "340 410 420 462", "246 426"),
        ("Bit Switch1", "Linha 2", "142 514 222 566", "48 530"),
        ("Bit Switch3", "Linha 4", "340 514 420 566", "246 530"),
    ]
    blocks = [
        *header("Faixa de Dados", "Periodo das tendencias", INDIGO),
        rect("CARD_RANGE", "24 132 456 340", CARD, BORDER),
        rect("ACCENT_RANGE", "24 132 30 340", INDIGO),
        text("TXT_UP", "Inicio", "48 158", "233", TEXT, "1"),
        text("TXT_UP_SUB", "Valor superior", "48 192", "8 16", MUTED),
        up,
        text("TXT_DOWN", "Fim", "48 258", "233", TEXT, "1"),
        text("TXT_DOWN_SUB", "Valor inferior", "48 292", "8 16", MUTED),
        down,
        rect("CARD_LINES", "24 374 456 592", CARD, BORDER),
        rect("ACCENT_LINES", "24 374 30 592", SKY),
        text("TXT_LINES", "Linhas do grafico", "48 392", "233", TEXT, "1"),
    ]
    for index, (part_name, label, area, point) in enumerate(line_switches):
        color = SKY if index % 2 == 0 else GREEN
        blocks.extend(
            [
                text(f"TXT_LINE_{index}", label, point, "14", TEXT, "1"),
                style_bit_button(part_by_name(src, part_name), area, color, "OFF", "ON"),
            ]
        )
    blocks.extend(
        [
            rect("ACTION_CARD", "24 650 456 768", CARD, BORDER),
            cancel,
            enter,
        ]
    )
    write_screen("1007.hsc", "1", blocks, script_block(src), screen_size="1")


def modernize_screen_1008() -> None:
    src = read_screen("1008.hsc")
    keys = key_parts(src)
    display = style_string(part_by_name(src, "STR_0"), "24 116 456 178", "304")
    display = set_attr(display, "General", "Align", "3")
    caps = style_bit_button(part_by_name(src, "BS_0"), "24 584 116 640", INDIGO, "ABC", "ABC")

    blocks = [
        *header("Teclado Alfanumerico", "Digite letras e numeros", INDIGO),
        rect("DISPLAY_CARD", "12 106 468 188", CARD, BORDER),
        display,
        rect("KEY_PANEL", "8 198 472 674", "0xe9eef6", BORDER),
    ]

    def add_row(chars: str, y: int, x: int, width: int, gap: int) -> None:
        for index, char in enumerate(chars):
            left = x + index * (width + gap)
            blocks.append(style_key(key_by_ascii(keys, char), f"{left} {y} {left + width} {y + 54}", char))

    add_row("1234567890", 212, 14, 40, 6)
    add_row("QWERTYUIOP", 278, 14, 40, 6)
    add_row("ASDFGHJKL", 344, 24, 42, 7)
    add_row("ZXCVBNM", 410, 58, 44, 9)
    blocks.extend(
        [
            style_key_icon(key_by_ctrl(keys, "3"), "368 30 444 86", "128"),
            style_key_icon(key_by_ctrl(keys, "1"), "24 506 116 562", "121"),
            style_key_icon(key_by_ascii(keys, " "), "128 506 352 562", "129"),
            style_key_icon(enter_key(keys), "364 506 456 562", "126"),
            caps,
            style_key(key_by_ctrl(keys, "2"), "128 584 456 640", "Limpar tudo"),
            bitmap("ICO_CLEAR_ALL", "152 596", "28", "28", "130"),
        ]
    )
    write_screen("1008.hsc", "0", blocks, script_block(src))


def modernize_screen_1009() -> None:
    src = read_screen("1009.hsc")
    total = style_numeric(part_by_name(src, "NUM_1"), "290 150 420 202", "233")
    start = style_numeric(part_by_name(src, "NUM_5"), "290 220 420 272", "233")
    current = style_numeric(part_by_name(src, "NUM_0"), "290 290 420 342", "233")
    admin_password = style_string(part_by_name(src, "STR_0"), "220 402 420 452", "233")
    password = style_string(part_by_name(src, "STR_1"), "220 466 420 516", "233")
    year = style_numeric(part_by_name(src, "NUM_2"), "58 594 154 642", "233")
    month = style_numeric(part_by_name(src, "NUM_4"), "192 594 288 642", "233")
    day = style_numeric(part_by_name(src, "NUM_6"), "326 594 422 642", "233")
    previous_period = style_word_icon(part_by_name(src, "WS_0"), "42 704 98 760", "128")
    next_period = style_word_icon(part_by_name(src, "WS_1"), "122 704 178 760", "103")
    save = style_word_icon(part_by_name(src, "WS_2"), "202 704 258 760", "126")
    cancel = style_word_icon(part_by_name(src, "WS_3"), "282 704 338 760", "130")
    exit_button = style_word_icon(part_by_name(src, "WS_4"), "362 704 418 760", "128")

    write_screen(
        "1009.hsc",
        "0",
        [
            *header("Periodo Manutencao", "Configuracao de validade", AMBER),
            rect("CARD_PERIOD", "24 132 456 360", CARD, BORDER),
            rect("ACCENT_PERIOD", "24 132 30 360", AMBER),
            text("TXT_TOTAL", "Total de periodos", "48 160", "233", TEXT, "1"),
            total,
            text("TXT_START", "Periodo inicial", "48 230", "233", TEXT, "1"),
            start,
            text("TXT_CURRENT", "Periodo atual", "48 300", "233", TEXT, "1"),
            current,
            rect("CARD_PASS", "24 384 456 532", CARD, BORDER),
            rect("ACCENT_PASS", "24 384 30 532", GRAY),
            text("TXT_ADMIN_PASS", "Senha superior", "48 414", "233", TEXT, "1"),
            admin_password,
            text("TXT_PASS", "Senha", "48 478", "233", TEXT, "1"),
            password,
            rect("CARD_DATE", "24 556 456 666", CARD, BORDER),
            rect("ACCENT_DATE", "24 556 30 666", SKY),
            text("TXT_DATE", "Validade", "48 572", "233", TEXT, "1"),
            text("TXT_YEAR", "Ano", "58 646", "8 16", MUTED, "1"),
            text("TXT_MONTH", "Mes", "192 646", "8 16", MUTED, "1"),
            text("TXT_DAY", "Dia", "326 646", "8 16", MUTED, "1"),
            year,
            month,
            day,
            rect("FOOTER_BG", "24 684 456 776", CARD, BORDER),
            previous_period,
            next_period,
            save,
            cancel,
            exit_button,
        ],
        script_block(src),
    )


def modernize_screen_1010() -> None:
    src = read_screen("1010.hsc")
    current = style_numeric(part_by_name(src, "NUM_0"), "286 168 420 230", "304")
    password = style_string(part_by_name(src, "STR_0"), "164 366 420 428", "304")
    enter = style_word_icon(part_by_name(src, "WS_0"), "208 624 272 688", "126")

    write_screen(
        "1010.hsc",
        "1",
        [
            *header("Periodo Atual", "Validacao de manutencao", AMBER),
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
            rect("ACTION_CARD", "24 608 456 718", CARD, BORDER),
            enter,
        ],
        script_block(src),
        screen_size="1",
    )


def modernize_screen_1011() -> None:
    src = read_screen("1011.hsc")
    user_list = style_downlist(part_by_name(src, "DL_1"), "190 212 420 274", "233")
    password = style_string(part_by_name(src, "STR_0"), "190 368 420 430", "304")
    cancel = style_function_icon(part_by_name(src, "FS_1"), "104 626 168 690", "128", "24 24")
    ok = style_bit_icon(part_by_name(src, "BS_1"), "312 626 376 690", "126", "24 24")

    write_screen(
        "1011.hsc",
        "0",
        [
            *header("Login", "Acesso de usuario", INDIGO),
            rect("CARD_USER", "24 166 456 308", CARD, BORDER),
            rect("ACCENT_USER", "24 166 30 308", INDIGO),
            text("TXT_USER", "Usuario", "48 230", "233", TEXT, "1"),
            user_list,
            rect("CARD_PASSWORD", "24 338 456 470", CARD, BORDER),
            rect("ACCENT_PASSWORD", "24 338 30 470", GRAY),
            text("TXT_PASSWORD", "Senha", "48 386", "233", TEXT, "1"),
            password,
            rect("ACTION_CARD", "24 596 456 724", CARD, BORDER),
            cancel,
            ok,
        ],
    )


def modernize_screen_1012() -> None:
    src = read_screen("1012.hsc")
    user = style_string(part_by_name(src, "STR_1"), "210 152 420 204", "233")
    current_password = style_string(part_by_name(src, "STR_0"), "210 256 420 308", "233")
    new_password = style_string(part_by_name(src, "STR_2"), "210 360 420 412", "233")
    confirm_password = style_string(part_by_name(src, "STR_3"), "210 464 420 516", "233")
    cancel = style_function_icon(part_by_name(src, "FS_0"), "104 648 168 712", "128", "24 24")
    ok = style_bit_icon(part_by_name(src, "BS_1"), "312 648 376 712", "126", "24 24")

    write_screen(
        "1012.hsc",
        "0",
        [
            *header("Alterar Senha", "Atualize o acesso do usuario", INDIGO),
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
            rect("ACTION_CARD", "24 616 456 744", CARD, BORDER),
            cancel,
            ok,
        ],
    )


def modernize_screen_17() -> None:
    src = read_screen("17.hsc")
    home = style_function_icon(part_by_name(src, "Function Switch0"), "208 704 272 768", "125", "32 32")
    back = style_function_icon(part_by_name(src, "Function Switch1"), "48 704 112 768", "128", "24 24")
    day = style_numeric(part_by_name(src, "Numeric Input/Display0"), "184 176 238 238", "262")
    month = style_numeric(part_by_name(src, "Numeric Input/Display1"), "270 176 324 238", "262")
    year = style_numeric(part_by_name(src, "Numeric Input/Display2"), "356 176 434 238", "262")
    hour = style_numeric(part_by_name(src, "Numeric Input/Display4"), "244 354 304 416", "262")
    minute = style_numeric(part_by_name(src, "Numeric Input/Display3"), "338 354 398 416", "262")
    write_screen(
        "17.hsc",
        "3",
        [
            *header("Data e Hora", "Ajuste do relogio interno", INDIGO),
            rect("CARD_DATE", "24 138 456 282", CARD, BORDER),
            rect("ACCENT_DATE", "24 138 30 282", INDIGO),
            text("TXT_DATE", "Data", "48 180", "233", TEXT, "1"),
            day,
            text("TXT_DATE_SEP1", "/", "248 182", "304", MUTED),
            month,
            text("TXT_DATE_SEP2", "/", "336 182", "304", MUTED),
            year,
            rect("CARD_TIME", "24 324 456 468", CARD, BORDER),
            rect("ACCENT_TIME", "24 324 30 468", INDIGO),
            text("TXT_TIME", "Hora", "48 366", "233", TEXT, "1"),
            hour,
            text("TXT_TIME_SEP", ":", "315 360", "304", MUTED),
            minute,
            rect("INFO_CARD", "24 506 456 606", CARD, BORDER),
            text("TXT_INFO", "Formato", "48 528", "233", TEXT, "1"),
            text("TXT_INFO_SUB", "Ajuste data e hora do relogio interno.", "48 564", "8 16", MUTED),
            *footer(back, home),
        ],
    )


def modernize_recipe_editor(file_name: str, recipe_no: int) -> None:
    src = read_screen(file_name)
    back = style_function_icon(first_part_by_type(src, "FunctionSwitch"), "48 704 112 768", "128", "24 24")
    name = style_string(part_by_name(src, "STR_0"), "48 174 432 238", "233")
    temperature = style_numeric(part_by_name(src, "NUM_0"), "284 336 418 416", "304")
    time_value = style_numeric(part_by_name(src, "NUM_1"), "284 504 418 584", "304")
    write_screen(
        file_name,
        screen_no(src),
        [
            *header(f"Receita {recipe_no}", "Nome, temperatura e tempo", AMBER),
            rect("CARD_NAME", "24 132 456 266", CARD, BORDER),
            rect("ACCENT_NAME", "24 132 30 266", AMBER),
            text("TXT_NAME", "Nome", "48 150", "233", TEXT, "1"),
            name,
            rect("CARD_TEMP", "24 300 456 444", CARD, BORDER),
            rect("ACCENT_TEMP", "24 300 30 444", RED),
            text("TXT_TEMP", "Temperatura", "48 326", "233", TEXT, "1"),
            text("TXT_TEMP_HINT", "Valores entre 180 e 400", "48 362", "12 24", MUTED),
            temperature,
            text("TXT_TEMP_UNIT", "C", "422 366", "233", MUTED),
            rect("CARD_TIME", "24 476 456 620", CARD, BORDER),
            rect("ACCENT_TIME", "24 476 30 620", SKY),
            text("TXT_TIME", "Tempo", "48 502", "233", TEXT, "1"),
            text("TXT_TIME_HINT", "Valores entre 1.00 e 9.99", "48 538", "12 24", MUTED),
            time_value,
            text("TXT_TIME_UNIT", "min", "420 536", "12 24", MUTED),
            *footer(back),
        ],
    )


def modernize_screen_16() -> None:
    src = read_screen("16.hsc")
    home = style_function_icon(part_by_name(src, "Function Switch2"), "208 704 272 768", "125", "32 32")
    back = style_function_icon(part_by_name(src, "Function Switch0"), "48 704 112 768", "128", "24 24")
    fields = [
        ("NUM_0", "Low Point", "0 a 40", "124 232", "286 148 436 212"),
        ("Numeric Input/Display0", "Low Offset", "-50 a 50", "258 366", "286 282 436 346"),
        ("Numeric Input/Display1", "High Point", "200 a 400", "392 500", "286 416 436 480"),
        ("Numeric Input/Display2", "High Offset", "-500 a 500", "526 634", "286 550 436 614"),
    ]
    blocks = [*header("Ajustes Offset", "Calibracao de pontos", GRAY)]
    for index, (part_name, label, hint, y_area, input_area) in enumerate(fields):
        top, bottom = y_area.split()
        accent = SKY if index < 2 else RED
        blocks.extend(
            [
                rect(f"CARD_OFFSET_{index}", f"24 {top} 456 {bottom}", CARD, BORDER),
                rect(f"ACCENT_OFFSET_{index}", f"24 {top} 30 {bottom}", accent),
                text(f"TXT_OFFSET_{index}", label, f"48 {int(top) + 24}", "233", TEXT, "1"),
                text(f"TXT_OFFSET_HINT_{index}", hint, f"48 {int(top) + 60}", "12 24", MUTED),
                style_numeric(part_by_name(src, part_name), input_area, "304"),
            ]
        )
    write_screen("16.hsc", screen_no(src), [*blocks, *footer(back, home)])


def main() -> None:
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


if __name__ == "__main__":
    main()
