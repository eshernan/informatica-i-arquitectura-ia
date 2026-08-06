# LibreReserva

Incremento vertical mínimo usado por todos los módulos. El núcleo de dominio no depende de FastAPI; la API es un adaptador reemplazable.

## Instalación

Desde la raíz:

```bash
./scripts/setup_python.sh --apply
make test
make run
```

## Prueba manual

```bash
curl -fsS http://127.0.0.1:8000/salud/viva

curl -i -X POST http://127.0.0.1:8000/reservas \
  -H 'content-type: application/json' \
  -d '{"recurso":"A-101","inicio":"2026-08-10T08:00:00Z","fin":"2026-08-10T09:00:00Z"}'

curl -fsS http://127.0.0.1:8000/reservas
```

El segundo POST con el mismo intervalo debe responder `409`. Un intervalo invertido debe responder `422`.

## Evolución esperada

Los módulos añaden puertos de persistencia, PostgreSQL, eventos, autenticación, telemetría, contenedor y despliegue. No incorpore todo desde el comienzo: cada cambio debe responder a un riesgo o resultado de aprendizaje.
