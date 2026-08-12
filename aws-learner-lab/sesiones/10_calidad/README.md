# Sesión 10 — Atributos de calidad medibles

**Fecha:** 21 de octubre de 2026, encuentro virtual de 6:00–10:00 p. m.
**Resultado:** convertir expectativas de calidad de LibreReserva en escenarios con estímulo, respuesta, medida y umbral; automatizar al menos una función de aptitud.

## Montaje docente en AWS Academy

Publique `S10 — LibreReserva — calidad medible` con este archivo, el notebook `modules/02_calidad/escenarios_calidad.ipynb` y la plantilla de evidencia. No despliegue infraestructura obligatoria: mantenga el Learner Lab disponible solo para consultar CloudWatch y relacionar métricas con escenarios. La entrega debe incluir el notebook sin salidas guardadas y la función automatizada.

## Secuencia de cuatro horas

| Hora | Tema y acción |
|---|---|
| 6:00–6:20 | revisión de línea base y activación del Learner Lab |
| 6:20–7:10 | calidad como respuesta medible: rendimiento, disponibilidad, modificabilidad y seguridad |
| 7:10–7:50 | demo de escenario, métrica y umbral; lectura de métricas de AWS |
| 8:00–9:25 | taller en notebook y prueba automatizada |
| 9:25–9:50 | análisis de falsos positivos y costo de medición |
| 9:50–10:00 | cierre; esta sesión no debe dejar recursos AWS |

## Taller

1. Formule cuatro escenarios: conflicto concurrente, latencia de consulta, recuperación y cambio de adaptador.
2. Complete el notebook y seleccione un escenario para convertirlo en prueba.
3. Ejecute una carga pequeña contra LibreReserva local; mida p50/p95 y tasa de error.
4. Relacione cada medida con una métrica que existiría en CloudWatch, sin inventar datos.
5. Falle deliberadamente el umbral y restáurelo con un cambio justificado.

```bash
./scripts/setup_python.sh --apply
.venv/bin/jupyter lab modules/02_calidad/escenarios_calidad.ipynb
make test-all
aws cloudwatch list-metrics --region "$AWS_REGION" --max-items 10
```

## Validación

Cada escenario debe contener fuente, estímulo, entorno, artefacto, respuesta, medida y umbral. La función de aptitud debe fallar ante una regresión observable y ejecutarse desde un clon limpio.

**Evidencia:** cuatro escenarios, una función automatizada, resultados medidos, explicación del umbral y confirmación de cero recursos nuevos.

**Ruta local:** es la ruta principal de esta sesión; Jupyter, pytest y LibreReserva son software libre. AWS se usa únicamente para reconocer el modelo de métricas.
