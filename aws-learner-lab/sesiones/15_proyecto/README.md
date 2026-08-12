# Sesión 15 — Jornada autónoma de proyecto

**Fecha:** 25 de noviembre de 2026, cuatro horas de trabajo autónomo, sin encuentro sincrónico.
**Resultado:** integrar un incremento demostrable de LibreReserva sin introducir servicios nuevos ni trasladar deuda de limpieza a la sesión final.

## Montaje docente en AWS Academy

Publique `S15 — LibreReserva — jornada autónoma` al menos 48 horas antes. Mantenga Learner Lab disponible durante la franja acordada y adjunte este archivo, la evidencia y la rúbrica. Habilite un canal institucional de consultas y anuncie dos puntos de control asincrónicos. No añada una plantilla nueva: cada equipo reutiliza únicamente servicios ya probados en sesiones 9–14.

## Plan de cuatro horas

| Tiempo | Actividad y evidencia |
|---:|---|
| 0:00–0:20 | seleccionar una historia, criterio de aceptación y riesgo |
| 0:20–1:00 | diseñar cambio y actualizar ADR/diagrama |
| 1:00–2:30 | implementar en rama corta con pruebas |
| 2:30–3:15 | integrar, desplegar localmente o en Learner Lab y ejecutar caso de fallo |
| 3:15–3:40 | revisar seguridad, logs, consumo y reproducibilidad |
| 3:40–4:00 | entregar bitácora, limpiar AWS y preparar demo final |

## Ejercicio propuesto

Cada equipo selecciona una sola capacidad: política de cancelación, consulta por recurso, notificación idempotente o prueba de concurrencia. El incremento debe atravesar dominio, puerto/adaptador, API y pruebas sin exceder lo practicado.

Si usa AWS:

1. inicie una sesión temporal;
2. despliegue una de las plantillas ya aprobadas con nombre `libre-reserva-s15-equipoXX`;
3. registre hora de inicio, recursos y consumo;
4. ejecute caso feliz y caso de fallo;
5. elimine la pila antes de terminar.

## Validación

```bash
make check
make test-all
git status --short
aws cloudformation list-stacks --region "$AWS_REGION" \
  --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE
```

**Entrega:** incremento integrado, bitácora de cuatro horas, pruebas, estado del despliegue, ADR, riesgos y confirmación de limpieza. Una lista de actividades sin un incremento ejecutable no satisface la jornada.

**Ruta local:** Podman, PostgreSQL, RabbitMQ y `kind` son suficientes; AWS no es obligatorio si el incremento elegido no lo necesita.
