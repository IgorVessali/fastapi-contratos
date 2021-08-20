import pydantic as _pydantic

class CidadeList(_pydantic.BaseModel):    
    id: int
    ccod: str
    nome: str
    uf: str
    ibge: int
    siafi: int
    
    class Config:
        orm_mode = True

class CidadeCreate(_pydantic.BaseModel):
    ccod: str
    nome: str
    uf: str
    ibge: int
    siafi: int

    class Config:
        orm_mode = True

class CidadeRespSinc(_pydantic.BaseModel):
    msg: str
