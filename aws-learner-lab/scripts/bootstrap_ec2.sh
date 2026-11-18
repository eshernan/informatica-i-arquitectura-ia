#!/bin/bash
# Datos de usuario para Ubuntu Server 24.04 x86_64.
set -Eeuo pipefail
umask 077

# Versión de LibreReserva utilizada en la sesión del 18 de noviembre.
LIBRERESERVA_COMMIT="${LIBRERESERVA_COMMIT:-b01941f4420b65c24a9255054342e084c0a532e6}"

if (( EUID != 0 )); then
  printf '%s\n' 'Este archivo está diseñado para el primer arranque de EC2 como root.' >&2
  exit 1
fi
[[ "${LIBRERESERVA_COMMIT:-}" =~ ^[a-f0-9]{40}$ ]] || {
  printf '%s\n' 'LIBRERESERVA_COMMIT debe ser un SHA Git completo.' >&2
  exit 1
}

state_dir=/var/lib/librereserva
config_dir=/etc/librereserva
app_dir=/opt/librereserva
log=/var/log/librereserva-bootstrap.log

install -d -m 0755 "$state_dir"
touch "$log"
chmod 0600 "$log"
exec >>"$log" 2>&1
trap 'status=$?; printf "FALLO (código %s, línea %s)\n" "$status" "$LINENO" > "$state_dir/estado"; exit "$status"' ERR
printf 'PREPARANDO\n' > "$state_dir/estado"
printf '%s Preparación de LibreReserva. Commit %s\n' "$(date -u +%FT%TZ)" "$LIBRERESERVA_COMMIT"

# shellcheck disable=SC1091
. /etc/os-release
if [[ "$ID" != ubuntu || "$VERSION_ID" != 24.04 || "$(dpkg --print-architecture)" != amd64 ]]; then
  printf 'Se requiere Ubuntu Server 24.04 x86_64.\n'
  false
fi
export DEBIAN_FRONTEND=noninteractive

# Ubuntu oficial normalmente incluye el agente. Si falta, instala la versión estable.
if systemctl cat snap.amazon-ssm-agent.amazon-ssm-agent.service >/dev/null 2>&1; then
  systemctl start snap.amazon-ssm-agent.amazon-ssm-agent.service
elif systemctl cat amazon-ssm-agent.service >/dev/null 2>&1; then
  systemctl enable --now amazon-ssm-agent.service
else
  snap install amazon-ssm-agent --classic
  systemctl start snap.amazon-ssm-agent.amazon-ssm-agent.service
fi

apt-get -o DPkg::Lock::Timeout=120 update
apt-get -o DPkg::Lock::Timeout=120 install -y ca-certificates curl git openssl python3
install -d -m 0755 "$app_dir"
if [[ ! -d "$app_dir/.git" ]]; then
  git -C "$app_dir" init --quiet
  git -C "$app_dir" remote add origin https://github.com/eshernan/informatica-i-arquitectura-ia.git
fi
git -C "$app_dir" fetch --depth 1 origin "$LIBRERESERVA_COMMIT"
git -C "$app_dir" checkout --quiet --detach "$LIBRERESERVA_COMMIT"
if ! docker info >/dev/null 2>&1 || ! docker compose version >/dev/null 2>&1; then
  bash "$app_dir/scripts/install_docker_ubuntu.sh" --apply
fi

install -d -m 0700 "$config_dir"
env_file="$config_dir/compose.env"
if [[ -e "$env_file" ]]; then
  chmod 0600 "$env_file"
elif docker volume inspect librereserva_reservas_pg >/dev/null 2>&1; then
  printf 'Existe el volumen de PostgreSQL. Recupera su configuración original antes de continuar.\n'
  false
else
  pg_password="$(openssl rand -hex 24)"
  {
    printf 'LAB_POSTGRES_PASSWORD=%s\n' "$pg_password"
    printf 'LAB_DATABASE_URL=postgresql://curso:%s@postgres:5432/reservas\n' "$pg_password"
  } > "$env_file"
  unset pg_password
fi

# Compose sustituye las credenciales ficticias de la referencia. Los valores
# viven en la instancia y se leen en tiempo de ejecución.
cat > "$config_dir/compose.ec2.yml" <<'YAML'
x-logs: &logs
  driver: local
  options:
    max-size: "10m"
    max-file: "3"

services:
  postgres:
    environment:
      POSTGRES_PASSWORD: ${LAB_POSTGRES_PASSWORD:?Falta la contraseña local}
    logging: *logs
  migracion:
    environment:
      PGPASSWORD: ${LAB_POSTGRES_PASSWORD:?Falta la contraseña local}
    logging: *logs
  api_a:
    environment:
      DATABASE_URL: ${LAB_DATABASE_URL:?Falta la conexión local}
    logging: *logs
  api_b:
    environment:
      DATABASE_URL: ${LAB_DATABASE_URL:?Falta la conexión local}
    logging: *logs
  balanceador:
    logging: *logs
YAML

cat > /usr/local/bin/librereserva-compose <<'BASH'
#!/bin/bash
set -euo pipefail
exec docker compose --project-name librereserva \
  --env-file /etc/librereserva/compose.env \
  -f /opt/librereserva/modules/06_apis_datos_eventos/compose.yml \
  -f /etc/librereserva/compose.ec2.yml "$@"
BASH
chmod 0755 /usr/local/bin/librereserva-compose

docker build -f "$app_dir/labs/librereserva/Containerfile" \
  -t localhost/librereserva:0.1.0 "$app_dir/labs/librereserva"
docker image inspect localhost/librereserva:0.1.0 --format '{{.Id}}' > "$state_dir/image-id"
printf '%s\n' "$LIBRERESERVA_COMMIT" > "$state_dir/commit"
librereserva-compose config --quiet
librereserva-compose pull postgres balanceador
librereserva-compose up -d --wait --wait-timeout 120 postgres
# Se conserva el log de la migración como evidencia de arranque.
librereserva-compose run --rm --no-deps migracion
librereserva-compose up -d api_a api_b balanceador
curl -fsS --retry 20 --retry-all-errors --retry-delay 2 --max-time 5 \
  http://127.0.0.1:8080/reservas | python3 -c '
import json, sys
if not isinstance(json.load(sys.stdin), list):
    sys.exit("GET /reservas no devolvió una lista")
'
printf 'LISTO\n' > "$state_dir/estado"
printf '%s LibreReserva lista. GET /reservas devolvió una lista.\n' "$(date -u +%FT%TZ)"
