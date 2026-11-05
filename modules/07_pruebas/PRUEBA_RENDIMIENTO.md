# Prueba de rendimiento con reservas

El archivo [performance_test.py](performance_test.py) prepara datos ficticios y evalúa cómo responde LibreReserva ante ráfagas de consultas. Es una ampliación opcional de la sesión 12. Se ejecuta directamente con Python y un cliente HTTP asíncrono; pytest mantiene su selección habitual.

## Preparación

Desde la raíz del repositorio, instale el ambiente y la dependencia opcional:

```bash
./scripts/setup_python.sh --apply
.venv/bin/python -m pip install -r modules/07_pruebas/requirements-rendimiento.txt
```

En una terminal, inicie una instancia nueva de laboratorio, sin reservas y sin recarga automática:

```bash
LIBRERESERVA_REPOSITORY=memory .venv/bin/python -m uvicorn \
  labs.librereserva.app.main:app --host 127.0.0.1 --port 8000 --no-access-log
```

Si ese puerto está ocupado, use otro y páselo con `--host`. Esta instancia usa memoria: reiniciarla deja los datos vacíos para repetir el ejercicio. La prueba conserva las 100 reservas al terminar. Si encuentra datos previos, se detiene antes de escribir para mantener el conjunto de exactamente 100 reservas.

## Ejecución

En otra terminal:

```bash
make test-rendimiento
```

También puede ejecutar el archivo directamente:

```bash
.venv/bin/python modules/07_pruebas/performance_test.py \
  --host http://127.0.0.1:8000
```

La secuencia es:

1. Verificar que `GET /reservas` responde y devuelve una lista vacía.
2. Crear **100 reservas** mediante `POST /reservas`, comprobando HTTP 201 e identificadores distintos. Los recursos tienen nombres ficticios únicos para evitar solapamientos.
3. Preparar **1.000 solicitudes GET**, liberarlas mediante una barrera común y esperar a que terminen o agoten su tiempo.
4. Repetir con **2.000, 5.000 y 6.000 solicitudes**, con una pausa de dos segundos entre tandas.
5. Comprobar en cada respuesta HTTP 200 que aparecen las 100 reservas preparadas y guardar las métricas.

Son **14.000 intentos de consulta**, además de las 100 creaciones y la verificación inicial. Cada tarea envía una sola consulta, sin reintentos automáticos de la aplicación. Las tandas son sucesivas; dentro de cada una las tareas se liberan juntas. El pool admite tantas conexiones como solicitudes tenga la tanda.

La concurrencia configurada es un objetivo del generador. La planificación del cliente, las conexiones disponibles, el sistema operativo y la cola del servidor determinan cuántas consultas procesa la API simultáneamente. `ultimo_inicio_ms` muestra cuánto tardó el cliente en iniciar todas las tareas. La prueba no demuestra por sí sola que el servidor procesó 6.000 consultas al mismo instante.

## Archivos de evidencia

Cada ejecución crea una carpeta nueva en `dist/rendimiento/<fecha-UTC>-<identificador>/`:

| Archivo | Contenido |
|---|---|
| `performance_test.log` | Un objeto JSON por línea: configuración, 100 creaciones, cada consulta, resúmenes y resultado final |
| `resumen.csv` | Una fila por tanda, con éxitos, fallos, distribución HTTP, duración, promedio y percentiles |
| `respuestas/<hash>.txt` | Cuerpo completo de cada respuesta distinta, asociado a las solicitudes mediante `respuesta_archivo` |

Cada consulta tiene un identificador, código HTTP, tiempo en milisegundos, tamaño, error si existe y referencia al cuerpo recibido. Las respuestas idénticas comparten archivo para conservar toda la evidencia sin repetir miles de veces el mismo JSON. El hash del nombre corresponde al SHA-256 del cuerpo. Los cuerpos y los registros de la tanda se escriben después de completar su tráfico para reducir la interferencia del disco.

`tiempo_ms` mide desde que comienza el intento HTTP hasta que se descarga el cuerpo completo, incluyendo espera por conexión y red. Un timeout o un fallo de conexión conserva su tiempo, error y estado HTTP nulo cuando no recibió cabeceras. Los percentiles incluyen todos los intentos; revise siempre los fallos junto a los tiempos. Un rechazo rápido puede bajar el promedio aunque el servicio esté fallando. Las fechas del log indican cuándo se guardó el registro; `inicio_relativo_ms` permite situar el inicio de cada intento dentro de su tanda.

## Interpretación en clase

El criterio didáctico inicial es **cero fallos y p95 menor a 500 ms**. p95 indica un tiempo que alcanza o mejora al menos el 95 % de los intentos, usando el método de rango más cercano. El umbral sirve para discutir resultados; no representa un acuerdo de servicio de producción. Al terminar, el programa devuelve `0` si todas las tandas cumplen, `1` si alguna no cumple y `2` si no pudo preparar o completar la ejecución.

Para cambiar timeout, umbral o hacer una comprobación pequeña:

```bash
.venv/bin/python modules/07_pruebas/performance_test.py \
  --concurrencias 10 20 --timeout 30 --p95-ms 500
```

La ejecución normal sigue usando 1.000, 2.000, 5.000 y 6.000. Utilice una instancia nueva para cada repetición. Si falla una creación, la prueba guarda su evidencia y se detiene antes de lanzar consultas masivas; pueden quedar reservas parcialmente preparadas. Una interrupción durante una tanda puede dejar esa tanda sin registros finales.

Compare p95, errores y solicitudes por segundo entre tandas. Explique qué cambió, dónde puede haber espera y qué evidencia adicional necesitaría para localizar el límite. Cliente y API en la misma máquina comparten recursos; esta medición caracteriza ese ambiente local con repositorio en memoria. Evaluar PostgreSQL, otra máquina o un despliegue cloud requiere registrar ese ambiente y repetir la medición. La prueba de carga se ejecuta por separado del workflow funcional para que el resultado de CI conserve su propósito.

El cliente utiliza [aiohttp](https://docs.aiohttp.org/en/stable/client_quickstart.html) y configura los [límites del pool de conexiones](https://docs.aiohttp.org/en/stable/client_advanced.html#limiting-connection-pool-size) para cada tanda.
