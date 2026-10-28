# Sesión 10 — Persistencia en archivos con múltiples instancias

**Fecha:** 27 de octubre de 2026, encuentro reprogramado de 6:00–10:00 p. m.
**Resultado:** ejecutar dos instancias detrás de un balanceador, persistir reservas en un Parquet compartido y comprobar los efectos de las escrituras concurrentes con y sin bloqueo local.

## Relación con AWS Academy

El módulo 9 de Cloud Foundations aporta el marco de arquitectura en la nube. Sus principios se aplican como preguntas sobre LibreReserva; no se crean recursos AWS ni se diseña una segunda implementación.

## Secuencia de cuatro horas

| Hora | Tema y acción |
|---|---|
| 6:00–6:30 | comprobar la imagen y la API en una instancia |
| 6:30–7:15 | ejecutar dos instancias detrás de Caddy y observar la distribución |
| 7:15–7:50 | persistir reservas en un archivo Parquet compartido |
| 8:00–8:45 | provocar escrituras concurrentes y observar actualizaciones perdidas |
| 8:45–9:30 | repetir con bloqueo de archivo y escritura atómica |
| 9:30–10:00 | comparar resultados, documentar límites y organizar la evidencia |

## Práctica de balanceo local

La práctica usa dos contenedores de LibreReserva y un contenedor Caddy como único punto de entrada. La topología está en [compose-balanceo.yml](compose-balanceo.yml) y la política del proxy en [Caddyfile.balanceo](Caddyfile.balanceo). No incorpora PostgreSQL: su propósito es demostrar que distribuir solicitudes no comparte el estado almacenado en la memoria de cada proceso.

Desde la raíz del repositorio, construya la imagen usada en la sesión 9:

```bash
docker build -f labs/librereserva/Containerfile \
  -t localhost/librereserva:0.1.0 labs/librereserva
```

Revise y levante el ensayo:

```bash
docker compose -p librereserva-s10 \
  -f aws-learner-lab/sesiones/10_calidad/compose-balanceo.yml config
docker compose -p librereserva-s10 \
  -f aws-learner-lab/sesiones/10_calidad/compose-balanceo.yml up -d
docker compose -p librereserva-s10 \
  -f aws-learner-lab/sesiones/10_calidad/compose-balanceo.yml ps
```

El balanceador es el único servicio publicado en el equipo:

```bash
curl -fsS http://127.0.0.1:8080/salud/viva
```

Observe en una terminal qué instancia atiende las solicitudes:

```bash
docker compose -p librereserva-s10 \
  -f aws-learner-lab/sesiones/10_calidad/compose-balanceo.yml \
  logs -f api_a api_b
```

En otra terminal, envíe varias solicitudes al balanceador:

```bash
for intento in 1 2 3 4 5 6; do
  curl -fsS http://127.0.0.1:8080/salud/viva
  echo
done
```

### Estado independiente

Cree una reserva a través del balanceador:

```bash
curl -i -X POST http://127.0.0.1:8080/reservas \
  -H 'content-type: application/json' \
  -d '{"recurso":"A-101","inicio":"2026-10-27T18:00:00-05:00","fin":"2026-10-27T19:00:00-05:00"}'
```

Consulte varias veces el mismo endpoint:

```bash
for intento in 1 2 3 4 5 6; do
  curl -fsS http://127.0.0.1:8080/reservas
  echo
done
```

El resultado puede alternar entre una lista con la reserva y `[]`. Caddy distribuye las solicitudes, pero `api_a` y `api_b` usan repositorios en memoria diferentes. La regla de no solapamiento tampoco se protege entre procesos.

Detenga este primer ensayo antes de reutilizar el puerto 8080:

```bash
docker compose -p librereserva-s10 \
  -f aws-learner-lab/sesiones/10_calidad/compose-balanceo.yml down
```

## Práctica de persistencia en Parquet

Continúe con el [laboratorio de persistencia compartida](LABORATORIO_PARQUET.md). El ejercicio conserva las dos instancias y Caddy, pero reemplaza la memoria de cada proceso por un archivo Parquet montado en ambas APIs.

La primera ejecución no coordina el ciclo leer, validar y escribir. La segunda usa un bloqueo `flock` y reemplazo atómico para mostrar qué mejora y qué limitaciones permanecen. La sesión se limita a archivos Parquet; la persistencia en base de datos corresponde a la sesión siguiente.

## Taller

1. Dibuje la arquitectura inicial: cliente, balanceador, dos API y dos agendas en memoria.
2. Dibuje el experimento: cliente, balanceador, dos API y un archivo Parquet compartido.
3. Ejecute dos escrituras incompatibles sin coordinación y registre las respuestas.
4. Identifique el ciclo crítico leer, validar y escribir, y explique la condición de carrera.
5. Repita la prueba con `flock` y escritura atómica.
6. Compare consistencia, costo de escritura, recuperación y posibilidad de ejecutar réplicas en otros hosts.
7. Entregue los resultados mediante una rama corta y un pull request.

## Validación

Los diagramas deben distinguir memoria por instancia y archivo compartido. El balanceador no cuenta como solución de persistencia. El bloqueo de archivo solo se acepta como mitigación del experimento en un host; no prueba integridad distribuida ni alta disponibilidad.

**Evidencia:** distribución observada, inconsistencia entre agendas, prueba concurrente sin bloqueo, prueba con bloqueo, análisis de Parquet, dos diagramas y pull request revisado.
