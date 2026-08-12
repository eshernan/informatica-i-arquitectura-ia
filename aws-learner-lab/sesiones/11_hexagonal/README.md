# Sesión 11 — Modularidad, dominio y núcleo hexagonal

**Fecha:** 28 de octubre de 2026, 6:00–10:00 p. m.
**Resultado:** separar el dominio de LibreReserva de DynamoDB mediante un puerto y dos adaptadores intercambiables.

## Montaje docente en AWS Academy

Publique `S11 — LibreReserva — dominio hexagonal` con este archivo, `s11-dynamodb.yaml`, `labs/librereserva/app/domain.py` y la evidencia. Verifique que el rol estudiantil pueda administrar una tabla DynamoDB creada por CloudFormation. No se requiere Lambda ni un rol nuevo.

## Secuencia de cuatro horas

| Hora | Tema y acción |
|---|---|
| 6:00–6:20 | prueba de dominio y revisión de atributos de calidad |
| 6:20–7:10 | dependencias, puertos, adaptadores y modelo de datos DynamoDB |
| 7:10–7:50 | demo de tabla, claves y condición de escritura |
| 8:00–9:25 | taller: puerto de repositorio, adaptador en memoria y adaptador DynamoDB |
| 9:25–9:50 | pruebas de contrato y comparación de acoplamiento/costo |
| 9:50–10:00 | borrar ítems y pila |

## Taller AWS

```bash
./aws-learner-lab/scripts/stack.sh deploy \
  libre-reserva-s11-equipoXX \
  aws-learner-lab/templates/s11-dynamodb.yaml --apply

table_name="$(aws cloudformation describe-stacks \
  --stack-name libre-reserva-s11-equipoXX --region "$AWS_REGION" \
  --query 'Stacks[0].Outputs[?OutputKey==`TableName`].OutputValue' --output text)"
[[ -n "$table_name" && "$table_name" != "None" ]] || exit 1

aws dynamodb put-item --table-name "$table_name" --region "$AWS_REGION" \
  --item '{"resource_id":{"S":"A-101"},"start_reservation_id":{"S":"2026-10-28T20:00:00Z#demo"},"fin":{"S":"2026-10-28T21:00:00Z"}}' \
  --condition-expression 'attribute_not_exists(resource_id) AND attribute_not_exists(start_reservation_id)'

aws dynamodb query --table-name "$table_name" --region "$AWS_REGION" \
  --key-condition-expression 'resource_id = :resource' \
  --expression-attribute-values '{":resource":{"S":"A-101"}}'
```

Implemente un protocolo `RepositorioReservas`, mantenga el adaptador en memoria y añada un adaptador DynamoDB. Ejecute la misma prueba de contrato contra ambos. Explique por qué una condición por clave no resuelve por sí sola todos los solapamientos temporales.

## Validación y limpieza

```bash
aws dynamodb delete-item --table-name "$table_name" --region "$AWS_REGION" \
  --key '{"resource_id":{"S":"A-101"},"start_reservation_id":{"S":"2026-10-28T20:00:00Z#demo"}}'
./aws-learner-lab/scripts/stack.sh delete libre-reserva-s11-equipoXX --apply
```

**Evidencia:** diagrama de dependencias, contrato del puerto, pruebas sobre dos adaptadores, consulta DynamoDB, limitación de consistencia y limpieza.

**Ruta local:** un adaptador SQLite o en memoria permite completar los mismos resultados sin AWS.
