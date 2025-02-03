import pytest
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from src.models import User
from tests.helpers import add_user


def test_create_user(session: Session) -> None:
    add_user(session)

    result = session.scalar(
        select(User).where(User.email == 'teste@teste.com')
    )

    assert result.id == 1
    assert result.email == 'teste@teste.com'


def test_delete_user(session_with_user: Session) -> None:
    user = session_with_user.scalar(
        select(User).where(User.email == 'teste@teste.com')
    )
    assert user is not None

    session_with_user.delete(user)
    session_with_user.commit()

    result = session_with_user.scalar(
        select(User).where(User.email == 'teste@teste.com')
    )
    assert result is None


def test_update_user(session_with_user: Session) -> None:
    user = session_with_user.scalar(select(User).where(User.id == 1))
    assert user is not None

    user.name = 'Teste Update'
    session_with_user.commit()
    session_with_user.refresh(user)

    updated_user = session_with_user.scalar(
        select(User).where(User.email == 'teste@teste.com')
    )
    assert updated_user.name == 'Teste Update'
    assert updated_user.updated_at is not None


def test_email_unique_constraint(session_with_user: Session) -> None:
    user2 = User(
        email='teste@teste.com',  # email já existente
        password_hash='12345',
        name='Teste 2',
        role='user',
        department='Teste',
    )
    session_with_user.add(user2)

    with pytest.raises(IntegrityError):
        session_with_user.commit()


def test_missing_required_fields(session: Session) -> None:
    user = User(
        email=None,
        password_hash='12345',
        name=None,
        role=None,
        department=None,
    )
    session.add(user)

    with pytest.raises(IntegrityError):
        session.commit()
