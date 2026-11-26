# Agenda de clases: segundo semestre de 2026

**Ajuste docente del 25 de noviembre.** La [última clase de contenido](../aws-learner-lab/sesiones/15_proyecto/SESION_2026-11-25.md) prepara un [ejercicio colectivo](../aws-learner-lab/sesiones/16_cierre/README.md) el 2 de diciembre. Las cifras de la sección siguiente describen la programación institucional original.

## Información general de la programación original

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

## Distribución docente del plan original

| Bloque | Semanas | Profesor | Actividad programada |
|---|---:|---|---:|
| Informática y conceptos básicos | 1–8 | Dr. Carlos Montenegro Marín | 32 horas sincrónicas |
| Arquitectura de software | 9–16 | Dr. Esteban Hernández Barragán | 28 horas sincrónicas y 4 horas de proyecto |

El primer bloque desarrolla los temas definidos por el profesor titular. El segundo los relaciona con prácticas contemporáneas, un proyecto acumulativo y laboratorios reproducibles. Los contenidos adicionales se incorporan como apoyo y no reemplazan la agenda oficial.

## Programación

[Carpeta de presentaciones por clase](../presentaciones/README.md)

| Semana | Fecha | Profesor | Tema | Presentaciones |
|---:|---|---|---|---|
| 1 | 12 ago. | Carlos Montenegro | Modelo de software frente a arquitectura de software; evolución de las arquitecturas; cliente-servidor, multicapas y arquitectura web | [Diseño del sistema](../presentaciones/01-03-diseno-del-sistema.ppt) |
| 2 | 19 ago. | Carlos Montenegro | UML y su papel en el desarrollo de software; introducción al repositorio | [UML · diap. 94–101](../presentaciones/01-03-diseno-del-sistema.ppt) |
| 3 | 26 ago. | Carlos Montenegro | Paradigma de programación orientada a objetos; principios de POO y relación entre UML y POO | [Objetos · diap. 26–27 y 100](../presentaciones/01-03-diseno-del-sistema.ppt) |
| 4 | 2 sep. | Carlos Montenegro | Lenguajes modernos orientados a objetos: Python y Java | Sin diapositivas localizadas |
| 5 | 9 sep. | Carlos Montenegro | Lenguajes modernos orientados a objetos: Python y Java | Sin diapositivas localizadas |
| 6 | 16 sep. | Carlos Montenegro | Lenguajes modernos orientados a objetos: Python y Java | Sin diapositivas localizadas |
| 7 | 23 sep. | Carlos Montenegro | Metapatrón MVC y manejo de comunicaciones | [MVC · apoyo, diap. 104–108](../presentaciones/01-03-diseno-del-sistema.ppt) |
| 8 | 30 sep. | Carlos Montenegro | Evaluación del primer bloque | Evaluación |
| — | 7 oct. | Semana Universitaria | No se programa una sesión ordinaria | Sin clase |
| 9 | 14 oct. | Esteban Hernández | Docker: construcción de imagen, ejecución de LibreReserva y pruebas de despliegue local | [Clase](../presentaciones/09-contenedores-con-librereserva.pptx) · [Docker y Podman](../presentaciones/09-docker-y-podman.pptx) · [Despliegue](../presentaciones/09-contenedores-kubernetes-y-despliegue.pptx) |
| 10 | 27 oct. | Esteban Hernández · virtual | Balanceo y persistencia en archivos: dos instancias, Parquet compartido, concurrencia y bloqueo local | [Estado y persistencia](../presentaciones/10-estado-persistencia-y-calidad.pptx) |
| 11 | 28 oct. | Esteban Hernández | Persistencia e integridad y temas de API confiable ya trabajados: idempotencia, errores, salud y recuperación | [PostgreSQL](../presentaciones/11-persistencia-e-integridad-postgresql.pptx) |
| 12 | 4 nov. | Esteban Hernández | Pruebas automatizadas y de desempeño, CI e imagen trazable al commit | [Pruebas y consultas seguras](../presentaciones/12-pruebas-y-consultas-seguras.pptx) |
| 13 | 11 nov. | Esteban Hernández | Clase suspendida. Configuración y despliegue se integran el 18 de noviembre | [Clase integrada del 18 nov.](../presentaciones/14-configuracion-diagnostico-y-recuperacion.pptx) |
| 14 | 18 nov. | Esteban Hernández | Clase integrada: configuración, despliegue, diagnóstico, respaldo y restauración | [Clase](../presentaciones/14-configuracion-diagnostico-y-recuperacion.pptx) · [Taller AWS](../presentaciones/14-taller-aws-learner-lab.pptx) |
| 15 | 25 nov. | Esteban Hernández | Última clase de contenido: sistemas distribuidos, CAP, datos y procesamiento; aplicación final y secretos locales | [Sistemas distribuidos](../presentaciones/15-sistemas-distribuidos.pptx) |
| 16 | 2 dic. | Esteban Hernández | Ejercicio colectivo de integración, incidente y recuperación | Ejercicio colectivo programado |

