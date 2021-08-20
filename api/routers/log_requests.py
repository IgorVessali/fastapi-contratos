import fastapi as _fastapi
import sqlalchemy.orm as _orm
import api.enums as _enums
import api.database as _database

from fastapi import APIRouter, status
from api.services import usuarios as _servicesUser
from api.services import log_request as _services
from api.schemas import log_request as _schemas
from fastapi_pagination import Page, paginate

router = APIRouter(
    tags=['Logs'],
    prefix='/logs'
)

@router.get("/requests", response_model=Page[_schemas.LogRequest])
async def get_all(
    sistema: _enums.LogSistemaPesquisa,
    db: _orm.Session = _fastapi.Depends(_database.get_db),
    user = _fastapi.Depends(_servicesUser.get_current_user),
):
    return paginate(await _services.get_all_logs(sistema, db))