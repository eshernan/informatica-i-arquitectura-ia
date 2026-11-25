# Módulo 8. Entrega continua, contenedores e infraestructura

## Resultado

Relacionar una confirmación Git con pruebas, imagen OCI, SBOM y despliegue reproducible en Kubernetes local.

En sesión 14, el mínimo es pruebas, imagen, Deployment/Service, acceso y recuperación. SBOM, Forgejo, registro remoto, escalado y TLS son ampliaciones anunciadas por el docente, no instalaciones simultáneas obligatorias. Consulte la [ruta de carga](../../docs/RUTA_CONTENEDORES.md).

## Del repositorio a una versión desplegada

![Sketch de repositorio, pruebas, construcción, registro y despliegue](../../docs/imagenes/desarrollo-moderno.jpg)

El flujo de entrega relaciona un commit con pruebas y una imagen identificable. Un registro de imágenes conserva artefactos de ejecución; el repositorio Git conserva código y decisiones. El archivo descargable de CI es una evidencia y no equivale a un registro remoto. La configuración y los secretos se proporcionan por ambiente.

![Sketch de despliegue sin estado con almacenamiento separado y servicios cloud](../../docs/imagenes/despliegue-sin-estado-cloud.jpg)

Los servicios gestionados de un proveedor pueden aportar cómputo, balanceo, autoescalado y almacenamiento durable. Kubernetes es una alternativa, no un requisito de esta visión. Nuestro manifiesto local demuestra réplicas y recuperación, pero la API base todavía mantiene agendas independientes en RAM. No interprete tres Pods como una solución de datos compartidos.

## Instalación paso a paso

### 1. Podman e imagen

Prepare Podman siguiendo la [guía de entorno](../01_entorno/README.md). La sesión 9 admite también [Docker en Ubuntu y EC2](../01_entorno/README.md#instalación-con-script-en-ubuntu-y-ec2); los pasos Kubernetes siguientes describen la ruta Podman. Todos los comandos de este módulo se ejecutan desde la raíz del repositorio.

```bash
podman info
podman build -f labs/librereserva/Containerfile -t localhost/librereserva:0.1.0 labs/librereserva
podman run --rm -p 127.0.0.1:8000:8000 localhost/librereserva:0.1.0
```

Detenga la ejecución con Ctrl+C antes de continuar con el clúster.

### 2. kubectl y kind

Siga la [guía oficial de kind](https://kind.sigs.k8s.io/docs/user/quick-start/) y la [instalación oficial de kubectl](https://kubernetes.io/docs/tasks/tools/). No se fija un binario antiguo dentro del repositorio. Verifique:

```bash
kubectl version --client
kind version
```

Con Podman puede ser necesario:

```bash
export KIND_EXPERIMENTAL_PROVIDER=podman
```

### 3. Clúster y despliegue

```bash
kind create cluster --name informatica1
kind load docker-image localhost/librereserva:0.1.0 --name informatica1
kubectl apply -f modules/08_entrega_plataforma/k8s.yml
kubectl rollout status deployment/librereserva --timeout=120s
kubectl get pods,service
kubectl port-forward service/librereserva 8000:80
```

Mantenga `port-forward` activo y abra `http://127.0.0.1:8000/docs`. En otra terminal, compruebe `/salud/viva`. No expone la API a Internet. Deténgalo con Ctrl+C antes de reiniciar el acceso tras un cambio de Pod. Esta ruta crea un clúster de un nodo; el dibujo multinodo de la presentación explica el modelo general.

### Recuperación de una instancia

En otra terminal, compruebe que el contexto sea `kind-informatica1` y seleccione exactamente un Pod del laboratorio:

```bash
kubectl config current-context
kubectl get pods -l app=librereserva
pod_name=$(kubectl get pods -l app=librereserva -o jsonpath='{.items[0].metadata.name}')
kubectl delete pod "$pod_name"
kubectl rollout status deployment/librereserva --timeout=120s
kubectl get pods -l app=librereserva
```

Debe aparecer un Pod de reemplazo. Cada réplica conserva su propia agenda en RAM y sus datos se pierden al reemplazarla. Las probes actuales comprueban estados fijos de la API, no dependencias PostgreSQL/RabbitMQ. Detenga y vuelva a iniciar `port-forward` si su Pod seleccionado dejó de existir.

### 4. Forgejo, ampliación opcional

Use una instancia institucional o instale Forgejo mediante su [documentación oficial](https://forgejo.org/docs/latest/admin/installation/docker/). Configure un runner aislado y adapte `.github/workflows/validate.yml` a `.forgejo/workflows/validate.yml`. Las acciones externas son código: fíjelas a una versión revisada.

El [flujo ya incluido](../../.github/workflows/validate.yml) ejecuta validaciones/pruebas, construye una imagen con etiqueta del commit y guarda un archivo descargable. No publica en un registro ni despliega en un ambiente real. En sesión 14 se usa la forja ya disponible; no se instala otra para cumplir el mismo resultado. El ejemplo Forgejo del libro requiere adaptación al runner y no es un segundo flujo listo para usar.

### 5. Lecturas opcionales de operación y despliegue

Elija una continuación: [escalar, actualizar, rollback y configuración](OPERACION.md) o [ambientes y ensayo de proxy TLS](DESPLIEGUE.md). Los objetos ConfigMap/Secret/PVC se muestran en una demo separada, sin atribuir persistencia a la agenda de la API.

## Ejercicio

Construya la imagen, registre su digest, despliegue dos réplicas, elimine un pod y observe reconciliación. Configure CI para rechazar una prueba fallida. No almacene secretos en el flujo.

## Validación

```bash
podman image inspect localhost/librereserva:0.1.0 --format '{{.Id}}'
kubectl rollout status deployment/librereserva --timeout=120s
kubectl get pods -l app=librereserva
```

**Evidencia:** ejecución CI, digest, manifiestos, recuperación y ADR de plataforma.

Una imagen local recién construida puede no tener digest de manifiesto de registro. Registre el ID local (`.Id`) y el commit; cuando la publique en ECR, registre además el digest remoto. No trate una salida vacía de `.Digest` como evidencia suficiente.

Al terminar, detenga `port-forward`. `kind delete cluster --name informatica1` elimina únicamente este clúster local y sus datos: conserve la evidencia antes. No elimine otros clústeres o contextos.
