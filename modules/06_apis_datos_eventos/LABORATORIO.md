# Laboratorio acumulativo: PostgreSQL y API confiable

La API inicial guarda reservas en la memoria del proceso. La sesión 10 mostró que dos instancias mantienen agendas distintas y que compartir un Parquet requiere serializar en la aplicación todo el ciclo leer, validar y escribir. Este laboratorio reemplaza esas soluciones por PostgreSQL en dos incrementos consecutivos. Todo cambio se realiza sobre LibreReserva; no se crea una API paralela.

## Preparación común

Desde la raíz del repositorio, elija un motor:

```bash
docker build -f labs/librereserva/Containerfile \
  -t localhost/librereserva:0.1.0 labs/librereserva
./modules/06_apis_datos_eventos/start_services.sh --motor docker
./modules/06_apis_datos_eventos/start_services.sh --motor docker --apply
docker exec librereserva-postgres pg_isready -U curso -d reservas
```

Con Podman, sustituya `docker` por `podman`. Revise antes la imagen, el volumen, el puerto y las credenciales de laboratorio definidos en `compose.yml`.

## Sesión 11: persistencia e integridad

### Incremento 1. Puerto y adaptadores

Revise el puerto en `labs/librereserva/app/ports.py` y los adaptadores en
`labs/librereserva/app/adapters/`. La variable `LIBRERESERVA_REPOSITORY`
selecciona `memory` o `postgres`; el dominio no importa `psycopg`.

Ejecute la misma prueba de contrato contra memoria y PostgreSQL:

```bash
LIBRERESERVA_TEST_DATABASE_URL=\
'postgresql://curso:solo-laboratorio@127.0.0.1:5432/reservas' \
  .venv/bin/python -m unittest \
  labs.librereserva.tests.test_repository_contract -v
```

### Incremento 2. Migración

La migración `labs/librereserva/migrations/001_crear_reservas.sql` crea la
tabla, valida que `fin > inicio` y protege el solapamiento del mismo recurso
entre todas las instancias mediante una restricción `EXCLUDE`.

Ejecútela como una operación separada antes de iniciar las réplicas:

```bash
docker compose -f modules/06_apis_datos_eventos/compose.yml \
  run --rm migracion
docker compose -f modules/06_apis_datos_eventos/compose.yml \
  up -d api_a api_b balanceador
docker compose -f modules/06_apis_datos_eventos/compose.yml ps
```

No haga que cada API modifique el esquema durante su arranque.

### Incremento 3. Durabilidad

Cree una reserva mediante Caddy:

```bash
curl -i -X POST http://127.0.0.1:8080/reservas \
  -H 'content-type: application/json' \
  -d '{"recurso":"A-101","inicio":"2026-10-28T18:00:00-05:00","fin":"2026-10-28T19:00:00-05:00"}'
curl -fsS http://127.0.0.1:8080/reservas
```

Reinicie únicamente una réplica y vuelva a consultar por el balanceador:

```bash
docker compose -f modules/06_apis_datos_eventos/compose.yml restart api_a
for intento in 1 2 3 4; do
  curl -fsS http://127.0.0.1:8080/reservas
  echo
done
```

La reserva debe conservar el mismo identificador, recurso e intervalo.

### Incremento 4. Concurrencia

Prepare el cuerpo fuera del repositorio y envíe dos solicitudes simultáneas:

```bash
printf '%s\n' \
  '{"recurso":"B-202","inicio":"2026-10-28T18:30:00-05:00","fin":"2026-10-28T19:30:00-05:00"}' \
  > /tmp/solicitud-conflictiva.json

for intento in 1 2; do
  curl -sS -o /tmp/respuesta-$intento.json \
    -w '%{http_code}\n' \
    -X POST http://127.0.0.1:8080/reservas \
    -H 'content-type: application/json' \
    -d @/tmp/solicitud-conflictiva.json &
done
wait
```

El resultado debe contener exactamente un `201` y un `409`. Una comprobación
`SELECT` seguida de `INSERT` sin protección en PostgreSQL no es suficiente.
La restricción debe funcionar aunque cada solicitud llegue a una réplica
diferente.

**Evidencia de sesión 11:** puerto, adaptadores, migración única, prueba de contrato, consultas consistentes mediante Caddy, reinicio con datos y prueba concurrente `201`/`409`.

## Sesión 12: idempotencia y recuperación

### Incremento 5. Clave de idempotencia

1. Reciba una clave de idempotencia al crear una reserva.
2. Almacene clave, huella de la solicitud y respuesta dentro de la transacción.
3. Misma clave y mismo contenido: entregue el resultado anterior sin crear otra reserva.
4. Misma clave y contenido diferente: responda conflicto.
5. Añada pruebas HTTP y de integración.

### Incremento 6. Vida y disponibilidad

- `/salud/viva` indica que el proceso HTTP responde.
- `/salud/lista` comprueba que PostgreSQL acepta una operación liviana dentro de un tiempo máximo.
- Una dependencia caída produce una respuesta controlada; no expone credenciales ni una traza interna al cliente.

### Incremento 7. Fallo y recuperación

1. Cree datos de prueba.
2. Detenga PostgreSQL sin eliminar el volumen.
3. Compruebe vida, disponibilidad y respuesta de una operación que necesita datos.
4. Inicie PostgreSQL.
5. Espere la recuperación y vuelva a consultar los datos.

| Experimento | Resultado esperado |
|---|---|
| repetir solicitud con misma clave y contenido | mismo resultado, sin segunda reserva |
| reutilizar clave con contenido diferente | conflicto |
| PostgreSQL detenido | vida diferenciada de disponibilidad |
| PostgreSQL iniciado nuevamente | disponibilidad recuperada y datos conservados |

**Evidencia de sesión 12:** migración de idempotencia, pruebas, respuestas HTTP y logs de caída/recuperación.

## Cierre del laboratorio

Detenga los contenedores sin borrar el volumen si continuará en la siguiente sesión:

```bash
docker compose -f modules/06_apis_datos_eventos/compose.yml stop
```

Use el comando equivalente de Podman cuando corresponda. La eliminación del volumen se realiza únicamente durante el ejercicio controlado de restauración de la sesión 14 y después de comprobar su nombre.
