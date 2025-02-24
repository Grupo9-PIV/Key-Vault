from typing import Union

from sqlalchemy.orm import Session
from sqlalchemy.sql import select

from src.enums import UserRole
from src.exceptions import (
    EmailAlreadyExistsException,
    PermissionDeniedException,
    UserNotFoundException,
)
from src.models import User
from src.schemas import UserSchema, UserUpdate
from src.security import get_password_hash


class UserService:
    @staticmethod
    def create_user(session: Session, user: UserSchema) -> User:
        UserService._validate_email_uniqueness(session, user.email)

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
        user_data: Union[UserSchema, UserUpdate],
        current_user: User,
        is_full_update: bool = False
    ) -> User:
        UserService._validate_permission(user_id, current_user)
        user = UserService._get_user_or_raise(session, user_id)

        dump_args = {} if is_full_update else {"exclude_unset": True}
        update_data = user_data.model_dump(**dump_args)

        if 'email' in update_data:
            UserService._validate_email_uniqueness(
                session=session,
                email=update_data['email'],
                excluded_user_id=user.id
            )

        for field, value in update_data.items():
            if field == 'password':
                user.password_hash = get_password_hash(value)
            else:
                setattr(user, field, value)

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

    # helper functions (DRY)
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

    @staticmethod
    def _validate_email_uniqueness(
        session: Session, email: str, excluded_user_id: int | None = None
    ) -> None:
        query = select(User).where(User.email == email)

        if excluded_user_id is not None:
            query = query.where(User.id != excluded_user_id)

        if session.scalar(query):
            raise EmailAlreadyExistsException()
