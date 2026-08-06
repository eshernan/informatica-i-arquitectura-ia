# Módulo 11. Desarrollo asistido por inteligencia artificial

## Resultado

Usar modelos como colaboradores no confiables, proteger contexto, verificar propuestas y comparar productividad mediante un protocolo reproducible.

## Instalación paso a paso

### Ollama local

1. Revise requisitos de memoria, licencia del modelo y política institucional.
2. Instale Ollama desde [su página oficial](https://ollama.com/download). No se incluye un instalador remoto automático.
3. Verifique el servicio.
4. Elija un modelo de código compatible con su hardware y registre nombre, etiqueta y licencia.

```bash
ollama --version
ollama list
./modules/11_ia/check_local_ai.sh
ollama pull qwen2.5-coder:7b   # ejemplo; verifique disponibilidad y licencia
ollama run qwen2.5-coder:7b
```

Un modelo cuantizado de 7 mil millones de parámetros puede requerir varios GiB de memoria. Si el equipo no lo soporta, trabaje por parejas o use el servicio institucional autorizado sin subir información restringida.

### Continue

Instale la extensión de código abierto Continue desde el mercado de VSCodium/VS Code y siga la [guía de conexión con Ollama](https://docs.continue.dev/guides/ollama-guide). Limite carpetas compartidas y desactive herramientas que el ejercicio no necesita.

### Notebook de evaluación

```bash
./scripts/setup_python.sh --apply
.venv/bin/jupyter lab modules/11_ia
```

## Ejercicio

Use cinco tareas con pruebas que el modelo no vea. Compare línea base humana y asistencia. Registre herramienta, versión, solicitud, archivos compartidos, salida usada, ediciones, pruebas, escaneos, tiempo y resultado. No registre cadenas de pensamiento privadas.

## Validación

El estudiante debe explicar y modificar su código sin asistencia. Cada propuesta se compila, prueba, escanea y contrasta con contrato o fuente. Una respuesta fluida no es evidencia.

**Evidencia:** registro de IA, notebook, parches aceptados/descartados y conclusión limitada.
