# Sesión 13 — API, datos, idempotencia y eventos

**Fecha:** 11 de noviembre de 2026, 6:00–10:00 p. m.
**Resultado:** desplegar un corte vertical serverless de LibreReserva, observar su consistencia y reconocer qué garantías todavía faltan.

## Montaje docente en AWS Academy

Publique `S13 — LibreReserva — API, datos y eventos` con este archivo, `s13-serverless-api.yaml`, el módulo 6 y la evidencia. En el anuncio entregue el **ARN del rol de Lambda ya habilitado por Learner Lab**, nunca credenciales. Pruebe que ese rol pueda escribir DynamoDB/SQS y logs. Si el rol o cualquier servicio está restringido, publique la ruta FastAPI/PostgreSQL/RabbitMQ como principal.

## Secuencia de cuatro horas

| Hora | Tema y acción |
|---|---|
| 6:00–6:20 | contrato y garantías acumuladas |
| 6:20–7:10 | API Gateway, Lambda, DynamoDB, eventos, idempotencia y outbox |
| 7:10–7:50 | demo del corte vertical y trazado de una solicitud |
| 8:00–9:25 | taller: POST/GET, duplicado, cola, logs y prueba concurrente |
| 9:25–9:50 | brecha entre ejemplo y sistema correcto; propuesta de outbox |
| 9:50–10:00 | eliminación de pila |

## Despliegue

```bash
export LAB_ROLE_ARN='ARN_COMUNICADO_POR_EL_DOCENTE'
./aws-learner-lab/scripts/stack.sh deploy \
  libre-reserva-s13-equipoXX \
  aws-learner-lab/templates/s13-serverless-api.yaml \
  LabRoleArn="$LAB_ROLE_ARN" --apply

api_url="$(aws cloudformation describe-stacks \
  --stack-name libre-reserva-s13-equipoXX --region "$AWS_REGION" \
  --query 'Stacks[0].Outputs[?OutputKey==`ApiUrl`].OutputValue' --output text)"
[[ "$api_url" == https://* ]] || exit 1

curl -i -X POST "$api_url/reservas" \
  -H 'content-type: application/json' \
  -H 'idempotency-key: equipoXX-demo-01' \
  -d '{"recurso":"A-101","inicio":"2026-11-11T20:00:00Z","fin":"2026-11-11T21:00:00Z"}'
curl -i -X POST "$api_url/reservas" \
  -H 'content-type: application/json' \
  -H 'idempotency-key: equipoXX-demo-01' \
  -d '{"recurso":"A-101","inicio":"2026-11-11T20:00:00Z","fin":"2026-11-11T21:00:00Z"}'
curl -fsS "$api_url/reservas"
```

La primera solicitud debe responder 201 y la repetición 409. Inspeccione tabla, cola y logs. Luego describa una falla entre `put_item` y `send_message`: la plantilla es deliberadamente un ejemplo para descubrir la doble escritura, no una implementación completa de outbox.

## Ejercicio de diseño

Proponga una evolución con tabla outbox, DynamoDB Streams o publicación transaccional equivalente. Incluya orden, duplicados, reintentos, recuperación y prueba que distinguiría la solución correcta. No amplíe la plantilla durante la clase si eso impide validar y limpiar a tiempo.

## Validación y limpieza

```bash
aws cloudformation describe-stack-resources \
  --stack-name libre-reserva-s13-equipoXX --region "$AWS_REGION" --output table
./aws-learner-lab/scripts/stack.sh delete libre-reserva-s13-equipoXX --apply
```

**Evidencia:** contrato probado, 201/409, ítem, mensaje, logs, análisis de doble escritura, diseño de outbox y limpieza.

**Ruta local:** FastAPI, PostgreSQL y RabbitMQ mediante `modules/06_apis_datos_eventos/`; es la contingencia oficial.
