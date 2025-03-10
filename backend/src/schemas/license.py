from datetime import datetime
from typing import Optional  # Permite definir campos opcionais

from pydantic import BaseModel

from src.enums import LicensePriority, LicenseStatus


class LicenseBase(BaseModel):
    """Modelo básico de uma licença"""

    software_name: str  # Nome do software
    license_type: str  # Tipo de licença (vitalícia, anual, mensal)
    status: LicenseStatus  # Status da licença (ativa, expirada)
    developed_by: str  # Marca ou empresa desenvolvedora
    start_date: datetime  # Data de início da licença
    end_date: datetime  # Validade da licença
    priority: Optional[LicensePriority] = (
        LicensePriority.MEDIA
    )  # Prioridade da licença, padrão "média"
    version: Optional[str] = '1.0.0'
    purchase_date: datetime
    current_usage: Optional[int] = 0  # Número de usos ou ativações
    subscription_plan: Optional[str] = None  # Plano da assinatura, ex: "Basic"
    conditions: Optional[str] = None  # Condições da licença
    license_key: Optional[str] = None  # Chave da licença
    assigned_to_id: Optional[int] = None  # ID do usuário atribuído
    manager_id: Optional[int] = None  # ID do gerente da licença


class LicenseCreate(LicenseBase): ...


class LicenseUpdate(LicenseBase):
    # Schema para atualização de uma licença

    software_name: Optional[str] = None
    license_type: Optional[str] = None
    status: Optional[LicenseStatus] = None
    developed_by: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    priority: Optional[LicensePriority] = None
    version: Optional[str] = None
    purchase_date: Optional[datetime] = None
    current_usage: Optional[int] = None
    subscription_plan: Optional[str] = None
    conditions: Optional[str] = None
    license_key: Optional[str] = None
    assigned_to_id: Optional[int] = None
    manager_id: Optional[int] = None


class LicenseResponse(LicenseBase):
    """Schema de resposta, retorna informações sobre uma licença"""

    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
