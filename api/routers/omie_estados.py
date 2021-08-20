import fastapi as _fastapi
import sqlalchemy.orm as _orm
import api.database as _database

from fastapi import APIRouter, status
from api.services import usuarios as _servicesUser
from api.services import omie_estados as _servicesEstado
from api.schemas import omie_estados as _schemas
from fastapi_pagination import Page, paginate

router = APIRouter(
    tags=['Estados'],
    prefix='/estados'
)

@router.get("/todos", response_model=Page[_schemas.EstadoList])
async def get_all(db: _orm.Session = _fastapi.Depends(_database.get_db),
                user = _fastapi.Depends(_servicesUser.get_current_user),
    ):
    return paginate(await _servicesEstado.get_all_estados(db))

@router.get("/sincroniar")
async def sincronize(db: _orm.Session = _fastapi.Depends(_database.get_db),
                    user = _fastapi.Depends(_servicesUser.get_current_user),
    ):
    return await _servicesEstado.sincronizar_estado(db)