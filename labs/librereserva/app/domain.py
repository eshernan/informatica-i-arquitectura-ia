"""Núcleo de dominio sin dependencias de infraestructura."""

from dataclasses import dataclass
from datetime import datetime


class IntervaloInvalido(ValueError):
    """El final no es posterior al inicio."""


class IntervaloOcupado(RuntimeError):
    """La reserva se solapa con otra reserva activa."""


@dataclass(frozen=True, slots=True)
class Intervalo:
    inicio: datetime
    fin: datetime

    def __post_init__(self) -> None:
        if self.fin <= self.inicio:
            raise IntervaloInvalido("fin debe ser posterior a inicio")

    def se_solapa(self, otro: "Intervalo") -> bool:
        return self.inicio < otro.fin and otro.inicio < self.fin


@dataclass(frozen=True, slots=True)
class Reserva:
    id: int
    recurso: str
    intervalo: Intervalo


class Agenda:
    """Repositorio en memoria útil para el primer incremento vertical."""

    def __init__(self) -> None:
        self._reservas: list[Reserva] = []

    def crear(self, recurso: str, intervalo: Intervalo) -> Reserva:
        if any(
            reserva.recurso == recurso
            and reserva.intervalo.se_solapa(intervalo)
            for reserva in self._reservas
        ):
            raise IntervaloOcupado(f"{recurso} ya está reservado")
        reserva = Reserva(len(self._reservas) + 1, recurso, intervalo)
        self._reservas.append(reserva)
        return reserva

    def listar(self) -> tuple[Reserva, ...]:
        return tuple(self._reservas)

    def limpiar(self) -> None:
        self._reservas.clear()
