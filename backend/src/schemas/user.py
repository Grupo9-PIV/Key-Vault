from enum import Enum

from pydantic import BaseModel, EmailStr


class UserRole(str, Enum):
    admin = 'admin'
    user = 'user'
    manager = 'manager'


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


class UserList(BaseModel):
    users: list[UserPublic]
