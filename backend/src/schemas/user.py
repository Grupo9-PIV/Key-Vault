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


class UserList(BaseModel):
    users: list[UserPublic]
