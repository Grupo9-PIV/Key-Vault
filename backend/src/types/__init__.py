from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.database import get_session
from src.models import User
from src.security import get_current_user

T_Session = Annotated[Session, Depends(get_session)]
T_CurrentUser = Annotated[User, Depends(get_current_user)]
T_OAuth2Form = Annotated[OAuth2PasswordRequestForm, Depends()]

__all__ = [
    'T_Session',
    'T_CurrentUser',
    'T_OAuth2Form',
]
