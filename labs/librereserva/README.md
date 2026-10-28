# LibreReserva

Incremento vertical mínimo usado por todos los módulos. El núcleo de dominio no depende de FastAPI; la API es un adaptador reemplazable.

Consulte la [documentación de la API](API.md) para ver el diagrama de arquitectura, los servicios, sus endpoints, ejemplos de solicitudes y respuestas, y las rutas de ejecución con Docker o Podman.

## Cómo se entrega este incremento

![Sketch del recorrido desde el repositorio hasta una imagen desplegada](../../docs/imagenes/desarrollo-moderno.jpg)

Este laboratorio cubre código, pruebas, imagen y ejecución local. La [visión moderna del curso](../../README.md#visión-moderna-del-desarrollo-y-despliegue) explica cómo continuar hacia ejecución sin estado y almacenamiento separado. La ejecución directa usa memoria para conservar la línea base de la sesión 9. El laboratorio de la sesión 11 selecciona PostgreSQL mediante variables de ambiente y ejecuta dos réplicas con el mismo almacén.

## Instalación

Prepare las herramientas con la [guía de entorno](../../modules/01_entorno/README.md). Para Docker en Ubuntu 26.04/EC2, siga la [instalación específica](../../modules/01_entorno/README.md#instalación-con-script-en-ubuntu-y-ec2).

Desde la raíz:

```bash
./scripts/setup_python.sh --apply
make test
make run
```

## Prueba manual

```bash
curl -fsS http://127.0.0.1:8000/salud/viva

curl -i -X POST http://127.0.0.1:8000/reservas \
  -H 'content-type: application/json' \
  -d '{"recurso":"A-101","inicio":"2026-08-10T08:00:00Z","fin":"2026-08-10T09:00:00Z"}'

curl -fsS http://127.0.0.1:8000/reservas

curl -i -X DELETE http://127.0.0.1:8000/reservas/1
```

El segundo POST con el mismo intervalo debe responder `409`. Un intervalo invertido debe responder `422`. Borrar una reserva inexistente debe responder `404`.

## Evolución esperada

El puerto `RepositorioReservas` permite ejecutar la API con el adaptador en
memoria o con PostgreSQL. Consulte el
[laboratorio acumulativo](../../modules/06_apis_datos_eventos/LABORATORIO.md)
para aplicar la migración, iniciar dos instancias detrás de Caddy y comprobar
durabilidad e integridad concurrente.
