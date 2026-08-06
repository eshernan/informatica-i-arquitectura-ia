#!/usr/bin/env bash
set -euo pipefail

mode="${1:-plan}"
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
results_dir="$repo_root/security-results"
image_name="localhost/librereserva:0.1.0"

printf 'Plan de análisis:\n'
printf '  Gitleaks sobre %s\n' "$repo_root"
printf '  SBOM y Trivy sobre %s\n' "$image_name"
printf '  Salidas en %s (ignorado por Git)\n' "$results_dir"

[[ "$mode" == "--apply" ]] || {
  printf 'Use %s --apply cuando las herramientas y la imagen estén disponibles.\n' "$0"
  exit 0
}

for tool_name in gitleaks syft trivy; do
  command -v "$tool_name" >/dev/null 2>&1 || {
    printf 'Falta %s. Consulte %s/modules/10_seguridad/README.md\n' "$tool_name" "$repo_root" >&2
    exit 1
  }
done

mkdir -p "$results_dir"
gitleaks detect --source "$repo_root" --redact --report-format sarif \
  --report-path "$results_dir/gitleaks.sarif"
syft "$image_name" -o cyclonedx-json="$results_dir/sbom.cdx.json"
trivy image --severity HIGH,CRITICAL --format json \
  --output "$results_dir/trivy.json" "$image_name"
printf 'Resultados generados en %s\n' "$results_dir"
