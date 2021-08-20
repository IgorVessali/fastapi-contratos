import fastapi as _fastapi
import sqlalchemy.orm as _orm
import api.database as _database
import api.models.enuns.database as _enums

from fastapi import APIRouter, status
from api.services import usuarios as _servicesUser
from api.services import empresas as _services
from api.schemas import empresas as _schemas
from fastapi_pagination import Page, paginate

router = APIRouter(
    tags=['Empresas']
)

@router.post("/novo", response_model=_schemas.Empresa)
async def create_empresa(
    empresa: _schemas.EmpresaCreate,
    user = _fastapi.Depends(_servicesUser.get_current_user),
    db: _orm.Session = _fastapi.Depends(_database.get_db),
):
    emp = await _services.existe_cnpj(empresa.cnpj, db)
    if emp:
        raise _fastapi.HTTPException(status_code=status.HTTP_412_PRECONDITION_FAILED, 
                                    detail="Já existe um usuário cadastrado com esse CNPJ.")

    return await _services.create_empresa(db, empresa)


@router.get("/empresas", response_model=Page[_schemas.Empresa])
async def get_empresas(
    status: _enums.StatusPesquisa, 
    user = _fastapi.Depends(_servicesUser.get_current_user),
    db: _orm.Session = _fastapi.Depends(_database.get_db),
):
    return paginate(await _services.get_all_empresas(status, db))


@router.get("/empresa/{empresa_id}", status_code=status.HTTP_200_OK)
async def get_empresa(
    empresa_id: int,
    user = _fastapi.Depends(_servicesUser.get_current_user),
    db: _orm.Session = _fastapi.Depends(_database.get_db),
):
    return await _services.get_empresa(empresa_id, db)


@router.delete("/deletar/{empresa_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_empresa(
    empresa_id: int,
    user = _fastapi.Depends(_servicesUser.get_current_user),
    db: _orm.Session = _fastapi.Depends(_database.get_db),
):
    await _services.delete_empresa(empresa_id, db)
    return {"message", "Objeto deletado com sucesso!"}


@router.put("/atualizar/{empresa_id}", status_code=status.HTTP_200_OK)
async def update_empresa(
    empresa_id: int,
    empresa: _schemas.EmpresaUpdate,
    user = _fastapi.Depends(_servicesUser.get_current_user),
    db: _orm.Session = _fastapi.Depends(_database.get_db),
):
    emp = await _services.existe_cnpj(empresa.cnpj, db)
    if not emp.id == empresa.id:
        raise _fastapi.HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                                    detail="Já existe um usuário cadastrado com esse CNPJ.")

    await _services.update_empresa(empresa_id, empresa, db)
    return {"message", "Objeto atualizado com sucesso!"}