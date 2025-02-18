from http import HTTPStatus

from fastapi.testclient import TestClient

from src.models import User


def test_get_token(client: TestClient, user: User) -> None:
    response = client.post(
        '/auth/token', data={'username': user.email, 'password': user.password}
    )

    token = response.json()

    assert response.status_code == HTTPStatus.OK
    assert token['token_type'] == 'Bearer'
    assert token['access_token']


def test_get_token_bad_request(client: TestClient, user: User) -> None:
    response = client.post(
        '/auth/token',
        data={'username': user.email, 'password': 'wrong-password'},
    )

    result = response.json()

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert result['detail'] == 'Incorrect email or password'
