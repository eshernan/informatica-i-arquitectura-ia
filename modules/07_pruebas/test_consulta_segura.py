"""Ejemplo docente de parametrización con datos ficticios y SQLite en memoria.

Esta búsqueda ilustra una posible ampliación de LibreReserva. No es una
prueba del adaptador PostgreSQL ni un nuevo endpoint de la aplicación.
"""

import sqlite3
import unittest


def buscar_por_recurso(
    conexion: sqlite3.Connection, recurso: str
) -> list[tuple[int, str]]:
    return conexion.execute(
        "SELECT id, recurso FROM reservas WHERE recurso = ? ORDER BY id",
        (recurso,),
    ).fetchall()


class ConsultaSeguraTest(unittest.TestCase):
    def setUp(self) -> None:
        self.conexion = sqlite3.connect(":memory:")
        self.addCleanup(self.conexion.close)
        self.conexion.execute(
            "CREATE TABLE reservas (id INTEGER PRIMARY KEY, recurso TEXT NOT NULL)"
        )
        self.conexion.executemany(
            "INSERT INTO reservas (id, recurso) VALUES (?, ?)",
            [(1, "A-101"), (2, "B-202")],
        )

    def test_busca_solo_el_recurso_solicitado(self) -> None:
        self.assertEqual(
            [(1, "A-101")], buscar_por_recurso(self.conexion, "A-101")
        )

    def test_admite_un_apostrofe_como_parte_del_dato(self) -> None:
        self.conexion.execute(
            "INSERT INTO reservas (id, recurso) VALUES (?, ?)",
            (3, "Sala O'Reilly"),
        )
        self.assertEqual(
            [(3, "Sala O'Reilly")],
            buscar_por_recurso(self.conexion, "Sala O'Reilly"),
        )

    def test_entrada_sql_no_amplia_los_resultados(self) -> None:
        entrada = "' OR '1'='1"
        self.assertEqual([], buscar_por_recurso(self.conexion, entrada))
        self.assertEqual(
            [(1, "A-101"), (2, "B-202")],
            self.conexion.execute(
                "SELECT id, recurso FROM reservas ORDER BY id"
            ).fetchall(),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
