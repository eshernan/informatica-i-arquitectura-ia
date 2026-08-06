#!/usr/bin/env bash
set -euo pipefail

mode="${1:-plan}"
if [[ "$mode" != "plan" && "$mode" != "--apply" ]]; then
  printf 'Uso: %s [--apply]\n' "$0" >&2
  exit 2
fi

os_name="$(uname -s)"
if [[ "$os_name" == "Darwin" ]]; then
  packages=(git make python podman plantuml graphviz jq)
  printf 'Plan macOS: brew install %s\n' "${packages[*]}"
  [[ "$mode" == "--apply" ]] || exit 0
  command -v brew >/dev/null 2>&1 || {
    printf 'Homebrew no está instalado. Revise https://brew.sh y la política del equipo.\n' >&2
    exit 1
  }
  brew install "${packages[@]}"
  printf 'Después ejecute: podman machine init && podman machine start\n'
elif [[ -r /etc/debian_version ]]; then
  packages=(git make python3 python3-venv python3-pip podman plantuml graphviz curl jq)
  printf 'Plan Debian/Ubuntu: sudo apt-get update; sudo apt-get install %s\n' "${packages[*]}"
  [[ "$mode" == "--apply" ]] || exit 0
  sudo apt-get update
  sudo apt-get install -y "${packages[@]}"
else
  printf 'Sistema no automatizado. Consulte modules/01_entorno/README.md.\n' >&2
  exit 1
fi
