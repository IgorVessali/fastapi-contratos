import fastapi as _fastapi
import fastapi.security as _security
import sqlalchemy.orm as _orm

from fastapi import APIRouter, status
from api.services import auth as _services
from api.schemas import usuarios as _schemas
from typing import List
from .. import database as _database


router = APIRouter(
    prefix="/auth",
    tags=['Autenticação']
)

@router.post("/token")
async def generate_token(
    form_data: _security.OAuth2PasswordRequestForm = _fastapi.Depends(),
    db: _orm.Session = _fastapi.Depends(_database.get_db),
):
    user = await _services.authenticate_user(form_data.username, form_data.password, db)

    if not user:
        raise _fastapi.HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuário ou senha inválidos.")

    return await _services.create_token(user)
