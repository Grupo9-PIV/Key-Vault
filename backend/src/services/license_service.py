from sqlalchemy.orm import Session
from src.models.license import License
from src.schemas.license import LicenseCreate, LicenseUpdate
from src.exceptions import  LicenseNotFoundException  # Exceção para código de licença não encontrada


# Função para criar uma nova licença
def create_license(db: Session, license_data: LicenseCreate):
    # Criação da nova licença
    new_license = License(**license_data.dict())  # Corrigido para usar `dict()` no lugar de `model_dump()`
    db.add(new_license)
    db.commit()
    db.refresh(new_license)
    return new_license

# Função para buscar uma licença por ID
def get_license(db: Session, license_id: int):
    license_obj = db.query(License).filter(License.id == license_id).first()
    if not license_obj:
        raise LicenseNotFoundException()
    return license_obj

# Função para buscar todas as licenças
def get_all_licenses(db: Session, skip: int = 0, limit: int = 10):
    return db.query(License).offset(skip).limit(limit).all()

# Função para atualizar uma licença
def update_license(db: Session, license_id: int, license_data: LicenseUpdate):
    license_obj = db.query(License).filter(License.id == license_id).first()
    if not license_obj:
        raise LicenseNotFoundException()
    
    # Atualizando os campos da licença
    for field, value in license_data.dict().items():  
        setattr(license_obj, field, value)
    
    db.commit()
    db.refresh(license_obj)
    return license_obj

# Função para atualizar parcialmente uma licença (parcial update)
def partial_update_license(db: Session, license_id: int, license_data: LicenseUpdate):
    license_obj = db.query(License).filter(License.id == license_id).first()
    if not license_obj:
        raise LicenseNotFoundException()
    
    # Atualizando apenas os campos fornecidos
    for field, value in license_data.dict(exclude_unset=True).items():
        setattr(license_obj, field, value)
    
    db.commit()
    db.refresh(license_obj)
    return license_obj

# Função para deletar uma licença
def delete_license(db: Session, license_id: int):
    license_obj = db.query(License).filter(License.id == license_id).first()
    if not license_obj:
        raise LicenseNotFoundException()
    
    db.delete(license_obj)
    db.commit()
    return True
