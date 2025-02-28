from datetime import datetime
from typing import Optional  # Permite definir campos opcionais
from pydantic import BaseModel, field_serializer
from src.enums import LicensePriority, LicenseStatus

"""Esse arquivo cria o esquema pras licenças a partir do pydantic, pra validar e sinalizar os dados, ele foi feito de acordo com
o arquivo license.py, refereciando as variáveis de lá
"""


class LicenseBase(BaseModel):
    """Modelo básico de uma licença""" 
    software_name: str  # Nome do software
    license_type: str  # Tipo de licença  vitlaícia, anual, mensal
    status: str  # Status da licença ativa, expirada
    developed_by: str  # Marca
    start_date: datetime  # Data de início da licença
    end_date: datetime  # Validade da licença
    priority: Optional[LicensePriority] = LicensePriority.MEDIA  # Prioridade da licença, padrão "média"
    version: Optional[str] = "1.0.0"
    purchase_date: Optional[datetime] = datetime.now()
    current_usage: Optional[int] = 0  # 0
    subscription_plan: Optional[str] = None  # Basic
    conditions: Optional[str] = None  # None


class LicenseCreate(LicenseBase):
    license_key: Optional[str] = None  # Chave da licença
    assigned_to_id: Optional[int] = None  # ID do usuário atribuído
    manager_id: Optional[int] = None  # ID de quem gerencia a licnça


class LicenseUpdate(BaseModel):
    """Schema para atualização de uma licença """
    status: Optional[str] = None  # Permite atualizar o status da licença
    end_date: Optional[datetime] = None  # Permite atualizar a data de expiração
    priority: Optional[LicensePriority] = LicensePriority.MEDIA  # Permite atualizar a prioridade
    version: Optional[str] = "1.0.0"
    current_usage: Optional[int] = None  
    subscription_plan: Optional[str] = None  
    conditions: Optional[str] = None  


class LicenseResponse(LicenseBase):
    """Schema de resposta, utilizado para retornar informações sobre uma licença"""
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    license_key: Optional[str] = None
    assigned_to_id: Optional[int] = None
    manager_id: Optional[int] = None
    status: LicenseStatus

    @field_serializer('created_at', 'updated_at', 'start_date', 'end_date', 'purchase_date')
    def serialize_dates(self, value: datetime) -> str:
        return value.isoformat() if value else None

    @field_serializer('priority', 'status')
    def serialize_enum(self, value) -> str:
        return value.value if value else None

    class Config:
        from_attributes = True
