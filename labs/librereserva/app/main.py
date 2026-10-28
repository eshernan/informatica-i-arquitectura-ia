"""Adaptador HTTP de LibreReserva."""

from datetime import datetime
import os

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, ConfigDict

from .adapters.memory import RepositorioMemoria
from .adapters.postgres import RepositorioPostgreSQL
from .domain import (
    Intervalo,
    IntervaloInvalido,
    IntervaloOcupado,
    ReservaNoEncontrada,
)
from .ports import RepositorioReservas

app = FastAPI(title="LibreReserva", version="0.1.0")


def crear_repositorio() -> RepositorioReservas:
    adaptador = os.getenv("LIBRERESERVA_REPOSITORY", "memory")
    if adaptador == "memory":
        return RepositorioMemoria()
    if adaptador == "postgres":
        dsn = os.environ.get("DATABASE_URL")
        if not dsn:
            raise RuntimeError(
                "DATABASE_URL es obligatoria con LIBRERESERVA_REPOSITORY=postgres"
            )
        return RepositorioPostgreSQL(dsn)
    raise RuntimeError(
        "LIBRERESERVA_REPOSITORY debe ser 'memory' o 'postgres'"
    )


repositorio = crear_repositorio()


class ReservaEntrada(BaseModel):
    recurso: str
    inicio: datetime
    fin: datetime


class ReservaSalida(ReservaEntrada):
    model_config = ConfigDict(from_attributes=True)
    id: int


@app.get("/salud/viva")
def viva() -> dict[str, str]:
    return {"estado": "viva"}


@app.get("/salud/lista")
def lista() -> dict[str, str]:
    return {"estado": "lista"}


@app.get("/reservas", response_model=list[ReservaSalida])
def listar_reservas() -> list[ReservaSalida]:
    return [
        ReservaSalida(
            id=reserva.id,
            recurso=reserva.recurso,
            inicio=reserva.intervalo.inicio,
            fin=reserva.intervalo.fin,
        )
        for reserva in repositorio.listar()
    ]


@app.post(
    "/reservas",
    response_model=ReservaSalida,
    status_code=status.HTTP_201_CREATED,
)
def crear_reserva(entrada: ReservaEntrada) -> ReservaSalida:
    try:
        reserva = repositorio.crear(
            entrada.recurso,
            Intervalo(entrada.inicio, entrada.fin),
        )
    except IntervaloInvalido as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except IntervaloOcupado as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc
    return ReservaSalida(
        id=reserva.id,
        recurso=reserva.recurso,
        inicio=reserva.intervalo.inicio,
        fin=reserva.intervalo.fin,
    )


@app.delete(
    "/reservas/{reserva_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def borrar_reserva(reserva_id: int) -> Response:
    try:
        repositorio.borrar(reserva_id)
    except ReservaNoEncontrada as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return Response(status_code=status.HTTP_204_NO_CONTENT)
