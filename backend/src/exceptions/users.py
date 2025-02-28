from http import HTTPStatus

from .base import AppException


class UserNotFoundException(AppException):
    def __init__(self):
        super().__init__(HTTPStatus.NOT_FOUND, 'User not found')


class PermissionDeniedException(AppException):
    def __init__(self):
        super().__init__(HTTPStatus.FORBIDDEN, 'Not enough permissions')


class EmailAlreadyExistsException(AppException):
    def __init__(self):
        super().__init__(HTTPStatus.BAD_REQUEST, 'Email already exists')
