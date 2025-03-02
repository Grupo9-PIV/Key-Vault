from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from src.database import get_session
from src.exceptions import LicenseNotFoundException
from src.models import User
from src.schemas.license import LicenseCreate, LicenseUpdate, LicenseResponse
from src.security import get_current_user
from src.services.license_service import LicenseService

router = APIRouter(prefix='/licenses', tags=['Licenses'])


# Rota para criar uma nova licença
@router.post(
    '/', status_code=HTTPStatus.CREATED, response_model=LicenseResponse
)
def create_license_route(
    license_data: LicenseCreate,
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    """
    Cria uma nova licença.
    Requer autenticação.
    """
    try:
        return LicenseService.create_license(db, license_data)
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=str(e),
        )


# Rota para buscar uma licença por ID
@router.get(
    '/{license_id}', status_code=HTTPStatus.OK, response_model=LicenseResponse
)
def get_license_route(
    license_id: int,
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    """
    Busca uma licença pelo ID.
    Requer autenticação.
    """

    try:
        license = LicenseService.get_license(db, license_id)
        return license
    except LicenseNotFoundException as e:
        # Retorna 404 quando a licença não for encontrada
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=e.detail,
        )
    except Exception as e:
        # Caso haja outro erro inesperado
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail='Erro interno no servidor: ' + str(e),
        )


# Rota para buscar todas as licenças
@router.get(
    '/', status_code=HTTPStatus.OK, response_model=List[LicenseResponse]
)
def get_all_licenses_route(
    db: Session = Depends(get_session),
    skip: int = 0,
    limit: int = 10,
    current_user: User = Depends(get_current_user),
):
    """
    Busca todas as licenças.
    Requer autenticação.
    """
    try:
        licenses = LicenseService.get_all_licenses(db, skip=skip, limit=limit)
        return licenses
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail='Erro interno no servidor: ' + str(e),
        )


# Rota para atualizar uma licença
@router.put(
    '/{license_id}', status_code=HTTPStatus.OK, response_model=LicenseResponse
)
def update_license_route(
    license_id: int,
    license_data: LicenseUpdate,
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    """
    Atualiza uma licença existente.
    Requer autenticação.
    """
    try:
        # Chama a função para atualizar a licença
        updated_license = LicenseService.update_license(
            db, license_id, license_data
        )

        # Se a licença não for encontrada (None), lançar erro 404
        if not updated_license:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND,
                detail='Licença não encontrada.',
            )
        return updated_license
    except LicenseNotFoundException as e:
        # Caso o erro seja devido a licença não encontrada, retornamos 404
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=str(e),
        )
    except Exception as e:
        # Outros erros inesperados
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=f'Erro interno no servidor: {str(e)}',
        )


# Rota para deletar uma licença
@router.delete('/{license_id}', status_code=HTTPStatus.NO_CONTENT)
def delete_license_route(
    license_id: int,
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    """
    Deleta uma licença existente.
    Requer autenticação.
    """
    try:
        success = LicenseService.delete_license(db, license_id)
        if success:
            return Response(
                status_code=HTTPStatus.NO_CONTENT
            )  # Retorna status 204
        else:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND,
                detail='Licença não encontrada.',
            )
    except LicenseNotFoundException as e:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=e.detail,
        )
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail='Erro interno no servidor: ' + str(e),
        )
