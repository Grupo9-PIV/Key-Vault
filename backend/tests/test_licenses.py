import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../backend/src")))

from http import HTTPStatus
from pydantic import TypeAdapter
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src.models import License
from src.schemas.license import LicenseResponse


def test_create_license(client: TestClient, token: str) -> None:
    license_data = {
        'software_name': 'Test Software',
        'license_type': 'Anual',
        'status': 'ativa',
        'developed_by': 'Test Company',
        'start_date': '2025-01-01T00:00:00',
        'end_date': '2026-01-01T00:00:00',
        'priority': 'alta',
        'license_key': '12345-ABCDE',
        'version': '1.0.0',
        'purchase_date': '2024-01-01T00:00:00',  
        'current_usage': 0,  
        'subscription_plan': 'Basic',  
        'conditions': 'None',  
    }

    response = client.post(
        '/licenses/',
        json=license_data,
        headers={'Authorization': f'Bearer {token}'},
    )
    data = response.json()

    assert data['software_name'] == license_data['software_name']
    assert data['license_type'] == license_data['license_type']
    assert data['status'] == license_data['status']
    assert data['developed_by'] == license_data['developed_by']
    assert data['start_date'] == license_data['start_date']
    assert data['end_date'] == license_data['end_date']
    assert data['priority'] == license_data['priority']
    assert data['license_key'] == license_data['license_key']
    assert data['version'] == license_data['version']
    assert data['purchase_date'] == license_data['purchase_date']
    assert data['current_usage'] == license_data['current_usage']
    assert data['subscription_plan'] == license_data['subscription_plan']
    assert data['conditions'] == license_data['conditions']
    assert 'id' in data and data['id'] is not None, "ID não foi retornado ou é inválido"


from datetime import datetime

def test_read_license(client: TestClient, token: str, license: License) -> None:
    license_schema = TypeAdapter(LicenseResponse).dump_python(license)

    # Verifique se o valor é do tipo datetime antes de chamar isoformat()
    if isinstance(license_schema['start_date'], datetime):
        license_schema['start_date'] = license_schema['start_date'].isoformat()
    else:
        license_schema['start_date'] = None if not license_schema['start_date'] else license_schema['start_date']

    if isinstance(license_schema['end_date'], datetime):
        license_schema['end_date'] = license_schema['end_date'].isoformat()
    else:
        license_schema['end_date'] = None if not license_schema['end_date'] else license_schema['end_date']

    if isinstance(license_schema['purchase_date'], datetime):
        license_schema['purchase_date'] = license_schema['purchase_date'].isoformat()
    else:
        license_schema['purchase_date'] = None if not license_schema['purchase_date'] else license_schema['purchase_date']

    if isinstance(license_schema['created_at'], datetime):
        license_schema['created_at'] = license_schema['created_at'].isoformat()
    else:
        license_schema['created_at'] = None if not license_schema['created_at'] else license_schema['created_at']

    if isinstance(license_schema['updated_at'], datetime):
        license_schema['updated_at'] = license_schema['updated_at'].isoformat()
    else:
        license_schema['updated_at'] = None if not license_schema['updated_at'] else license_schema['updated_at']

    response = client.get(
        f'/licenses/{license.id}',
        headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == license_schema



def test_read_license_not_found(client: TestClient, token: str) -> None:
    response = client.get(
        '/licenses/404', 
        headers={'Authorization': f'Bearer {token}'},
    )
    
    # O servidor deve retornar 404, indicando que a licença não foi encontrada
    assert response.status_code == HTTPStatus.NOT_FOUND



def test_update_license(client: TestClient, token: str, license: License) -> None:
    updated_data = {
        'software_name': 'Test Software',
        'license_type': 'Anual',
        'status': 'expirada',
        'developed_by': 'Test Company',
        'start_date': '2025-06-01T00:00:00',
        'end_date': '2026-06-01T00:00:00',
        'priority': 'baixa',
    }

    response = client.put(
        f'/licenses/{license.id}',
        json=updated_data,
        headers={'Authorization': f'Bearer {token}'},
    )
    print(response.status_code, response.json())
    data = response.json()

    assert response.status_code == HTTPStatus.OK
    assert data['software_name'] == updated_data['software_name']
    assert data['license_type'] == updated_data['license_type']
    assert data['license_key'] == license.license_key  # A chave não deve mudar


def test_update_license_not_found(client: TestClient, token: str) -> None:
    updated_data = {
        'software_name': 'Test Software',
        'license_type': 'Mensal',
        'status': 'expirada',
        'developed_by': 'Test Company',
        'start_date': '2025-06-01T00:00:00',
        'end_date': '2026-06-01T00:00:00',
        'priority': 'baixa',
    }

    response = client.put(
        '/licenses/404',
        json=updated_data,
        headers={'Authorization': f'Bearer {token}'},
    )
    

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_license(client: TestClient, token: str, license: License) -> None:
    # Usando LicenseResponse no lugar de LicensePublic
    license_schema = TypeAdapter(LicenseResponse).dump_python(license)
    response = client.delete(
        f'/licenses/{license.id}',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.OK


def test_delete_license_not_found(client: TestClient, token: str) -> None:
    response = client.delete(
        '/licenses/404',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_partial_update_license(client: TestClient, token: str, license: License) -> None:
    updated_data = {'status': 'expirada'}

    response = client.patch(
        f'/licenses/{license.id}',
        json=updated_data,
        headers={'Authorization': f'Bearer {token}'},
    )
        # Imprima o status e o corpo da resposta para entender o erro
    print(response.status_code)
    print(response.json())
    
    assert response.status_code == HTTPStatus.OK
    assert response.json()['status'] == updated_data['status']
    assert response.json()['license_key'] == license.license_key  # A chave não deve mudar


def test_partial_update_license_not_found(client: TestClient, token: str) -> None:
    updated_data = {'status': 'expirada'}

    response = client.patch(
        '/licenses/404',
        json=updated_data,
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.NOT_FOUND