## Uso de AWS Academy

AWS Academy Cloud Foundations y LibreReserva son recorridos paralelos. Los módulos 1–8 de Cloud Foundations se registran como desarrollados. El módulo 9 acompaña la revisión de arquitectura de la semana 10 y el módulo 10 acompaña operación y recuperación en la semana 14. Los números de AWS Academy no son semanas de Informática I ni números de las carpetas `modules/`.

LibreReserva se construye en un ambiente reproducible con Docker, Compose y PostgreSQL. AWS Academy publica las consignas y evidencias. La [sesión del 18 de noviembre](../aws-learner-lab/sesiones/14_pruebas_entrega/README.md) ejecuta el mismo ambiente en EC2 dentro de Learner Lab.

- No se incorpora un curso Associate completo de AWS Academy dentro de estas 64 horas.
- Los servicios y cuotas se validan antes de cualquier actividad oficial de Learner Lab.
- Cada equipo registra consumo, elimina sus recursos y nunca almacena credenciales en Git.
- El ajuste docente del 25 de noviembre organiza cuatro horas locales de cierre de contenido.

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

**Ajuste del 18 de noviembre:** el docente confirmó la suspensión de la clase del día 11. El encuentro del 18 integra configuración y despliegue con diagnóstico y recuperación mediante un solo laboratorio. Incluye cuatro horas con pausa y una práctica de 55 minutos. La restauración guiada utiliza una base vacía separada y conserva el origen. El 25 se prepara la verificación del respaldo y el 2 de diciembre se ejecuta en un volumen limpio separado. Las pruebas de desempeño del 4 de noviembre se recuperan brevemente como antecedente.

El 4 de noviembre también se trabajaron pruebas de desempeño. El ejercicio crea 100 reservas y consulta en tandas de 1.000, 2.000, 5.000 y 6.000 solicitudes concurrentes. La sesión del 18 aprovecha el resumen de ese ejercicio durante la apertura y el diagnóstico.

La [ruta por sesiones](RUTA_CONTENEDORES.md) conserva una sola arquitectura y una sola entrega:

- Sesión 9: imagen Docker, contenedor, API local y pérdida del estado al reiniciar.
- Sesión 10: balanceador local, dos instancias, Parquet compartido y comparación de escrituras con y sin bloqueo.
- Sesión 11: PostgreSQL, migraciones, puerto/adaptador y concurrencia, junto con los temas de API confiable ya trabajados.
- Sesión 12: convertir riesgos y casos conocidos en pruebas, evaluar desempeño, ejecutar CI y relacionar commit e imagen.
- Sesión 13: separar configuración y secretos de la imagen, revisar permisos y reproducir el despliegue con migraciones.
- Sesión 14: diagnosticar con logs y mediciones previas, y demostrar respaldo/restauración.
- Sesión 15: conceptos, principios, esquemas e implementaciones de sistemas distribuidos. El bloque final aplica lo aprendido al proyecto, retoma los secretos locales y prepara las pruebas.
- Sesión 16: integración desde un clon limpio y ejercicio colectivo de fallo, recuperación y decisiones.

Colas, una implementación serverless paralela y Kubernetes no forman parte de la ruta evaluable del segundo bloque.

## Alcance del cierre

El 25 de noviembre cada pareja entrega una vista de ejecución, un ADR, una ficha de prueba y un procedimiento de recuperación. El 2 de diciembre todo el grupo opera una sola versión desde un clon limpio y documenta la integración en una bitácora compartida.

## Evidencia final

Como mínimo, un evaluador debe poder partir de un clon limpio, ejecutar pruebas, construir la imagen, levantar LibreReserva con PostgreSQL, realizar una reserva, reiniciar la API sin perder datos, comprobar concurrencia e idempotencia, provocar una indisponibilidad y recuperar el servicio.

La entrega incluye los ADR, logs del caso de fallo, respaldo restaurado y trazabilidad entre commit e imagen. Si se usó Learner Lab para los módulos oficiales de AWS Academy, el cierre incluye además consumo y confirmación de eliminación de recursos.

Última actualización metodológica: 25 de noviembre de 2026.
