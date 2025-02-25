from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_session
from src.schemas.license import LicenseCreate, LicenseUpdate, LicenseResponse
from src.services.license_service import (
    create_license, get_license, get_all_licenses, update_license, delete_license
)

router = APIRouter(prefix="/licenses", tags=["Licenses"])

# Rota para criar uma nova licença
@router.post("/", status_code=HTTPStatus.CREATED, response_model=LicenseResponse)
def create_license_route(
    license_data: LicenseCreate,
    db: Session = Depends(get_session),
):
    return create_license(db, license_data)

# Rota para buscar uma licença por ID
@router.get("/{license_id}", status_code=HTTPStatus.OK, response_model=LicenseResponse)
def get_license_route(
    license_id: int,
    db: Session = Depends(get_session),
):
    return get_license(db, license_id)

# Rota para buscar todas as licenças
@router.get("/", status_code=HTTPStatus.OK, response_model=list[LicenseResponse])
def get_all_licenses_route(
    db: Session = Depends(get_session),
    skip: int = 0,
    limit: int = 10,
):
    return get_all_licenses(db)

# Rota para atualizar uma licença
@router.put("/{license_id}", status_code=HTTPStatus.OK, response_model=LicenseResponse)
def update_license_route(
    license_id: int,
    license_data: LicenseUpdate,
    db: Session = Depends(get_session),
):
    return update_license(db, license_id, license_data)

# Rota para deletar uma licença
@router.delete("/{license_id}", status_code=HTTPStatus.OK)
def delete_license_route(
    license_id: int,
    db: Session = Depends(get_session),
):
    if delete_license(db, license_id):
        return {"message": "Licença deletada com êxito!"}
    raise HTTPException(status_code=404, detail="Licença não encontrada")
