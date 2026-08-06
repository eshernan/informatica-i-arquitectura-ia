# Módulo 6. API, datos, consistencia y eventos

## Resultado

Diseñar contratos compatibles, persistencia transaccional, idempotencia y publicación confiable de eventos.

## Instalación paso a paso

1. Prepare Podman con el módulo 1.
2. Revise las imágenes, puertos, volúmenes y credenciales de laboratorio.
3. Muestre el plan y luego inicie los servicios.
4. Compruebe salud sin instalar PostgreSQL ni RabbitMQ en el sistema anfitrión.

```bash
sed -n '1,240p' modules/06_apis_datos_eventos/compose.yml
./modules/06_apis_datos_eventos/start_services.sh
./modules/06_apis_datos_eventos/start_services.sh --apply
podman ps
```

Servicios locales:

- PostgreSQL: `localhost:5432`, base `reservas`.
- RabbitMQ AMQP: `localhost:5672`.
- Consola RabbitMQ: `http://localhost:15672`.

Las credenciales son únicamente de laboratorio y están aisladas en la máquina local. No se reutilizan en ningún entorno.

## Temas

- OpenAPI y compatibilidad evolutiva.
- Idempotencia y concurrencia.
- Transacciones, aislamiento y restricciones de base de datos.
- Mensajería asíncrona y entrega al menos una vez.
- Patrón outbox y consumidores idempotentes.

## Ejercicio

Sustituya la agenda en memoria por un puerto de repositorio PostgreSQL. Añada una restricción que impida solapamientos, una migración y una tabla outbox escrita en la misma transacción. El publicador puede fallar y reintentar sin perder la reserva.

## Validación

```bash
podman exec librereserva-postgres pg_isready -U curso -d reservas
curl -fsS http://localhost:15672 >/dev/null
```

Pruebe dos solicitudes concurrentes y demuestre que solo una reserva incompatible se confirma. Reinicie el publicador y compruebe que el evento pendiente se entrega sin duplicar el efecto.

**Evidencia:** contrato, migración, prueba concurrente, evento y explicación de consistencia.
