# Preparación de AWS Learner Lab para LibreReserva

**Sesión integrada del 18 de noviembre de 2026.** La práctica utiliza EC2 dentro de AWS Academy Learner Lab. Cada instancia ejecuta Caddy, las dos API y PostgreSQL con Docker Compose. Session Manager abre la terminal de EC2 desde el navegador. La prueba de la API se hace con `curl` en esa terminal o con Swagger a través de un túnel autorizado.

## 1. Comprobaciones en AWS Academy

1. Abre la actividad **AWS Academy Learner Lab**, selecciona **Start Lab** y entra a la consola desde el enlace **AWS** de la actividad cuando el entorno esté listo.
2. En el README de tu sandbox, verifica región habilitada, tiempo restante, crédito y límites para EC2. Selecciona esa región en la consola. La pantalla de lanzamiento muestra disponibilidad, mientras que el permiso efectivo se comprueba al lanzar o al reutilizar una instancia autorizada.
3. En **AWS Details**, localiza **LabIDEURL** si necesitas una terminal para editar el repositorio o preparar archivos antes de lanzar EC2. El enlace incluye autenticación y se usa desde la sesión asignada. El Lab IDE y la terminal de EC2 son entornos distintos.
4. Confirma qué VPC, subred y grupo de seguridad puedes utilizar. El README del sandbox indica que puedes asociar **LabInstanceProfile**, que ya contiene **LabRole**. IAM tiene acceso de lectura para roles ordinarios. Si aparece un error de autorización, registra la operación y la región y pasa al ensayo docente o a la alternativa prevista.

| Recurso | Función en la práctica | Configuración propuesta |
|---|---|---|
| EC2 | Aloja LibreReserva | `t3.small` On-Demand como punto de partida. Confirma que el selector permite la AMI oficial Ubuntu Server 24.04 LTS x86-64 y que su agente SSM está disponible. Si eliges otra distribución, usa su procedimiento de instalación correspondiente |
| Cuota de EC2 | Limita el trabajo simultáneo | Hasta 9 instancias encendidas en el mismo sandbox, incluida la docente si comparte la cuenta. Con una instancia docente quedan hasta 8 para equipos en esa cuenta. Coordina turnos si hacen falta |
| EBS | Aloja los archivos y los volúmenes Docker | Disco raíz `gp2` de 20 GiB como punto de partida. El README fija un máximo de 35 GB por volumen. Revisa el ajuste de eliminación al terminar la instancia |
| VPC y subred | Conectividad de la instancia | Usa una red existente con salida HTTPS a SSM, GitHub y repositorios de paquetes e imágenes. Verifica DNS. Usa la salida ya disponible en el laboratorio |
| Grupo de seguridad | Controla quién llega a EC2 | Con Session Manager, deja la entrada cerrada. Para el respaldo por SSH, habilita TCP 22 solo desde la IP autorizada. Caddy y PostgreSQL quedan vinculados a loopback |
| Perfil de instancia | Autoriza al agente y, cuando corresponde, a la aplicación | Selecciona `LabInstanceProfile` al lanzar. Verifica en una instancia piloto las operaciones concretas que utilizarás |
| Etiquetas | Identifican los recursos | Por ejemplo, `Course=InformaticaI`, `Session=14`, `Team=02` y `Name=librereserva-s14-e02` |

La ruta base usa EC2, EBS, la red existente y Session Manager. PostgreSQL, Caddy y las API son contenedores. CloudWatch Logs y Parameter Store se incorporan como ampliaciones tras ensayar sus permisos. RDS es una opción para una clase sobre bases gestionadas. El respaldo y la restauración de esta práctica usan el PostgreSQL de Compose.

Si la cuenta permite guardar una plantilla de lanzamiento EC2, registra la AMI, el tipo, el disco, el grupo de seguridad, el perfil y los datos de usuario. Asigna las etiquetas de equipo al lanzar. Si usas CloudFormation para repetir el despliegue, la pila debe referenciar el perfil existente; comprueba sus operaciones en una sola instancia antes de desplegar varias. [Plantillas de lanzamiento EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-launch-template.html).

