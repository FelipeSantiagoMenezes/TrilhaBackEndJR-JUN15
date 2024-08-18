from http import HTTPStatus

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.database.database import get_session
from src.models.models import User
from src.models.schemas import (
    Hello,
    ListUsersSchema,
    PublicUserSchema,
    UserSchema,
)

app = FastAPI()


@app.get('/', response_model=Hello)
def hello():
    return {'mensage': 'Hello, world!'}


@app.post(
    '/users/', response_model=PublicUserSchema, status_code=HTTPStatus.OK
)
def create_user(user: UserSchema, session: Session = Depends(get_session)):
    db_user = session.scalar(
        select(User).where(
            (User.username == user.username) | (User.email == user.email)
        )
    )
    if not db_user:
        db_user = User(
            username=user.username, email=user.email, password=user.password
        )
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user

    if db_user.username == user.username:
        raise HTTPException(
            HTTPStatus.BAD_REQUEST, detail='Username already Exists.'
        )
    if db_user.email == user.email:
        raise HTTPException(
            HTTPStatus.BAD_REQUEST, detail='Email already Exists.'
        )


@app.get(
    '/users/{id}', response_model=PublicUserSchema, status_code=HTTPStatus.OK
)
def read_user(id: int, session: Session = Depends(get_session)):
    db_user = session.scalar(select(User).where(User.id == id))
    if not db_user:
        raise HTTPException(HTTPStatus.NOT_FOUND, detail='Not found user.')
    return db_user


@app.get('/users/', response_model=ListUsersSchema, status_code=HTTPStatus.OK)
def read_users(
    skip: int = 0, limit: int = 100, session: Session = Depends(get_session)
):
    users = session.scalars(select(User).limit(limit).offset(skip)).all()
    return {'users': users}


@app.put('/users/{id}', response_model=PublicUserSchema)
def put_user(
    id: int, user: UserSchema, session: Session = Depends(get_session)
):
    db_user = session.scalar(select(User).where(User.id == id))
    if not db_user:
        raise HTTPException(HTTPStatus.NOT_FOUND, detail='Not found user.')

    db_user.username = user.username
    db_user.email = user.email
    db_user.password = user.password
    session.commit()
    session.refresh(db_user)

    return db_user


@app.delete('/users/{id}', response_model=PublicUserSchema)
def delete_user(id: int, session: Session = Depends(get_session)):
    db_user = session.scalar(select(User).where(User.id == id))
    if not db_user:
        raise HTTPException(HTTPStatus.NOT_FOUND, detail='Not found user.')
    session.delete(db_user)
    session.commit()

    return db_user
