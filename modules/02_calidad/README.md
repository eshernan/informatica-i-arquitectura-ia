# Módulo 2. Requisitos, restricciones y atributos de calidad

## Resultado

Transformar cualidades vagas en escenarios medibles y comparar decisiones mediante evidencia.

## Instalación paso a paso

Este módulo no requiere servicios. Usa el entorno Python común y un notebook.

```bash
./scripts/setup_python.sh            # muestra el plan
./scripts/setup_python.sh --apply
.venv/bin/jupyter lab modules/02_calidad
```

Abra `escenarios_calidad.ipynb`, seleccione el kernel `.venv` y ejecute **Restart Kernel and Run All Cells**. Las gráficas son ilustrativas; el estudiante debe reemplazar datos simulados por resultados del laboratorio y declarar el entorno.

## Temas

- Escenario: fuente, estímulo, entorno, artefacto, respuesta y medida.
- Rendimiento, disponibilidad, seguridad, privacidad y modificabilidad.
- Restricción frente a decisión.
- Compromisos y funciones de aptitud.

## Ejercicio

Escriba tres escenarios para LibreReserva. Implemente una función automática para uno y diseñe un experimento para otro. Use el notebook para comparar dos alternativas sin ocultar la variabilidad.

## Validación

- Cada medida contiene unidad, umbral y condiciones.
- La conclusión no generaliza más allá de los datos.
- El notebook se ejecuta de principio a fin y no contiene rutas personales.

**Evidencia:** escenarios, notebook ejecutado o exportado, datos y decisión explicada.
