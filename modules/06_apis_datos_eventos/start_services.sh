#!/usr/bin/env bash
set -euo pipefail

mode="${1:-plan}"
module_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

printf 'Plan: iniciar PostgreSQL y RabbitMQ definidos en %s/compose.yml\n' "$module_dir"
[[ "$mode" == "--apply" ]] || {
  printf 'Use %s --apply después de revisar imágenes, puertos y credenciales.\n' "$0"
  exit 0
}

command -v podman >/dev/null 2>&1 || {
  printf 'Falta Podman. Complete el módulo 1.\n' >&2
  exit 1
}

podman compose -f "$module_dir/compose.yml" up -d
podman ps --filter name=librereserva
