# Syllabus actualizado de Informática I

## Identidad

- Programa: Especialización en Ingeniería de Software.
- Periodo académico: segundo semestre de 2026.
- Enfoque: arquitectura moderna y desarrollo asistido por IA.
- Caso conductor: LibreReserva.
- Modalidad: explicación breve, laboratorio acumulativo, validación y defensa.
- Agenda: [Programación docente de las 16 semanas](AGENDA_16_SEMANAS.md).

[Presentaciones organizadas por sesión](../presentaciones/README.md).

## Unidades

### 1. Fundamentos y decisiones arquitectónicas

Requisitos, restricciones, atributos de calidad, compromisos, estilos, modularidad, dominio, C4, UML y ADR. Corresponde a los módulos 1–5.

### 2. Construcción e integración

Componentes, API, persistencia PostgreSQL, transacciones, concurrencia, idempotencia, control de versiones y pruebas automatizadas. Corresponde a los módulos 4, 6 y 7.

La clase de sistemas distribuidos sigue una medición meteorológica desde el sensor hasta el archivo y el mapa. Se estudian las garantías de CAP durante una partición y los costos de coordinación en operación normal. En ejercicios de diseño se comparan fragmentación, replicación, cuórums y transacciones distribuidas. El tablero meteorológico permite contrastar MapReduce, consultas paralelas y flujos con eventos tardíos o duplicados.

### 3. Entrega, operación y seguridad

Contenedores, Compose, CI, configuración externa, salud, logs, medición, respaldo, restauración y recuperación. Corresponde a los módulos 7, 9 y 12.

### 4. Proyecto integrador

Arquitectura objetivo, ADR, integración desde un clon limpio, fallo controlado, recuperación, trazabilidad y defensa. Corresponde a los módulos 3 y 12.

## Resultados de aprendizaje

1. Analizar problema, actores y restricciones.
2. Formular atributos de calidad verificables.
3. Comunicar arquitectura con vistas y decisiones.
4. Diseñar límites modulares y dependencias.
5. Construir contratos, persistencia, integridad concurrente e idempotencia.
6. Implementar incrementos y pruebas por riesgo.
7. Automatizar artefactos y despliegues reproducibles.
8. Diagnosticar fallos y ejecutar recuperación y restauración.
9. Gestionar configuración y secretos sin incorporarlos al código o la imagen.
10. Defender decisiones y límites con evidencia reproducible.

La [última clase de contenido del 25 de noviembre](../aws-learner-lab/sesiones/15_proyecto/README.md) cierra con la aplicación a LibreReserva y el ejercicio local de secretos. El [2 de diciembre](../aws-learner-lab/sesiones/16_cierre/README.md) todo el grupo integra una versión y registra el resultado en una bitácora compartida.

## Evaluación sugerida

| Evidencia | Peso |
|---|---:|
| Escenarios, arquitectura y ADR | 20 % |
| Persistencia, concurrencia e idempotencia | 25 % |
| Pruebas, CI e imagen trazable | 20 % |
| Diagnóstico, respaldo y recuperación | 20 % |
| Reproducibilidad y defensa | 15 % |

La hoja de cálculo institucional se conserva en [Syllabus_Informatica_I_Actualizado_2026.xlsx](Syllabus_Informatica_I_Actualizado_2026.xlsx).
