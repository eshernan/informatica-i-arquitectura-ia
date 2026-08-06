#!/usr/bin/env bash
set -euo pipefail

module_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
command -v plantuml >/dev/null 2>&1 || {
  printf 'Falta PlantUML. Siga %s/README.md\n' "$module_dir" >&2
  exit 1
}
plantuml -checkonly "$module_dir/contexto.puml"
plantuml -tsvg "$module_dir/contexto.puml"
printf 'Generado: %s/contexto.svg\n' "$module_dir"
