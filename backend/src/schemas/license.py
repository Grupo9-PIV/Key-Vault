from datetime import datetime
from typing import Optional  # Permite definir campos opcionais

from pydantic import BaseModel, Field, field_serializer

from src.enums import LicensePriority, LicenseStatus, LicenseType


class LicenseBase(BaseModel):
    """Modelo básico de uma licença"""

    assigned_to_id: Optional[int] = Field(None, gt=0)  # Ajuste para > 0
    manager_id: Optional[int] = Field(None, gt=0)  # Ajusta para > 0
    software_name: str  # Nome do software
    license_type: LicenseType  # Tipo de licença (vitalícia, anual, mensal)
    status: LicenseStatus  # Status da licença (ativa, expirada)
    developed_by: str  # Marca ou empresa desenvolvedora
    version: Optional[str] = None
    purchase_date: Optional[datetime] = None
    start_date: datetime  # Data de início da licença
    end_date: datetime  # Validade da licença
    license_key: Optional[str] = None  # Chave da licença
    current_usage: Optional[int] = 0  # Número de usos ou ativações
    subscription_plan: Optional[str] = None  # Plano da assinatura, ex: "Basic"
    conditions: Optional[str] = None  # Condições da licença
    priority: Optional[LicensePriority] = (
        LicensePriority.MEDIA
    )  # Prioridade da licença, padrão "média"


class LicenseCreate(LicenseBase):
    software_name: str
    license_key: str


class LicenseUpdate(LicenseBase):
    # Schema para atualização de uma licença
    assigned_to_id: Optional[int] = Field(None, gt=0)  # Ajuste para > 0
    manager_id: Optional[int] = Field(None, gt=0)  # Ajusta para > 0
    software_name: str  # Nome do software
    license_type: LicenseType  # Tipo de licença (vitalícia, anual, mensal)
    status: LicenseStatus  # Status da licença (ativa, expirada)
    developed_by: str  # Marca ou empresa desenvolvedora
    version: Optional[str] = None
    priority: Optional[LicensePriority] = None
    version: Optional[str] = None
    purchase_date: Optional[datetime] = None
    license_key: Optional[str] = None  # Chave da licença
    current_usage: Optional[int] = 0  # Número de usos ou ativações
    subscription_plan: Optional[str] = None  # Plano da assinatura, ex: "Basic"
    conditions: Optional[str] = None  # Condições da licença
    priority: Optional[LicensePriority] = (
        LicensePriority.MEDIA
    )  # Prioridade da licença, padrão "média"


class LicensePartialUpdate(BaseModel):
    # atualização parcial

    assigned_to_id: Optional[int] = Field(None, gt=0)
    manager_id: Optional[int] = Field(None, gt=0)
    software_name: Optional[str] = None
    license_type: Optional[LicenseType] = None
    status: Optional[LicenseStatus] = None
    developed_by: Optional[str] = None
    version: Optional[str] = None
    purchase_date: Optional[datetime] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    license_key: Optional[str] = None
    current_usage: Optional[int] = None
    subscription_plan: Optional[str] = None
    conditions: Optional[str] = None
    priority: Optional[LicensePriority] = None


class LicenseResponse(LicenseBase):
    """Schema de resposta, retorna informações sobre uma licença"""

    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    @field_serializer(
        'created_at', 'updated_at', 'start_date', 'end_date', 'purchase_date'
    )
    @staticmethod
    def serialize_dates(value: datetime) -> str:
        return value.isoformat() if value else None

    @field_serializer('priority', 'status')
    @staticmethod
    def serialize_enum(value) -> str:
        return value.value if value else None

    class Config:
        from_attributes = True
