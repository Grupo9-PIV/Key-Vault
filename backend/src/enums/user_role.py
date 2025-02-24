from enum import Enum


class UserRole(str, Enum):
    ADMIN = 'admin'
    USER = 'user'
    MANAGER = 'manager'

    def __str__(self):
        return self.value
