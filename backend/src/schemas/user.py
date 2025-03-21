from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr

from src.enums import UserRole
from src.types import PasswordType


class UserSchema(BaseModel):
    name: str
    email: EmailStr
    password: PasswordType
    role: UserRole
    department: str


class UserPublic(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: UserRole
    department: str
    is_active: bool

    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[PasswordType] = None
    role: Optional[UserRole] = None
    department: Optional[str] = None
    is_active: Optional[bool] = None

    class Config:
        extra = 'forbid'  # evita campos extras não definidos


class UserList(BaseModel):
    users: list[UserPublic]
