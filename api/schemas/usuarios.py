import datetime as _dt
import pydantic as _pydantic

class _UserBase(_pydantic.BaseModel):    
    nome: str
    email: str
    ativo: bool
    email: str


class UserCreate(_UserBase):
    password: str

    class Config:
        orm_mode = True


class User(_UserBase):
    id: int

    class Config:
        orm_mode = True

class UserList(_UserBase):
    id: int
    created: _dt.datetime
    updated: _dt.datetime

    class Config:
        orm_mode = True