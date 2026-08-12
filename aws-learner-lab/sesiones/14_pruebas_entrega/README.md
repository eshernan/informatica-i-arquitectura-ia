# Sesión 14 — Implementación, pruebas y entrega

**Fecha:** 18 de noviembre de 2026, 6:00–10:00 p. m.
**Resultado:** relacionar commit, pruebas, imagen OCI, digest y despliegue reproducible; usar ECR solo como registro opcional.

## Montaje docente en AWS Academy

Publique `S14 — LibreReserva — pruebas y entrega` con este archivo, `s14-ecr.yaml`, los módulos 7 y 8 y la evidencia. Una semana antes recuerde ejecutar `check_preparation.sh --full`. Verifique previamente que ECR admita crear repositorio, obtener token, subir y eliminar imágenes. Si no está habilitado, quite la sección ECR de la actividad: Podman y `kind` cubren el resultado completo.

## Secuencia de cuatro horas

| Hora | Tema y acción |
|---|---|
| 6:00–6:20 | revisión del corte vertical y estrategia de pruebas |
| 6:20–7:10 | pirámide de pruebas, OCI, digest, CI y reconciliación |
| 7:10–7:50 | demo de suite, construcción y despliegue `kind` |
| 8:00–9:25 | taller: prueba de fallo, imagen, digest, dos réplicas y recuperación |
| 9:25–9:50 | ECR opcional, trazabilidad y evidencia de cadena de entrega |
| 9:50–10:00 | eliminar clúster, imágenes remotas y pila |

## Ruta principal con software libre

```bash
./scripts/setup_python.sh --apply
make test-all
podman build -t localhost/librereserva:s14 labs/librereserva
podman image inspect localhost/librereserva:s14 --format '{{.Id}}'
export KIND_EXPERIMENTAL_PROVIDER=podman
kind create cluster --name informatica1
kind load docker-image localhost/librereserva:s14 --name informatica1
kubectl apply -f modules/08_entrega_plataforma/k8s.yml
kubectl rollout status deployment/librereserva --timeout=120s
```

Elimine un pod y observe la reconciliación. Añada una prueba que proteja idempotencia o el contrato del adaptador.

## Extensión ECR, solo si fue habilitada

```bash
./aws-learner-lab/scripts/stack.sh deploy \
  libre-reserva-s14-equipoXX \
  aws-learner-lab/templates/s14-ecr.yaml --apply

repository_uri="$(aws cloudformation describe-stacks \
  --stack-name libre-reserva-s14-equipoXX --region "$AWS_REGION" \
  --query 'Stacks[0].Outputs[?OutputKey==`RepositoryUri`].OutputValue' --output text)"
[[ "$repository_uri" == *.amazonaws.com/* ]] || exit 1
registry="${repository_uri%%/*}"
aws ecr get-login-password --region "$AWS_REGION" | \
  podman login --username AWS --password-stdin "$registry"
podman tag localhost/librereserva:s14 "$repository_uri:s14"
podman push "$repository_uri:s14"
aws ecr describe-images --repository-name "${repository_uri#*/}" \
  --region "$AWS_REGION" --output table
```

## Validación y limpieza

```bash
kind delete cluster --name informatica1
./aws-learner-lab/scripts/stack.sh delete libre-reserva-s14-equipoXX --apply
```

La plantilla usa `EmptyOnDelete`, de modo que CloudFormation elimina las imágenes del repositorio de esta práctica. Revise ECR después del borrado.

**Evidencia:** pruebas, digest local/remoto si aplica, manifiesto, recuperación de pod, commit trazable y limpieza.
