import sqlalchemy.orm as _orm
import api.models.enuns.database as _enums

from sqlalchemy.sql.sqltypes import String
from fastapi import status, HTTPException
from api.models import empresas as _models
from api.schemas import empresas as _schemas

async def create_empresa(db: _orm.Session, empresa: _schemas.EmpresaCreate):
    obj = _models.Empresa(**empresa.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return _schemas.Empresa.from_orm(obj)


async def get_all_empresas(status: _enums.StatusPesquisa, db: _orm.Session):
    if status == _enums.StatusPesquisa.Todos:
        empresas = db.query(_models.Empresa).all()
    else:
        empresas = db.query(_models.Empresa).filter_by(status=status).all()

    return list(map(_schemas.Empresa.from_orm, empresas))


async def busca_id(empresa_id: int, db: _orm.Session):
    obj = (db.query(_models.Empresa).get(empresa_id))
    if obj is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Empresa não encontrada.")

    return obj


async def existe_cnpj(cnpj: String, db: _orm.Session):
    obj = (db.query(_models.Empresa).filter_by(cnpj=cnpj).first())
    return obj


async def get_empresa(empresa_id: int, db: _orm.Session):
    obj = await busca_id(empresa_id, db)
    return _schemas.Empresa.from_orm(obj)


async def delete_empresa(empresa_id: int, db: _orm.Session):
    obj = await busca_id(empresa_id, db)
    obj.status = _enums.Status.Inativo 

    db.commit()
    db.refresh(obj)

async def update_empresa(empresa_id: int, empresa: _schemas.EmpresaUpdate, db: _orm.Session):
    obj = await busca_id(empresa_id,  db)

    obj.razao = empresa.razao
    obj.fantasia = empresa.fantasia
    obj.cnpj = empresa.cnpj
    obj.omie_key = empresa.omie_key
    obj.omie_secret = empresa.omie_secret
    obj.alq_imposto = empresa.alq_imposto

    db.commit()
    db.refresh(obj)

    return _schemas.Empresa.from_orm(obj)
