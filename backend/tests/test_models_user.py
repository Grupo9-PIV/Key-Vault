import pytest
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from src.models import License, User
from src.security import get_password_hash, verify_password


def test_create_user(session: Session) -> None:
    user = User(
        email='teste@teste.com',
        password_hash=get_password_hash('12345678'),
        name='Teste',
        role='admin',
        department='Teste',
    )
    session.add(user)
    session.commit()

    result = session.scalar(
        select(User).where(User.email == 'teste@teste.com')
    )

    assert result.id == 1
    assert result.email == 'teste@teste.com'
    assert verify_password('12345678', result.password_hash)


def test_delete_user(session: Session, user: User) -> None:
    session.delete(user)
    session.commit()

    deleted_user = session.scalar(select(User).where(User.id == user.id))
    assert deleted_user is None


def test_update_user(session: Session, user: User) -> None:
    user.name = 'Teste Update'
    user.role = 'manager'
    session.commit()
    session.refresh(user)

    updated_user = session.scalar(select(User).where(User.id == user.id))

    assert updated_user.name == 'Teste Update'
    assert updated_user.role == 'manager'
    assert updated_user.updated_at is not None


def test_email_unique_constraint(session: Session, user: User) -> None:
    user2 = User(
        email=user.email,  # email já existente
        password_hash='12345',
        name='Teste 2',
        role='user',
        department='Teste',
    )
    session.add(user2)

    with pytest.raises(IntegrityError):
        session.commit()


def test_missing_required_fields(session: Session) -> None:
    user = User(
        email=None,
        password_hash='12345',
        name=None,
        role=None,
        department=None,
    )
    session.add(user)

    with pytest.raises(IntegrityError) as exc_info:
        session.commit()
    assert 'NOT NULL constraint failed' in str(exc_info.value)


def test_delete_user_with_license(
    session: Session, user: User, mock_license: License
) -> None:
    assert mock_license.assigned_to == user

    session.delete(user)
    session.commit()
    session.refresh(mock_license)

    assert mock_license.assigned_to is None
    assert mock_license.assigned_to_id is None


def test_user_license_relationship(user: User, mock_license: License) -> None:
    assert mock_license in user.licenses
    assert mock_license.assigned_to == user


def test_updated_at_auto_update(session: Session, user: User) -> None:
    original_updated_at = user.updated_at
    user.name = 'Updated Name'
    session.commit()
    session.refresh(user)

    assert user.updated_at != original_updated_at
