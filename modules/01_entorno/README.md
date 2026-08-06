# Módulo 1. Sistemas modernos y entorno reproducible

## Resultado

Preparar una estación verificable, explicar qué es una decisión arquitectónica y registrar la primera evidencia reproducible.

## Requisitos

- 8 GiB de RAM y 20 GiB libres como referencia mínima.
- GNU/Linux Debian/Ubuntu, macOS o Windows con WSL2.
- Permiso institucional para instalar paquetes.

## Instalación paso a paso

1. Clone el repositorio y entre en él.
2. Revise el instalador; no lo ejecute a ciegas.
3. Muestre el plan sin cambiar el sistema.
4. Aplique el plan solo si coincide con su plataforma.
5. Cree el entorno Python y valide.

```bash
sed -n '1,240p' scripts/install_base.sh
./scripts/install_base.sh
./scripts/install_base.sh --apply
./scripts/setup_python.sh --apply
./scripts/check_environment.sh
make test
```

### macOS y Podman

```bash
podman machine init     # una vez
podman machine start
podman info
```

### Windows

Instale WSL2 con la guía oficial de Microsoft, cree una distribución Debian/Ubuntu y ejecute los pasos GNU/Linux dentro de WSL. Guarde el repositorio bajo `/home`, no en una unidad montada, para conservar rendimiento y permisos.

## Ejercicio

Complete `docs/entorno.md` con sistema, arquitectura, RAM, versiones y desviaciones. Cree una rama, ejecute las pruebas y confirme solo el documento.

## Validación

```bash
git status --short
python3 --version
podman info
make check
```

**Evidencia:** archivo de entorno, salida de validación y explicación de una decisión tomada durante la instalación.
