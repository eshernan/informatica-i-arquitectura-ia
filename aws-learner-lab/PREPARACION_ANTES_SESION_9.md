# Preparación obligatoria antes de la sesión 9

Esta actividad no consume tiempo del encuentro del 14 de octubre. Debe quedar completada por docentes y estudiantes antes de las 6:00 p. m. de ese día.

## Preparación institucional y docente

El responsable de la clase debe verificar:

- membresía activa de la institución en AWS Academy;
- acceso docente y finalización del proceso de incorporación requerido por AWS Academy;
- clase de Learner Lab creada para Informática I, segundo semestre de 2026;
- estudiantes invitados con el correo institucional y capacidad de iniciar el laboratorio;
- región común, presupuesto/crédito, duración de la sesión y fecha de cierre;
- disponibilidad real de CloudFormation, S3, DynamoDB, SQS, Lambda, API Gateway, CloudWatch y, solo si se usará, ECR;
- rol de ejecución disponible para Lambda y su ARN, sin crear roles adicionales;
- acceso a CloudShell o, como alternativa, uso de la consola y AWS CLI local con credenciales temporales;
- una cuenta de prueba con la misma experiencia y permisos que un estudiante.

Si Lambda, API Gateway o el rol de laboratorio no están habilitados, la sesión 13 usa FastAPI local y los servicios habilitados solo como comparación. Si ECR no está disponible, la sesión 14 termina en el registro local de Podman y `kind`.

## Prueba docente de humo

Con una sesión de prueba de Learner Lab iniciada:

```bash
export AWS_REGION=REGION_ACORDADA
./aws-learner-lab/scripts/check_preparation.sh

./aws-learner-lab/scripts/stack.sh deploy \
  libre-reserva-s09-docente \
  aws-learner-lab/templates/s09-foundation.yaml --apply

aws cloudformation describe-stacks \
  --stack-name libre-reserva-s09-docente \
  --region "$AWS_REGION" \
  --query 'Stacks[0].Outputs' --output table

./aws-learner-lab/scripts/stack.sh delete \
  libre-reserva-s09-docente --apply
```

El docente repite la validación de la plantilla de cada semana antes de publicar la práctica. No basta con que el servicio aparezca en la consola: el rol estudiantil debe poder desplegarlo y eliminarlo.

## Preparación del estudiante

1. Acepte la invitación a la clase con su cuenta institucional.
2. Inicie Learner Lab y ubique el acceso a la consola de AWS.
3. Abra CloudShell si está habilitado. Si no lo está, instale AWS CLI v2 en su equipo y use únicamente las credenciales temporales entregadas por el laboratorio.
4. Clone este repositorio y compruebe el entorno local:

```bash
git clone https://github.com/eshernan/informatica-i-arquitectura-ia.git
cd informatica-i-arquitectura-ia
./scripts/check_environment.sh
./scripts/install_base.sh          # muestra el plan
./scripts/install_base.sh --apply  # solo después de revisarlo
./scripts/setup_python.sh --apply
./aws-learner-lab/scripts/check_preparation.sh
make test
```

5. Registre en la entrega previa: identificador de cuenta parcialmente oculto, región, servicios disponibles, salida de `make test` y cualquier restricción encontrada.
6. Repase los conceptos equivalentes a AWS Academy Cloud Foundations: regiones y zonas, responsabilidad compartida, IAM, cómputo, almacenamiento, redes, bases de datos, monitoreo y costos.

### Preparación escalonada de contenedores

Podman no es necesario en la sesión 9 y `kind` no es necesario hasta la sesión 14. Para evitar dedicar esa clase a instalaciones, complete antes del 18 de noviembre la [instalación de Podman](../modules/08_entrega_plataforma/README.md) y las guías oficiales de `kubectl` y `kind` enlazadas allí. Después ejecute:

```bash
./aws-learner-lab/scripts/check_preparation.sh --full
podman info
kind version
kubectl version --client
```

El docente publica este recordatorio al terminar la sesión 12 y verifica el modo `--full` al inicio de la sesión 14.

## Reglas de credenciales

- No copie valores de `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` o `AWS_SESSION_TOKEN` en un archivo del repositorio, chat, captura o entrega.
- Prefiera CloudShell para evitar transportar credenciales.
- Si usa CLI local, renueve las credenciales cuando el laboratorio se reinicie y elimine el perfil temporal al terminar.
- Nunca use credenciales personales ni una cuenta AWS propia para completar una práctica del curso.

## Criterio de habilitación

La sesión 9 puede empezar su práctica si al menos el 90 % del grupo inicia Learner Lab, obtiene identidad con STS y conoce la región acordada. Los casos pendientes trabajan en pareja durante el encuentro y se resuelven con soporte institucional; no se cambia a cuentas personales.
