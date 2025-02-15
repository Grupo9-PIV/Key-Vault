from http import HTTPStatus

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from src.database import get_session
from src.schemas import UserList, UserPublic, UserSchema
from src.services import UserService

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Olá Mundo!'}


@app.post('/users', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema, session: Session = Depends(get_session)):
    try:
        new_user = UserService.create_user(session, user)
        return new_user
    except ValueError as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))


@app.get('/users', status_code=HTTPStatus.OK, response_model=UserList)
def read_users(
    limit: int = 10, skip: int = 0, session: Session = Depends(get_session)
):
    users = UserService.get_users(session, skip, limit)

    return {'users': users}


@app.get(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def read_user(user_id: int, session: Session = Depends(get_session)):
    try:
        user = UserService.get_user(session, user_id)
        return user
    except ValueError as e:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=str(e))


@app.put(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def update_user(
    user_id: int, user: UserSchema, session: Session = Depends(get_session)
):
    try:
        updated_user = UserService.update_user(session, user_id, user)
        return updated_user
    except ValueError as e:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=str(e))


@app.delete(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def delete_user(user_id: int, session: Session = Depends(get_session)):
    try:
        deleted_user = UserService.delete_user(session, user_id)
        return deleted_user
    except ValueError as e:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=str(e))
