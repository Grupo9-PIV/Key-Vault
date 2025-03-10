from http import HTTPStatus

from .base import AppException


class LicenseNotFoundException(AppException):
    def __init__(self):
        super().__init__(HTTPStatus.NOT_FOUND, 'License not found')


class LicenseExpiredException(AppException):
    def __init__(self):
        super().__init__(HTTPStatus.BAD_REQUEST, 'License expired')


class LicensePendingException(AppException):
    def __init__(self):
        super().__init__(HTTPStatus.FORBIDDEN, 'License pending approval')


class LicenseDeactivatedException(AppException):
    def __init__(self):
        super().__init__(HTTPStatus.FORBIDDEN, 'License deactivated')


class LicenseInvalidException(AppException):
    def __init__(self):
        super().__init__(HTTPStatus.BAD_REQUEST, 'License invalid')
