#!/usr/bin/env bash
set -euo pipefail

usage() {
  printf '%s\n' \
    'Uso:' \
    '  stack.sh deploy STACK TEMPLATE [KEY=VALUE ...] [--apply]' \
    '  stack.sh delete STACK [--apply]' \
    '' \
    'Sin --apply solo muestra y valida el plan.'
}

if (($# < 2)); then
  usage
  exit 2
fi

action="$1"
stack_name="$2"
shift 2

if [[ ! "$stack_name" =~ ^libre-reserva-s(09|10|11|12|13|14|15|16)-[a-z0-9-]+$ ]]; then
  printf 'Nombre rechazado: use libre-reserva-sNN-equipoXX.\n' >&2
  exit 2
fi

region="${AWS_REGION:-${AWS_DEFAULT_REGION:-}}"
if [[ -z "$region" ]]; then
  region="$(aws configure get region 2>/dev/null || true)"
fi
if [[ -z "$region" ]]; then
  printf 'Defina AWS_REGION con la región acordada.\n' >&2
  exit 2
fi

apply=false
arguments=()
for argument in "$@"; do
  if [[ "$argument" == '--apply' ]]; then
    apply=true
  else
    arguments+=("$argument")
  fi
done

case "$action" in
  deploy)
    if ((${#arguments[@]} < 1)); then
      usage
      exit 2
    fi
    template="${arguments[0]}"
    if [[ ! -f "$template" || "$template" != aws-learner-lab/templates/*.yaml ]]; then
      printf 'La plantilla debe existir dentro de aws-learner-lab/templates/.\n' >&2
      exit 2
    fi
    parameters=("${arguments[@]:1}")
    for parameter in "${parameters[@]}"; do
      if [[ ! "$parameter" =~ ^[A-Za-z][A-Za-z0-9]*=.+$ ]]; then
        printf 'Parámetro inválido: %s. Use KEY=VALUE.\n' "$parameter" >&2
        exit 2
      fi
    done
    aws cloudformation validate-template \
      --template-body "file://$template" \
      --region "$region" >/dev/null
    printf 'Plan: desplegar %s desde %s en %s\n' "$stack_name" "$template" "$region"
    if ((${#parameters[@]} > 0)); then
      printf 'Parámetros: %s\n' "${parameters[*]}"
    fi
    if [[ "$apply" != true ]]; then
      printf 'No se hicieron cambios. Repita con --apply.\n'
      exit 0
    fi
    command=(aws cloudformation deploy --stack-name "$stack_name" --template-file "$template" --region "$region" --no-fail-on-empty-changeset)
    if ((${#parameters[@]} > 0)); then
      command+=(--parameter-overrides "${parameters[@]}")
    fi
    "${command[@]}"
    aws cloudformation describe-stack-resources --stack-name "$stack_name" --region "$region" --output table
    ;;
  delete)
    if ((${#arguments[@]} > 0)); then
      usage
      exit 2
    fi
    if ! aws cloudformation describe-stacks --stack-name "$stack_name" --region "$region" >/dev/null 2>&1; then
      printf 'La pila exacta %s no existe en %s; no se borró nada.\n' "$stack_name" "$region" >&2
      exit 1
    fi
    printf 'Recursos que pertenecen a %s:\n' "$stack_name"
    aws cloudformation describe-stack-resources --stack-name "$stack_name" --region "$region" --output table
    if [[ "$apply" != true ]]; then
      printf 'No se hicieron cambios. Revise la lista y repita con --apply.\n'
      exit 0
    fi
    printf 'Eliminando únicamente la pila %s en %s...\n' "$stack_name" "$region"
    aws cloudformation delete-stack --stack-name "$stack_name" --region "$region"
    aws cloudformation wait stack-delete-complete --stack-name "$stack_name" --region "$region"
    printf 'Pila eliminada: %s\n' "$stack_name"
    ;;
  *)
    usage
    exit 2
    ;;
esac
