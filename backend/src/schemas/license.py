from datetime import datetime
from typing import Optional  # Permite definir campos opcionais

from pydantic import BaseModel


class LicenseBase(BaseModel):
    software_name: str  # Nome do software
    license_type: str  # Tipo de licença  vitlaícia, anual, mensal
    status: str  # Status da licença ativa, expirada
    developed_by: str  # Marca
    start_date: datetime  # Data de início da licença
    end_date: datetime  # Validade da licença
    priority: Optional[str] = 'média'  # Prioridade da licença, padrão "média"


class LicenseCreate(LicenseBase):
    license_key: Optional[str] = None  # Chave da licença
    assigned_to_id: Optional[int] = None  # ID do usuário atribuído
    manager_id: Optional[int] = None  # ID de quem gerencia a licnça


class LicenseUpdate(BaseModel):
    status: Optional[str] = None  # Permite atualizar o status da licença
    # Permite atualizar a data de expiração
    end_date: Optional[datetime] = None
    priority: Optional[str] = None  # Permite atualizar a prioridade


class LicenseResponse(LicenseBase):
    id: int  # Identificador único da licença
    created_at: datetime  # Data de criação da licença
    updated_at: Optional[datetime] = None  # Data de atualização

    class Config:
        from_attributes = True
