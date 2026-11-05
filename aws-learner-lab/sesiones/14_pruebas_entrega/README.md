# Sesión 14 — Diagnóstico y recuperación de datos

**Fecha:** 18 de noviembre de 2026, 6:00–10:00 p. m.
**Resultado:** diagnosticar una solicitud, detectar la indisponibilidad de PostgreSQL y restaurar los datos en un volumen limpio.

## Alcance

Se utiliza la imagen verificada en sesión 12 y la configuración preparada en sesión 13. Vida/disponibilidad y recuperación de PostgreSQL ya se trataron el 28 de octubre, por lo que hoy se usan como señales de diagnóstico, sin volver a implementar los endpoints. La novedad es relacionar solicitudes con logs, medir bajo condiciones declaradas y demostrar una restauración de datos.

## Relación con AWS Academy

El módulo 10 de Cloud Foundations permite relacionar las señales locales con CloudWatch, Elastic Load Balancing y Auto Scaling. La práctica de LibreReserva permanece en el ambiente local acumulativo.

## Secuencia de cuatro horas

| Hora | Tema y acción |
|---|---|
| 6:00–6:20 | desplegar la versión identificada de la semana 13 |
| 6:20–7:10 | logs estructurados, correlación, salud y medición |
| 7:10–7:50 | respaldo, RPO, RTO y procedimiento de restauración |
| 8:00–9:25 | instrumentar lo mínimo y ejecutar respaldo/restauración |
| 9:25–9:50 | inducir fallo y seguir el runbook |
| 9:50–10:00 | congelar alcance para la jornada autónoma |

## Taller

1. Genere o propague un identificador por solicitud.
2. Registre hora, identificador, método, ruta normalizada, estado y duración.
3. No registre cuerpos sensibles, credenciales ni cadenas de conexión.
4. Relacione una solicitud fallida con su log.
5. Mida un conjunto declarado de solicitudes y reporte p50, p95 y tasa de error.
6. Cree un respaldo de PostgreSQL.
7. Detenga el ambiente y elimine únicamente el volumen de laboratorio identificado.
8. Cree un volumen limpio, restaure el respaldo y compruebe las reservas.
9. Escriba un runbook con detección, diagnóstico, recuperación, validación y reversión.

## Validación

La restauración debe demostrarse; conservar un archivo de respaldo sin abrirlo no es suficiente. La medición debe declarar equipo, versión, número de solicitudes y condiciones.

**Evidencia:** logs correlacionados, medición, respaldo, restauración comprobada y runbook.
