# Libro de Informática I — 2026

Fuente LaTeX del libro **Arquitectura de Software Moderna y desarrollo asistido por inteligencia artificial**.

## Compilación

Requiere una distribución TeX con `pdflatex`, TikZ, `tcolorbox`, `listings`, `hyperref` y `cleveref`.

```bash
make
```

La salida se genera en `build/Libro_Informatica_I_2026.pdf`. Para limpiar auxiliares:

```bash
make clean
```

Los capítulos están en `chapters/`. La compilación no descarga recursos ni necesita conexión de red.
