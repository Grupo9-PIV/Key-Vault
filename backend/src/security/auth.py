from datetime import datetime, timedelta

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jwt import decode, encode
from jwt.exceptions import ExpiredSignatureError, PyJWTError
from sqlalchemy.orm import Session
from sqlalchemy.sql import select
from zoneinfo import ZoneInfo

from src.database import get_session
from src.exceptions import CredentialsException
from src.models import User
from src.settings import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/token')


def create_access_token(data: dict) -> str:
    to_encode = data.copy()

    expire = datetime.now(tz=ZoneInfo('UTC')) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({'exp': expire})

    encoded_jwt = encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(
    session: Session = Depends(get_session),
    token: str = Depends(oauth2_scheme),
) -> User:
    try:
        payload = decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get('sub')
        if not email:
            raise CredentialsException()
    except ExpiredSignatureError:
        raise CredentialsException()
    except PyJWTError:
        raise CredentialsException()
    else:
        user = session.scalar(select(User).where(User.email == email))

    if user is None:
        raise CredentialsException()

    return user
