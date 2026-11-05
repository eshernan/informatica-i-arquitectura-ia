# Sesión 9 — Docker y despliegue local

**Fecha:** 14 de octubre de 2026, 6:00–10:00 p. m.
**Resultado alcanzado:** construir la imagen de LibreReserva, ejecutar la API en un contenedor y probar su despliegue local.

Esta guía registra el alcance realmente trabajado. Git y los pull requests se usan en los incrementos posteriores como mecanismo de entrega, sin abrir una sesión de recuperación independiente.

## Práctica realizada

Desde la raíz del repositorio, el equipo eligió Docker y ejecutó:

```bash
docker info
docker build -f labs/librereserva/Containerfile \
  -t localhost/librereserva:0.1.0 labs/librereserva
docker run --rm -p 127.0.0.1:8000:8000 \
  localhost/librereserva:0.1.0
```

En otra terminal:

```bash
curl -fsS http://127.0.0.1:8000/salud/viva

curl -i -X POST http://127.0.0.1:8000/reservas \
  -H 'content-type: application/json' \
  -d '{"recurso":"A-101","inicio":"2026-10-14T18:00:00-05:00","fin":"2026-10-14T19:00:00-05:00"}'

curl -fsS http://127.0.0.1:8000/reservas
```

## Experimento de cierre

1. Crear una reserva.
2. Detener el contenedor.
3. Ejecutar un contenedor nuevo con la misma imagen.
4. Consultar las reservas.
5. Registrar que la lista vuelve a estar vacía.

La pérdida de datos no es un defecto del motor de contenedores: la implementación actual guarda la agenda en la memoria del proceso. Este resultado establece el problema que se resuelve con PostgreSQL en la sesión 11.

## Evidencia

- versión de Docker;
- comando de construcción;
- imagen creada;
- contenedor en ejecución;
- respuesta de salud;
- creación y consulta de una reserva;
- lista vacía después de recrear el contenedor;
- explicación de por qué se perdió el estado.

## Continuidad

- Sesión 10: ejecutar dos instancias, introducir el balanceador y experimentar con un Parquet compartido.
- Sesión 11: persistencia PostgreSQL y temas de API confiable ya trabajados el 28 de octubre.
- Sesión 12: automatizar pruebas, comprobar CI y relacionar commit e imagen.
- Sesión 13: separar configuración y secretos y reproducir el despliegue.
- Sesión 14: diagnosticar, respaldar y restaurar.
