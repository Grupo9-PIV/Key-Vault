import pytest
from datetime import datetime
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from src.models import License
from src.enums import LicenseStatus, LicenseType, LicensePriority
from src.services.license_service import LicenseService

#testes refeitos, agora com factory 

def test_create_license(session: Session, license_factory):
    """
    Testa a criação de uma licença usando a LicenseFactory.
    """
    new_license = license_factory(
        software_name="Test Software",
        license_type=LicenseType.TRIAL,
        status=LicenseStatus.ATIVA,
        developed_by="Test Corp",
        version="v1.2.3",
        priority=LicensePriority.ALTA,
        purchase_date=datetime(2024, 1, 1),
        start_date=datetime(2024, 1, 1),
        end_date=datetime(2025, 1, 1),
    )

    assert new_license is not None
    assert new_license.software_name == "Test Software"
    assert new_license.status == LicenseStatus.ATIVA
    assert new_license.priority == LicensePriority.ALTA


def test_get_licenses(client: TestClient, token: str):
    """
    Testa a listagem de licenças via API.
    """
    response = client.get("/licenses/", headers={"Authorization": f"Bearer {token}"})
    
    
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_get_license_by_id(client: TestClient, token: str, license_factory):
    """
    Testa a busca de uma licença específica pelo ID.
    """
    new_license = license_factory(software_name="Software Teste")
    response = client.get(f"/licenses/{new_license.id}", headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == new_license.id
    assert data["software_name"] == "Software Teste"


def test_update_license(client: TestClient, token: str, license_factory):
    """
    Testa a atualização de uma licença.
    """
    new_license = license_factory(software_name="Software Antigo")
    
    update_data = {
        "software_name": "windows",
        "license_type": LicenseService.normalize_license_type("anual"),  
        "status": "ativa",  
        "developed_by": "Nova Empresa",  
        "start_date": "2025-01-01T00:00:00",  
        "end_date": "2025-12-31T23:59:59",
        "license_key": "12345ABCDE67890FGHIJ11123"  
        }
    response = client.put(
        f"/licenses/{new_license.id}",
        json=update_data,
        headers={"Authorization": f"Bearer {token}"},
    )
    
    assert response.status_code == 200
    updated_license = response.json()
    assert updated_license["software_name"] == "windows"
    assert updated_license["license_key"] == "12345ABCDE67890FGHIJ11123"

def test_delete_license(client: TestClient, token: str, license_factory, session: Session):
    """
    Testa a exclusão de uma licença.
    """
    # Cria uma nova licença
    new_license = license_factory()
    
    # Realiza a requisição DELETE
    response = client.delete(f"/licenses/{new_license.id}", headers={"Authorization": f"Bearer {token}"})
    
    # Verifica se o status da resposta é 204 (sem conteúdo)
    assert response.status_code == 204  # Código 204 indica sucesso sem conteúdo
    
    # Verifica se a licença foi removida do banco de dados
    deleted_license = session.get(License, new_license.id)
    assert deleted_license is None  # A licença deve ser removida do banco de dados
