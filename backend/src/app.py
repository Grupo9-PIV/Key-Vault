from http import HTTPStatus

from fastapi import FastAPI

from src.schemas import UserList, UserPublic, UserSchema

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Olá Mundo!'}


@app.post('/users', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    # TODO: implementar criação de users

    new_user = UserPublic(id=1, **user.model_dump())

    return new_user


@app.get('/users', status_code=HTTPStatus.OK, response_model=UserList)
def read_all_user():
    # TODO: implementar retorno de users

    raise NotImplementedError


@app.get(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def read_user(user_Id: int):
    # TODO: implementar retorno de user por id

    raise NotImplementedError


@app.put(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def update_user(user_id: int, user: UserSchema):
    # TODO: implementar update de users

    raise NotImplementedError


@app.delete(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def delete_user(user_id: int):
    # TODO: implementar exclusão de user

    raise NotImplementedError
