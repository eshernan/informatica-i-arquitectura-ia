"""Núcleo de dominio sin dependencias de infraestructura."""

from dataclasses import dataclass
from datetime import datetime


class IntervaloInvalido(ValueError):
    """El final no es posterior al inicio."""


class IntervaloOcupado(RuntimeError):
    """La reserva se solapa con otra reserva activa."""


class ReservaNoEncontrada(LookupError):
    """No existe una reserva con el identificador solicitado."""


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
