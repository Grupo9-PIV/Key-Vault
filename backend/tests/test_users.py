from http import HTTPStatus

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from sqlalchemy.sql import select

from src.models import User
from src.schemas import UserPublic


def test_create_user_valid(client: TestClient, session: Session) -> None:
    user_data = {
        'email': 'test@test.com',
        'password': '12345678',
        'name': 'Test',
        'role': 'user',
        'department': 'Test',
    }

    response = client.post('/users', json=user_data)
    data = response.json()

    db_user = session.scalar(
        select(User).where(User.email == user_data['email'])
    )

    assert response.status_code == HTTPStatus.CREATED
    assert data['email'] == user_data['email']
    assert 'id' in data

    assert db_user is not None
    assert db_user.email == user_data['email']


def test_create_user_duplicate_email(client: TestClient, user: User) -> None:
    user_data = {
        'email': 'teste@teste.com',  # email já existente
        'password': 'senha',
        'name': 'teste',
        'role': 'user',
        'department': 'Teste',
    }
    response = client.post('/users', json=user_data)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json()['detail'] == 'Email already exists'


def test_create_user_missing_required_fields(client: TestClient) -> None:
    user_data = {
        'email': 'test@test.com',
        # senha faltando
        'name': 'Test',
        'role': 'admin',
        'department': 'Teste',
    }
    response = client.post('/users', json=user_data)
    errors = response.json()['detail']

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert any(error['loc'] == ['body', 'password'] for error in errors)


def test_read_users_existing(client: TestClient, user: User) -> None:
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': [user_schema]}


def test_read_users_without_users(client: TestClient) -> None:
    response = client.get('/users')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_read_user_existing(client: TestClient, user: User) -> None:
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get(f'/users/{user.id}')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == user_schema


def test_read_user_not_found(client: TestClient) -> None:
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json()['detail'] == 'User not found'


def test_update_user_existing(
    client: TestClient, user: User, session: Session
) -> None:
    user_data = {
        'email': 'update@teste.com',
        'password': 'senha',
        'name': 'update',
        'role': 'user',
        'department': 'Teste',
    }
    response = client.put(f'/users/{user.id}', json=user_data)
    updated_user = session.scalar(select(User).where(User.id == user.id))

    assert response.status_code == HTTPStatus.OK
    assert response.json()['email'] == user_data['email']
    assert response.json()['id'] == user.id

    assert updated_user.updated_at is not None
    assert updated_user.email == user_data['email']
    assert updated_user.role == user_data['role']


def test_update_user_not_found(client: TestClient) -> None:
    user_data = {
        'email': 'teste@teste.com',
        'password': 'senha',
        'name': 'teste',
        'role': 'user',
        'department': 'Teste',
    }

    response = client.put('/users/1', json=user_data)

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json()['detail'] == 'User not found'


def test_delete_user_existing(
    client: TestClient, user: User, session: Session
) -> None:
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.delete(f'/users/{user.id}')

    deleted_user = session.scalar(select(User).where(User.id == user.id))

    assert response.status_code == HTTPStatus.OK
    assert response.json() == user_schema
    assert deleted_user is None


def test_delete_user_not_found(client: TestClient) -> None:
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json()['detail'] == 'User not found'
