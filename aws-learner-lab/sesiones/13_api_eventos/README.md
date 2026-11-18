# Sesión 13 — Configuración segura y despliegue reproducible

**Fecha prevista:** 11 de noviembre de 2026, 6:00–10:00 p. m.

**Estado confirmado el 18 de noviembre:** clase suspendida. Los contenidos esenciales se integran en la [clase del 18 de noviembre](../14_pruebas_entrega/README.md). La secuencia que sigue conserva la planificación original como referencia, sin registrar estos temas como dictados el día 11.
**Resultado:** ejecutar la imagen identificada en sesión 12 con configuración externa, sin secretos incorporados y con un procedimiento reproducible de migración y arranque.

## Alcance

Pruebas, CI y pruebas de desempeño se trabajaron el 4 de noviembre, según confirmación docente del 9 de noviembre. La prueba disponible crea 100 reservas y consulta en tandas de 1.000, 2.000, 5.000 y 6.000 solicitudes concurrentes, conservando respuestas y tiempos. Su explicación y ejecución completa ya pertenecen a la clase anterior.

Esta sesión utiliza esa entrega y se concentra en configuración, secretos, permisos y reproducción del despliegue. Aunque la imagen sea la misma, cada ambiente debe aportar su configuración sin incorporar credenciales al artefacto ni al repositorio.

Se conserva FastAPI, Caddy, Compose y PostgreSQL. El trabajo principal es un despliegue local reproducible. Logs del servidor, correlación y respaldo/restauración se reservan al 18 de noviembre. Kubernetes, gestores externos de secretos y un despliegue cloud no se añaden al taller.

## Pregunta que orienta la clase

**¿Qué necesita otro equipo para ejecutar nuestra misma versión sin conocer los detalles de nuestra máquina ni recibir nuestras credenciales?**

La apertura usa el experimento de desempeño para recordar que una medición depende de la versión, la configuración y el ambiente. Un p95 alto o un fallo de conexión no permite atribuir por sí solo la causa a PostgreSQL, al balanceador o al código. Hoy se documenta el ambiente para que otra persona pueda reproducir la ejecución.

## Ideas que deben quedar claras

| Elemento | Explicación para la clase | Ejemplo en LibreReserva |
|---|---|---|
| Código e imagen | Definen la versión del programa que vamos a ejecutar | Commit, ID de imagen y dependencias |
| Configuración | Indica cómo debe ejecutarse esa versión en un ambiente | Adaptador `postgres`, puerto y nombre de base |
| Secreto | Es un valor cuyo acceso debemos restringir | Contraseña o cadena de conexión con credenciales |
| Permisos | Definen qué puede hacer cada proceso | La API ya se ejecuta con UID `10001`, sin ser root |
| Datos persistentes | Deben conservarse al reemplazar el proceso de la API | PostgreSQL y su volumen separado |

![Sketch del despliegue sin estado y almacenamiento separado](../../../docs/imagenes/despliegue-sin-estado-cloud.jpg)

El dibujo presenta la visión general. En este taller se usa su parte local: imagen identificada, configuración externa, API y PostgreSQL. Aunque las réplicas puedan reemplazarse, los datos deben permanecer. Los servicios cloud del dibujo quedan como contexto de arquitectura.

