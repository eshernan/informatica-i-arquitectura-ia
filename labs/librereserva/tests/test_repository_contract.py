"""El mismo contrato se ejecuta contra memoria y PostgreSQL."""

from concurrent.futures import ThreadPoolExecutor
from datetime import UTC, datetime, timedelta
import os
from pathlib import Path
import unittest

from labs.librereserva.app.adapters.memory import RepositorioMemoria
from labs.librereserva.app.adapters.postgres import (
    RepositorioPostgreSQL,
    psycopg,
)
from labs.librereserva.app.domain import (
    Intervalo,
    IntervaloOcupado,
    ReservaNoEncontrada,
)


DSN_PRUEBAS = os.getenv("LIBRERESERVA_TEST_DATABASE_URL")
MIGRACION = Path(__file__).parents[1] / "migrations" / "001_crear_reservas.sql"


class ContratoRepositorio:
    repositorio: object

    def test_crea_lista_y_borra(self) -> None:
        inicio = datetime(2026, 10, 28, 18, tzinfo=UTC)
        creada = self.repositorio.crear(
            "A-101",
            Intervalo(inicio, inicio + timedelta(hours=1)),
        )

        self.assertEqual((creada,), self.repositorio.listar())
        self.repositorio.borrar(creada.id)
        self.assertEqual((), self.repositorio.listar())
        with self.assertRaises(ReservaNoEncontrada):
            self.repositorio.borrar(creada.id)

    def test_rechaza_solapamiento(self) -> None:
        inicio = datetime(2026, 10, 28, 18, tzinfo=UTC)
        self.repositorio.crear(
            "A-101",
            Intervalo(inicio, inicio + timedelta(hours=1)),
        )

        with self.assertRaises(IntervaloOcupado):
            self.repositorio.crear(
                "A-101",
                Intervalo(
                    inicio + timedelta(minutes=30),
                    inicio + timedelta(hours=2),
                ),
            )


class RepositorioMemoriaTest(ContratoRepositorio, unittest.TestCase):
    def setUp(self) -> None:
        self.repositorio = RepositorioMemoria()


@unittest.skipUnless(
    DSN_PRUEBAS and psycopg is not None,
    "Defina LIBRERESERVA_TEST_DATABASE_URL para probar PostgreSQL",
)
class RepositorioPostgreSQLTest(ContratoRepositorio, unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        with psycopg.connect(DSN_PRUEBAS, autocommit=True) as conexion:
            conexion.execute(MIGRACION.read_text(encoding="utf-8"))

    def setUp(self) -> None:
        self.repositorio = RepositorioPostgreSQL(DSN_PRUEBAS)
        self.repositorio.limpiar()

    def test_protege_solicitudes_concurrentes(self) -> None:
        inicio = datetime(2026, 10, 28, 18, tzinfo=UTC)
        intervalo = Intervalo(inicio, inicio + timedelta(hours=1))

        def crear() -> str:
            try:
                self.repositorio.crear("A-101", intervalo)
                return "creada"
            except IntervaloOcupado:
                return "conflicto"

        with ThreadPoolExecutor(max_workers=2) as ejecutor:
            resultados = sorted(ejecutor.map(lambda _: crear(), range(2)))

        self.assertEqual(["conflicto", "creada"], resultados)
        self.assertEqual(1, len(self.repositorio.listar()))


if __name__ == "__main__":
    unittest.main()
