import sqlalchemy.orm as _orm
import api.enums as _enums
import api.models as _models

from api.schemas import log_request as _schemas

async def create_log(values, db: _orm.Session):
    # if status_code == 200:
    #     response = ""
    obj = _models.LogRequests(**values)
    db.add(obj)
    db.commit()
    db.refresh(obj)

async def get_all_logs(sistema: _enums.LogSistemaPesquisa, db: _orm.Session):
    if sistema == _enums.LogSistemaPesquisa.TODOS:
        logs = db.query(_models.LogRequests).all()
    else:
        logs = db.query(_models.LogRequests).filter_by(sistema=sistema.name).all()

    return list(map(_schemas.LogRequest.from_orm, logs))




