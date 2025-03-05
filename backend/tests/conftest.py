from collections.abc import Callable, Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session
from testcontainers.postgres import PostgresContainer

from src.app import app
from src.database import get_session, table_registry
from src.models import AuditLog, License, Notification, RenewalRequest, User
from tests.factory import LicenseFactory, UserFactory
from tests.factory.user_factory import DEFAULT_TEST_PWD, UserRole


@pytest.fixture(scope='session')
def engine() -> Generator[Engine, None, None]:
    with PostgresContainer('postgres:17', driver='psycopg') as postgres:
        _engine = create_engine(postgres.get_connection_url())

        with _engine.begin():
            yield _engine


@pytest.fixture
def session(engine: Engine) -> Generator[Session, None, None]:
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session
        session.rollback()

    table_registry.metadata.drop_all(engine)


@pytest.fixture
def client(session: Session) -> Generator[TestClient, None, None]:
    def get_test_session() -> Session:
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_test_session
        yield client

    app.dependency_overrides.clear()


@pytest.fixture
def create_user(session: Session) -> Callable[..., User]:
    def _create_user(**kwargs) -> User:
        user = UserFactory(**kwargs)

        session.add(user)
        session.commit()
        session.refresh(user)

        user.password = kwargs.get('plain_password', DEFAULT_TEST_PWD)
        return user

    return _create_user


@pytest.fixture
def user(create_user) -> User:
    return create_user(role=UserRole.USER)


@pytest.fixture
def admin(create_user) -> User:
    return create_user(admin=True)  # Usa o trait 'admin'


@pytest.fixture
def create_license(session: Session) -> Callable[..., License]:
    def _create_license(**kwargs) -> License:
        mock_license = LicenseFactory(**kwargs)

        session.add(mock_license)
        session.commit()
        session.refresh(mock_license)

        return mock_license

    return _create_license


@pytest.fixture
def mock_license(create_license) -> License:
    return create_license()


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
        '/auth/token',
        data={'username': user.email, 'password': user.password},
    )

    return response.json()['access_token']


@pytest.fixture
def admin_token(client, admin) -> str:
    response = client.post(
        '/auth/token',
        data={'username': admin.email, 'password': admin.password},
    )

    return response.json()['access_token']
