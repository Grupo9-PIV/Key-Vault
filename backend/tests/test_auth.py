from http import HTTPStatus

from fastapi.testclient import TestClient
from freezegun import freeze_time

from src.models import User


def test_get_token(client: TestClient, user: User) -> None:
    response = client.post(
        '/auth/token', data={'username': user.email, 'password': user.password}
    )

    token = response.json()

    assert response.status_code == HTTPStatus.OK
    assert token['token_type'] == 'Bearer'
    assert token['access_token']


def test_get_token_wrong_password(client: TestClient, user: User) -> None:
    response = client.post(
        '/auth/token',
        data={'username': user.email, 'password': 'wrong-password'},
    )

    result = response.json()

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert result['detail'] == 'Incorrect email or password'


def test_get_token_user_not_found(client: TestClient, user: User) -> None:
    response = client.post(
        '/auth/token',
        data={'username': 'not_real@user.com', 'password': user.password},
    )

    result = response.json()

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert result['detail'] == 'Incorrect email or password'


def test_token_expired_after_time(client: TestClient, user: User) -> None:
    with freeze_time('2025-02-24 12:00:00'):
        response = client.post(
            '/auth/token',
            data={
                'username': user.email,
                'password': user.password,
            },
        )

        assert response.status_code == HTTPStatus.OK
        token = response.json()['access_token']

    with freeze_time('2025-02-24 12:31:00'):
        response = client.delete(
            f'/users/{user.id}', headers={'Authorization': f'Bearer {token}'}
        )

        assert response.status_code == HTTPStatus.UNAUTHORIZED
        assert response.json() == {'detail': 'Token has expired'}
