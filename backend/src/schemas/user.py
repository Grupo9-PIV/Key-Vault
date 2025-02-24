from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr

from src.enums import UserRole


class UserSchema(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: UserRole
    department: str


class UserPublic(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: UserRole

    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    role: Optional[UserRole] = None
    department: Optional[str] = None

    class Config:
        extra = "forbid"  # evita campos extras não definidos


class UserList(BaseModel):
    users: list[UserPublic]
