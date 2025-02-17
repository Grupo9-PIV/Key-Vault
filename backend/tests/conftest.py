from collections.abc import Generator
from datetime import datetime

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import Engine, create_engine, event
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from src.app import app
from src.database import get_session, table_registry
from src.models import AuditLog, License, Notification, RenewalRequest, User
from src.security import get_password_hash


@pytest.fixture
def engine() -> Generator[Engine, None, None]:
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )

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
def client(session: Session) -> Generator[TestClient, None, None]:
    def get_test_session() -> Session:
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_test_session
        yield client

    app.dependency_overrides.clear()


@pytest.fixture
def user(session: Session) -> User:
    plain_password = '12345678'

    user = User(
        email='teste@teste.com',
        password_hash=get_password_hash(plain_password),
        name='Teste',
        role='user',
        department='Teste',
    )
    session.add(user)
    session.commit()
    session.refresh(user)

    user.password = plain_password

    return user


@pytest.fixture
def admin(session: Session) -> User:
    plain_password = '12345678'

    admin_user = User(
        email='admin@admin.com',
        password_hash=get_password_hash(plain_password),
        name='Admin',
        role='admin',
        department='Admin',
    )
    session.add(admin_user)
    session.commit()
    session.refresh(admin_user)

    admin_user.password = plain_password

    return admin_user


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


@pytest.fixture
def audit_log(session: Session, user: User, mock_license: License) -> AuditLog:
    audit_log = AuditLog(
        performed_by_id=user.id,
        entity_id=mock_license.id,
        entity=type(mock_license).__name__,
        action='delete',
    )

    session.add(audit_log)
    session.commit()

    return audit_log


@pytest.fixture
def token(client, user) -> str:
    response = client.post(
        '/token',
        data={'username': user.email, 'password': user.password},
    )

    return response.json()['access_token']


@pytest.fixture
def adm_token(client, admin) -> str:
    response = client.post(
        '/token',
        data={'username': admin.email, 'password': admin.password},
    )

    return response.json()['access_token']
