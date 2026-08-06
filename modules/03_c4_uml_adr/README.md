# Módulo 3. Comunicación de arquitectura: C4, UML y ADR

## Resultado

Comunicar una decisión a la audiencia correcta mediante vistas C4, UML selectivo y un ADR versionado.

## Instalación paso a paso

PlantUML requiere Java y Graphviz. El instalador base intenta preparar ambos componentes mediante el gestor del sistema.

```bash
./scripts/install_base.sh
./scripts/install_base.sh --apply
java -version
dot -V
plantuml -version
```

Renderice el diagrama incluido:

```bash
./modules/03_c4_uml_adr/render.sh
```

Si `plantuml` no está disponible, consulte [la instalación oficial](https://plantuml.com/starting) y use un paquete verificable de su distribución. El servidor público de PlantUML no debe recibir diagramas confidenciales.

## Ejercicio

1. Actualice `contexto.puml` con actores y sistemas reales.
2. Cree una vista de contenedores que muestre tecnología y responsabilidad.
3. Escriba `docs/adr/0001-estilo-inicial.md` con contexto, alternativas, decisión, consecuencias y evidencia.
4. Use UML solo para una interacción o estructura que necesite detalle adicional.

## Validación

```bash
plantuml -checkonly modules/03_c4_uml_adr/contexto.puml
./modules/03_c4_uml_adr/render.sh
```

**Evidencia:** fuentes del diagrama, SVG/PNG generado y ADR coherente con el código.
