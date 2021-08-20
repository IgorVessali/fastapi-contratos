import fastapi as _fastapi
import sqlalchemy.orm as _orm
import api.database as _database

from fastapi import APIRouter, status
from api.services import auth as _servicesAuth
from api.services import usuarios as _servicesUser
from api.schemas import usuarios as _schemas
from fastapi_pagination import Page, paginate
from typing import List


router = APIRouter(
    tags=['Usuários'],
    prefix='/usuarios'
)


@router.post("/novo")
async def create(
    user: _schemas.UserCreate, db: _orm.Session = _fastapi.Depends(_database.get_db)
):
    db_user = await _servicesUser.get_user_by_email(user.email, db)
    if db_user:
        raise _fastapi.HTTPException(status_code=400, detail="Email already in use")

    user = await _servicesUser.create_user(user, db)

    return await _servicesAuth.create_token(user)


@router.get("/logado", response_model=_schemas.User)
async def get(user: _schemas.User = _fastapi.Depends(_servicesUser.get_current_user)):
    return user


@router.get("/todos", response_model=Page[_schemas.UserList])
async def get_all(db: _orm.Session = _fastapi.Depends(_database.get_db),
                user: _schemas.User = _fastapi.Depends(_servicesUser.get_current_user),
    ):
    return paginate(await _servicesUser.get_all_users(db))