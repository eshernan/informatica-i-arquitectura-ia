#!/usr/bin/env bash
set -euo pipefail

failures=0
full=false
if (($# > 1)) || (($# == 1)) && [[ "$1" != '--full' ]]; then
  printf 'Uso: check_preparation.sh [--full]\n' >&2
  exit 2
fi
if (($# == 1)); then
  full=true
fi

check_required() {
  local command_name="$1"
  if command -v "$command_name" >/dev/null 2>&1; then
    printf 'OK   %-16s %s\n' "$command_name" "$(command -v "$command_name")"
  else
    printf 'FALTA %-16s requerido\n' "$command_name"
    failures=$((failures + 1))
  fi
}

check_optional() {
  local command_name="$1"
  if command -v "$command_name" >/dev/null 2>&1; then
    printf 'OK   %-16s %s\n' "$command_name" "$(command -v "$command_name")"
  else
    printf 'INFO %-16s opcional para una sesión posterior\n' "$command_name"
  fi
}

printf 'Herramientas locales\n'
check_required git
check_required python3
check_required aws
if [[ "$full" == true ]]; then
  check_required podman
  check_required kind
  check_required kubectl
else
  check_optional podman
  check_optional kind
  check_optional kubectl
fi

if ! command -v aws >/dev/null 2>&1; then
  printf '\nInstale AWS CLI v2 o ejecute esta comprobación en AWS CloudShell.\n'
  exit 1
fi

printf '\nSesión temporal de AWS\n'
if ! identity="$(aws sts get-caller-identity --output json 2>/dev/null)"; then
  printf 'FALTA una sesión válida. Inicie Learner Lab y renueve las credenciales temporales.\n'
  exit 1
fi

account="$(python3 -c 'import json,sys; print(json.load(sys.stdin)["Account"])' <<<"$identity")"
arn="$(python3 -c 'import json,sys; print(json.load(sys.stdin)["Arn"])' <<<"$identity")"
masked_account="${account:0:2}******${account: -2}"
identity_label="${arn##*/}"
printf 'OK   cuenta          %s\n' "$masked_account"
printf 'OK   sesión/rol      %s\n' "$identity_label"

region="${AWS_REGION:-${AWS_DEFAULT_REGION:-}}"
if [[ -z "$region" ]]; then
  region="$(aws configure get region 2>/dev/null || true)"
fi
if [[ -z "$region" ]]; then
  printf 'FALTA región. Ejecute: export AWS_REGION=REGION_ACORDADA\n'
  failures=$((failures + 1))
else
  printf 'OK   región          %s\n' "$region"
fi

printf '\nAcceso de lectura a servicios (un AVISO puede indicar una restricción del laboratorio)\n'
if [[ -n "$region" ]]; then
  if aws cloudformation list-stacks --region "$region" --max-items 1 >/dev/null 2>&1; then
    printf 'OK   %-16s acceso de lectura\n' cloudformation
  else
    printf 'AVISO %-16s sin acceso de lectura\n' cloudformation
  fi
  if aws s3api list-buckets --region "$region" >/dev/null 2>&1; then
    printf 'OK   %-16s acceso de lectura\n' s3
  else
    printf 'AVISO %-16s sin acceso de lectura\n' s3
  fi
  if aws dynamodb list-tables --region "$region" --limit 1 >/dev/null 2>&1; then
    printf 'OK   %-16s acceso de lectura\n' dynamodb
  else
    printf 'AVISO %-16s sin acceso de lectura\n' dynamodb
  fi
  if aws sqs list-queues --region "$region" --max-results 1 >/dev/null 2>&1; then
    printf 'OK   %-16s acceso de lectura\n' sqs
  else
    printf 'AVISO %-16s sin acceso de lectura\n' sqs
  fi
  if aws lambda list-functions --region "$region" --max-items 1 >/dev/null 2>&1; then
    printf 'OK   %-16s acceso de lectura\n' lambda
  else
    printf 'AVISO %-16s sin acceso de lectura\n' lambda
  fi
  if aws apigatewayv2 get-apis --region "$region" --max-results 1 >/dev/null 2>&1; then
    printf 'OK   %-16s acceso de lectura\n' apigatewayv2
  else
    printf 'AVISO %-16s sin acceso de lectura\n' apigatewayv2
  fi
  if aws logs describe-log-groups --region "$region" --limit 1 >/dev/null 2>&1; then
    printf 'OK   %-16s acceso de lectura\n' logs
  else
    printf 'AVISO %-16s sin acceso de lectura\n' logs
  fi
  if aws ecr describe-repositories --region "$region" --max-results 1 >/dev/null 2>&1; then
    printf 'OK   %-16s acceso de lectura\n' ecr
  else
    printf 'AVISO %-16s sin acceso de lectura\n' ecr
  fi
fi

printf '\nLa comprobación no creó recursos ni mostró credenciales.\n'
if ((failures > 0)); then
  printf 'Preparación incompleta: %d requisito(s) pendiente(s).\n' "$failures"
  exit 1
fi
printf 'Preparación básica completa. El docente aún debe probar permisos y cuotas con cada plantilla.\n'
