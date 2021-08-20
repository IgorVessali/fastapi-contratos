import datetime as _dt
from pydantic import BaseModel

class UserCreate(BaseModel):
    nome: str
    email: str
    ativo: bool
    email: str
    password: str

    class Config:
        orm_mode = True

class User(BaseModel):
    id: int
    nome: str
    email: str
    ativo: bool
    email: str

    class Config:
        orm_mode = True

class UserList(BaseModel):
    id: int
    nome: str
    email: str
    ativo: bool
    email: str
    created: _dt.datetime
    updated: _dt.datetime

    class Config:
        orm_mode = True