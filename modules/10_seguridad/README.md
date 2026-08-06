# Módulo 10. Seguridad, privacidad y cadena de suministro

## Resultado

Modelar amenazas, diseñar controles, generar una SBOM y priorizar hallazgos por exposición e impacto.

## Instalación paso a paso

Las herramientas cambian con frecuencia. Instálelas desde sus publicaciones oficiales, compruebe origen y registre versión:

1. [Gitleaks](https://github.com/gitleaks/gitleaks): secretos en repositorios.
2. [Syft](https://github.com/anchore/syft): SBOM SPDX/CycloneDX.
3. [Trivy](https://trivy.dev/latest/getting-started/installation/): vulnerabilidades y configuración.
4. [OWASP ZAP](https://www.zaproxy.org/docs/docker/about/): análisis dinámico autorizado.

Compruebe antes de escanear:

```bash
gitleaks version
syft version
trivy --version
podman --version
./modules/10_seguridad/scan.sh
```

El script muestra el plan por defecto. Para generar resultados sobre la imagen local:

```bash
cd labs/librereserva
podman build -t localhost/librereserva:0.1.0 .
cd ../..
./modules/10_seguridad/scan.sh --apply
```

Nunca dirija ZAP u otro escáner a un sistema externo sin autorización expresa.

## Ejercicio

Dibuje flujo de datos y límites de confianza. Registre ocho amenazas STRIDE; priorice cuatro y asocie una prueba a cada control. Genere SBOM, escanee repositorio e imagen y haga triage de cinco hallazgos.

## Validación

Un hallazgo incluye componente, versión, ruta, exposición, impacto, corrección, responsable y fecha. Una aceptación temporal vence. Si aparece un secreto real, se revoca: borrarlo del último cambio no basta.

**Evidencia:** modelo de amenazas, pruebas, SBOM, reportes sin secretos y triage humano.
