from fastapi.testclient import TestClient

from labs.librereserva.app.main import app, repositorio


client = TestClient(app)


def setup_function() -> None:
    repositorio.limpiar()


def test_api_crea_y_rechaza_solapamiento() -> None:
    datos = {
        "recurso": "A-101",
        "inicio": "2026-08-10T08:00:00Z",
        "fin": "2026-08-10T09:00:00Z",
    }
    assert client.post("/reservas", json=datos).status_code == 201
    assert client.post("/reservas", json=datos).status_code == 409


def test_api_borra_una_reserva() -> None:
    datos = {
        "recurso": "A-101",
        "inicio": "2026-08-10T08:00:00Z",
        "fin": "2026-08-10T09:00:00Z",
    }
    creada = client.post("/reservas", json=datos).json()

    respuesta = client.delete(f"/reservas/{creada['id']}")

    assert respuesta.status_code == 204
    assert respuesta.content == b""
    assert client.get("/reservas").json() == []


def test_api_informa_si_la_reserva_que_se_borra_no_existe() -> None:
    respuesta = client.delete("/reservas/99")

    assert respuesta.status_code == 404
    assert respuesta.json() == {"detail": "No existe una reserva con id 99"}
