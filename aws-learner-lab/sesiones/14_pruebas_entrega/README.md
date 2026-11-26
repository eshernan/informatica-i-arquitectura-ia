# Sesión 14 — Diagnóstico y recuperación de datos

**Fecha:** 18 de noviembre de 2026, 6:00–10:00 p. m.
**Clase integrada:** configuración, despliegue, diagnóstico y recuperación de LibreReserva.
**Resultado:** ejecutar una imagen identificada, explicar su configuración, diagnosticar un fallo de dependencia y comprobar una restauración.

**Diapositivas:** [Configuración, diagnóstico y recuperación](../../../presentaciones/14-configuracion-diagnostico-y-recuperacion.pptx) · [Taller AWS Learner Lab](../../../presentaciones/14-taller-aws-learner-lab.pptx).

## Alcance ajustado

El docente confirmó que la clase del 11 de noviembre se suspendió. Este encuentro incorpora los fundamentos de la [sesión 13](../13_api_eventos/README.md) y los temas esenciales de operación de hoy en un solo recorrido práctico.

Las pruebas automatizadas y de desempeño se trabajaron el 4 de noviembre. Se recupera brevemente su evidencia, sin repetir las tandas de 1.000, 2.000, 5.000 y 6.000 consultas. La arquitectura conserva FastAPI, Caddy, Compose y PostgreSQL. Aunque las réplicas puedan reemplazarse, los datos deben permanecer.

Se distingue lo implementado de lo propuesto: la API recibe configuración externa y usa PostgreSQL, pero la referencia mantiene respuestas fijas en los endpoints de salud y aún necesita correlación de solicitudes. Los ejemplos de logs estructurados y Compose parametrizado se identifican como propuestas, sin atribuirles ejecución actual.

## Secuencia de cuatro horas

| Hora | Actividad |
|---|---|
| 6:00–6:10 | Revisar la entrega y la evidencia de desempeño ya trabajada |
| 6:10–7:00 | Código, configuración, secretos, imagen y permisos |
| 7:00–7:35 | Demostrar el arranque reproducible y una reserva persistente |
| 7:35–7:45 | Pausa |
| 7:45–8:20 | Señales, diagnóstico y caída breve de PostgreSQL |
| 8:20–8:45 | Respaldo, restauración, RPO y RTO |
| 8:45–9:40 | Práctica integrada por parejas |
| 9:40–10:00 | Revisión de evidencia y preparación de la integración |

## Preparación docente

- El laboratorio de esta clase se ejecuta en EC2 dentro de AWS Academy Learner Lab. Sigue la [guía de preparación del sandbox](PREPARACION_AWS_LEARNER_LAB.md) para probar Session Manager con `LabInstanceProfile`, preparar las imágenes y comprobar la API. SSH queda disponible como ruta de respaldo cuando el lab lo autoriza.
- Conservar una imagen local identificada y el ambiente de PostgreSQL disponible. El artefacto de CI del 4 de noviembre pudo caducar por su retención de tres días.
- Ensayar el orden PostgreSQL disponible, migración completada, API y balanceador. El [Compose actual](../../../modules/06_apis_datos_eventos/compose.yml) no hace depender las API de la terminación de la migración.
- Llevar un resumen de desempeño y logs identificados como alternativa si algún equipo no puede levantar el ambiente.
- Utilizar valores ficticios y datos de laboratorio. La parametrización de Compose y el ejemplo de entorno siguen como ajustes si no se implementaron.
- Preparar una base de destino vacía y separada para la restauración lógica. El origen se conserva durante el ensayo.

## Demostración y taller

Ejecuta los pasos con la [guía práctica en EC2](TALLER_EC2.md). Usa solo la instancia y los datos ficticios de tu equipo.

1. Identificar la imagen y las variables `LIBRERESERVA_REPOSITORY` y `DATABASE_URL`. Comprobar el usuario no privilegiado que ya define la imagen.
2. Iniciar PostgreSQL, ejecutar la migración y luego iniciar las API y Caddy. Cada paso debe terminar correctamente antes de continuar.
3. Crear una reserva conocida, recrear las API y Caddy con PostgreSQL en ejecución y volver a consultarla.
4. Registrar hora y ruta de una consulta. Detener brevemente PostgreSQL y contrastar la respuesta con los logs disponibles. Recuperar el servicio y esperar a que esté disponible antes de consultar otra vez.
5. Explicar por qué una respuesta fija de salud no demuestra conexión a PostgreSQL. La correlación por identificador se presenta como objetivo de instrumentación.
6. Con las escrituras detenidas para comparar un estado conocido, conservar las filas esperadas y generar un respaldo con `pg_dump -Fc` fuera del contenedor.
7. Restaurar mediante `pg_restore --exit-on-error` en una base vacía de nombre nuevo, conservando la base de origen.
8. Comparar las filas ordenadas y consultar la reserva conocida desde una API temporal conectada a la base restaurada. Detener esa API y reanudar las originales.
9. Registrar instrucciones, resultado, duración, reversión y pendientes en un procedimiento breve de recuperación.

La práctica por parejas distribuye 20 minutos para configuración y despliegue, 15 para diagnóstico y 20 para respaldo y verificación. Si no se ejecuta la consulta HTTP del destino, se registra que la comprobación quedó limitada a SQL. Las capturas y logs excluyen credenciales reales, cuerpos sensibles y datos personales.

La restauración en otra base del mismo servidor demuestra recuperación lógica, sin demostrar recuperación del host ni del volumen. El [25 de noviembre](../15_proyecto/README.md) se retoma el ejercicio de secretos en local y se diseña la verificación del respaldo. El [2 de diciembre](../16_cierre/README.md) el grupo ensaya la restauración en un volumen limpio separado y registra las brechas de disponibilidad y de correlación de logs. No se elimina el volumen de origen durante esta clase integrada.

## Validación y evidencia

La evidencia reúne imagen identificada, variables documentadas, usuario de ejecución, reserva persistente, solicitud fallida relacionada con registros, respaldo, destino de restauración y reservas verificadas. Distingue lo ejecutado, lo observado en la demostración y lo pendiente.

RPO expresa el objetivo de pérdida tolerable de datos en tiempo. RTO expresa el objetivo de tiempo para recuperar el servicio. Se comparan con un ejemplo didáctico, sin confundir objetivos con resultados medidos.

Una ejecución verde de pruebas funcionales no sustituye la restauración comprobada. Conservar un archivo de respaldo sin restaurarlo tampoco verifica recuperación.

El módulo 10 de Cloud Foundations permite relacionar las señales de la aplicación con servicios gestionados. El laboratorio de hoy ejecuta el mismo ambiente acumulativo de Compose dentro de EC2.
