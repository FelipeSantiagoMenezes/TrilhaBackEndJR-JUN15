from pydantic import BaseModel, EmailStr


class BaseUserSchema(BaseModel):
    username: str
    email: EmailStr


class UserSchema(BaseUserSchema):
    password: str


class TarefaSchema(BaseModel):
    user: UserSchema
    description: str


class Hello(BaseModel):
    mensage: str
