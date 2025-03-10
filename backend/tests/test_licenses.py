from datetime import datetime
from http import HTTPStatus

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from sqlalchemy.sql import select

from src.models import License
from tests.factory.faker import fake
from tests.utils import get_license_data

# from src.schemas.license import LicenseResponse


def test_create_license(
    session: Session, client: TestClient, token: str
) -> None:
    """
    Testa a criação de uma licença usando a LicenseFactory.
    """
    license_data = get_license_data()

    response = client.post(
        '/licenses',
        json=license_data,
        headers={'Authorization': f'Bearer {token}'},
    )
    data = response.json()

    print('Resposta recebida:', response.json())

    assert response.status_code == HTTPStatus.CREATED

    db_license = session.scalar(
        select(License).where(License.id == data['id'])
    )

    assert (
        db_license.software_name == license_data.get('software_name').lower()
    )
    assert db_license.purchase_date == datetime.fromisoformat(
        license_data.get('purchase_date')
    )
    assert db_license.created_at is not None
    assert db_license.updated_at is None


def test_get_licenses_no_license(client: TestClient, token: str) -> None:
    """
    Testa a listagem de licenças via API.
    """
    response = client.get(
        '/licenses', headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == []


def test_get_license_by_id(
    client: TestClient, token: str, mock_license: License
) -> None:
    """
    Testa a busca de uma licença específica pelo ID.
    """
    response = client.get(
        f'/licenses/{mock_license.id}',
        headers={'Authorization': f'Bearer {token}'},
    )
    data = response.json()

    assert response.status_code == HTTPStatus.OK
    assert data['id'] == mock_license.id
    assert data['version'] == mock_license.version


def test_update_license(
    client: TestClient, token: str, mock_license: License, session: Session
) -> None:
    """
    Testa a atualização de uma licença.
    """
    update_data = get_license_data()
    update_data['license_key'] = fake.uuid4()

    response = client.put(
        f'/licenses/{mock_license.id}',
        json=update_data,
        headers={'Authorization': f'Bearer {token}'},
    )
    data = response.json()

    db_license = session.scalar(
        select(License).where(License.id == data.get('id'))
    )

    assert response.status_code == HTTPStatus.OK
    assert data['purchase_date'] == update_data['purchase_date']

    assert update_data['software_name'] == db_license.software_name
    assert update_data['license_key'] == db_license.license_key
    assert db_license.updated_at is not None


def test_partial_update_license(
    client: TestClient, token: str, mock_license: License, session: Session
) -> None:
    """
    Testa a atualização parcial de uma licença.
    """
    partial_update_data = {'software_name': 'NovoSoftware'}

    response = client.patch(
        f'/licenses/{mock_license.id}',
        json=partial_update_data,
        headers={'Authorization': f'Bearer {token}'},
    )
    data = response.json()

    db_license = session.scalar(
        select(License).where(License.id == data.get('id'))
    )

    assert response.status_code == HTTPStatus.OK
    assert data['software_name'] == partial_update_data['software_name']
    assert db_license.software_name == partial_update_data['software_name']
    assert db_license.updated_at is not None


def test_delete_license(
    client: TestClient, token: str, mock_license: License, session: Session
):
    """
    Testa a exclusão de uma licença.
    """
    # license_schema=LicenseResponse.model_validate(mock_license).model_dump()

    response = client.delete(
        f'/licenses/{mock_license.id}',
        headers={'Authorization': f'Bearer {token}'},
    )

    deleted_license = session.scalar(
        select(License).where(License.id == mock_license.id)
    )

    assert response.status_code == HTTPStatus.NO_CONTENT
    # assert response.json() == license_schema
    assert deleted_license is None
