"""Puertos que el dominio necesita de la infraestructura."""

from typing import Protocol

from .domain import Intervalo, Reserva


class RepositorioReservas(Protocol):
    """Contrato de persistencia usado por la API."""

    def crear(self, recurso: str, intervalo: Intervalo) -> Reserva: ...

    def listar(self) -> tuple[Reserva, ...]: ...

    def borrar(self, reserva_id: int) -> None: ...

    def limpiar(self) -> None: ...
