# Módulo 4. Modularidad, dominio y patrones

## Resultado

Separar reglas de negocio de detalles externos mediante módulos, puertos y adaptadores.

## Instalación paso a paso

```bash
./scripts/check_environment.sh
./scripts/setup_python.sh --apply
make test
```

Examine la frontera existente:

```bash
sed -n '1,240p' labs/librereserva/app/domain.py
sed -n '1,260p' labs/librereserva/app/main.py
```

El dominio utiliza únicamente la biblioteca estándar. FastAPI pertenece al adaptador HTTP. Esta diferencia debe poder comprobarse sin depender del diagrama.

## Temas

- Cohesión, acoplamiento y dirección de dependencias.
- Lenguaje ubicuo y contexto delimitado.
- Arquitectura hexagonal.
- Repository, DAO, MVC e inversión de dependencia.
- Patrones como respuestas con costo, no recetas.

## Ejercicio

Añada cancelación sin importar FastAPI en `domain.py`. Defina un puerto de repositorio con `typing.Protocol` y cree un adaptador en memoria. Escriba una prueba que falle si el dominio depende de `fastapi`, `sqlalchemy` o un cliente de mensajería.

## Validación

```bash
python3 -m unittest discover -s labs/librereserva/tests -v
python3 -m compileall -q labs/librereserva
```

**Evidencia:** diagrama de dependencias, prueba de arquitectura y ADR si cambia un límite.
