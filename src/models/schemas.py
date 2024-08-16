from pydantic import BaseModel, EmailStr


class UserModel(BaseModel):
    username: str
    email: EmailStr


class User(UserModel):
    password: str


class Tarefa(BaseModel):
    user: User
    description: str


class Hello(BaseModel):
    mensage: str
