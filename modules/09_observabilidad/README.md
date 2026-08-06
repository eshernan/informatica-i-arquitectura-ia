# Módulo 9. Observabilidad, confiabilidad y costo

## Resultado

Correlacionar registros, métricas y trazas; formular SLI/SLO; usar presupuesto de error para decidir.

## Instalación paso a paso

### Ruta ligera: notebook

```bash
./scripts/setup_python.sh --apply
.venv/bin/jupyter lab modules/09_observabilidad
```

Abra `slo_error_budget.ipynb` y ejecute todas las celdas.

### Ruta completa: demostración OpenTelemetry

1. Instale Git, Podman y Compose mediante el módulo 1.
2. Verifique al menos 6 GiB de memoria libre; si no, use la ruta ligera.
3. Clone la [demostración oficial de OpenTelemetry](https://opentelemetry.io/docs/demo/).
4. Registre la etiqueta o confirmación usada; no dependa silenciosamente de `main`.
5. Revise imágenes, puertos y recursos antes de iniciar.
6. Siga el perfil Docker/Compose del proyecto sustituyendo Docker por Podman cuando sea compatible.

Para instrumentar la API Python:

```bash
./scripts/setup_python.sh --apply
.venv/bin/python -m pip install opentelemetry-distro opentelemetry-exporter-otlp
.venv/bin/opentelemetry-bootstrap -a install

export OTEL_SERVICE_NAME=librereserva-api
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc
.venv/bin/opentelemetry-instrument \
  .venv/bin/uvicorn labs.librereserva.app.main:app --port 8000
```

Prometheus, Grafana, Jaeger y el Collector son software libre o de código abierto, pero cada imagen conserva su licencia. Fije versión y digest antes de una entrega evaluada.

## Ejercicio

Formule una pregunta antes de crear el panel. Genere tráfico correcto, conflicto 409 y demora artificial. Relacione una métrica RED, una traza lenta y un registro con `trace_id`. Compare la tasa de consumo del presupuesto antes y después del fallo.

## Validación

- 409 no se clasifica automáticamente como error del servidor.
- Ninguna etiqueta contiene usuario, token o URL sin normalizar.
- El p95 se calcula bajo condiciones declaradas.
- El panel conduce a una acción y no es solamente decorativo.

**Evidencia:** SLI/SLO, consultas, captura de traza, panel versionado y diagnóstico.
