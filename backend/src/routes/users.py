from http import HTTPStatus

from fastapi import APIRouter

from src.schemas import UserList, UserPublic, UserSchema, UserUpdate
from src.services import UserService
from src.types import T_CurrentUser, T_Session

router = APIRouter(prefix='/users', tags=['Users'])


@router.post('/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema, session: T_Session):
    return UserService.create_user(session, user)


@router.get('/', status_code=HTTPStatus.OK, response_model=UserList)
def read_users(
    session: T_Session,
    current_user: T_CurrentUser,
    skip: int = 0,
    limit: int = 10,
):
    return {'users': UserService.get_users(session, skip, limit)}


@router.get('/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic)
def read_user(
    user_id: int,
    session: T_Session,
    current_user: T_CurrentUser,
):
    return UserService.get_user(session, user_id)


@router.put('/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic)
def update_user_full(
    user_id: int,
    user_data: UserSchema,
    session: T_Session,
    current_user: T_CurrentUser,
):
    return UserService.update_user(
        session, user_id, user_data, current_user, is_full_update=True
    )


@router.patch(
    '/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def update_user_partial(
    user_id: int,
    user_data: UserUpdate,
    session: T_Session,
    current_user: T_CurrentUser,
):
    return UserService.update_user(session, user_id, user_data, current_user)


@router.delete(
    '/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def delete_user(
    user_id: int,
    session: T_Session,
    current_user: T_CurrentUser,
):
    return UserService.delete_user(session, user_id, current_user)
