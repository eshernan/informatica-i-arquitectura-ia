# Agenda de clases: segundo semestre de 2026

## Información general

- Duración: 16 semanas.
- Intensidad: 4 horas cada miércoles.
- Horario: 6:00 p. m. a 10:00 p. m.
- Total presencial: 64 horas.
- Periodo académico: segundo semestre de 2026.
- Primera sesión: miércoles 12 de agosto de 2026.
- Última sesión: miércoles 25 de noviembre de 2026.
- Caso conductor: LibreReserva.

## Distribución docente

| Bloque | Sesiones | Profesor | Horas |
|---|---:|---|---:|
| Diseño y construcción | 1–8 | Dr. Esteban Hernández Barragán | 32 |
| Entrega, operación y evolución | 9–16 | Dr. Carlos Montenegro Marin | 32 |

La primera mitad produce una versión funcional y probada. La segunda transforma ese incremento en un sistema desplegable, observable, seguro y defendible.

## Programación

| Semana | Fecha | Profesor | Tema central | Resultado verificable |
|---:|---|---|---|---|
| 1 | 12 ago. 2026 | Esteban Hernández | Introducción, LibreReserva y entorno reproducible | Repositorio ejecutable, entorno registrado y equipos conformados |
| 2 | 19 ago. 2026 | Esteban Hernández | Requisitos, restricciones y atributos de calidad | Tres escenarios de calidad con unidad, umbral y condiciones |
| 3 | 26 ago. 2026 | Esteban Hernández | Comunicación arquitectónica: C4, UML y ADR | Contexto, contenedores y primera decisión arquitectónica |
| 4 | 2 sep. 2026 | Esteban Hernández | Modularidad, dominio y arquitectura hexagonal | Límites, puertos, adaptadores y prueba de dependencias |
| 5 | 9 sep. 2026 | Esteban Hernández | Monolito modular y sistemas distribuidos | Matriz de decisión y ADR del estilo inicial |
| 6 | 16 sep. 2026 | Esteban Hernández | API REST, OpenAPI, persistencia y transacciones | Incremento vertical con contrato y PostgreSQL |
| 7 | 23 sep. 2026 | Esteban Hernández | Eventos, idempotencia, consistencia y outbox | Publicación confiable y consumidor idempotente |
| 8 | 30 sep. 2026 | Esteban Hernández | Implementación evolutiva y estrategia de pruebas | Versión `v0.1`, suite y paquete de transición |
| 9 | 7 oct. 2026 | Carlos Montenegro | Git, contenedores OCI y CI con Forgejo | Imagen reproducible, digest y canalización automatizada |
| 10 | 14 oct. 2026 | Carlos Montenegro | Kubernetes local, configuración e infraestructura | Despliegue en kind con sondas, límites y reconciliación |
| 11 | 21 oct. 2026 | Carlos Montenegro | Registros, métricas y trazas | Instrumentación OpenTelemetry y diagnóstico correlacionado |
| 12 | 28 oct. 2026 | Carlos Montenegro | SLI/SLO, rendimiento, resiliencia y costo | Presupuesto de error y experimento controlado de fallos |
| 13 | 4 nov. 2026 | Carlos Montenegro | Secure by Design, privacidad y amenazas | Modelo de amenazas y pruebas de controles prioritarios |
| 14 | 11 nov. 2026 | Carlos Montenegro | Seguridad de la cadena de suministro | SBOM, Gitleaks, Syft, Trivy, ZAP y triage humano |
| 15 | 18 nov. 2026 | Carlos Montenegro | Generación de código y agentes de IA | Evaluación controlada con Ollama/Continue y registro de uso |
| 16 | 25 nov. 2026 | Carlos Montenegro | Presentación y defensa del proyecto | Demostración, fallo inducido, defensa y evaluación final |

## Estructura de una sesión de cuatro horas

| Horario | Actividad |
|---|---|
| 6:00–6:20 p. m. | Activación, revisión de evidencias y preguntas |
| 6:20–7:20 p. m. | Fundamentos, decisiones y demostración breve |
| 7:20–7:30 p. m. | Pausa |
| 7:30–8:25 p. m. | Taller guiado |
| 8:25–8:35 p. m. | Pausa |
| 8:35–9:35 p. m. | Laboratorio acumulativo sobre LibreReserva |
| 9:35–10:00 p. m. | Validación, retroalimentación y siguiente entrega |

## Hitos acumulativos

| Semana | Hito |
|---:|---|
| 1 | Entorno reproducible y línea base |
| 3 | Arquitectura inicial y ADR |
| 6 | API y persistencia |
| 8 | Incremento probado `v0.1` |
| 10 | Entrega y despliegue local |
| 12 | Observabilidad y resiliencia |
| 14 | Seguridad y cadena de suministro |
| 15 | Evaluación de asistencia de IA |
| 16 | Versión final y defensa |

## Transición entre profesores

Al terminar la sesión 8, el profesor Esteban entrega:

- etiqueta `v0.1` y confirmación estable;
- API y persistencia funcionales;
- diagramas C4 y ADR vigentes;
- suite de pruebas y resultados;
- backlog, riesgos y deuda conocida;
- instrucciones verificadas desde un clon limpio.

La sesión 9 comienza con la reproducción de ese paquete bajo la dirección del profesor Carlos. Si una evidencia no puede reproducirse, se registra como riesgo y se corrige antes de ampliar la plataforma.

## Ajustes para cumplir las 64 horas

- C4 se concentra en contexto y contenedores; componentes se detallan cuando sean necesarios para el proyecto.
- UML se limita a secuencia y componentes con valor explicativo.
- REST se implementa; gRPC y serverless se comparan sin construir plataformas adicionales.
- Se utiliza Podman y un único clúster local kind; no se exige una nube comercial.
- PostgreSQL y RabbitMQ se ejecutan en contenedores.
- Observabilidad utiliza una pila reducida con OpenTelemetry y backends libres.
- No se entrenan modelos de IA; se evalúan asistentes y agentes existentes bajo permisos limitados.
- El proyecto se desarrolla desde la primera semana y no se aplaza para la sesión final.

## Evidencia final

El repositorio debe permitir que un evaluador parta de un clon limpio y pueda ejecutar pruebas, construir la imagen, generar la SBOM, desplegar LibreReserva, realizar una reserva, observar su traza y relacionar el artefacto con una decisión arquitectónica.

Última actualización: 2026-08-10
