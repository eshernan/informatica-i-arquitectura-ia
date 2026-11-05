# Ejercicios de pruebas y consultas seguras

**Sesión 12, 4 de noviembre de 2026.** Cada equipo trabaja dos riesgos: una regla de reservas y una consulta que debe conservar la entrada como dato. En ambos ejercicios se ejecuta una prueba correcta, se introduce un error pequeño y se comprueba que la prueba lo detecta. La entrega conserva la implementación restaurada.

![Elementos de las pruebas de hoy](../../docs/imagenes/pruebas-sesion12.jpg)

La demostración HTTP relaciona las reglas con la respuesta al cliente. PostgreSQL es una ampliación para equipos con una base exclusiva de pruebas ya preparada. La sesión termina con evidencia de los casos, sus resultados y la relación entre CI e imagen.

## Preparación

Si necesita una copia nueva:

```bash
git clone --branch update_esteban https://github.com/eshernan/informatica-i-arquitectura-ia.git
cd informatica-i-arquitectura-ia
```

Si ya tiene el repositorio, actualice la rama del curso antes de iniciar la práctica. Con sus cambios anteriores guardados y estando en `update_esteban`:

```bash
git pull --ff-only origin update_esteban
```

Desde la raíz del repositorio, prepare el entorno antes de clase y ejecute la selección de pruebas:

```bash
./scripts/setup_python.sh --apply
make test-sesion12
```

El comando usa memoria para HTTP y selecciona dominio, respuestas de la API y consulta segura: **13 pruebas** con el código de referencia. No necesita Docker ni PostgreSQL. El entorno `.venv` contiene las dependencias de desarrollo del curso. Los comandos de esta guía usan Bash en Linux o macOS.

Abra una rama para el trabajo de su equipo antes de introducir errores deliberados. Restaure solamente las líneas que cambie en el ejercicio, conservando sus demás avances.

## Ejercicio 1 Reglas de reservas y regresión funcional

**Riesgo:** rechazar una reserva permitida cuando comienza exactamente al terminar la anterior.

| Elemento del caso | Valor |
|---|---|
| Primera reserva | 08:00 a 09:00 |
| Segunda reserva | 09:00 a 10:00 |
| Acción | Preguntar si los intervalos se solapan |
| Expectativa | No existe solapamiento |

### Lectura y primera ejecución

Abra [test_domain.py](../../labs/librereserva/tests/test_domain.py) y localice `test_intervalos_contiguos_no_se_solapan`. Identifique la preparación, la acción y la aserción antes de ejecutar:

```bash
.venv/bin/python -m unittest \
  labs.librereserva.tests.test_domain.IntervaloTest.test_intervalos_contiguos_no_se_solapan -v
```

La prueba debe pasar. Explique por qué `self.assertFalse(...)` expresa la regla del caso.

### Error controlado

En [domain.py](../../labs/librereserva/app/domain.py), localice `Intervalo.se_solapa`. Su regla es:

```python
return self.inicio < otro.fin and otro.inicio < self.fin
```

Cambie temporalmente las dos comparaciones:

```python
return self.inicio <= otro.fin and otro.inicio <= self.fin
```

Prediga el resultado y repita el mismo comando. La prueba debe fallar porque el cambio interpreta el límite compartido como solapamiento. Conserve el nombre del caso y la diferencia que informa el resultado.

### Restauración y explicación

Restaure la regla original y ejecute de nuevo. La prueba debe pasar. La expectativa se mantiene porque la decisión sobre reservas contiguas no cambió.

**Entregue:** entrada y expectativa, resultado inicial, fallo con `<=`, resultado restaurado y una explicación del efecto que tendría el error para quien reserva una sala.

## Ejercicio 2 Consulta parametrizada y regresión de seguridad

**Riesgo:** una entrada modifica el filtro SQL y devuelve reservas distintas de las solicitadas.

Abra [test_consulta_segura.py](test_consulta_segura.py). Es un ejemplo docente de búsqueda por sala con SQLite en memoria y datos ficticios. El endpoint actual `GET /reservas` todavía no ofrece ese filtro; estas pruebas no verifican el adaptador PostgreSQL de la aplicación.

### Lectura y primera ejecución

```bash
.venv/bin/python modules/07_pruebas/test_consulta_segura.py
```

Las tres pruebas deben pasar:

| Entrada | Expectativa |
|---|---|
| `A-101` | Solo la fila de esa sala |
| `Sala O'Reilly` | El apóstrofe se conserva como parte del dato |
| `' OR '1'='1` | No amplía el filtro; no hay una sala con ese nombre literal |

Cada prueba prepara su propia base. El caso del apóstrofe añade ese nombre como un registro adicional únicamente dentro de su ejecución.

### Error controlado

La función `buscar_por_recurso` utiliza el marcador `?` y entrega el valor por separado. Sustituya temporalmente su cuerpo por la siguiente construcción insegura:

