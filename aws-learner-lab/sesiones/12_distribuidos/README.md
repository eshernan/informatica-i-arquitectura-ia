# Sesión 12 — Pruebas automatizadas y entrega trazable

**Fecha:** 4 de noviembre de 2026, 6:00–10:00 p. m.
**Resultado:** convertir riesgos conocidos de LibreReserva en pruebas, comprobar que CI detecta una regresión y relacionar la imagen construida con el commit que la produjo.

## Alcance

Idempotencia, errores, vida/disponibilidad y recuperación de PostgreSQL ya se trabajaron el 28 de octubre, según confirmación docente del 2 de noviembre. Hoy se usan como casos para probar, sin repetir su explicación ni dedicar otra clase a implementarlos desde cero.

La revisión inicial dura 10 minutos. Cada equipo declara qué tiene implementado, qué demuestra y qué sigue pendiente. Después se explican los fundamentos antes de entrar en LibreReserva. Aunque un tema ya se haya enseñado, una prueba debe comprobar que la implementación lo cumple. La referencia del repositorio todavía necesita completar idempotencia y disponibilidad real, por lo que no se debe presentar una suite verde como prueba de garantías que no verifica.

Se utiliza la misma aplicación, PostgreSQL, Compose y la forja existente. Configuración y secretos se desarrollan el 11 de noviembre. Respaldo/restauración se reservan al 18. No se instalan colas, Kubernetes, otra forja ni una plataforma de telemetría.

## Secuencia de cuatro horas

| Hora | Tema y acción |
|---|---|
| 6:00–6:10 | revisar evidencia del 28 de octubre y registrar pendientes por equipo |
| 6:10–6:50 | explicar propósito, casos y tipos de pruebas con un ejemplo cotidiano |
| 6:50–7:10 | aplicar los conceptos a LibreReserva y demostrar una regresión funcional |
| 7:10–7:30 | comparar consulta concatenada y parametrizada mediante un caso aislado |
| 7:30–7:50 | recorrer el flujo CI existente y la construcción condicionada por las pruebas |
| 7:50–8:00 | pausa |
| 8:00–9:25 | completar una selección pequeña de pruebas y comprobar su ejecución en CI |
| 9:25–9:50 | relacionar commit, resultado de pruebas, etiqueta e ID de imagen |
| 9:50–10:00 | pull request, evidencia y preparación de la siguiente sesión |

## Material de trabajo

- [Ejercicios para estudiantes](../../../modules/07_pruebas/EJERCICIOS_SESION12.md): dos ejercicios guiados, comandos y resultados esperados.
- [Plantilla de evidencia](../../../modules/07_pruebas/EVIDENCIA_SESION12.md): ficha para completar en la rama del equipo.
- [Desarrollo de la clase](DESARROLLO_CLASE.md): explicación para el grupo, regresión funcional, riesgo de inyección SQL, taller y ficha de evidencia.
- [Esquema sketch del cambio a la imagen](../../../docs/imagenes/pruebas-entrega-trazable.jpg).
- [Pruebas por riesgo](../../../modules/07_pruebas/README.md).
- [Consulta parametrizada con datos ficticios](../../../modules/07_pruebas/test_consulta_segura.py): ejemplo ejecutable de seguridad sin servicios adicionales.
- [Flujo CI existente](../../../.github/workflows/validate.yml).
- [Contrato de repositorios](../../../labs/librereserva/tests/test_repository_contract.py).
- [Laboratorio PostgreSQL](../../../modules/06_apis_datos_eventos/LABORATORIO.md), solo como consulta de los casos ya trabajados.

Las carpetas conservan sus nombres históricos. El título y la fecha de esta guía indican la actividad vigente.

## Taller

1. Seleccione dos riesgos del incremento implementado o del ejemplo aislado de consultas. Un tercer riesgo es una ampliación opcional.
2. Defina la entrada, el resultado esperado y la condición que debe hacer fallar cada prueba.
3. Mantenga una prueba rápida de dominio y seleccione otra HTTP, de seguridad o de integración relevante.
4. Introduzca en una rama de prueba un fallo controlado, compruebe que la prueba lo detecta y restaure la implementación antes de entregar.
5. Revise qué pruebas ejecuta CI y cuáles necesitan PostgreSQL, migraciones y variables de entorno.
6. Ejecute las pruebas seleccionadas en CI. Si una integración no se ejecuta allí, registre esa brecha y su comprobación local; no la declare cubierta por el resultado verde.
7. Compruebe que una prueba fallida impide construir la imagen en el flujo.
8. Identifique el commit aprobado, la etiqueta de imagen y su ID. Distinga la imagen local del artefacto descargable y de una publicación a un registro.

## Selección de pruebas

| Riesgo | Comprobación posible |
|---|---|
| aceptar intervalos inválidos o solapados | regla de dominio y respuesta HTTP esperada |
| perder datos al reiniciar una instancia | consulta antes/después del reinicio con PostgreSQL |
| confirmar reservas concurrentes incompatibles | una confirmación y un conflicto |
| alterar el filtro de una consulta mediante una entrada | consulta parametrizada y prueba aislada con datos ficticios |
| duplicar una operación o informar disponibilidad falsa | prueba del caso ya implementado, o brecha de implementación explícita |

No se exige completar toda la matriz en cuatro horas. Cada equipo selecciona pocos casos y demuestra que sus pruebas detectan un error real.

## Validación

```bash
make test-sesion12
make check
make test-all
git status --short
```

`make test-sesion12` selecciona 13 pruebas de dominio, HTTP con memoria y consulta segura. No requiere servicios de base de datos. La suite completa añade contrato y propiedades, con PostgreSQL sujeto a configuración.

Los comandos anteriores son el punto de partida. Verifique si las pruebas PostgreSQL necesitan configuración adicional y si alguna quedó omitida. Un resultado verde no equivale a haber probado todo el sistema. La imagen debe corresponder al commit mostrado, no únicamente a una etiqueta `latest`.

**Evidencia:** selección de riesgos, prueba que detectó el fallo, pruebas ejecutadas y omitidas, ejecución CI, commit, etiqueta/ID de imagen y pull request.
