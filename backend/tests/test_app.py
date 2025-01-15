from http import HTTPStatus

from fastapi.testclient import TestClient

from src.app import app


def test_read_root_retorna_ok_e_ola_mundo() -> None:
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}