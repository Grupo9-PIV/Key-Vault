from datetime import datetime
from typing import Optional  # Permite definir campos opcionais
from pydantic import BaseModel, field_serializer, Field
from src.enums import LicensePriority, LicenseStatus

"""Esse arquivo cria o esquema pras licenças a partir do pydantic, pra validar e sinalizar os dados, ele foi feito de acordo com
o arquivo license.py, refereciando as variáveis de lá
"""


class LicenseBase(BaseModel):
    """Modelo básico de uma licença""" 
    software_name: str  # Nome do software
    license_type: str  # Tipo de licença (vitalícia, anual, mensal)
    status: LicenseStatus  # Status da licença (ativa, expirada)
    developed_by: str  # Marca ou empresa desenvolvedora
    start_date: datetime  # Data de início da licença
    end_date: datetime  # Validade da licença
    priority: Optional[LicensePriority] = LicensePriority.MEDIA  # Prioridade da licença, padrão "média"
    version: Optional[str] = "1.0.0"
    purchase_date: Optional[datetime] = Field(default_factory=datetime.now)
    current_usage: Optional[int] = 0  # Número de usos ou ativações
    subscription_plan: Optional[str] = None  # Plano da assinatura, ex: "Basic"
    conditions: Optional[str] = None  # Condições da licença
    license_key: Optional[str] = None  # Chave da licença
    assigned_to_id: Optional[int] = None  # ID do usuário atribuído
    manager_id: Optional[int] = None  # ID do gerente da licença


class LicenseCreate(LicenseBase):
    software_name: str
    license_key: str  # obrigatório
    manager_id: int # ID do gerente da licença


class LicenseUpdate(LicenseBase):
    """Schema para atualização de uma licença """
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
    """Schema de resposta, utilizado para retornar informações sobre uma licença"""
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    @field_serializer('created_at', 'updated_at', 'start_date', 'end_date', 'purchase_date')
    def serialize_dates(self, value: datetime) -> str:
        return value.isoformat() if value else None

    @field_serializer('priority', 'status')
    def serialize_enum(self, value) -> str:
        return value.value if value else None

    class Config:
        from_attributes = True
