#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

while IFS= read -r script_path; do
  bash -n "$script_path"
done < <(find scripts modules -name '*.sh' -type f | sort)

python3 -m compileall -q labs/librereserva
python3 -m unittest discover -s labs/librereserva/tests -v
python3 scripts/validate_content.py

printf 'Repositorio válido: scripts, código, pruebas, notebooks y 12 módulos.\n'
