from sqlalchemy.orm import Session
from sqlalchemy.sql import select

from src.exceptions import WrongEmailOrPasswordException
from src.models import User
from src.security import create_access_token, verify_password
from src.types import T_CurrentUser, T_OAuth2Form


class AuthService:
    @staticmethod
    def get_access_token(session: Session, form_data: T_OAuth2Form):
        user = AuthService._get_user_or_raise(session, form_data)

        access_token = create_access_token(data={'sub': user.email})
        return {'user_id': user.id, 'access_token': access_token}

    @staticmethod
    def refresh_access_token(user: T_CurrentUser):
        new_access_token = create_access_token(data={'sub': user.email})
        return {'user_id': user.id, 'access_token': new_access_token}

    # helper functions (DRY)
    @staticmethod
    def _get_user_or_raise(session: Session, form_data: T_OAuth2Form) -> User:
        user = session.scalar(
            select(User).where(User.email == form_data.username)
        )

        if not user or not verify_password(
            form_data.password, user.password_hash
        ):
            raise WrongEmailOrPasswordException()
        return user
