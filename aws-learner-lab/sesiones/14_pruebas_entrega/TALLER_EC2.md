# Taller de operación de LibreReserva en EC2

**18 de noviembre de 2026.** Trabaja en la EC2 de tu equipo y utiliza datos ficticios. Sigue la [preparación de Learner Lab](PREPARACION_AWS_LEARNER_LAB.md) hasta que `GET /reservas` devuelva una lista. Usa la misma sesión Bash para los comandos.

~~~bash
dc=(sudo librereserva-compose)
"${dc[@]}" ps
sudo cat /var/lib/librereserva/commit /var/lib/librereserva/image-id
"${dc[@]}" exec -T api_a id
~~~

Si preparaste EC2 de forma interactiva, ejecuta los comandos desde la raíz del clon y usa `dc=(sudo docker compose -f modules/06_apis_datos_eventos/compose.yml)`. Obtén la revisión con `git rev-parse HEAD` y el ID de imagen con `sudo docker image inspect localhost/librereserva:0.1.0 --format '{{.Id}}'`.

## Reserva persistente

Envía esta reserva de ejemplo. Si el intervalo ya está ocupado, cambia las horas y conserva el ID que devuelve la API.

~~~bash
curl -fsS -X POST http://127.0.0.1:8080/reservas \
  -H 'Content-Type: application/json' \
  -d '{"recurso":"A-101","inicio":"2026-12-03T15:00:00-05:00","fin":"2026-12-03T16:00:00-05:00"}'
~~~

Recrea las API y Caddy en una sola operación para que el balanceador vuelva a resolver sus destinos. `--no-deps` deja PostgreSQL en ejecución. Busca en la respuesta la reserva que acabas de crear.

~~~bash
"${dc[@]}" up -d --no-deps --force-recreate api_a api_b balanceador
curl -fsS --retry 8 --retry-all-errors --retry-delay 1 \
  http://127.0.0.1:8080/reservas
~~~

## Fallo de PostgreSQL

Detén PostgreSQL brevemente y registra hora, código HTTP y tiempo de respuesta. Contrasta la consulta con `/salud/lista` y con los logs. Después inicia PostgreSQL y repite la consulta.

~~~bash
"${dc[@]}" stop postgres
date -u
curl -sS --max-time 15 -o /dev/null -w 'reservas HTTP %{http_code} en %{time_total}s\n' \
  http://127.0.0.1:8080/reservas
curl -sS --max-time 15 -o /dev/null -w 'salud HTTP %{http_code}\n' \
  http://127.0.0.1:8080/salud/lista
"${dc[@]}" logs --since 2m --tail 40 api_a api_b
"${dc[@]}" up -d --wait --wait-timeout 120 postgres
curl -fsS --retry 8 --retry-all-errors --retry-delay 1 \
  http://127.0.0.1:8080/reservas
~~~

## Respaldo y restauración en una base separada

El bloque pausa el acceso de la aplicación mientras compara un estado conocido. Guarda el respaldo y dos listados SQL en un directorio privado de EC2. Si falla un paso, el bloque vuelve a iniciar los servicios originales al salir y conserva los archivos generados para el diagnóstico.

~~~bash
evidencia="$(mktemp -d "$HOME/librereserva-evidencia.XXXXXXXX")"
destino="reservas_restaurada_$(date -u +%Y%m%d%H%M%S)_$$"
consulta='SELECT id, recurso, inicio, fin FROM reservas ORDER BY id'

(
  set -euo pipefail
  trap '"${dc[@]}" up -d api_a api_b balanceador' EXIT
  "${dc[@]}" stop balanceador api_a api_b
  "${dc[@]}" exec -T postgres psql -X -v ON_ERROR_STOP=1 -U curso -d reservas \
    --csv -c "$consulta" > "$evidencia/origen.csv"
  "${dc[@]}" exec -T postgres pg_dump -U curso -Fc reservas \
    > "$evidencia/reservas.dump"
  "${dc[@]}" exec -T postgres createdb -U curso -T template0 "$destino"
  time "${dc[@]}" exec -T postgres pg_restore -U curso --exit-on-error \
    --single-transaction -d "$destino" < "$evidencia/reservas.dump"
  "${dc[@]}" exec -T postgres psql -X -v ON_ERROR_STOP=1 -U curso -d "$destino" \
    --csv -c "$consulta" > "$evidencia/restaurada.csv"
  diff -u "$evidencia/origen.csv" "$evidencia/restaurada.csv"
  printf 'Filas verificadas en %s. Evidencias en %s\n' "$destino" "$evidencia"
)
~~~

Si el bloque termina correctamente, abre una API temporal contra la base restaurada. El nombre de la base se sustituye dentro del contenedor y la cadena de conexión permanece en su entorno.

~~~bash
"${dc[@]}" run --rm --no-deps -p 127.0.0.1:18081:8000 api_a sh -ec '
  export DATABASE_URL="${DATABASE_URL%/*}/$1"
  exec python -m uvicorn labs.librereserva.app.main:app --host 0.0.0.0 --port 8000
' sh "$destino"
~~~

Desde otra terminal de la misma EC2, ejecuta `curl -fsS http://127.0.0.1:18081/reservas` y confirma que aparece el ID registrado. Detén la API temporal con Ctrl+C. El resultado verifica una restauración lógica dentro del mismo servidor. Registra la duración de `pg_restore` y el tiempo observado de recuperación de la aplicación como mediciones distintas.

## Evidencia y cierre

- Registra commit, imagen, ID de la reserva y los códigos HTTP antes, durante y después del fallo.
- Conserva el respaldo, el resultado de la comparación y el ID observado en la API temporal. Indica si la comprobación llegó hasta SQL o también recibió respuesta HTTP.
- Si los permisos del lab lo permiten, añade el resultado del piloto de Parameter Store o CloudWatch Logs. Sigue los [pasos de comprobación](PREPARACION_AWS_LEARNER_LAB.md#5-secretos-registros-y-evidencias).
- Guarda la evidencia requerida fuera de EC2 y sigue las reglas del laboratorio para cerrar la instancia del equipo.