Un `.env.example` describe nombres y valores ficticios que sí pueden compartirse. Un `.env` local no cifra ni protege automáticamente un secreto. En Compose, el archivo `.env` puede alimentar la interpolación; la configuración debe declarar cómo pasan los valores al contenedor mediante `environment` o `env_file`. Consulte la [interpolación de variables](https://docs.docker.com/compose/how-tos/environment-variables/variable-interpolation/).

Las variables de entorno pueden aparecer en inspecciones o salidas de diagnóstico. Para credenciales reales, los [secretos de Compose](https://docs.docker.com/compose/how-tos/use-secrets/) permiten conceder archivos a servicios concretos. La API de referencia todavía lee `DATABASE_URL` desde el entorno; no se atribuye soporte a `DATABASE_URL_FILE` ni a un gestor de secretos. El mínimo de clase trabaja exclusivamente con valores ficticios.

## Secuencia de cuatro horas

| Hora | Tema y acción |
|---|---|
| 6:00–6:15 | revisar un resumen de desempeño e identificar versión, ambiente y condiciones; sin repetir la carga |
| 6:15–6:40 | clasificar ejemplos como código, configuración, secretos o datos |
| 6:40–7:10 | explicar imagen identificada, variables, `.env.example`, secretos y permisos mínimos |
| 7:10–7:50 | demostrar configuración externa y orden PostgreSQL → migración → API → balanceador; retirar una variable y observar el diagnóstico |
| 7:50–8:00 | pausa |
| 8:00–8:45 | taller por parejas: documentar variables, preparar ejemplo y desplegar la imagen identificada |
| 8:45–9:25 | intercambiar instrucciones con otra pareja y reproducir el arranque |
| 9:25–9:50 | crear una reserva, reemplazar la API y comprobar datos, imagen y usuario de ejecución |
| 9:50–10:00 | entregar evidencia y registrar pendientes de diagnóstico y recuperación |

## Demostración guiada

1. Mostrar el ID de imagen y explicar que cambiar una variable de ejecución no exige reconstruirla.
2. Localizar `LIBRERESERVA_REPOSITORY` y `DATABASE_URL` en la API y relacionarlas con Compose.
3. Arrancar PostgreSQL, aplicar la migración una vez para el despliegue y después iniciar las API y el balanceador. El servicio `migracion` ya existe; la dependencia actual de las API solo espera a PostgreSQL, por lo que el procedimiento debe asegurar que la migración termine antes de servir solicitudes. Compose distingue [servicio saludable y tarea completada](https://docs.docker.com/compose/how-tos/startup-order/).
4. Retirar `DATABASE_URL` manteniendo explícitamente el adaptador `postgres`. Observar el error y corregir la configuración sin imprimir credenciales. Si se omite el adaptador, la referencia selecciona memoria; ese caso no demuestra persistencia.
5. Crear y consultar una reserva. Reemplazar únicamente la API conservando la misma imagen, configuración y volumen de PostgreSQL; consultar de nuevo.
6. Mostrar que `USER 10001:10001` ya está definido y comprobarlo en el contenedor. No se vuelve a implementar un requisito que la imagen ya cumple.

## Taller

1. Use la imagen y el commit identificados en la sesión anterior; registre ambos.
2. Documente las variables obligatorias, su significado y el comportamiento si faltan.
3. Obtenga la conexión a PostgreSQL mediante configuración externa.
4. Prepare un `.env.example` con valores ficticios, sin credenciales reales.
5. Compruebe que archivos con secretos no se versionan ni se copian a la imagen.
6. Separe los valores públicos de laboratorio de cualquier configuración real.
7. Compruebe que el proceso del contenedor se ejecuta como usuario no privilegiado.
8. Ejecute las migraciones mediante un paso separado antes de iniciar las réplicas, sin lanzarlas desde cada API.
9. Pida a otro integrante reproducir el arranque con las instrucciones y la configuración de ejemplo.
10. Cree y consulte una reserva. Reemplace únicamente la API y compruebe que la reserva sigue disponible; registre los permisos o variables que impidieron el arranque si los hubo.

El mínimo entregable es una configuración de laboratorio reproducible, un ejemplo sin secretos reales y una validación funcional. Roles separados de base de datos, secretos montados y automatización adicional pueden registrarse como ampliaciones si el grupo completa ese mínimo.

## Preparación docente y estado del repositorio

| Material | Estado revisado el 9 de noviembre | Preparación necesaria |
|---|---|---|
| [Prueba de desempeño](../../../modules/07_pruebas/PRUEBA_RENDIMIENTO.md) | Disponible en módulo 7; ya trabajada en clase | Llevar un `resumen.csv`; usarlo solo en la apertura |
| [API](../../../labs/librereserva/app/main.py) | Lee el adaptador y `DATABASE_URL` del entorno | Preparar los casos de configuración correcta y variable faltante |
| [Compose acumulativo](../../../modules/06_apis_datos_eventos/compose.yml) | Contiene valores ficticios escritos directamente y etiqueta `0.1.0` | Preparar una variante parametrizada, referencia de imagen identificada y `.env.example` antes del encuentro |
| [Imagen](../../../labs/librereserva/Containerfile) | Ya utiliza `USER 10001:10001`; copia explícitamente la aplicación | Preparar inspección del usuario y del contenido de la imagen |
| [Migración](../../../labs/librereserva/migrations/001_crear_reservas.sql) | Disponible y ejecutada por un servicio separado | Ensayar el orden de ejecución con la base de laboratorio |
| Exclusión de archivos locales | `.env` ya está en `.gitignore` | Comprobar también nombres alternativos que se decida usar y las reglas del contexto de construcción |

Estos ajustes de configuración son preparación pendiente del laboratorio; esta guía no afirma que la variante parametrizada ya esté implementada. Ensaye con el motor elegido para la clase y conserve una imagen local disponible para evitar que una descarga o instalación consuma el taller.

## Validación

```bash
make check
make test-all
git status --short
```

La misma imagen debe poder arrancar con su configuración documentada. Otro equipo debe lograrlo siguiendo las instrucciones. La reserva creada debe permanecer tras reemplazar la API y el usuario de ejecución debe ser no privilegiado.

No copie secretos reales en logs, capturas, README o historial de comandos. El registro de cuerpos de `performance_test.py` se diseñó para datos ficticios; no se traslada automáticamente a logs de operación con datos sensibles. Las pruebas siguen ejecutándose como comprobación del despliegue, sin repetir el taller de CI ni la carga completa. La suite local omite las pruebas PostgreSQL si no se configura su conexión de pruebas; una ejecución verde no sustituye la comprobación del despliegue.

**Evidencia:** commit e imagen utilizados, variables documentadas, configuración de ejemplo, revisión de secretos, usuario de ejecución, procedimiento de migración/arranque reproducido por otra persona y reserva consultada después de reemplazar la API.
