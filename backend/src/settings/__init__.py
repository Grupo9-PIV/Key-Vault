from .settings import Settings

settings = Settings()

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES


__all__ = [
    'settings',
    'ALGORITHM',
    'ACCESS_TOKEN_EXPIRE_MINUTES',
    'SECRET_KEY',
]
