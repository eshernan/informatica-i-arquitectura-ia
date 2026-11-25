"""Ejemplo local: configuración pública y secreto leído al iniciar."""

import os
from pathlib import Path


def main():
    ambiente = os.getenv("AMBIENTE", "desarrollo")
    ruta = os.getenv("TOKEN_FILE")
    if not ruta:
        raise SystemExit("Error: indique la ruta del secreto en TOKEN_FILE")
    try:
        token = Path(ruta).read_text(encoding="utf-8").rstrip("\r\n")
    except OSError:
        raise SystemExit("Error: no se puede leer el archivo del secreto") from None
    if not token:
        raise SystemExit("Error: el archivo del secreto está vacío")
    print(f"Ambiente: {ambiente}")
    print("Secreto: cargado (valor oculto)")
    print("Configuración aceptada; ejemplo local, sin conexión a servicios")


if __name__ == "__main__":
    main()
