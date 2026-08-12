# Sesión 16 — Despliegue, demostración y cierre

**Fecha:** 2 de diciembre de 2026, 6:00–10:00 p. m.
**Resultado:** demostrar LibreReserva desde una revisión identificable, defender decisiones con evidencia y dejar Learner Lab sin recursos del proyecto.

## Montaje docente en AWS Academy

Publique `S16 — LibreReserva — demostración y cierre` con este archivo, la rúbrica final y la evidencia. Asigne ventanas de demostración y exija que cada equipo declare anticipadamente ruta local o AWS y plantilla aprobada. Mantenga 40 minutos finales protegidos para limpieza y auditoría; no permita servicios nuevos en esta sesión.

## Secuencia de cuatro horas

| Hora | Tema y acción |
|---|---|
| 6:00–6:20 | congelar alcance, identificar commit y comprobar entornos |
| 6:20–7:00 | reconstrucción desde clon limpio y preparación de demos |
| 7:00–8:50 | demostraciones: decisión, caso feliz, fallo, medición y recuperación |
| 8:50–9:20 | preguntas cruzadas y retroalimentación |
| 9:20–9:40 | entrega final, trazabilidad y consumo |
| 9:40–10:00 | eliminación y auditoría de recursos por servicio |

## Guion obligatorio de demostración

1. Mostrar commit o etiqueta y arquitectura vigente.
2. Ejecutar pruebas desde un clon limpio.
3. Desplegar con comandos documentados.
4. Crear y consultar una reserva.
5. Repetir una solicitud o provocar un fallo relevante.
6. Mostrar la medición asociada a un atributo de calidad.
7. Relacionar el resultado con un ADR.
8. Eliminar los recursos y mostrar la verificación final.

## Auditoría de limpieza

Revise CloudFormation y, aun si no aparecen pilas activas, inspeccione S3, DynamoDB, SQS, Lambda, API Gateway, CloudWatch Logs y ECR. Una pila fallida puede dejar recursos; cada equipo debe identificar los suyos por nombre y etiquetas, sin borrar recursos ajenos.

```bash
aws cloudformation list-stacks --region "$AWS_REGION" \
  --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE ROLLBACK_COMPLETE \
  --query 'StackSummaries[?starts_with(StackName, `libre-reserva-`)].[StackName,StackStatus]' \
  --output table
git status --short
```

Si aparece una pila del equipo, liste sus recursos, resuelva los depósitos con contenido y elimínela con `stack.sh delete NOMBRE_EXACTO --apply`. No use scripts de borrado masivo.

**Evidencia final:** instrucciones de reproducción, pruebas, artefacto, demo, caso de fallo, medición, ADR, consumo y comprobación de limpieza.

**Ruta local:** la demostración puede hacerse con Podman y `kind`. La evaluación se centra en reproducibilidad y decisiones, no en consumir más servicios AWS.
