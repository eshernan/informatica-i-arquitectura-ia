#!/usr/bin/env bash
set -euo pipefail

required=(git python3 make)
optional=(podman plantuml kubectl kind trivy syft gitleaks ollama)
missing_required=0

printf 'Sistema: %s\n' "$(uname -a)"
printf '\nHerramientas esenciales\n'
for command_name in "${required[@]}"; do
  if command -v "$command_name" >/dev/null 2>&1; then
    printf '  [ok] %-12s %s\n' "$command_name" "$(command -v "$command_name")"
  else
    printf '  [falta] %s\n' "$command_name"
    missing_required=1
  fi
done

printf '\nHerramientas por módulo\n'
for command_name in "${optional[@]}"; do
  if command -v "$command_name" >/dev/null 2>&1; then
    printf '  [ok] %-12s %s\n' "$command_name" "$(command -v "$command_name")"
  else
    printf '  [opcional] %s\n' "$command_name"
  fi
done

if [[ "$missing_required" -ne 0 ]]; then
  printf '\nInstale las herramientas esenciales con ./scripts/install_base.sh --apply\n'
  exit 1
fi

printf '\nEntorno esencial disponible. Instale herramientas adicionales al comenzar cada módulo.\n'
