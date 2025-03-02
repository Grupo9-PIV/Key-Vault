from http import HTTPStatus

from fastapi import HTTPException
from .auth import (
    CredentialsException,
    ExpiredTokenException,
    InvalidTokenException,
    WrongEmailOrPasswordException,
)
from .base import AppException
from .users import (
    EmailAlreadyExistsException,
    PermissionDeniedException,
    UserNotFoundException,
)


# Exceção para licença não encontrada
class LicenseNotFoundException(AppException):
    def __init__(self):
        super().__init__(HTTPStatus.NOT_FOUND, 'License not found')


# Exceção para licença expirada
class LicenseExpiredException(AppException):
    def __init__(self):
        super().__init__(HTTPStatus.BAD_REQUEST, 'License expired')


# Exceção para licença pendente
class LicensePendingException(AppException):
    def __init__(self):
        super().__init__(HTTPStatus.FORBIDDEN, 'License pending approval')


# Exceção para licença desativada
class LicenseDeactivatedException(AppException):
    def __init__(self):
        super().__init__(HTTPStatus.FORBIDDEN, 'License deactivated')


# Exceção para licença inválida
class LicenseInvalidException(AppException):
    def __init__(self):
        super().__init__(HTTPStatus.BAD_REQUEST, 'License invalid')


__all__ = [
    'AppException',
    'CredentialsException',
    'ExpiredTokenException',
    'InvalidTokenException',
    'PermissionDeniedException',
    'UserNotFoundException',
    'EmailAlreadyExistsException',
    'WrongEmailOrPasswordException',
    'LicenseNotFoundException',
    'LicenseExpiredException',
    'LicensePendingException',
    'LicenseDeactivatedException',
    'LicenseInvalidException',
]
