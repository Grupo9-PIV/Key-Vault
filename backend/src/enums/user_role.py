from enum import Enum


class UserRole(str, Enum):
    ADMIN = 'admin'
    USER = 'user'
    MANAGER = 'manager'

    def __str__(self):   # pragma: no cover
        return self.value
