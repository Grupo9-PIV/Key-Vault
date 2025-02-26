import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

if os.getenv('ENVIRONMENT') != 'production':
    load_dotenv()


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        extra = 'ignore'
