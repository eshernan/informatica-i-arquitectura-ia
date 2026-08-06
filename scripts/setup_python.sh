#!/usr/bin/env bash
set -euo pipefail

mode="${1:-plan}"
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

printf 'Plan: crear %s/.venv e instalar requirements-dev.txt\n' "$repo_root"
[[ "$mode" == "--apply" ]] || {
  printf 'Use %s --apply después de revisar requirements-dev.txt.\n' "$0"
  exit 0
}

python3 -m venv "$repo_root/.venv"
"$repo_root/.venv/bin/python" -m pip install --upgrade pip
"$repo_root/.venv/bin/python" -m pip install -r "$repo_root/requirements-dev.txt"
"$repo_root/.venv/bin/python" -m pip check
