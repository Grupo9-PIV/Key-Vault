from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models import User


def test_create_user(session: Session) -> None:
    user = User(
        email='teste@teste.com',
        password_hash='12345678',
        name='Teste',
        role='admin',
        department='Teste',
    )

    session.add(user)
    session.commit()

    result = session.scalar(
        select(User).where(User.email == 'teste@teste.com')
    )

    assert result.email == 'teste@teste.com'
