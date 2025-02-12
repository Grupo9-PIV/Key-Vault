from sqlalchemy.orm import Session
from sqlalchemy.sql import select

from src.models import User
from src.schemas import UserSchema
from src.security import get_password_hash


class UserService:
    @staticmethod
    def create_user(session: Session, user: UserSchema) -> User:
        db_user = session.scalar(select(User).where(User.email == user.email))
        if db_user:
            raise ValueError('Email already exists')

        new_user = User(
            email=user.email,
            password_hash=get_password_hash(user.password),
            name=user.name,
            role=user.role,
            department=user.department,
        )
        session.add(new_user)
        session.commit()
        session.refresh(new_user)

        return new_user

    @staticmethod
    def get_users(
        session: Session, skip: int = 0, limit: int = 10
    ) -> list[User]:
        return session.scalars(select(User).offset(skip).limit(limit)).all()

    @staticmethod
    def get_user(session: Session, user_id: int) -> User:
        user = session.scalar(select(User).where(User.id == user_id))

        if not user:
            raise ValueError('User not found')

        return user

    @staticmethod
    def update_user(
        session: Session, user_id: int, user_data: UserSchema
    ) -> User:
        user = session.scalar(select(User).where(User.id == user_id))
        if not user:
            raise ValueError('User not found')

        user.email = user_data.email
        user.password_hash = get_password_hash(user_data.password)
        user.name = user_data.name
        user.role = user_data.role
        user.department = user_data.department

        session.commit()
        session.refresh(user)

        return user

    @staticmethod
    def delete_user(session: Session, user_id: int) -> User:
        user = session.scalar(select(User).where(User.id == user_id))
        if not user:
            raise ValueError('User not found')

        session.delete(user)
        session.commit()

        return user
