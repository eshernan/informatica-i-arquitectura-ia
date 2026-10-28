"""Validaciones de contenido sin dependencias externas."""

from __future__ import annotations

import ast
import json
from pathlib import Path
import re
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
CORE_MODULES = (
    "01_entorno", "02_calidad", "03_c4_uml_adr", "04_modularidad",
    "05_distribucion", "06_apis_datos_eventos", "07_pruebas",
    "08_entrega_plataforma", "09_observabilidad", "10_seguridad",
    "11_ia", "12_proyecto",
)

TEACHING_GUIDES = {
    "aws-learner-lab/sesiones/10_calidad/README.md": (
        "Persistencia en archivos", "Parquet", "bloqueo",
    ),
    "aws-learner-lab/sesiones/11_hexagonal/README.md": (
        "Persistencia e integridad", "PostgreSQL", "prueba concurrente",
    ),
    "aws-learner-lab/sesiones/12_distribuidos/README.md": (
        "API confiable", "idempotencia", "/salud/lista",
    ),
    "aws-learner-lab/sesiones/13_api_eventos/README.md": (
        "Entrega segura y trazable", "flujo CI", "usuario no privilegiado",
    ),
    "aws-learner-lab/sesiones/14_pruebas_entrega/README.md": (
        "Operación y recuperación", "respaldo", "restauración",
    ),
    "aws-learner-lab/sesiones/15_proyecto/README.md": (
        "Jornada autónoma de integración", "clon limpio", "versión candidata",
    ),
    "aws-learner-lab/sesiones/16_cierre/README.md": (
        "Demostración de robustez", "fallo", "recuperación",
    ),
}

ROUTE_FORBIDDEN = (
    "s11-dynamodb.yaml",
    "s12-messaging.yaml",
    "s13-serverless-api.yaml",
    "s14-ecr.yaml",
    "kind create cluster",
    "rabbitmq:4",
)


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
    # Los materiales históricos del primer bloque no siguen esta estructura.
    # Se conservan sin imponerles los encabezados del laboratorio LibreReserva.
    modules = [ROOT / "modules" / name for name in CORE_MODULES]
    for module in modules:
        readme = module / "README.md"
        if not readme.exists():
            raise SystemExit(f"Falta {readme.relative_to(ROOT)}")
        content = readme.read_text(encoding="utf-8")
        for heading in ("## Resultado", "## Instalación paso a paso", "## Validación"):
            if heading not in content:
                raise SystemExit(f"Falta '{heading}' en {readme.relative_to(ROOT)}")


def validate_notebooks() -> None:
    notebooks = sorted(
        path for name in CORE_MODULES
        for path in (ROOT / "modules" / name).rglob("*.ipynb")
    )
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


def validate_teaching_route() -> None:
    failures: list[str] = []
    for relative, required in TEACHING_GUIDES.items():
        path = ROOT / relative
        content = path.read_text(encoding="utf-8")
        missing = [phrase for phrase in required if phrase not in content]
        if missing:
            failures.append(f"{relative}: faltan {', '.join(missing)}")
        present = [phrase for phrase in ROUTE_FORBIDDEN if phrase in content]
        if present:
            failures.append(f"{relative}: conserva instrucciones fuera de ruta: {', '.join(present)}")

    compose = (ROOT / "modules/06_apis_datos_eventos/compose.yml").read_text(
        encoding="utf-8"
    )
    for service in ("postgres", "migracion", "api_a", "api_b", "balanceador"):
        if f"  {service}:" not in compose:
            failures.append(f"compose.yml: falta el servicio {service}")
    if "rabbitmq" in compose.lower():
        failures.append("compose.yml: RabbitMQ no pertenece a la ruta evaluable")

    for relative in (
        "labs/librereserva/app/ports.py",
        "labs/librereserva/app/adapters/memory.py",
        "labs/librereserva/app/adapters/postgres.py",
        "labs/librereserva/migrations/001_crear_reservas.sql",
        "labs/librereserva/tests/test_repository_contract.py",
        "modules/06_apis_datos_eventos/Caddyfile",
    ):
        if not (ROOT / relative).exists():
            failures.append(f"Sesión 11: falta {relative}")

    migration = (
        ROOT / "labs/librereserva/migrations/001_crear_reservas.sql"
    ).read_text(encoding="utf-8")
    for phrase in ("CHECK (fin > inicio)", "EXCLUDE USING gist", "'[)'"):
        if phrase not in migration:
            failures.append(f"Migración de reservas: falta {phrase}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for phrase in (
        "Dos recorridos que no comparten numeración",
        "Progreso en AWS Academy Cloud Foundations",
        "Ruta acumulativa del segundo bloque",
    ):
        if phrase not in readme:
            failures.append(f"README.md: falta '{phrase}'")

    if failures:
        raise SystemExit("Ruta docente desalineada:\n" + "\n".join(failures))
    print("Ruta docente alineada: sesiones 10–16 y PostgreSQL acumulativo.")


if __name__ == "__main__":
    validate_markdown_links()
    validate_modules()
    validate_notebooks()
    validate_teaching_route()
    print("Contenido y enlaces locales válidos.")
