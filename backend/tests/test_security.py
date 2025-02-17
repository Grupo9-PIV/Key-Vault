from datetime import datetime, timezone
from http import HTTPStatus

from fastapi.testclient import TestClient
from jwt import decode

from src.security import create_access_token
from src.security.auth import ALGORITHM, SECRET_KEY


def test_create_access_token() -> None:
    data = {'sub': 'test@test.com'}
    token = create_access_token(data)

    decoded_token = decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    assert decoded_token['sub'] == data['sub']
    assert decoded_token['exp']
    assert decoded_token['exp'] > datetime.now(timezone.utc).timestamp()


def test_jwt_invalid_token(client: TestClient) -> None:
    response = client.delete(
        '/users/1', headers={'Authorization': 'Bearer token-invalido'}
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}


def test_jwt_missing_email(client: TestClient) -> None:
    data = {}
    token = create_access_token(data)

    response = client.delete(
        '/users/1', headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}


def test_jwt_user_not_found(client: TestClient) -> None:
    data = {'sub': 'not_real@user.com'}
    token = create_access_token(data)

    response = client.delete(
        '/users/1', headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}
