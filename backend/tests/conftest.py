from collections.abc import Generator
from datetime import datetime

import pytest
from factory import Factory, LazyAttribute, Sequence, Faker
from fastapi.testclient import TestClient
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session
from testcontainers.postgres import PostgresContainer

from src.app import app
from src.database import get_session, table_registry
from src.enums import UserRole, LicenseStatus, LicensePriority, LicenseType
from src.models import AuditLog, License, Notification, RenewalRequest, User
from src.security import get_password_hash

import factory
import re
from factory.alchemy import SQLAlchemyModelFactory
from faker import Faker


class UserFactory(Factory):
    class Meta:
        model = User

    name: str = Sequence(lambda x: f'test-{x}')
    email: str = LazyAttribute(lambda obj: f'{obj.name}@test.com')
    password_hash: str = LazyAttribute(
        lambda obj: get_password_hash(obj.name + '-senha')
    )
    role: UserRole = UserRole.USER
    department: str = 'Teste'


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
def user(session: Session) -> User:
    plain_password = '12345678'

    user = UserFactory(password_hash=get_password_hash(plain_password))

    session.add(user)
    session.commit()
    session.refresh(user)

    user.password = plain_password

    return user


@pytest.fixture
def admin(session: Session) -> User:
    plain_password = '12345678'

    admin_user = UserFactory(
        password_hash=get_password_hash(plain_password), role=UserRole.ADMIN
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
        '/auth/token',
        data={'username': user.email, 'password': user.password},
    )

    return response.json()['access_token']


@pytest.fixture
def adm_token(client, admin) -> str:
    response = client.post(
        '/auth/token',
        data={'username': admin.email, 'password': admin.password},
    )

    return response.json()['access_token']


fake = Faker()


class LicenseFactory(SQLAlchemyModelFactory):
    class Meta:
        model = License
        sqlalchemy_session = None  # Inicialmente, a sessão é None
        sqlalchemy_session_persistence = (
            'commit'  # Salva o objeto no banco de dados
        )

    # Atributos da licença
    software_name = LazyAttribute(lambda _: fake.word())
    license_type = 'trial'
    status = LicenseStatus.ATIVA
    developed_by = LazyAttribute(lambda _: fake.company())
    version = 'v1.0.0'
    start_date = datetime(1900, 1, 1)
    end_date = datetime(1900, 1, 1)
    priority = LicensePriority.MEDIA
    purchase_date = datetime(1900, 1, 1)
    current_usage = 0
    subscription_plan = None
    conditions = None

    # Relacionamentos (assigned_to e manager)
    assigned_to_id = factory.LazyAttribute(lambda obj: obj.assigned_to.id)
    manager_id = factory.LazyAttribute(lambda obj: obj.manager.id)

    # Gera uma license_key válida com base no software_name
    @factory.lazy_attribute
    def license_key(self):
        # Regras de validação do LicenseService
        SOFTWARE_LICENSE_RULES = {
            'windows': 25,
            'adobe': 24,
            'office': 20,
        }

        # Normaliza o nome do software para minúsculas
        software_name = self.software_name.lower()

        # Verifica se o software está na lista de regras
        if software_name in SOFTWARE_LICENSE_RULES:
            expected_length = SOFTWARE_LICENSE_RULES[software_name]
            # Gera uma chave alfanumérica com o tamanho esperado
            return fake.pystr(
                min_chars=expected_length, max_chars=expected_length
            )

        # Se o software não estiver na lista, gera uma chave com tamanho padrão
        return fake.pystr(min_chars=20, max_chars=25)


@pytest.fixture
def license_factory(session: Session, user: User):
    """
    Fixture que cria e retorna uma licença no banco
    de dados usando a LicenseFactory.
    """
    # Configura a sessão da LicenseFactory
    LicenseFactory._meta.sqlalchemy_session = session

    def _create_license(**kwargs) -> License:
        license = LicenseFactory(
            assigned_to_id=user.id,  # Passa apenas o ID do usuário
            manager_id=user.id,  # Passa apenas o ID do usuário
            **kwargs,
        )
        session.add(license)
        session.commit()
        session.refresh(license)
        return license

    return _create_license
