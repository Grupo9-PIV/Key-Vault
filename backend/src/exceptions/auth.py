from http import HTTPStatus

from .base import AppException


class CredentialsException(AppException):
    def __init__(self):
        super().__init__(
            HTTPStatus.UNAUTHORIZED, 'Could not validate credentials'
        )
        self.headers = {'WWW-Authenticate': 'Bearer'}


class ExpiredTokenException(AppException):
    def __init__(self):
        super().__init__(HTTPStatus.UNAUTHORIZED, 'Token has expired')
        self.headers = {'WWW-Authenticate': 'Bearer'}


class InvalidTokenException(AppException):
    def __init__(self):
        super().__init__(HTTPStatus.UNAUTHORIZED, 'Invalid token')
        self.headers = {'WWW-Authenticate': 'Bearer'}


class WrongEmailOrPasswordException(AppException):
    def __init__(self):
        super().__init__(HTTPStatus.BAD_REQUEST, 'Incorrect email or password')
