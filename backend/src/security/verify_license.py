from sqlalchemy.orm import Session
from src.models.license import License
from datetime import datetime
from src.exceptions import LicenseNotFoundException, LicenseExpiredException, LicenseInactiveException

def verify_license_key(db: Session, license_key: str):
    """
    Função para verificar a chave de licença.
    Valida se a licença existe, se está ativa e se não está expirada.

    """
    # Busca a licença pelo código (license_key)
    license = db.query(License).filter(License.license_key == license_key).first()
    
    if not license:
        raise LicenseNotFoundException(f"License with key {license_key} not found.")
    
    # Verifica se a licença está expirada
    if license.end_date < datetime.now():
        raise LicenseExpiredException(f"License with key {license_key} is expired.")
    
    # Verifica se o status da licença é 'ativa'
    if license.status != 'ativa':
        raise LicenseInactiveException(f"License with key {license_key} is inactive.")
    
    # Se a licença passar nas verificações, retorna a licença
    return license
