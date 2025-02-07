from sqlalchemy.orm import registry

table_registry = registry()

__all__ = [
    'table_registry',
]
