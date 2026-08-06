from datetime import UTC, datetime, timedelta

from hypothesis import given, strategies as st

from labs.librereserva.app.domain import Intervalo


@given(st.integers(min_value=1, max_value=24 * 60))
def test_intervalo_nunca_se_solapa_con_su_contiguo(duracion_minutos: int) -> None:
    inicio = datetime(2026, 8, 10, tzinfo=UTC)
    fin = inicio + timedelta(minutes=duracion_minutos)
    primero = Intervalo(inicio, fin)
    segundo = Intervalo(fin, fin + timedelta(minutes=1))
    assert not primero.se_solapa(segundo)
