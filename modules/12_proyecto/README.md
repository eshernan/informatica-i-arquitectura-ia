# Módulo 12. Proyecto integrador: LibreReserva operable

## Resultado

Integrar arquitectura, código, entrega, operación, seguridad e IA responsable en un producto pequeño y defendible.

## Instalación paso a paso

No existe una instalación adicional única. Prepare únicamente las capacidades elegidas y registre versiones:

```bash
./scripts/check_environment.sh
./scripts/setup_python.sh --apply
make check
make test
```

Después complete, según la arquitectura del equipo:

1. Módulo 6: PostgreSQL y RabbitMQ.
2. Módulo 8: Podman, kind, kubectl y Forgejo.
3. Módulo 9: OpenTelemetry y backends seleccionados.
4. Módulo 10: Gitleaks, Syft, Trivy y ZAP.
5. Módulo 11: Ollama/Continue solo si el experimento local es viable.

## Iteraciones

1. **Descubrimiento:** actores, alcance, escenarios, C4 y dos ADR.
2. **Incremento:** crear y consultar reservas con persistencia y pruebas.
3. **Entrega segura:** CI, imagen OCI, SBOM y despliegue local.
4. **Operación:** telemetría, SLO, alerta y fallo controlado.
5. **IA y cierre:** comparación asistida, deuda, costo, README y defensa.

## Definición de terminado

- Criterios aprobados y revisión de otra persona.
- Pruebas por riesgo y contrato actualizado.
- Telemetría suficiente y amenaza examinada.
- Ningún secreto o dato personal confirmado.
- Imagen trazable por digest y despliegue reproducible.
- Asistencia de IA declarada y comprendida.

## Validación final

Un evaluador parte de un clon limpio y debe poder crear entorno, ejecutar pruebas, construir imagen, generar SBOM, desplegar, crear una reserva y observar su traza. Cada excepción se registra como deuda con riesgo, responsable y fecha.

## Defensa

Quince minutos: problema y decisión; recorrido funcional; fallo inducido y diagnóstico; control de seguridad; resultado de IA; deuda reconocida. Después, cada integrante realiza un cambio pequeño seleccionado al azar.

**Evidencia:** etiqueta de versión, digest, paquete de evidencias y matriz resultado de aprendizaje–archivo.
