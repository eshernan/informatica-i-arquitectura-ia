# Guía docente para publicar el bloque en AWS Academy

AWS Academy Cloud Foundations y el proyecto LibreReserva se administran como recorridos paralelos. Los módulos 1–8 de Cloud Foundations se registran como desarrollados; el módulo 9 acompaña la semana 10 y el módulo 10 acompaña la semana 14. Las prácticas del proyecto usan el ambiente local acumulativo.

## 1. Preparar la clase

1. Seleccione la clase institucional de Informática I.
2. Publique el enlace a la revisión del repositorio que usarán los equipos.
3. Publique la actividad semanal con el README de la sesión y la plantilla de evidencia.
4. Verifique la práctica desde un clon limpio antes de abrirla.
5. Cuando una actividad oficial de Cloud Foundations requiera Learner Lab, comunique región, restricciones, crédito y procedimiento de limpieza.

Los estudiantes no usan cuentas AWS personales ni almacenan credenciales temporales en Git.

## 2. Formato de la actividad

```text
Título: SNN — LibreReserva — nombre de la sesión
Disponibilidad: miércoles, 5:45 p. m. a 10:15 p. m.
Duración esperada: 4 horas
Lectura principal: README de la sesión
Revisión base: rama, etiqueta o commit
Entrega: pull request y evidencia Markdown
Criterio de cierre: incremento demostrado y entorno local detenido
```

Para la semana 15, la ventana corresponde a trabajo autónomo y permanece disponible durante las cuatro horas acordadas.

## 3. Validación docente

Antes de publicar:

1. clone la revisión en un directorio limpio;
2. ejecute `make check`;
3. ejecute las pruebas disponibles para el estado de esa semana;
4. revise el Compose, las migraciones y las variables requeridas;
5. complete el caso feliz y el caso de fallo de la sesión;
6. confirme que la evidencia solicitada cabe en cuatro horas;
7. compruebe que ninguna instrucción requiere una tecnología fuera de la ruta.

## 4. Matriz de publicación

| Sesión | Publicar | Verificación docente |
|---:|---|---|
| 9 | Docker y despliegue local | imagen, API y pérdida de estado al reiniciar |
| 10 | persistencia en archivos con múltiples instancias | balanceo, carrera sobre Parquet y bloqueo local |
| 11 | persistencia y API confiable, ya trabajadas | registrar cobertura docente y evidencia de implementación por equipo |
| 12 | pruebas y entrega trazable | prueba que detecta una regresión, CI e imagen por commit |
| 13 | configuración y despliegue seguro | variables, ausencia de secretos, permisos y arranque reproducible |
| 14 | diagnóstico y recuperación de datos | logs, medición, respaldo, restauración y runbook |
| 15 | integración autónoma | recorrido completo desde clon limpio |
| 16 | cierre | demostración, decisiones y deuda reconocida |

## 5. Uso de AWS Academy

El ajuste del 2 de noviembre reconoce que idempotencia, errores, salud y recuperación ya se trabajaron el 28 de octubre. Publique para el 4 de noviembre la actividad de pruebas/CI. Reserve 10 minutos iniciales para comprobar pendientes por equipo y 40 minutos para explicar fundamentos antes del caso. No cambie fechas ni añada nuevas plataformas para ocupar el espacio liberado.

- Módulo 9: relacionar sus principios con los escenarios y ADR de la semana 10.
- Módulo 10: relacionar monitoreo, balanceo y escalado con las señales y el runbook de la semana 14.
- Learner Lab se inicia únicamente si la actividad oficial lo exige.
- Cualquier recurso creado se identifica por equipo, se mide y se elimina al terminar.
- No se publican plantillas de Lambda, DynamoDB, SQS o ECR como ruta de LibreReserva.

## 6. Cierre

La entrega final se evalúa sobre la definición de terminado del proyecto, no por cantidad de servicios utilizados. Antes de cerrar la clase, revise los recursos AWS creados durante actividades oficiales y registre los incidentes de permisos como restricciones de plataforma.

## Fuentes de operación

- [AWS Academy](https://aws.amazon.com/training/awsacademy/)
- [AWS Academy FAQ](https://aws.amazon.com/training/awsacademy/faq/)
