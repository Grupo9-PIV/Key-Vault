from datetime import datetime
from typing import Optional  # Permite definir campos opcionais
from pydantic import BaseModel

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
    priority: Optional[str] = "média"  # Prioridade da licença, padrão "média"


class LicenseCreate(LicenseBase):
    """Schema para criação de uma nova licença, o que tá com optional é porque não é obrigatório, talvez deva ser?"""
    license_key: Optional[str] = None  # Chave da licença
    assigned_to_id: Optional[int] = None  # ID do usuário atribuído
    manager_id: Optional[int] = None  # ID de quem gerencia a licnça

class LicenseUpdate(BaseModel):
    """Schema para atualização de uma licença """
    status: Optional[str] = None  # Permite atualizar o status da licença
    end_date: Optional[datetime] = None  # Permite atualizar a data de expiração
    priority: Optional[str] = None  # Permite atualizar a prioridade

class LicenseResponse(LicenseBase):
    """Schema de resposta, utilizado para retornar informações sobre uma licença"""
    id: int  # Identificador único da licença
    created_at: datetime  # Data de criação da licença
    updated_at: Optional[datetime] = None  # Data de atualização
    class Config:
        from_attributes = True  # Permite converter objetos do SQLAlchemy automaticamente
