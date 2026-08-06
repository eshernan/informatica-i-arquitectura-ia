#!/usr/bin/env bash
set -euo pipefail

command -v ollama >/dev/null 2>&1 || {
  printf 'Ollama no está instalado. Consulte https://ollama.com/download\n' >&2
  exit 1
}

ollama --version
printf '\nModelos disponibles localmente:\n'
ollama list
printf '\nRevise la licencia de cada modelo antes de usarlo con código institucional.\n'
