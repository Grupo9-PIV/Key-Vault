from http import HTTPStatus

from fastapi import APIRouter

from src.schemas import Token
from src.services import AuthService
from src.types import T_CurrentUser, T_OAuth2Form, T_Session

router = APIRouter(prefix='/auth', tags=['auth'])


@router.post('/token', status_code=HTTPStatus.OK, response_model=Token)
def login_for_access_token(session: T_Session, form_data: T_OAuth2Form):
    return AuthService.get_access_token(session, form_data)


@router.post('/refresh_token', response_model=Token)
def refresh_access_token(user: T_CurrentUser):
    return AuthService.refresh_access_token(user)
