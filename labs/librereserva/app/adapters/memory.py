"""Adaptador en memoria para pruebas rápidas y la línea base de la sesión 9."""

from ..domain import (
    Intervalo,
    IntervaloOcupado,
    Reserva,
    ReservaNoEncontrada,
)


class RepositorioMemoria:
    def __init__(self) -> None:
        self._reservas: list[Reserva] = []
        self._siguiente_id = 1

    def crear(self, recurso: str, intervalo: Intervalo) -> Reserva:
        if any(
            reserva.recurso == recurso
            and reserva.intervalo.se_solapa(intervalo)
            for reserva in self._reservas
        ):
            raise IntervaloOcupado(f"{recurso} ya está reservado")
        reserva = Reserva(self._siguiente_id, recurso, intervalo)
        self._reservas.append(reserva)
        self._siguiente_id += 1
        return reserva

    def listar(self) -> tuple[Reserva, ...]:
        return tuple(self._reservas)

    def borrar(self, reserva_id: int) -> None:
        for indice, reserva in enumerate(self._reservas):
            if reserva.id == reserva_id:
                del self._reservas[indice]
                return
        raise ReservaNoEncontrada(f"No existe una reserva con id {reserva_id}")

    def limpiar(self) -> None:
        self._reservas.clear()
        self._siguiente_id = 1
