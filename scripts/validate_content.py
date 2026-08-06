"""Validaciones de contenido sin dependencias externas."""

from __future__ import annotations

import ast
import json
from pathlib import Path
import re
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def validate_markdown_links() -> None:
    failures: list[str] = []
    for document in ROOT.rglob("*.md"):
        if ".git" in document.parts:
            continue
        text = document.read_text(encoding="utf-8")
        for raw_target in LINK.findall(text):
            target = raw_target.split(maxsplit=1)[0].strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            path_text = unquote(target.split("#", 1)[0])
            if not path_text:
                continue
            resolved = (document.parent / path_text).resolve()
            if not resolved.exists():
                failures.append(f"{document.relative_to(ROOT)} -> {target}")
    if failures:
        raise SystemExit("Enlaces locales rotos:\n" + "\n".join(failures))


def validate_modules() -> None:
    modules = sorted(path for path in (ROOT / "modules").iterdir() if path.is_dir())
    if len(modules) != 12:
        raise SystemExit(f"Se esperaban 12 módulos y se encontraron {len(modules)}")
    for module in modules:
        readme = module / "README.md"
        if not readme.exists():
            raise SystemExit(f"Falta {readme.relative_to(ROOT)}")
        content = readme.read_text(encoding="utf-8")
        for heading in ("## Resultado", "## Instalación paso a paso", "## Validación"):
            if heading not in content:
                raise SystemExit(f"Falta '{heading}' en {readme.relative_to(ROOT)}")


def validate_notebooks() -> None:
    notebooks = sorted((ROOT / "modules").rglob("*.ipynb"))
    if len(notebooks) != 3:
        raise SystemExit(f"Se esperaban 3 notebooks y se encontraron {len(notebooks)}")
    code_cells = 0
    for notebook in notebooks:
        data = json.loads(notebook.read_text(encoding="utf-8"))
        if data.get("nbformat") != 4:
            raise SystemExit(f"Formato inesperado: {notebook.relative_to(ROOT)}")
        for cell in data.get("cells", []):
            if cell.get("cell_type") != "code":
                continue
            code_cells += 1
            ast.parse("".join(cell.get("source", [])))
            if cell.get("outputs"):
                raise SystemExit(f"Notebook con salidas: {notebook.relative_to(ROOT)}")
            if cell.get("execution_count") is not None:
                raise SystemExit(f"Notebook ejecutado: {notebook.relative_to(ROOT)}")
    print(f"Notebooks válidos y sin salidas: {len(notebooks)} ({code_cells} celdas)")


if __name__ == "__main__":
    validate_markdown_links()
    validate_modules()
    validate_notebooks()
    print("Contenido y enlaces locales válidos.")
