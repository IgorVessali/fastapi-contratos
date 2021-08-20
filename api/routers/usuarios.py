import fastapi as _fastapi
import sqlalchemy.orm as _orm
import api.database as _database

from fastapi import APIRouter, status
from api.services import auth as _servicesAuth
from api.services import usuarios as _servicesUser
from api.schemas import usuarios as _schemas
from typing import List


router = APIRouter(
    tags=['Usuários']
)


@router.post("/novo")
async def create_user(
    user: _schemas.UserCreate, db: _orm.Session = _fastapi.Depends(_database.get_db)
):
    db_user = await _servicesUser.get_user_by_email(user.email, db)
    if db_user:
        raise _fastapi.HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                                    detail="Já existe um usuário cadastrado com esse e-mail")

    user = await _servicesUser.create_user(user, db)

    return await _servicesAuth.create_token(user)


@router.get("/usuario-logado", response_model=_schemas.User)
async def get_user(user: _schemas.User = _fastapi.Depends(_servicesUser.get_current_user)):
    return user


@router.get("/usuarios", response_model=List[_schemas.UserList])
async def get_all_users(db: _orm.Session = _fastapi.Depends(_database.get_db),
                        user: _schemas.User = _fastapi.Depends(_servicesUser.get_current_user),
    ):
    return await _servicesUser.get_all_users(db)