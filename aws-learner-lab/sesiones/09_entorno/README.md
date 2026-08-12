# Sesión 9 — Entorno reproducible y línea base

**Fecha:** 14 de octubre de 2026, 6:00–10:00 p. m.
**Resultado:** ejecutar LibreReserva localmente, entrar a Learner Lab y desplegar una pila mínima sin confundir entorno, aplicación e infraestructura.

## Montaje docente en AWS Academy

Publique `S09 — LibreReserva — entorno y línea base` con enlaces a este archivo, `PREPARACION_ANTES_SESION_9.md`, `s09-foundation.yaml` y la plantilla de evidencia. Configure la entrega para las 10:10 p. m. e indique región y formato de equipo. Antes de abrirla, pruebe S3 y CloudFormation con un usuario estudiantil.

## Secuencia de cuatro horas

| Hora | Tema y acción |
|---|---|
| 6:00–6:20 | acceso, identidad temporal, región y reglas de seguridad |
| 6:20–7:10 | reproducibilidad, configuración, infraestructura efímera y responsabilidad compartida |
| 7:10–7:50 | demo de LibreReserva local y de una pila CloudFormation |
| 8:00–9:25 | taller: línea base local, despliegue, objeto S3 y cambio reproducible |
| 9:25–9:50 | comparar evidencia local/AWS, costo y restricciones |
| 9:50–10:00 | vaciar bucket, borrar pila y comprobar limpieza |

## Taller

```bash
./scripts/check_environment.sh
make test
export AWS_REGION=REGION_ACORDADA
./aws-learner-lab/scripts/check_preparation.sh

./aws-learner-lab/scripts/stack.sh deploy \
  libre-reserva-s09-equipoXX \
  aws-learner-lab/templates/s09-foundation.yaml --apply

bucket_name="$(aws cloudformation describe-stacks \
  --stack-name libre-reserva-s09-equipoXX \
  --region "$AWS_REGION" \
  --query 'Stacks[0].Outputs[?OutputKey==`BucketName`].OutputValue' \
  --output text)"
[[ -n "$bucket_name" && "$bucket_name" != "None" ]] || exit 1
printf '{"equipo":"XX","estado":"preparado"}\n' > /tmp/libre-reserva-s09-equipoXX.json
aws s3 cp /tmp/libre-reserva-s09-equipoXX.json "s3://$bucket_name/evidencia.json"
aws s3 cp "s3://$bucket_name/evidencia.json" -
```

Cambie una regla del dominio en una rama del equipo, añada una prueba que falle primero y deje la suite verde. Explique qué parte pertenece al entorno local, cuál a AWS y cuál al repositorio.

## Validación y limpieza

```bash
aws s3 rm "s3://$bucket_name/evidencia.json"
./aws-learner-lab/scripts/stack.sh delete libre-reserva-s09-equipoXX --apply
aws cloudformation list-stacks --region "$AWS_REGION" \
  --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE
```

**Evidencia:** salida de pruebas, identidad parcialmente oculta, región, commit, nombre del bucket, lectura del objeto y confirmación de limpieza.

**Ruta local:** todo el ejercicio de dominio y Git funciona sin AWS; si Learner Lab falla, documente el incidente y use un directorio temporal como adaptador de evidencia.
