from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session

from src.app import app
from src.database import table_registry
from tests.helpers import add_license, add_user


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture
def engine():
    engine = create_engine('sqlite:///:memory:')
    table_registry.metadata.create_all(engine)

    yield engine

    table_registry.metadata.drop_all(engine)


@pytest.fixture
def session(engine: Engine) -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


@pytest.fixture
def session_with_user(session: Session) -> Session:
    add_user(session)
    return session


@pytest.fixture
def session_with_user_and_license(session: Session) -> Session:
    add_user(session)
    add_license(session)
    return session
