import pydantic as _pydantic

class EstadoList(_pydantic.BaseModel):    
    id: int
    codigo: str
    descricao: str
    sigla: str
    
    class Config:
        orm_mode = True

class EstadoCreate(_pydantic.BaseModel):
    codigo: str
    descricao: str
    sigla: str

    class Config:
        orm_mode = True

class EstadoRespSinc(_pydantic.BaseModel):
    msg: str
