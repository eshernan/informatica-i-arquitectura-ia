# Guía docente para montar las sesiones en AWS Academy

AWS Academy y Learner Lab no son lo mismo: en la **clase** se organiza la experiencia académica; en el **Learner Lab** se ejecutan los recursos de nube. Los nombres exactos de botones y menús pueden variar con la interfaz institucional, pero el paquete que se publica y la secuencia de control se mantienen.

## 1. Crear y comprobar la clase

1. Ingrese al portal de AWS Academy con el perfil docente.
2. Cree o seleccione la clase de Learner Lab para `Informática I — 2026-II — LibreReserva`.
3. Configure apertura antes del 14 de octubre y cierre posterior al 2 de diciembre.
4. Invite a los estudiantes mediante el mecanismo institucional del portal.
5. Publique primero `PREPARACION_ANTES_SESION_9.md` y el enlace al repositorio.
6. Entre con un usuario de prueba, inicie el laboratorio y ejecute `check_preparation.sh`.
7. Registre región, rol disponible, crédito y restricciones en el anuncio inicial.

La creación de la clase y las invitaciones las realiza el docente. Los estudiantes no deben intentar crear por sí mismos una cuenta de AWS Academy.

## 2. Crear una actividad semanal

En la sección de proyecto, actividad o asignación disponible en su clase, publique una entrada con esta estructura:

```text
Título: SNN — LibreReserva — nombre de la sesión
Disponibilidad: miércoles, 5:45 p. m. a 10:15 p. m.
Duración esperada: 4 horas, incluida limpieza
Lectura principal: enlace al README de la sesión
Adjuntos/enlaces: plantilla CloudFormation, evidencia y código base
Región: la región acordada para el curso
Pila: libre-reserva-sNN-equipoXX
Entrega: enlace al commit/PR y evidencia en Markdown
Criterio de cierre: recursos eliminados y costo/consumo registrado
```

Para la semana 15, la ventana corresponde a trabajo autónomo y debe permanecer abierta durante la jornada completa. No se anuncia como encuentro sincrónico.

## 3. Adjuntar el contenido correcto

Cada actividad debe contener o enlazar:

- el `README.md` de la sesión;
- la plantilla de `aws-learner-lab/templates/` indicada en la matriz;
- [la plantilla de evidencia](evidencias/PLANTILLA.md);
- la rúbrica de cuatro criterios: decisión, ejecución, validación y limpieza;
- el repositorio y el identificador exacto de rama o etiqueta que se usará.

Es preferible enlazar una revisión inmutable del repositorio. Si se adjuntan copias, actualice al mismo tiempo README y plantilla para evitar instrucciones divergentes.

## 4. Validación antes de publicar

Para cada sesión, el docente:

1. inicia un Learner Lab de prueba;
2. comprueba identidad, región y tiempo restante;
3. ejecuta el despliegue con el mismo rol que tendrán los estudiantes;
4. realiza el caso feliz y al menos un caso de fallo;
5. estima el tiempo real y el consumo;
6. elimina la pila y comprueba que no queden recursos;
7. publica la actividad solo después de completar estos pasos.

Una plantilla válida sintácticamente puede fallar por política del laboratorio. La prueba con el rol estudiantil es el criterio definitivo.

## 5. Operación durante las cuatro horas

| Hora | Acción docente en Learner Lab |
|---|---|
| 6:00–6:20 | confirmar que todos iniciaron el laboratorio y revisar prerrequisitos |
| 6:20–7:10 | relacionar la decisión arquitectónica con el problema de LibreReserva |
| 7:10–7:50 | desplegar el ejemplo docente y explicar recursos, permisos y costo |
| 7:50–8:00 | pausa |
| 8:00–9:25 | acompañar el ejercicio; observar errores y espacios de trabajo |
| 9:25–9:50 | validar resultados, métricas, consumo y evidencia |
| 9:50–10:00 | ordenar limpieza y comprobar CloudFormation/servicios |

No se dedica el encuentro a crear cuentas ni a instalar herramientas extensas: esas acciones pertenecen a la preparación previa.

## 6. Matriz de montaje

| Sesión | Publicar | Plantilla | Verificación docente |
|---:|---|---|---|
| 9 | entorno y línea base | `s09-foundation.yaml` | S3 y CloudFormation; crear/leer/borrar objeto antes de borrar pila |
| 10 | calidad medible | sin despliegue obligatorio | notebook local; confirmar acceso de consulta a CloudWatch |
| 11 | dominio hexagonal | `s11-dynamodb.yaml` | escribir, leer y eliminar ítem DynamoDB |
| 12 | sistemas distribuidos | `s12-messaging.yaml` | mensaje, reintento, DLQ y purga |
| 13 | API, datos y eventos | `s13-serverless-api.yaml` | `LabRoleArn`, POST/GET, DynamoDB, SQS y logs |
| 14 | pruebas y entrega | `s14-ecr.yaml` opcional | push/pull, digest y eliminación de imágenes |
| 15 | jornada de proyecto | plantillas ya aprobadas | no introducir servicios nuevos |
| 16 | cierre | pila final del equipo | demo desde cero y barrido de recursos |

## 7. Revisión y cierre

Use las funciones disponibles en Learner Lab para inspeccionar los espacios de trabajo y las métricas de tiempo/dinero. Compare esa información con la evidencia entregada. Antes de cerrar la clase:

- las pilas `libre-reserva-*` deben estar eliminadas;
- no deben quedar tablas, colas, API, funciones, logs, repositorios o buckets del proyecto;
- cada equipo entrega confirmación de limpieza y consumo;
- los incidentes de permisos se documentan como restricciones de plataforma, no se evaden creando cuentas externas.

## Fuentes de operación

- [AWS Academy: capacidades de Learner Lab](https://aws.amazon.com/training/awsacademy/)
- [AWS Academy FAQ: incorporación institucional y docente](https://aws.amazon.com/training/awsacademy/faq/)
- [Inicio de sesión de AWS Academy](https://www.awsacademy.com/SelfRegister)
