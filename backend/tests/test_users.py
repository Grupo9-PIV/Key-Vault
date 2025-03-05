from http import HTTPStatus

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from sqlalchemy.sql import select

from src.models import User
from src.schemas import UserPublic
from src.security import verify_password
from tests.factory.faker import fake
from tests.utils import get_fake_password, get_user_data


def test_create_user_valid(client: TestClient, session: Session) -> None:
    user_data = get_user_data()

    response = client.post('/users', json=user_data)
    data = response.json()

    db_user = session.scalar(
        select(User).where(User.email == user_data['email'])
    )

    assert response.status_code == HTTPStatus.CREATED
    assert data['email'] == user_data['email']
    assert data['is_active'] is False
    assert 'id' in data

    assert db_user is not None
    assert db_user.email == user_data['email']
    assert verify_password(user_data['password'], db_user.password_hash)


def test_create_user_duplicate_email(client: TestClient, user: User) -> None:
    user_data = get_user_data()
    user_data['email'] = user.email  # email já existente

    response = client.post('/users', json=user_data)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json()['detail'] == 'Email already exists'


def test_create_user_invalid_email(client: TestClient) -> None:
    user_data = get_user_data()
    user_data['email'] = 'invalid-email'  # email já existente

    response = client.post('/users', json=user_data)
    errors = response.json()['detail']

    assert response.status_code == HTTPStatus.UNPROCESSABLE_CONTENT
    assert any(error['loc'] == ['body', 'email'] for error in errors)


def test_create_user_missing_required_fields(client: TestClient) -> None:
    user_data = get_user_data()
    user_data.pop('password')

    response = client.post('/users', json=user_data)
    errors = response.json()['detail']

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert any(error['loc'] == ['body', 'password'] for error in errors)


def test_read_users(client: TestClient, user: User, token: str) -> None:
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get(
        '/users', headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': [user_schema]}


def test_read_user_existing(
    client: TestClient, user: User, token: str
) -> None:
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get(
        f'/users/{user.id}', headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == user_schema


def test_read_user_not_found(client: TestClient, token: str) -> None:
    response = client.get(
        '/users/404', headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json()['detail'] == 'User not found'


def test_update_user(
    client: TestClient, user: User, session: Session, token: str
) -> None:
    user_data = get_user_data()

    response = client.put(
        f'/users/{user.id}',
        json=user_data,
        headers={'Authorization': f'Bearer {token}'},
    )
    updated_user = session.scalar(select(User).where(User.id == user.id))

    assert response.status_code == HTTPStatus.OK
    assert response.json()['email'] == user_data['email']
    assert response.json()['id'] == user.id

    assert updated_user.updated_at is not None
    assert updated_user.email == user_data['email']
    assert updated_user.role == user_data['role']
    assert verify_password(user_data['password'], updated_user.password_hash)


def test_update_user_forbidden(
    client: TestClient, token: str, admin: User
) -> None:
    user_data = get_user_data()

    response = client.put(
        f'/users/{admin.id}',
        json=user_data,
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json()['detail'] == 'Not enough permissions'


def test_update_not_found(client: TestClient, admin_token: str) -> None:
    user_data = get_user_data()

    response = client.put(
        '/users/404',
        json=user_data,
        headers={'Authorization': f'Bearer {admin_token}'},
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json()['detail'] == 'User not found'


def test_delete_user(
    client: TestClient, user: User, session: Session, token: str
) -> None:
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.delete(
        f'/users/{user.id}', headers={'Authorization': f'Bearer {token}'}
    )

    deleted_user = session.scalar(select(User).where(User.id == user.id))

    assert response.status_code == HTTPStatus.OK
    assert response.json() == user_schema
    assert deleted_user is None


def test_delete_user_forbidden(
    client: TestClient, token: str, admin: User
) -> None:
    response = client.delete(
        f'/users/{admin.id}', headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json()['detail'] == 'Not enough permissions'


def test_delete_not_found(client: TestClient, admin_token: str) -> None:
    response = client.delete(
        '/users/404', headers={'Authorization': f'Bearer {admin_token}'}
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json()['detail'] == 'User not found'


def test_partial_update_single_field(
    client: TestClient, user: User, token: str
) -> None:
    update_data = {'name': fake.name()}
    response = client.patch(
        f'/users/{user.id}',
        json=update_data,
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json()['name'] == update_data['name']
    assert response.json()['id'] == user.id


def test_partial_update_multiple_fields(
    client: TestClient, user: User, token: str
) -> None:
    update_data = {'department': fake.word(), 'is_active': True}

    response = client.patch(
        f'/users/{user.id}',
        json=update_data,
        headers={'Authorization': f'Bearer {token}'},
    )
    data = response.json()

    assert response.status_code == HTTPStatus.OK
    assert data['department'] == update_data['department']
    assert data['is_active'] == update_data['is_active']


def test_partial_update_duplicate_email(
    client: TestClient, user: User, token: str, admin: User
) -> None:
    response = client.patch(
        f'/users/{user.id}',
        json={'email': admin.email},
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert 'already exists' in response.json()['detail']


def test_partial_update_password(
    client: TestClient, user: User, token: str, session: Session
) -> None:
    new_password = get_fake_password()
    old_password = user.password_hash

    response = client.patch(
        f'/users/{user.id}',
        json={'password': new_password},
        headers={'Authorization': f'Bearer {token}'},
    )
    session.refresh(user)

    assert response.status_code == HTTPStatus.OK
    assert user.password_hash != new_password
    assert user.password_hash != old_password
    assert verify_password(new_password, user.password_hash)


def test_partial_update_other_user(
    client: TestClient, token: str, admin: User
) -> None:
    response = client.patch(
        f'/users/{admin.id}',
        json={'name': fake.name()},
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.FORBIDDEN


def test_partial_update_invalid_fields(
    client: TestClient, user: User, token: str
) -> None:
    response = client.patch(
        f'/users/{user.id}',
        json={'invalid_field': fake.word()},
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_partial_update_nonexistent_user(
    client: TestClient, admin_token: str
) -> None:
    response = client.patch(
        '/users/404',
        json={'name': fake.name()},
        headers={'Authorization': f'Bearer {admin_token}'},
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json()['detail'] == 'User not found'
