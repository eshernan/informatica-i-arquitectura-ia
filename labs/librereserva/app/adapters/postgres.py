"""Adaptador PostgreSQL con las reglas compartidas protegidas por la base."""

from collections.abc import Sequence
from datetime import datetime
from typing import cast

try:
    import psycopg
except ModuleNotFoundError:  # Permite ejecutar las pruebas puras sin instalar extras.
    psycopg = None

from ..domain import (
    Intervalo,
    IntervaloInvalido,
    IntervaloOcupado,
    Reserva,
    ReservaNoEncontrada,
)


class RepositorioPostgreSQL:
    def __init__(self, dsn: str) -> None:
        self._dsn = dsn

    def _conectar(self):
        if psycopg is None:
            raise RuntimeError(
                "Instale psycopg para usar el adaptador PostgreSQL"
            )
        return psycopg.connect(self._dsn)

    @staticmethod
    def _reserva(fila: Sequence[object]) -> Reserva:
        reserva_id, recurso, inicio, fin = fila
        return Reserva(
            id=int(reserva_id),
            recurso=str(recurso),
            intervalo=Intervalo(
                inicio=cast(datetime, inicio),
                fin=cast(datetime, fin),
            ),
        )

    def crear(self, recurso: str, intervalo: Intervalo) -> Reserva:
        try:
            with self._conectar() as conexion:
                fila = conexion.execute(
                    """
                    INSERT INTO reservas (recurso, inicio, fin)
                    VALUES (%s, %s, %s)
                    RETURNING id, recurso, inicio, fin
                    """,
                    (recurso, intervalo.inicio, intervalo.fin),
                ).fetchone()
        except Exception as exc:
            if getattr(exc, "sqlstate", None) == "23P01":
                raise IntervaloOcupado(f"{recurso} ya está reservado") from exc
            if getattr(exc, "sqlstate", None) == "23514":
                raise IntervaloInvalido("fin debe ser posterior a inicio") from exc
            raise
        if fila is None:
            raise RuntimeError("PostgreSQL no devolvió la reserva creada")
        return self._reserva(fila)

    def listar(self) -> tuple[Reserva, ...]:
        with self._conectar() as conexion:
            filas = conexion.execute(
                "SELECT id, recurso, inicio, fin FROM reservas ORDER BY id"
            ).fetchall()
        return tuple(self._reserva(fila) for fila in filas)

    def borrar(self, reserva_id: int) -> None:
        with self._conectar() as conexion:
            cursor = conexion.execute(
                "DELETE FROM reservas WHERE id = %s",
                (reserva_id,),
            )
            if cursor.rowcount == 0:
                raise ReservaNoEncontrada(
                    f"No existe una reserva con id {reserva_id}"
                )

    def limpiar(self) -> None:
        """Vacía el adaptador para las pruebas de contrato."""
        with self._conectar() as conexion:
            conexion.execute("TRUNCATE TABLE reservas RESTART IDENTITY")
