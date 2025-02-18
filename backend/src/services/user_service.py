from sqlalchemy.orm import Session
from sqlalchemy.sql import select

from src.enums import UserRole
from src.exceptions import (
    EmailAlreadyExistsException,
    PermissionDeniedException,
    UserNotFoundException,
)
from src.models import User
from src.schemas import UserSchema
from src.security import get_password_hash


class UserService:
    @staticmethod
    def create_user(session: Session, user: UserSchema) -> User:
        if session.scalar(select(User).where(User.email == user.email)):
            raise EmailAlreadyExistsException()

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
        return UserService._get_user_or_raise(session, user_id)

    @staticmethod
    def update_user(
        session: Session,
        user_id: int,
        user_data: UserSchema,
        current_user: User,
    ) -> User:
        UserService._validate_permission(user_id, current_user)
        user = UserService._get_user_or_raise(session, user_id)

        user.email = user_data.email
        user.password_hash = get_password_hash(user_data.password)
        user.name = user_data.name
        user.role = user_data.role
        user.department = user_data.department

        session.commit()
        session.refresh(user)

        return user

    @staticmethod
    def delete_user(
        session: Session, user_id: int, current_user: User
    ) -> User:
        UserService._validate_permission(user_id, current_user)
        user = UserService._get_user_or_raise(session, user_id)

        session.delete(user)
        session.commit()

        return user

    @staticmethod
    def _get_user_or_raise(session: Session, user_id: int) -> User:
        user = session.scalar(select(User).where(User.id == user_id))
        if not user:
            raise UserNotFoundException()
        return user

    @staticmethod
    def _validate_permission(user_id: int, current_user: User) -> None:
        if current_user.id != user_id and current_user.role != UserRole.ADMIN:
            raise PermissionDeniedException()
