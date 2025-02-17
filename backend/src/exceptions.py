from http import HTTPStatus

from fastapi import HTTPException


class AppException(HTTPException):
    def __init__(self, status_code: int, detail: str):
        super().__init__(status_code=status_code, detail=detail)


class UserNotFoundException(AppException):
    def __init__(self):
        super().__init__(HTTPStatus.NOT_FOUND, 'User not found')


class PermissionDeniedException(AppException):
    def __init__(self):
        super().__init__(HTTPStatus.FORBIDDEN, 'Not enough permission')


class EmailAlreadyExistsException(AppException):
    def __init__(self):
        super().__init__(HTTPStatus.BAD_REQUEST, 'Email already exists')


class CredentialsException(AppException):
    def __init__(self):
        super().__init__(
            HTTPStatus.UNAUTHORIZED, 'Could not validate credentials'
        )
        self.headers = {'WWW-Authenticate': 'Bearer'}