```python
return conexion.execute(
    f"SELECT id, recurso FROM reservas WHERE recurso = '{recurso}' ORDER BY id"
).fetchall()
```

Ejecute solamente el caso de seguridad:

```bash
.venv/bin/python modules/07_pruebas/test_consulta_segura.py \
  ConsultaSeguraTest.test_entrada_sql_no_amplia_los_resultados
```

La prueba espera una lista vacía y debe fallar al recibir las filas de A-101 y B-202. Explique qué parte de la entrada cambió el significado de la consulta.

### Restauración y explicación

Restaure el cuerpo parametrizado:

```python
return conexion.execute(
    "SELECT id, recurso FROM reservas WHERE recurso = ? ORDER BY id",
    (recurso,),
).fetchall()
```

Ejecute las tres pruebas nuevamente. Aunque la entrada parezca SQL, debe tratarse como un valor. En psycopg, el adaptador de PostgreSQL usa `%s` como marcador; el ejemplo SQLite usa `?`. La parametrización de valores y la autorización de usuarios resuelven riesgos diferentes.

**Entregue:** resultados de las tres entradas, fallo observado con concatenación, resultado restaurado y explicación de por qué eliminar apóstrofes manualmente podría rechazar nombres válidos.

## Demostración HTTP

Abra [test_http.py](test_http.py) y localice `test_api_crea_y_rechaza_solapamiento`. Prediga las respuestas para dos POST con el mismo recurso e intervalo:

```bash
LIBRERESERVA_REPOSITORY=memory .venv/bin/python -m pytest \
  modules/07_pruebas/test_http.py -v
```

La creación devuelve `201` y el conflicto `409`. Las otras pruebas verifican el borrado con `204` y una reserva inexistente con `404`. `setup_function` limpia el repositorio antes de cada caso. `TestClient` ejecuta la aplicación dentro de Python; esta comprobación no atraviesa Caddy, contenedores ni PostgreSQL cuando se selecciona memoria.

Como ampliación breve, añada al caso de creación y conflicto una consulta que compruebe que quedó exactamente una reserva y que conserva el recurso solicitado. Explique qué evidencia aporta esa aserción además del código HTTP.

## Ampliación con PostgreSQL

Use [las pruebas de contrato](../../labs/librereserva/tests/test_repository_contract.py) solo si dispone de una **base exclusiva de pruebas**. El código aplica la migración y vacía la tabla `reservas` antes de cada caso. Una conexión ausente produce tres pruebas omitidas; eso no comprueba la integración.

Con el PostgreSQL del laboratorio activo, puede crear una base separada, una sola vez:

```bash
docker exec librereserva-postgres psql -U curso -d postgres \
  -c 'CREATE DATABASE reservas_pruebas OWNER curso;'
```

Si ya existe esa base de pruebas, utilícela sin repetir su creación. Ejecute:

```bash
LIBRERESERVA_TEST_DATABASE_URL=\
'postgresql://curso:solo-laboratorio@127.0.0.1:5432/reservas_pruebas' \
  .venv/bin/python -m unittest \
  labs.librereserva.tests.test_repository_contract -v
```

Con Podman, sustituya `docker` por `podman`. Estos valores corresponden al ambiente local ficticio de [Compose](../06_apis_datos_eventos/compose.yml). El contrato comprueba crear, listar, borrar y rechazar solapamientos en ambos adaptadores. El caso concurrente de PostgreSQL espera exactamente una creación y un conflicto.

## CI e identificación de la imagen

Con las reglas restauradas, ejecute:

```bash
make test-sesion12
make check
make test-all
git diff --check
```

Las tres pruebas de PostgreSQL pueden quedar omitidas en la suite completa si no hay conexión de pruebas configurada. Registre esa condición. La selección específica de sesión 12 no incluye esa integración.

En la rama del equipo, conserve una ejecución CI fallida con un error controlado y otra correcta después de restaurar el código. En la fallida, compruebe que el paso de construcción se omite. El [workflow](../../.github/workflows/validate.yml) ejecuta la suite, construye una imagen etiquetada con el SHA probado y conserva `image-id.txt` y `librereserva-image.tar.gz` como artefacto durante tres días.

Registre el SHA que realmente usó CI. En un pull request puede corresponder a la integración de prueba de GitHub. La etiqueta, el commit y el ID de imagen tienen propósitos diferentes; reúna la evidencia de la misma ejecución. Descargar ese artefacto no equivale a publicar en un registro ni a desplegar la aplicación.

## Entrega

Complete la [plantilla de evidencia](EVIDENCIA_SESION12.md) en la rama de su equipo y añada el enlace al pull request. La implementación final debe conservar las consultas parametrizadas y la regla correcta de intervalos.

La revisión comprueba que el equipo puede explicar sus dos riesgos, identificar las aserciones, demostrar un error detectado y reconocer qué quedó fuera del alcance. Las pruebas de rendimiento y una suite E2E automatizada siguen como ampliaciones; no se exigen hoy.
