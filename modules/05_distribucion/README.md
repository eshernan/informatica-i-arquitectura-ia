# Módulo 5. Estilos arquitectónicos y sistemas distribuidos

## Resultado

Elegir entre monolito modular, microservicios, eventos y funciones a partir de restricciones observadas, no de tendencias.

## Instalación paso a paso

La discusión arquitectónica no requiere instalar una plataforma. Para el experimento de fallo se necesita Podman:

```bash
./scripts/install_base.sh
./scripts/install_base.sh --apply
podman info
cd labs/librereserva
podman build -t localhost/librereserva:0.1.0 .
podman run --rm -p 8000:8000 localhost/librereserva:0.1.0
```

En macOS inicie primero `podman machine start`. En Windows ejecute el laboratorio dentro de WSL2 o use Podman Desktop y documente la red.

## Temas

- Monolito modular como línea base.
- Microservicios y costo operacional.
- Comunicación síncrona, eventos y consistencia eventual.
- Serverless y dependencia de plataforma.
- Strangler, outbox, saga y circuit breaker.

## Ejercicio

Compare tres opciones para notificaciones: módulo interno, consumidor asíncrono o función administrada. Use criterios de despliegue, fallos, datos, equipo, costo y portabilidad. Simule la caída del proceso de notificación y observe si la reserva principal continúa.

## Validación

La decisión debe incluir una alternativa más simple, condiciones que justificarían migrar y una estrategia de reversión. Una demostración distribuida no es suficiente sin evidencia del problema que resuelve.

**Evidencia:** matriz de decisión, diagrama, experimento de fallo y ADR.