Referencias de [AWS Academy](https://aws.amazon.com/training/awsacademy/), [red pública de VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html), [acceso SSH en EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-to-linux-instance.html), [pares de claves](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) y [volúmenes EBS](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes.html).

## Lanzamiento manual desde la consola EC2

1. En Learner Lab, abre **Start Lab → AWS → EC2 → Launch instance** en la región habilitada.
2. Usa un nombre propio del equipo, por ejemplo `librereserva-s14-equipo01`. Selecciona **Ubuntu Server 24.04 LTS x86-64**, `t3.small` bajo demanda y **20 GiB gp2**. En configuración avanzada selecciona **LabInstanceProfile**. El README permite hasta nueve EC2 en ejecución por sandbox y volúmenes gp2 de hasta 35 GB.
3. Selecciona una subred con salida HTTPS a SSM, GitHub, Docker y repositorios de Ubuntu. Usa un grupo de seguridad de esa VPC con entrada cerrada para Session Manager. Usa IPv4 pública únicamente si la necesitas para la salida a Internet y el laboratorio la permite.
4. Si quieres instalar LibreReserva en el primer arranque, descarga [el archivo de datos de usuario](../../scripts/bootstrap_ec2.sh) mediante **Download raw file** en GitHub. En **Advanced details → User data**, carga el archivo como texto con la casilla «ya codificado en base64» desactivada. El archivo ya fija el commit de la práctica.

Para repetir la instalación con otra versión, genera una copia desde la raíz del repositorio y sustituye `SHA_PUBLICADO` por su SHA completo.

~~~bash
{
  printf '#!/bin/bash\n'
  printf 'export LIBRERESERVA_COMMIT=%s\n' SHA_PUBLICADO
  tail -n +2 aws-learner-lab/scripts/bootstrap_ec2.sh
} > librereserva-ec2-user-data.sh
bash -n librereserva-ec2-user-data.sh
~~~

Los datos de usuario usan un commit público y generan la contraseña de PostgreSQL en la EC2. La credencial queda en un archivo accesible por root. Los administradores de Docker pueden inspeccionar el entorno de los contenedores. El proceso prepara imágenes, aplica la migración y configura la rotación local de logs. Los permisos opcionales de AWS se ensayan después.

Desde **EC2 → Connect → Session Manager**, comprueba el primer arranque:

~~~bash
sudo cloud-init status --wait
sudo cat /var/lib/librereserva/estado
sudo librereserva-compose ps
curl -fsS http://127.0.0.1:8080/reservas
~~~

`LISTO` indica que `GET /reservas` devolvió una lista. Si el proceso dejó `FALLO`, revisa `sudo tail -n 80 /var/log/librereserva-bootstrap.log`. Usa `sudo librereserva-compose` para operar esta instalación. Si preparas la EC2 de forma interactiva, sigue las secciones de herramientas y arranque de esta guía.

## 2. Acceso a EC2 y a LibreReserva

En la consola abre **EC2 → Instances → Connect → Session Manager**. La instancia debe tener el agente SSM activo, el perfil `LabInstanceProfile` y conectividad hacia Systems Manager. Cuando aparezca la terminal, comprueba `hostname` y `sudo -v`. En esa misma terminal podrás ejecutar `curl -fsS http://127.0.0.1:8080/reservas` después de levantar Compose. [Requisitos de Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-prerequisites.html) y [conectividad de SSM](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-create-vpc.html).

Para abrir Swagger desde el portátil mediante SSM, comprueba primero que tu sesión temporal está activa en AWS CLI local, que instalaste el complemento de Session Manager y que tienes permiso para usar el documento `AWS-StartPortForwardingSession`. Sustituye el identificador y la región por los de tu instancia.

~~~bash
aws ssm start-session \
  --region REGION_DEL_LAB \
  --target i-ID_DE_TU_INSTANCIA \
  --document-name AWS-StartPortForwardingSession \
  --parameters '{"portNumber":["8080"],"localPortNumber":["18080"]}'
~~~

Con la sesión abierta, entra a `http://127.0.0.1:18080/docs`. El permiso para abrir una terminal en la consola y el permiso para usar el documento de túnel se comprueban por separado. Si el túnel no está disponible, usa `curl` en la terminal de EC2 o el acceso SSH de respaldo. [Reenvío de puertos con Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-sessions-start.html#sessions-start-port-forwarding).

### Acceso SSH de respaldo

Si el lab autoriza SSH directo, verifica la IPv4 pública, la ruta de la subred y la regla de entrada TCP 22 restringida a tu IP. Usa el par de claves asociado a la instancia. En la terminal local, sustituye la ruta de la clave y la IP pública. El usuario de la AMI Ubuntu suele ser `ubuntu`.

~~~bash
chmod 400 /ruta/clave-lab.pem
ssh -i /ruta/clave-lab.pem ubuntu@IP_PUBLICA
~~~

Abre otra terminal local para mantener activo el túnel:

~~~bash
ssh -N -o ExitOnForwardFailure=yes -i /ruta/clave-lab.pem \
  -L 127.0.0.1:8080:127.0.0.1:8080 ubuntu@IP_PUBLICA
~~~

El primer `127.0.0.1:8080` pertenece al portátil. El segundo pertenece a EC2. Después de iniciar Compose, abre `http://127.0.0.1:8080/docs`. Si el 8080 local ya está ocupado, cambia el primer puerto a 18080 y usa `http://127.0.0.1:18080/docs`.

El descriptor del curso publica Caddy y PostgreSQL en loopback. Las API usan la red interna de Compose. Deja cerrada la entrada pública a TCP 8080, 8000 y 5432. Si cambias de red, revisa la IP de origen autorizada en el grupo de seguridad. Si reinicias una instancia sin IP elástica, verifica su IPv4 pública antes de reconectar.

## 3. Herramientas e imágenes en EC2

Ejecuta en la terminal de Ubuntu abierta mediante Session Manager o SSH. Si el repositorio ya existe, entra en él y verifica rama, cambios locales y revisión acordada antes de actualizar. Si automatizas el primer arranque con datos de usuario, incluye aquí la instalación y la preparación de imágenes. Mantén los secretos fuera de esos datos. [Preparación de EC2 con datos de usuario](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html).

~~~bash
cat /etc/os-release
sudo -v
sudo apt-get update
sudo apt-get install -y git curl
git clone --branch update_esteban \
  https://github.com/eshernan/informatica-i-arquitectura-ia.git
cd informatica-i-arquitectura-ia
./scripts/install_docker_ubuntu.sh
./scripts/install_docker_ubuntu.sh --apply
sudo docker version
sudo docker compose version
~~~

El script del curso muestra el plan en la primera ejecución. Instala Docker Engine y su complemento Compose con `--apply`. Si Docker ya está instalado y funciona en la instancia, sigue con la preparación de imágenes. La ruta anterior requiere Ubuntu, permisos sudo y conectividad a los repositorios de paquetes. [Guía del instalador del curso](../../../modules/01_entorno/README.md#instalación-con-script-en-ubuntu-y-ec2) y [documentación de Docker para Ubuntu](https://docs.docker.com/engine/install/ubuntu/).

~~~bash
git branch --show-current
git rev-parse HEAD
sudo docker build -f labs/librereserva/Containerfile \
  -t localhost/librereserva:0.1.0 labs/librereserva
sudo docker image inspect localhost/librereserva:0.1.0 --format '{{.Id}}'
sudo docker pull docker.io/library/postgres:17-alpine
sudo docker pull docker.io/library/caddy:2-alpine
df -h /
~~~

Guarda el commit y el ID de la imagen. El Compose actual utiliza la etiqueta `localhost/librereserva:0.1.0`. Si falla una descarga, revisa primero DNS y conectividad de egreso. Si solo falla la construcción, conserva la salida y comprueba la disponibilidad de la imagen base y el acceso al índice de paquetes Python.

## 4. Ensayo de arranque antes de clase

Desde la raíz del repositorio en EC2, usa Bash. Ejecuta cada paso cuando el anterior termine correctamente. Esta ruta interactiva emplea la credencial de ejemplo del Compose del curso y datos ficticios. Mantén PostgreSQL en loopback y usa la instalación por datos de usuario si necesitas generar una contraseña por instancia.

~~~bash
dc=(sudo docker compose -f modules/06_apis_datos_eventos/compose.yml)
"${dc[@]}" config --quiet
"${dc[@]}" up -d --wait postgres
"${dc[@]}" run --rm --no-deps migracion
"${dc[@]}" up -d api_a api_b balanceador
"${dc[@]}" ps
"${dc[@]}" exec -T api_a id
curl -fsS --retry 8 --retry-all-errors --retry-delay 1 \
  http://127.0.0.1:8080/reservas
~~~

El servicio `migracion` prepara el esquema después de que PostgreSQL está disponible. La referencia espera la salud de PostgreSQL antes de iniciar las API. La ejecución explícita de la migración garantiza el orden de la demostración. Si el ensayo se realiza sobre un ambiente que ya está atendiendo, detén primero las API del equipo para ejecutar la secuencia en un estado controlado. [Orden de inicio en Compose](https://docs.docker.com/compose/how-tos/startup-order/) y [descriptor utilizado](../../../modules/06_apis_datos_eventos/compose.yml).

La comprobación mínima es un `GET /reservas` con HTTP 200 desde EC2. Una lista vacía es válida en una base nueva. Si habilitaste el túnel, repite la consulta desde Swagger en el portátil. La ruta de salud fija por sí sola no verifica la consulta a PostgreSQL.

## 5. Secretos, registros y evidencias

El ZIP compartido contiene `work/`, la configuración básica de Git y un archivo vacío de `.voc`. La captura muestra `resource/asnlib/lab.policy`, cuyo contenido se revisa desde el editor de autoría cuando el curso da acceso. El README confirma los servicios habilitados y que IAM tiene acceso de lectura para roles ordinarios. Para diagnosticar una denegación registra la operación, región, recurso y la identidad que la ejecutó. El docente autorizado o el administrador del laboratorio revisa la política concreta y el alcance permitido. [Políticas de AWS Cloud Labs en Vocareum](https://help.vocareum.com/en/articles/9425419-creating-an-aws-cloud-lab).

### Identidades y permisos

La consola del estudiante y el programa que corre en la EC2 usan identidades distintas. En la instancia, instala [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) si vas a probar los servicios opcionales. Usa las credenciales del perfil de instancia. Antes de probar, confirma que el ARN indica `assumed-role/LabRole/…`. Un resultado con otra identidad no prueba los permisos de la EC2. [Uso de roles desde AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-role.html).

~~~bash
aws sts get-caller-identity --region REGION_DEL_LAB --query Arn --output text
~~~

| Servicio | Operación a comprobar | Identidad y alcance |
|---|---|---|
| Session Manager | Abrir la terminal de la instancia seleccionada | El estudiante inicia la sesión. La EC2 usa el perfil existente `LabInstanceProfile` y necesita conectividad al servicio |
| SSM Parameter Store | Crear un parámetro ficticio `SecureString` y leerlo con descifrado desde EC2 | Para crear `ssm:PutParameter` en el nombre acordado. Para leer `ssm:GetParameter` en ese parámetro y autorización efectiva de descifrado en la clave usada |
| CloudWatch Logs | Crear un grupo de laboratorio con retención y publicar un evento de prueba | El operador del grupo necesita `logs:CreateLogGroup` y `logs:PutRetentionPolicy`. La EC2 necesita `logs:PutLogEvents` en su flujo y `logs:CreateLogStream` si va a crearlo |
| CloudTrail | Consultar eventos de creación o detención de EC2 en la región | La identidad que consulta necesita `cloudtrail:LookupEvents` |
| S3 | Guardar y recuperar un archivo de evidencia ficticia en un bucket privado autorizado | `s3:PutObject` y `s3:GetObject` en el prefijo o el objeto del equipo. La preparación del bucket queda a cargo de la identidad autorizada |

Los permisos se revisan solo si la operación falla y con el recurso específico. `Secrets Manager` queda fuera del plan porque el README compartido no lo enumera. El acceso de listado de KMS no demuestra descifrado. Si el lab restringe una operación de creación o uso, conserva la alternativa local en EC2. [Permisos de Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/ps-restrict-parameter-access.html), [CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/permissions-reference-cwl.html), [CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events-cli.html) y [S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-policy-actions.html).

### Piloto de un secreto

En la consola del sandbox, intenta crear un parámetro **Standard SecureString** con valor ficticio, por ejemplo `/informatica-i/s14/demo/equipo01/postgres-password`. Prueba con la clave administrada `alias/aws/ssm` que ofrezca la cuenta. El uso de un rol común y la clave administrada motiva usar datos ficticios para el ensayo. Desde la EC2 verifica el descifrado mostrando únicamente el nombre:

~~~bash
aws ssm get-parameter --region REGION_DEL_LAB \
  --name /informatica-i/s14/demo/equipo01/postgres-password \
  --with-decryption --query Parameter.Name --output text
~~~

Si devuelve el nombre, el acceso para ese parámetro queda comprobado. El piloto no cambia la contraseña de LibreReserva. La instalación por datos de usuario conserva su contraseña local. Una integración posterior debe suministrar un valor coherente a PostgreSQL, la migración y las API. La variable de inicialización de PostgreSQL se aplica a bases nuevas. [Cifrado SecureString](https://docs.aws.amazon.com/systems-manager/latest/userguide/secure-string-parameter-kms-encryption.html) y [configuración de PostgreSQL](https://hub.docker.com/_/postgres).

### Piloto de CloudWatch Logs

En la consola, prepara `/informatica-i/librereserva/sesion-14` con retención breve si tu identidad lo permite. Desde la EC2 ya preparada, ejecuta un contenedor de prueba que use el controlador de logs de AWS. El evento es un mensaje del contenedor de ejemplo. Usa un nombre de flujo propio del equipo:

~~~bash
sudo docker run --rm --log-driver=awslogs \
  --log-opt awslogs-region=REGION_DEL_LAB \
  --log-opt awslogs-group=/informatica-i/librereserva/sesion-14 \
  --log-opt awslogs-stream=equipo01/piloto \
  docker.io/library/hello-world
~~~

Comprueba que aparece el evento en **CloudWatch → Log groups**. Si el piloto funciona, se puede incorporar Caddy primero. Conserva los logs de la aplicación accesibles en EC2 mediante `sudo librereserva-compose logs`. El log local del primer arranque permite investigar la instalación. CloudTrail registra las operaciones de infraestructura; las solicitudes a LibreReserva se observan en Caddy y las API. [Controlador awslogs](https://docs.docker.com/engine/logging/drivers/awslogs/).

### Demostración

- Ten a mano una reserva ficticia de A-101 y su identificador. Para probar la configuración faltante, lanza un contenedor temporal con `LIBRERESERVA_REPOSITORY=postgres` y `DATABASE_URL` vacía. La aplicación debe detener el arranque con un mensaje explícito.
- Confirma que `api_a` corre como usuario no privilegiado. La imagen ya establece `USER 10001:10001`. La parametrización del Compose y el formato de logs por solicitud se explican como propuestas.
- Usa un entorno propio para detener PostgreSQL y observar el fallo. Guarda hora, ruta, estado y un fragmento de log, con valores ficticios.
- Guarda el respaldo fuera del contenedor y restaura en una base separada con un nombre nuevo. Mantén la base original. El ensayo comprueba una recuperación lógica dentro de la misma EC2.
- Conserva fuera de EC2 la evidencia ficticia que necesites entregar. Usa un bucket S3 privado y autorizado o SCP en la ruta de respaldo por SSH. Al cerrar, sigue las reglas del curso para detener o terminar solo la instancia del equipo. Verifica dónde quedarán los archivos y el disco antes de terminarla.

En la instancia piloto comprueba **Session Manager**, `docker compose version` y un **GET /reservas desde la EC2**. Si usarás Swagger, añade la comprobación del túnel. Si usarás los servicios opcionales, añade una lectura descifrada del parámetro ficticio y confirma que el evento del contenedor de prueba llega al grupo de CloudWatch. La disponibilidad de un servicio en el README y la autorización para una operación específica se verifican en momentos distintos.
