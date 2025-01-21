from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.models.user import User, table_registry


def test_create_user():
    engine = create_engine('sqlite:///:memory:')

    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        user = User(
            email='teste@teste.com',
            password_hash='12345678',
            name='Teste',
            role='admin',
            department='Teste',
        )

        session.add(user)
        session.commit()
        session.refresh(user)

    assert user.email == 'teste@teste.com'
