# Agenda de clases: segundo semestre de 2026

## Información general

- Duración: 16 semanas académicas.
- Horario de los encuentros: miércoles de 6:00 p. m. a 10:00 p. m.
- Encuentros sincrónicos: 15, equivalentes a 60 horas.
- Trabajo de proyecto programado para el 25 de noviembre: 4 horas sin encuentro sincrónico.
- Actividad académica programada: 64 horas.
- Primera sesión: miércoles 12 de agosto de 2026.
- Última sesión: miércoles 2 de diciembre de 2026.
- Semana Universitaria: miércoles 7 de octubre, sin sesión ordinaria.
- Caso conductor y práctica exclusiva del bloque del Dr. Esteban Hernández: LibreReserva. No se exige en las sesiones del Dr. Carlos Montenegro.

La institución debe confirmar si las cuatro horas de proyecto del 25 de noviembre se reconocen como trabajo directo. Si no es así, se requiere una actividad de recuperación para completar 64 horas de trabajo directo.

## Distribución docente

| Bloque | Semanas | Profesor | Actividad programada |
|---|---:|---|---:|
| Informática y conceptos básicos | 1–8 | Dr. Carlos Montenegro Marín | 32 horas sincrónicas |
| Arquitectura de software | 9–16 | Dr. Esteban Hernández Barragán | 28 horas sincrónicas y 4 horas de proyecto |

El primer bloque desarrolla los temas definidos por el profesor titular. El segundo los relaciona con prácticas contemporáneas, un proyecto acumulativo y laboratorios reproducibles. Los contenidos adicionales se incorporan como apoyo y no reemplazan la agenda oficial.

## Programación

| Semana | Fecha | Profesor | Tema |
|---:|---|---|---|
| 1 | 12 ago. | Carlos Montenegro | Modelo de software frente a arquitectura de software; evolución de las arquitecturas; cliente-servidor, multicapas y arquitectura web |
| 2 | 19 ago. | Carlos Montenegro | UML y su papel en el desarrollo de software; introducción al repositorio |
| 3 | 26 ago. | Carlos Montenegro | Paradigma de programación orientada a objetos; principios de POO y relación entre UML y POO |
| 4 | 2 sep. | Carlos Montenegro | Lenguajes modernos orientados a objetos: Python y Java |
| 5 | 9 sep. | Carlos Montenegro | Lenguajes modernos orientados a objetos: Python y Java |
| 6 | 16 sep. | Carlos Montenegro | Lenguajes modernos orientados a objetos: Python y Java |
| 7 | 23 sep. | Carlos Montenegro | Metapatrón MVC y manejo de comunicaciones |
| 8 | 30 sep. | Carlos Montenegro | Evaluación del primer bloque |
| — | 7 oct. | Semana Universitaria | No se programa una sesión ordinaria |
| 9 | 14 oct. | Esteban Hernández | Docker: construcción de imagen, ejecución de LibreReserva y pruebas de despliegue local |
| 10 | 27 oct. | Esteban Hernández · virtual | Balanceo y persistencia en archivos: dos instancias, Parquet compartido, concurrencia y bloqueo local |
| 11 | 28 oct. | Esteban Hernández | Persistencia e integridad y temas de API confiable ya trabajados: idempotencia, errores, salud y recuperación |
| 12 | 4 nov. | Esteban Hernández | Pruebas automatizadas, CI e imagen trazable al commit |
| 13 | 11 nov. | Esteban Hernández | Configuración segura, secretos y despliegue reproducible |
| 14 | 18 nov. | Esteban Hernández | Diagnóstico, logs, medición, respaldo y restauración |
| 15 | 25 nov. | Trabajo de proyecto | Integración desde un clon limpio; jornada autónoma sin temas nuevos |
| 16 | 2 dic. | Esteban Hernández | Demostración de robustez, defensa de decisiones y cierre |

## Uso de AWS Academy

AWS Academy Cloud Foundations y LibreReserva son recorridos paralelos. Los módulos 1–8 de Cloud Foundations se registran como desarrollados. El módulo 9 acompaña la revisión de arquitectura de la semana 10 y el módulo 10 acompaña operación y recuperación en la semana 14. Los números de AWS Academy no son semanas de Informática I ni números de las carpetas `modules/`.

LibreReserva se construye en un ambiente local reproducible con Docker, Compose y PostgreSQL. AWS Academy publica las consignas y evidencias, y Learner Lab se usa solo para las actividades oficiales que lo requieran. No se implementa una segunda versión de LibreReserva con servicios AWS diferentes.

