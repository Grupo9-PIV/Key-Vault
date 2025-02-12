from http import HTTPStatus

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import select

from src.database import get_session
from src.models import User
from src.schemas import UserList, UserPublic, UserSchema

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Olá Mundo!'}


@app.post('/users', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema, session: Session = Depends(get_session)):
    db_user = session.scalar(select(User).where(User.email == user.email))

    if db_user:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Email already exists',
        )

    new_user = User(
        email=user.email,
        password_hash=user.password,
        name=user.name,
        role=user.role,
        department=user.department,
    )

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return new_user


@app.get('/users', status_code=HTTPStatus.OK, response_model=UserList)
def read_users(
        limit: int = 10,
        skip: int = 0,
        session: Session = Depends(get_session)
):
    users = session.scalars(select(User).offset(skip).limit(limit))
    return {'users': users}


@app.get(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def read_user(user_id: int, session: Session = Depends(get_session)):
    user = session.scalar(
        select(User).where(User.id == user_id)
    )

    if not user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='User does not exist in database'
        )

    return user


@app.put(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def update_user(
    user_id: int, user: UserSchema, session: Session = Depends(get_session)
):
    db_user = session.scalar(
        select(User).where(User.id == user_id)
    )

    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='User does not exist in database'
        )

    db_user.email = user.email
    db_user.password_hash = user.password
    db_user.name = user.name
    db_user.role = user.role
    db_user.department = user.department

    session.commit()
    session.refresh(db_user)

    return db_user


@app.delete(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def delete_user(user_id: int, session: Session = Depends(get_session)):
    user = session.scalar(
        select(User).where(User.id == user_id)
    )

    if not user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='User does not exist in database'
        )

    session.delete(user)
    session.commit()

    return user
