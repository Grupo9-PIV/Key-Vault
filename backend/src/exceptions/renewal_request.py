from http import HTTPStatus

from .base import AppException


class RenewalRequestNotFoundException(AppException):
    def __init__(self):
        super().__init__(HTTPStatus.NOT_FOUND, 'Request not found')
