from sqlalchemy import select
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

    user.name = "Teste Update"
    session_with_user.commit()
    session_with_user.refresh(user)

    updated_user = session_with_user.scalar(
        select(User).where(User.email == 'teste@teste.com'))
    assert updated_user.name == "Teste Update"
