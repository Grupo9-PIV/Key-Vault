from collections.abc import Generator
from datetime import datetime

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import Engine, create_engine, event
from sqlalchemy.orm import Session

from src.app import app
from src.database import table_registry
from src.models import License, Notification, RenewalRequest, User


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture
def engine():
    engine = create_engine('sqlite:///:memory:')

    # garante que a feature de foreign keys esteja ativada no sqlite
    @event.listens_for(engine, 'connect')
    def enable_foreign_keys(dbapi_connection, connection_record):
        cursor = dbapi_connection.cursor()
        cursor.execute('PRAGMA foreign_keys=ON')
        cursor.close()

    table_registry.metadata.create_all(engine)

    yield engine

    table_registry.metadata.drop_all(engine)


@pytest.fixture
def session(engine: Engine) -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


@pytest.fixture
def user(session: Session) -> User:
    user = User(
        email='teste@teste.com',
        password_hash='12345678',
        name='Teste',
        role='admin',
        department='Teste',
    )
    session.add(user)
    session.commit()
    return user


@pytest.fixture
def mock_license(session: Session, user: User) -> License:
    mock_license = License(
        assigned_to_id=user.id,
        manager_id=user.id,
        software_name='XYZ Soft',
        license_type='trial',
        status='ativa',
        developed_by='Test Soft',
        version='v1.0.0',
        purchase_date=datetime(1900, 1, 1),
        start_date=datetime(1900, 1, 1),
        end_date=datetime(1900, 1, 1),
        license_key=None,
        current_usage=None,
        subscription_plan=None,
        conditions=None,
    )
    session.add(mock_license)
    session.commit()
    return mock_license


@pytest.fixture
def notification(session: Session, user: User) -> Notification:
    notification = Notification(
        user_id=user.id,
        license_id=None,
        request_id=None,
        message='Test Notification',
    )
    session.add(notification)
    session.commit()
    return notification


@pytest.fixture
def renewal_request(
    session: Session, user: User, mock_license: License
) -> RenewalRequest:
    renewal_request = RenewalRequest(
        license_id=mock_license.id,
        requested_by_id=user.id,
        manager_id=None,
        reason=None,
        feedback=None,
        status='pendente',
    )

    session.add(renewal_request)
    session.commit()
    return renewal_request
