# Sesión 12 — Decidir antes de distribuir

**Fecha:** 4 de noviembre de 2026, 6:00–10:00 p. m.
**Resultado:** comparar una notificación dentro del monolito con una cola asíncrona y justificar la distribución mediante evidencia de fallos.

## Montaje docente en AWS Academy

Publique `S12 — LibreReserva — decidir antes de distribuir` con este archivo, `s12-messaging.yaml`, el módulo 5 y la evidencia. Pruebe previamente envío, recepción repetida, visibilidad y movimiento a DLQ. Aclare que SQS ofrece entrega al menos una vez y que la idempotencia pertenece al consumidor.

## Secuencia de cuatro horas

| Hora | Tema y acción |
|---|---|
| 6:00–6:20 | estado del núcleo modular y pregunta de distribución |
| 6:20–7:10 | latencia, disponibilidad, consistencia, entrega al menos una vez y costo operativo |
| 7:10–7:50 | demo de SQS, visibility timeout, reintento y DLQ |
| 8:00–9:25 | taller de consumidor idempotente y experimento de fallo |
| 9:25–9:50 | matriz monolito/cola/función y ADR |
| 9:50–10:00 | purga y eliminación |

## Taller AWS

```bash
./aws-learner-lab/scripts/stack.sh deploy \
  libre-reserva-s12-equipoXX \
  aws-learner-lab/templates/s12-messaging.yaml --apply

queue_url="$(aws cloudformation describe-stacks \
  --stack-name libre-reserva-s12-equipoXX --region "$AWS_REGION" \
  --query 'Stacks[0].Outputs[?OutputKey==`QueueUrl`].OutputValue' --output text)"
[[ "$queue_url" == https://* ]] || exit 1

aws sqs send-message --queue-url "$queue_url" --region "$AWS_REGION" \
  --message-body '{"type":"ReservaCreada","id":"demo-01","recurso":"A-101"}'
aws sqs receive-message --queue-url "$queue_url" --region "$AWS_REGION" \
  --wait-time-seconds 10 --visibility-timeout 5 --max-number-of-messages 1
```

No elimine el mensaje recibido; repita la recepción después del tiempo de visibilidad y demuestre el reintento. Construya un consumidor local que guarde identificadores procesados y que produzca un solo efecto aunque reciba el mensaje dos veces. Envíe un mensaje inválido y observe su tratamiento hasta la DLQ.

## Validación y limpieza

```bash
aws sqs purge-queue --queue-url "$queue_url" --region "$AWS_REGION"
./aws-learner-lab/scripts/stack.sh delete libre-reserva-s12-equipoXX --apply
```

**Evidencia:** dos entregas del mismo mensaje, un solo efecto, fallo controlado, estado de DLQ, matriz de decisión, ADR y limpieza.

**Ruta local:** use RabbitMQ con `modules/06_apis_datos_eventos/compose.yml`; documente las diferencias semánticas frente a SQS.
