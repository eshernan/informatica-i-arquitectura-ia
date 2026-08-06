# Módulo 7. Implementación evolutiva y pruebas

## Resultado

Construir un incremento vertical y seleccionar pruebas unitarias, de integración, de contrato, propiedades y rendimiento según el riesgo.

## Instalación paso a paso

```bash
./scripts/setup_python.sh
./scripts/setup_python.sh --apply
.venv/bin/python -m pytest modules/07_pruebas -v
.venv/bin/python -m pytest --cov=labs.librereserva --cov-branch
```

El primer comando muestra el plan. El segundo instala pytest, pytest-cov, HTTPX e Hypothesis dentro de `.venv`; no use `sudo pip`.

## Pirámide por riesgo

- Unitarias: reglas rápidas y deterministas.
- Integración: base de datos, cola o sistema de archivos real.
- Contrato: acuerdo consumidor/proveedor.
- Aceptación: recorrido externo del sistema.
- Rendimiento y seguridad: propiedades no funcionales bajo condiciones declaradas.

## Ejercicio

Implemente consulta y cancelación. Añada una propiedad para intervalos contiguos, una prueba HTTP y una prueba de integración PostgreSQL. Mute deliberadamente `<` por `<=` en la regla de solapamiento y confirme que la suite lo detecta; restaure el código antes de confirmar.

## Validación

```bash
.venv/bin/python -m pytest modules/07_pruebas -v
.venv/bin/python -m pytest --cov=labs.librereserva --cov-branch --cov-report=term-missing
```

La cobertura indica ejecución, no calidad de las aserciones. Justifique cualquier umbral mediante riesgo.

**Evidencia:** suite, informe, mutación detectada y defecto real encontrado.
