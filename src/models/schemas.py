from pydantic import BaseModel, ConfigDict, EmailStr


class PublicUserSchema(BaseModel):
    username: str
    email: EmailStr
    id: int
    model_config = ConfigDict(from_attributes=True)


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str
    model_config = ConfigDict(from_attributes=True)


class ListUsersSchema(BaseModel):
    users: list[PublicUserSchema]
    model_config = ConfigDict(from_attributes=True)


class TarefaSchema(BaseModel):
    user: UserSchema
    description: str


class Hello(BaseModel):
    mensage: str
