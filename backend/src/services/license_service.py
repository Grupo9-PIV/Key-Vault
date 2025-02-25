from sqlalchemy.orm import Session
from src.models.license import License
from src.schemas.license import LicenseCreate, LicenseUpdate
from src.exceptions import LicenseCodeAlreadyExistsException  # Exceção para código de licença duplicado

# Função para criar uma nova licença
def create_license(db: Session, license_data: LicenseCreate):
    # Verifica se já existe uma licença com o mesmo código (serial number)
    existing_license = db.query(License).filter(License.license_key == license_data.code).first()
    if existing_license:
        raise LicenseCodeAlreadyExistsException()  # Levanta exceção se o código já existe

    # Criação da nova licença
    new_license = License(**license_data.model_dump())
    db.add(new_license)
    db.commit()
    db.refresh(new_license)
    return new_license

# Função para buscar uma licença por ID
def get_license(db: Session, license_id: int):
    return db.query(License).filter(License.id == license_id).first()

# Função para buscar todas as licenças
def get_all_licenses(db: Session):
    return db.query(License).all()

# Função para atualizar uma licença
def update_license(db: Session, license_id: int, license_data: LicenseUpdate):
    license_obj = db.query(License).filter(License.id == license_id).first()
    if license_obj:
        for field, value in license_data.model_dump(exclude_unset=True).items():
            setattr(license_obj, field, value)
        db.commit()
        db.refresh(license_obj)
    return license_obj

# Função para deletar uma licença
def delete_license(db: Session, license_id: int):
    license_obj = db.query(License).filter(License.id == license_id).first()
    if license_obj:
        db.delete(license_obj)
        db.commit()
        return True
    return False
