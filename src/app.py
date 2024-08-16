from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from src.models.schemas import Hello, User, UserModel

app = FastAPI()

# Isto é apenas para simular
# um banco de dados e será removido.

# ------------------------------- #
tarefas = {}
usuarios = {}
# ------------------------------- #


@app.get('/', response_model=Hello)
def hello():
    return {'mensage': 'Hello, world!'}


@app.post('/users/', response_model=UserModel)
def create_user(user: User):
    if user in usuarios.values():
        raise HTTPException(
            HTTPStatus.BAD_REQUEST, detail='Usuario já existente.'
        )
    usuarios[len(usuarios) + 1] = user
    return user


@app.get('/users/{id}', response_model=UserModel)
def read_user(id: int):
    try:
        user = usuarios.get(id)
        return user
    except IndexError:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Usuario inexistente.'
        )


@app.put('/users/{id}')
def put_user(id: int, user: UserModel):
    try:
        usuarios[id] = user
        return user
    except IndexError:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Usuario inexistente.'
        )


@app.delete('/users/{id}', response_model=UserModel)
def delete_user(id: int):
    try:
        user = usuarios.get(id)
        usuarios.pop(id)
        return user
    except IndexError:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Usuario inexistente.'
        )
