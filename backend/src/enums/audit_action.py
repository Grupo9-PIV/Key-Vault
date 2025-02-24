from enum import Enum


class AuditAction(str, Enum):
    CREATE = 'create'
    UPDATE = 'update'
    DELETE = 'delete'

    def __str__(self):   # pragma: no cover
        return self.value
