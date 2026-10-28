#!/usr/bin/env bash
set -euo pipefail

mode=plan
motor=podman
while (($#)); do
  case "$1" in
    --apply) mode=apply; shift ;;
    --motor)
      [[ $# -ge 2 ]] || { printf 'Falta el valor de --motor.\n' >&2; exit 2; }
      motor="$2"; shift 2 ;;
    *) printf 'Uso: %s [--motor podman|docker] [--apply]\n' "$0" >&2; exit 2 ;;
  esac
done
[[ "$motor" == podman || "$motor" == docker ]] || {
  printf 'Motor no admitido: %s. Use podman o docker.\n' "$motor" >&2; exit 2;
}
module_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

printf 'Plan: iniciar PostgreSQL definido en %s/compose.yml\n' "$module_dir"
printf 'Motor: %s. Comando: %s compose -f %s/compose.yml up -d postgres\n' "$motor" "$motor" "$module_dir"
[[ "$mode" == apply ]] || {
  printf 'Use %s --apply después de revisar imágenes, puertos y credenciales.\n' "$0"
  exit 0
}

command -v "$motor" >/dev/null 2>&1 || {
  printf 'Falta %s. Complete el módulo 1.\n' "$motor" >&2
  exit 1
}

"$motor" info >/dev/null || { printf 'El motor no responde; revise servicio, máquina o permisos.\n' >&2; exit 1; }
"$motor" compose version >/dev/null || {
  printf 'Compose no está disponible. Podman requiere un proveedor como podman-compose; Docker requiere el plugin Compose.\n' >&2
  exit 1
}
"$motor" compose -f "$module_dir/compose.yml" config >/dev/null
"$motor" compose -f "$module_dir/compose.yml" up -d postgres
"$motor" ps --filter name=librereserva
