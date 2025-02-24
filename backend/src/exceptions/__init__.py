from http import HTTPStatus

from fastapi import HTTPException
from .license_exceptions import LicenseCodeAlreadyExistsException #para a exceção

class AppException(HTTPException):
    def __init__(self, status_code: int, detail: str):
        super().__init__(status_code=status_code, detail=detail)


class UserNotFoundException(AppException):
    def __init__(self):
        super().__init__(HTTPStatus.NOT_FOUND, 'User not found')


class PermissionDeniedException(AppException):
    def __init__(self):
        super().__init__(HTTPStatus.FORBIDDEN, 'Not enough permissions')


class EmailAlreadyExistsException(AppException):
    def __init__(self):
        super().__init__(HTTPStatus.BAD_REQUEST, 'Email already exists')


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


__all__ = [
    'AppException',
    'UserNotFoundException',
    'PermissionDeniedException',
    'EmailAlreadyExistsException',
    'CredentialsException',
    'ExpiredTokenException',
    'InvalidTokenException',
    'LicenseCodeAlreadyExistsException',
]
