"""Adaptador HTTP de LibreReserva."""

from datetime import datetime

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, ConfigDict

from .domain import Agenda, Intervalo, IntervaloInvalido, IntervaloOcupado

app = FastAPI(title="LibreReserva", version="0.1.0")
agenda = Agenda()


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
        for reserva in agenda.listar()
    ]


@app.post(
    "/reservas",
    response_model=ReservaSalida,
    status_code=status.HTTP_201_CREATED,
)
def crear_reserva(entrada: ReservaEntrada) -> ReservaSalida:
    try:
        reserva = agenda.crear(
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
