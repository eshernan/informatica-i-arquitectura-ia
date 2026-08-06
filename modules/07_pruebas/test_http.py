from fastapi.testclient import TestClient

from labs.librereserva.app.main import agenda, app


client = TestClient(app)


def setup_function() -> None:
    agenda.limpiar()


def test_api_crea_y_rechaza_solapamiento() -> None:
    datos = {
        "recurso": "A-101",
        "inicio": "2026-08-10T08:00:00Z",
        "fin": "2026-08-10T09:00:00Z",
    }
    assert client.post("/reservas", json=datos).status_code == 201
    assert client.post("/reservas", json=datos).status_code == 409