- No se incorpora un curso Associate completo de AWS Academy dentro de estas 64 horas.
- Los servicios y cuotas se validan antes de cualquier actividad oficial de Learner Lab.
- Cada equipo registra consumo, elimina sus recursos y nunca almacena credenciales en Git.
- La semana 15 se publica como actividad autónoma de cuatro horas; no se presenta como encuentro sincrónico.

## Estructura de un encuentro de cuatro horas

| Horario | Actividad |
|---|---|
| 6:00–6:20 p. m. | Activación, verificación de prerrequisitos y revisión de evidencia |
| 6:20–7:10 p. m. | Conceptos, problema y decisión arquitectónica |
| 7:10–7:50 p. m. | Demostración guiada y preparación del laboratorio |
| 7:50–8:00 p. m. | Pausa |
| 8:00–9:25 p. m. | Laboratorio práctico acumulativo |
| 9:25–9:50 p. m. | Validación, medición, costo y registro de evidencia |
| 9:50–10:00 p. m. | Cierre, limpieza de recursos y siguiente entrega |

Las instalaciones extensas y las lecturas se realizan en las horas de trabajo cooperativo o autónomo. Durante el encuentro se priorizan decisiones, experimentos, construcción y validación.

## Ruta acumulativa de LibreReserva

### Cobertura confirmada y ajuste del 2 de noviembre

El docente confirmó que idempotencia, errores, vida/disponibilidad y caída/recuperación de PostgreSQL ya se trabajaron el miércoles 28 de octubre. Esos contenidos dejan de ser el tema nuevo del 4 de noviembre. La primera revisión comprueba el avance de cada equipo durante 10 minutos y continúa con 40 minutos de fundamentos antes del caso, sin repetir la clase anterior.

La cobertura docente y el estado de la implementación se registran por separado. Aunque un tema ya se haya explicado, cada equipo debe presentar evidencia de su implementación. En la referencia actual del repositorio, la idempotencia y la disponibilidad real aún requieren completar código y pruebas. Esas brechas se registran como pendientes de integración, no se convierten de nuevo en una clase completa.

### Próximos incrementos

La [ruta por sesiones](RUTA_CONTENEDORES.md) conserva una sola arquitectura y una sola entrega:

- Sesión 9: imagen Docker, contenedor, API local y pérdida del estado al reiniciar.
- Sesión 10: balanceador local, dos instancias, Parquet compartido y comparación de escrituras con y sin bloqueo.
- Sesión 11: PostgreSQL, migraciones, puerto/adaptador y concurrencia, junto con los temas de API confiable ya trabajados.
- Sesión 12: convertir riesgos y casos conocidos en pruebas, ejecutar CI y relacionar commit e imagen.
- Sesión 13: separar configuración y secretos de la imagen, revisar permisos y reproducir el despliegue con migraciones.
- Sesión 14: diagnosticar con logs, medir bajo condiciones declaradas y demostrar respaldo/restauración.
- Sesión 15: integración desde un clon limpio, sin tecnologías nuevas.
- Sesión 16: demostración de caso feliz, fallo, recuperación y decisiones.

Colas, una implementación serverless paralela y Kubernetes no forman parte de la ruta evaluable del segundo bloque.

## Alcance de la jornada del 25 de noviembre

La jornada de proyecto debe tener una duración esperada de cuatro horas y producir:

- versión candidata integrada desde un clon limpio;
- bitácora de actividades y tiempo;
- pruebas ejecutadas;
- construcción de la imagen y despliegue local con PostgreSQL;
- prueba de fallo, recuperación, respaldo y restauración;
- riesgos, decisiones y dudas para la sesión final.

El canal de acompañamiento y el mecanismo de entrega deben publicarse antes de esa fecha.

## Evidencia final

Como mínimo, un evaluador debe poder partir de un clon limpio, ejecutar pruebas, construir la imagen, levantar LibreReserva con PostgreSQL, realizar una reserva, reiniciar la API sin perder datos, comprobar concurrencia e idempotencia, provocar una indisponibilidad y recuperar el servicio.

La entrega incluye los ADR, logs del caso de fallo, respaldo restaurado y trazabilidad entre commit e imagen. Si se usó Learner Lab para los módulos oficiales de AWS Academy, el cierre incluye además consumo y confirmación de eliminación de recursos.

Última actualización metodológica: 4 de noviembre de 2026.
