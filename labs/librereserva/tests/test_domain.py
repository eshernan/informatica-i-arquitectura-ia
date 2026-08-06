from datetime import UTC, datetime, timedelta
import unittest

from labs.librereserva.app.domain import (
    Agenda,
    Intervalo,
    IntervaloInvalido,
    IntervaloOcupado,
)


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


class AgendaTest(unittest.TestCase):
    def test_rechaza_solapamiento_del_mismo_recurso(self) -> None:
        inicio = datetime(2026, 8, 10, 8, tzinfo=UTC)
        agenda = Agenda()
        agenda.crear("A-101", Intervalo(inicio, inicio + timedelta(hours=1)))

        with self.assertRaises(IntervaloOcupado):
            agenda.crear(
                "A-101",
                Intervalo(inicio + timedelta(minutes=30), inicio + timedelta(hours=2)),
            )

    def test_permite_mismo_intervalo_en_otro_recurso(self) -> None:
        inicio = datetime(2026, 8, 10, 8, tzinfo=UTC)
        intervalo = Intervalo(inicio, inicio + timedelta(hours=1))
        agenda = Agenda()
        agenda.crear("A-101", intervalo)
        agenda.crear("B-202", intervalo)
        self.assertEqual(2, len(agenda.listar()))


if __name__ == "__main__":
    unittest.main()
