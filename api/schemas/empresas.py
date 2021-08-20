import pydantic as _pydantic
import decimal as _decimal
from typing import Any
import api.models.enuns.database as _enums

class Empresa(_pydantic.BaseModel):    
    id: int
    status: _enums.Status
    razao: str
    fantasia: str
    cnpj: str
    omie_key: str
    omie_secret: str
    alq_imposto: _decimal.Decimal
    
    class Config:
        orm_mode = True

class EmpresaCreate(_pydantic.BaseModel):
    status: _enums.Status
    razao: str
    fantasia: str
    cnpj: str
    omie_key: str
    omie_secret: str  
    alq_imposto: _decimal.Decimal
    class Config:
        orm_mode = True

class EmpresaUpdate(_pydantic.BaseModel):
    razao: str
    fantasia: str
    cnpj: str
    omie_key: str
    omie_secret: str  
    alq_imposto: _decimal.Decimal
    class Config:
        orm_mode = True

class EmpresaRespSinc(_pydantic.BaseModel):
    msg: str

