# Sesión 11 — Persistencia e integridad

**Fecha:** 28 de octubre de 2026, 6:00–10:00 p. m.
**Resultado:** sustituir la agenda en memoria y el experimento Parquet por un puerto de repositorio y un adaptador PostgreSQL compartido por las dos instancias, con migraciones y protección frente a concurrencia.

## Alcance

Se conserva FastAPI, Caddy y las dos instancias del experimento anterior. PostgreSQL pasa a ser el único almacén operacional. Parquet queda como evidencia comparativa; no se mantiene como adaptador de producción ni se implementa una segunda API.

## Secuencia de cuatro horas

| Hora | Tema y acción |
|---|---|
| 6:00–6:20 | revisar escenarios y levantar PostgreSQL |
| 6:20–7:10 | puertos, adaptadores, transacciones y migraciones |
| 7:10–7:50 | diseño de tablas y regla de no solapamiento |
| 8:00–9:25 | implementar repositorio PostgreSQL y pruebas de integración |
| 9:25–9:50 | reinicio y prueba concurrente |
| 9:50–10:00 | pull request y registro de deuda |

## Preparación

Desde la raíz, revise el plan y levante PostgreSQL con un solo motor:

```bash
docker build -f labs/librereserva/Containerfile \
  -t localhost/librereserva:0.1.0 labs/librereserva
./modules/06_apis_datos_eventos/start_services.sh --motor docker
./modules/06_apis_datos_eventos/start_services.sh --motor docker --apply
docker exec librereserva-postgres pg_isready -U curso -d reservas
```

Sustituya `docker` por `podman` si esa es la ruta preparada por el equipo.
Después ejecute la migración una sola vez y levante las réplicas:

```bash
docker compose -f modules/06_apis_datos_eventos/compose.yml \
  run --rm migracion
docker compose -f modules/06_apis_datos_eventos/compose.yml \
  up -d api_a api_b balanceador
```

## Taller

1. Defina `RepositorioReservas` como puerto del dominio.
2. Mantenga un adaptador en memoria para pruebas unitarias.
3. Implemente el adaptador PostgreSQL.
4. Cree una migración versionada para reservas.
5. Proteja la regla de solapamiento dentro de la base de datos y traduzca la violación de integridad a una respuesta `409`.
6. Ejecute la misma prueba de contrato contra el adaptador en memoria y PostgreSQL.
7. Conecte las dos instancias al mismo PostgreSQL y mantenga Caddy como único punto de entrada.
8. Ejecute una sola vez la migración antes de iniciar o actualizar las réplicas; no permita que cada instancia compita por modificar el esquema.
9. Cree una reserva mediante Caddy, reinicie una instancia y compruebe que la reserva continúa disponible.
10. Envíe mediante Caddy dos solicitudes concurrentes incompatibles y compruebe que solo una se confirma.

Los comandos de migración, reinicio, prueba de contrato y concurrencia se
encuentran en el [laboratorio PostgreSQL](../../../modules/06_apis_datos_eventos/LABORATORIO.md).

## Validación

No basta con iniciar PostgreSQL: ambas API deben leer y escribir a través del puerto. Las pruebas HTTP se ejecutan contra Caddy, no directamente contra una sola instancia. La prueba concurrente debe fallar si se retira la restricción de integridad.

**Evidencia:** puerto, adaptadores, migración única, dos instancias con datos consistentes, reinicio con datos y resultado concurrente `201`/`409` mediante el balanceador.
