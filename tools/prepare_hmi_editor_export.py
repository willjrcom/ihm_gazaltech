#!/usr/bin/env python3
"""Prepare a flat project folder for the vendor HMI editor.

The local preview keeps screen XML files in ./screens, but LCD Gazal.ump
references them as plain filenames such as 0.hsc. Some HMI editors expect the
.hsc files beside the .ump, so this script creates a generated export folder
with that flat layout without changing the source tree.
"""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCREEN_DIR = ROOT / "screens"
DEFAULT_EXPORT_DIR = ROOT / "editor_export"

PROJECT_FILES = [
    "LCD Gazal.ump",
    "LCD Gazal.ehmt",
    "LCD Gazal.eblb",
    "Font.hft",
    "Font.lib",
    "PlcAddrInfo.xml",
    "bmplib.blb",
    "G_bmplib.blb",
]

def parse_screen_files(project_file: Path) -> list[str]:
    text = project_file.read_text(encoding="utf-8", errors="replace")
    return re.findall(r'ScrnFile="([^"]+)"', text)


def ensure_safe_destination(path: Path) -> None:
    resolved = path.resolve()
    root = ROOT.resolve()
    if resolved == root:
        raise SystemExit("Refusing to export over the project root.")
    if root not in resolved.parents:
        raise SystemExit("Export destination must stay inside the project folder.")


def copy_project_file(name: str, destination: Path) -> None:
    source = ROOT / name
    if source.exists():
        shutil.copy2(source, destination / name)


def copy_project_dir(name: str, destination: Path) -> None:
    source = ROOT / name
    target = destination / name
    if source.exists():
        shutil.copytree(source, target)


def prepare_export(destination: Path, *, include_g_picture: bool = False) -> list[str]:
    ensure_safe_destination(destination)

    if not SCREEN_DIR.exists():
        raise SystemExit(f"Missing screen directory: {SCREEN_DIR}")

    if destination.exists():
        shutil.rmtree(destination)
    destination.mkdir(parents=True)

    for name in PROJECT_FILES:
        copy_project_file(name, destination)

    if include_g_picture:
        copy_project_dir("G_Picture", destination)

    for screen_file in sorted(SCREEN_DIR.glob("*.hsc"), key=lambda item: item.name):
        shutil.copy2(screen_file, destination / screen_file.name)

    screen_refs = parse_screen_files(ROOT / "LCD Gazal.ump")
    missing = sorted(ref for ref in screen_refs if not (destination / ref).exists())
    if missing:
        raise SystemExit("Export missing screen files: " + ", ".join(missing))

    readme = destination / "README_EXPORT.txt"
    readme.write_text(
        "\n".join(
            [
                "Export gerado para abrir no software oficial da IHM.",
                "",
                "Abra o arquivo 'LCD Gazal.ump' desta pasta.",
                "Os arquivos .hsc foram copiados para o mesmo nivel do .ump,",
                "porque o projeto referencia as telas como 0.hsc, 7.hsc etc.",
                "",
                "Depois de abrir no editor, recompile/exporte novamente para",
                "regenerar os arquivos LCD Gazal.ehmt/LCD Gazal.eblb.",
                "",
                "A pasta bruta G_Picture nao e copiada por padrao; as bibliotecas",
                ".blb foram copiadas. Use --include-g-picture somente se o editor",
                "pedir essa pasta ao abrir o projeto.",
                "",
            ]
        ),
        encoding="utf-8",
    )

    return screen_refs


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "destination",
        nargs="?",
        type=Path,
        default=DEFAULT_EXPORT_DIR,
        help="Export folder to create inside the project.",
    )
    parser.add_argument(
        "--include-g-picture",
        action="store_true",
        help="Also copy the raw G_Picture folder. This can be slow if files are placeholders.",
    )
    args = parser.parse_args()

    destination = args.destination
    if not destination.is_absolute():
        destination = ROOT / destination

    screen_refs = prepare_export(destination, include_g_picture=args.include_g_picture)
    print(f"Export created: {destination}")
    print(f"Screen references validated: {len(screen_refs)}")


if __name__ == "__main__":
    main()
