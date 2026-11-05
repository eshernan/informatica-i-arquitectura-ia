# Esquemas ligeros para los laboratorios

Los cinco sketches originales reutilizan las imágenes aprobadas de la presentación CyberColombia V9. Mantienen el recorte de la presentación y no requieren versiones de alta resolución. Esos cinco JPEG suman aproximadamente 175 KiB.

Se usan en las guías de `.venv`/contenedores, YAML, RabbitMQ, ambientes y Kubernetes. Los diagramas Mermaid complementarios describen pasos y relaciones del repositorio; las imágenes conservan el estilo visual de la presentación.

## Visión moderna para los README

Se añadieron únicamente dos imágenes nuevas, generadas con la herramienta integrada de imágenes. Los originales se conservaron; las copias del repositorio se exportaron a JPEG, ancho máximo 1100 píxeles y calidad 84, sin cambiar el contenido. Se reutilizan por referencia, sin crear duplicados para cada README.

- [Del código al despliegue](desarrollo-moderno.jpg): Git, pruebas/construcción, imagen OCI, registro, despliegue y observación.
- [Aplicación sin estado y datos separados](despliegue-sin-estado-cloud.jpg): balanceo, réplicas reemplazables, base de datos, objetos y escalado con servicios cloud.

Los dibujos describen principios y una arquitectura objetivo. No afirman que la API base ya tenga persistencia compartida o autoescalado. Los proveedores pueden gestionar cómputo y almacenamiento mediante servicios distintos; el contorno cloud del segundo dibujo enfatiza el cómputo, no una obligación de alojar los datos fuera del proveedor.

## Esquemas de la sesión del 4 de noviembre

La clase de pruebas y entrega utiliza cinco esquemas sketch: [pruebas y construcción de la imagen](pruebas-entrega-trazable.jpg), [consulta concatenada frente a parametrizada](consulta-parametrizada.jpg), [tipos según alcance](tipos-pruebas-alcance.jpg), [propósitos](tipos-pruebas-proposito.jpg) y [elementos de las pruebas de hoy](pruebas-sesion12.jpg). Mantienen líneas azules, acentos cian y púrpura, fondo blanco y recorte compacto para continuar el estilo de los materiales CyberColombia. Las copias se exportan a JPEG de 1100 píxeles de ancho y calidad 84. Los [prompts iniciales](PROMPTS_SESION12.md) y las [especificaciones de los gráficos actuales](PROMPTS_SESION12_V3.json) documentan su elaboración con la herramienta integrada. El título del flujo actual es «Pruebas y construcción de la imagen».

## Criterio de redacción docente

En las explicaciones docentes se debe relacionar la condición con lo que el diseño necesita garantizar. La formulación acordada es: «Aunque las réplicas puedan reemplazarse, los datos deben permanecer». Evite presentar la permanencia de datos como una consecuencia automática de reemplazar réplicas. Este criterio también se aplica a los textos de las imágenes.

Los títulos deben nombrar el concepto de forma directa. No utilizar las fórmulas «De X a Y», «Del X al Y» ni variantes equivalentes. La preferencia se aplica también a los títulos incorporados en sketches y a los materiales que se elaboren en adelante.

## Prompts de generación

### Del código al despliegue

```text
Use case: scientific-educational.
Asset type: Spanish educational sketch diagram for Markdown README, wide landscape about 2.6:1.
Primary request: Explain the modern software delivery workflow to graduating students with limited infrastructure knowledge. One clear horizontal left-to-right flow with six connected hand-drawn scenes, not UI cards: developer laptop, Git repository branch symbol, test/check and build gears, a container image package, a shelf registry of images, deployment into a small cloud. Put the six exact large Spanish labels under their scenes in this order: "Código", "Repositorio Git", "Pruebas y build", "Imagen OCI", "Registro", "Despliegue". Beneath the whole flow one simple thin feedback arrow from deployment back toward code labeled exactly "Observar y mejorar". Above it, short title exactly "Del código al despliegue". A short bottom note exactly "Misma imagen. Configuración por ambiente." No more text.
Style: lightweight friendly hand-drawn technical sketch, crisp dark-blue ink contours, sparse blue/cyan/purple accents compatible with CyberColombia teaching slides, pure white background, no textured paper or gradients, no photorealism, no logos, no vendor branding. Large clear hand-lettered labels with correct Spanish accents, readable when reduced to 1100px wide. The container image is a software package, not a literal cargo port. Arrows show correct order Git then tests and build then image then registry then deploy.
Composition: diagram fills the canvas tightly with balanced minimal padding, no large blank top/bottom areas, no overlapping arrows or labels, no decorative border, no paragraphs, no watermark.
```

### Aplicación sin estado y datos separados

Especificación con el texto final acordado y prompt de la edición aplicada a la leyenda.

```text
Use case: scientific-educational.
Asset type: Spanish teaching sketch diagram for Markdown README, wide landscape about 2:1.
Primary request: Explain stateless application replicas, separate durable storage and using cloud services to scale. Title exactly "Aplicación sin estado y datos separados". On far left one group of people labelled "Usuarios" sends a request arrow to a simple splitter labelled "Balanceador". It routes to three equally sized hand-sketched application/container icons arranged vertically, each labelled "API" inside a large cloud outline labelled "Servicios cloud". A small label alongside the group exactly "Réplicas sin estado". Add a small scaling motif next to the replicas: 1 icon to 3 icons with label "Escalar según demanda". From the replica group draw two clear outgoing connections to durable services on the right: one database cylinder labelled exactly "Base de datos" and below it a folder/object-store labelled exactly "Archivos y objetos". Under both, one shared label exactly "Almacenamiento separado". A short footer exactly "Aunque las réplicas puedan reemplazarse, los datos deben permanecer." No other text.
Technical meaning: replicas handle requests but do not keep durable user data in process memory or local container disks; database and object store are distinct services shared by replicas. The cloud may provide load balancing, managed compute/autoscaling, managed database and object storage, no Kubernetes is mandatory. Do not draw a database inside each replica and do not suggest scaling compute automatically scales or backs up the database.
Style: clean friendly hand-drawn sketch, crisp dark-blue ink, small blue/cyan/purple color accents consistent with CyberColombia, pure white background, no photorealism, no gradients, no vendor-specific logos or icons, large clear Spanish labels.
Composition: tight balanced crop, use almost all width and height, minimal margin above title/below footer, arrows do not overlap text, no empty large whitespace strips, no UI card grid, no watermark.
```

```text
Use case: text-localization.
Edit target: the provided Spanish sketch of stateless application replicas and separate durable storage.
Change ONLY the bottom caption. Replace its current text exactly with: "Aunque las réplicas puedan reemplazarse, los datos deben permanecer."
Preserve everything else: title, users, load balancer, cloud outline, the three API replicas, scaling motif, database, files/objects, all other labels, colors, white background, drawing style, proportions, connections, and tight framing. Keep this new caption clearly readable and correctly accented on one or two compact lines at the bottom; do not add a large blank margin. No new objects or words. Do not alter the architecture.
```
