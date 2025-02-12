from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, registry

from src.settings import Settings

# registro de tabelas com metadados
table_registry = registry()

# cria a engine de conexão com o db
engine = create_engine(Settings().DATABASE_URL)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


__all__ = [
    'get_session',
    'table_registry',
]
