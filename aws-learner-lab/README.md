# LibreReserva en AWS Academy Learner Lab

Este paquete contiene las prácticas del bloque orientado por el **Dr. Esteban Hernández Barragán**, semanas 9 a 16. LibreReserva no se usa como práctica obligatoria en las sesiones del Dr. Carlos Montenegro Marín.

AWS Academy cumple dos funciones diferentes:

1. la clase de AWS Academy publica la consigna, los enlaces, la rúbrica y la entrega;
2. cada AWS Academy Learner Lab proporciona un entorno temporal donde el estudiante despliega y elimina sus recursos.

No se almacenan credenciales de AWS en Git. Las plantillas no crean usuarios, claves ni roles IAM; cuando una función Lambda necesita ejecución, recibe el ARN del rol habilitado por el laboratorio.

## Antes del segundo bloque

1. El docente completa la [preparación antes de la sesión 9](PREPARACION_ANTES_SESION_9.md).
2. Configura la clase siguiendo la [guía docente](GUIA_DOCENTE_AWS_ACADEMY.md).
3. Publica la actividad previa con al menos cinco días de anticipación.
4. Cada estudiante inicia su Learner Lab y ejecuta:

```bash
git clone https://github.com/eshernan/informatica-i-arquitectura-ia.git
cd informatica-i-arquitectura-ia
./aws-learner-lab/scripts/check_preparation.sh
```

El script es de solo lectura: comprueba herramientas, identidad temporal, región y acceso a los servicios usados. No imprime secretos ni crea recursos.

## Ruta de ocho sesiones

| Semana | Fecha | Paquete que se publica | Recursos principales | Producto |
|---:|---|---|---|---|
| 9 | 14 oct. | [Entorno y línea base](sesiones/09_entorno/README.md) | Learner Lab, CloudFormation, S3 | entorno verificado y línea base |
| 10 | 21 oct. | [Calidad medible](sesiones/10_calidad/README.md) | CloudWatch como referencia; laboratorio local | escenarios y funciones de aptitud |
| 11 | 28 oct. | [Dominio hexagonal](sesiones/11_hexagonal/README.md) | DynamoDB | puerto, adaptador y persistencia |
| 12 | 4 nov. | [Decidir antes de distribuir](sesiones/12_distribuidos/README.md) | SQS y DLQ | experimento de fallo y ADR |
| 13 | 11 nov. | [API, datos y eventos](sesiones/13_api_eventos/README.md) | API Gateway, Lambda, DynamoDB, SQS | reserva idempotente y evento |
| 14 | 18 nov. | [Pruebas y entrega](sesiones/14_pruebas_entrega/README.md) | ECR opcional; OCI y kind local | pruebas, imagen y despliegue |
| 15 | 25 nov. | [Jornada autónoma](sesiones/15_proyecto/README.md) | servicios ya aprobados | incremento y bitácora de 4 horas |
| 16 | 2 dic. | [Demostración y cierre](sesiones/16_cierre/README.md) | pila final aprobada | demo, evidencia y limpieza total |

## Convenciones operativas

- Región: el docente selecciona una región habilitada y la comunica; el material usa `AWS_REGION` y no fija una región en las plantillas.
- Nombres de pilas: `libre-reserva-sNN-equipoXX`.
- Etiquetas mínimas: `Course=InformaticaI`, `Project=LibreReserva`, `Session=SNN`, `Team=equipoXX`.
- Una pila por sesión y equipo; no compartir credenciales entre integrantes.
- Capacidad bajo demanda o niveles mínimos; no se dejan recursos activos después de la evidencia.
- Cada práctica incluye una ruta local con software libre si el servicio no está habilitado.
- La limpieza se comprueba en CloudFormation y en la consola del servicio; cerrar la pestaña no elimina recursos.

## Despliegue conservador

El ayudante de pilas muestra el comando por defecto. Solo modifica AWS con `--apply`:

```bash
./aws-learner-lab/scripts/stack.sh deploy \
  libre-reserva-s11-equipo01 \
  aws-learner-lab/templates/s11-dynamodb.yaml

./aws-learner-lab/scripts/stack.sh deploy \
  libre-reserva-s11-equipo01 \
  aws-learner-lab/templates/s11-dynamodb.yaml --apply

./aws-learner-lab/scripts/stack.sh delete \
  libre-reserva-s11-equipo01 --apply
```

Antes de borrar una pila, el script exige el prefijo `libre-reserva-`, confirma que la pila existe y muestra sus recursos. Los repositorios ECR y los buckets con objetos deben vaciarse explícitamente antes de eliminar su pila.

## Evidencia común

Cada equipo copia [la plantilla de evidencia](evidencias/PLANTILLA.md), registra comandos y mediciones, enlaza su ADR y confirma la limpieza. Las capturas pueden apoyar la entrega, pero no sustituyen resultados reproducibles ni texto que explique la decisión.

## Referencias oficiales

- [AWS Academy](https://aws.amazon.com/es/training/awsacademy/)
- [Preguntas frecuentes de AWS Academy](https://aws.amazon.com/training/awsacademy/faq/)
- [Tutorial oficial: API HTTP con Lambda y DynamoDB](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-dynamo-db.html)
- [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
