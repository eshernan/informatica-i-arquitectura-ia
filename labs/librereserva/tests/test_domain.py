from datetime import UTC, datetime, timedelta
import unittest

from labs.librereserva.app.domain import (
    Intervalo,
    IntervaloInvalido,
    IntervaloOcupado,
    ReservaNoEncontrada,
)
from labs.librereserva.app.adapters.memory import RepositorioMemoria


class IntervaloTest(unittest.TestCase):
    def setUp(self) -> None:
        self.inicio = datetime(2026, 8, 10, 8, tzinfo=UTC)

    def test_rechaza_duracion_no_positiva(self) -> None:
        with self.assertRaises(IntervaloInvalido):
            Intervalo(self.inicio, self.inicio)

    def test_intervalos_contiguos_no_se_solapan(self) -> None:
        primero = Intervalo(self.inicio, self.inicio + timedelta(hours=1))
        segundo = Intervalo(
            self.inicio + timedelta(hours=1),
            self.inicio + timedelta(hours=2),
        )
        self.assertFalse(primero.se_solapa(segundo))


class RepositorioMemoriaTest(unittest.TestCase):
    def test_rechaza_solapamiento_del_mismo_recurso(self) -> None:
        inicio = datetime(2026, 8, 10, 8, tzinfo=UTC)
        agenda = RepositorioMemoria()
        agenda.crear("A-101", Intervalo(inicio, inicio + timedelta(hours=1)))

        with self.assertRaises(IntervaloOcupado):
            agenda.crear(
                "A-101",
                Intervalo(inicio + timedelta(minutes=30), inicio + timedelta(hours=2)),
            )

    def test_permite_mismo_intervalo_en_otro_recurso(self) -> None:
        inicio = datetime(2026, 8, 10, 8, tzinfo=UTC)
        intervalo = Intervalo(inicio, inicio + timedelta(hours=1))
        agenda = RepositorioMemoria()
        agenda.crear("A-101", intervalo)
        agenda.crear("B-202", intervalo)
        self.assertEqual(2, len(agenda.listar()))

    def test_borra_una_reserva_por_id(self) -> None:
        inicio = datetime(2026, 8, 10, 8, tzinfo=UTC)
        agenda = RepositorioMemoria()
        primera = agenda.crear(
            "A-101", Intervalo(inicio, inicio + timedelta(hours=1))
        )
        segunda = agenda.crear(
            "B-202", Intervalo(inicio, inicio + timedelta(hours=1))
        )

        agenda.borrar(primera.id)

        self.assertEqual((segunda,), agenda.listar())

    def test_informa_si_la_reserva_que_se_borra_no_existe(self) -> None:
        agenda = RepositorioMemoria()

        with self.assertRaisesRegex(
            ReservaNoEncontrada, "No existe una reserva con id 99"
        ):
            agenda.borrar(99)

    def test_no_reutiliza_ids_despues_de_borrar(self) -> None:
        inicio = datetime(2026, 8, 10, 8, tzinfo=UTC)
        intervalo = Intervalo(inicio, inicio + timedelta(hours=1))
        agenda = RepositorioMemoria()
        primera = agenda.crear("A-101", intervalo)
        agenda.crear("B-202", intervalo)

        agenda.borrar(primera.id)
        tercera = agenda.crear("C-303", intervalo)

        self.assertEqual(3, tercera.id)


if __name__ == "__main__":
    unittest.main()
