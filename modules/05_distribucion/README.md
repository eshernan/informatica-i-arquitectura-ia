# Módulo 5. Estilos arquitectónicos y sistemas distribuidos

## Resultado

Elegir entre monolito modular, microservicios, eventos y funciones a partir de restricciones observadas, no de tendencias.

## Aplicación en la sesión del 25 de noviembre

La [clase de sistemas distribuidos](../../aws-learner-lab/sesiones/15_proyecto/README.md) recorre una red de estaciones meteorológicas en cuatro niveles: conceptos, principios, esquemas e implementaciones. El bloque final aplica el mapa a LibreReserva y recupera el ejercicio local de secretos.

## Ejecución reemplazable y datos separados

![Sketch de réplicas sin estado, balanceo y almacenamiento separado](../../docs/imagenes/despliegue-sin-estado-cloud.jpg)

Una réplica sin estado puede atender una solicitud sin depender de memoria durable de otra solicitud en esa misma instancia. Aunque se reemplacen o se añadan réplicas, los datos compartidos deben conservarse fuera del proceso. Para lograrlo se deben resolver consistencia, capacidad de la base de datos y costos. Los servicios cloud pueden facilitar el balanceo y el autoescalado, y un monolito modular también puede usar este diseño sin convertirse en microservicios.

El dibujo es un objetivo arquitectónico: la agenda en RAM de LibreReserva aún no lo cumple. Relacione el experimento con esa limitación antes de distribuir la aplicación.

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
