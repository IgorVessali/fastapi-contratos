import datetime as _dt
import pydantic as _pydantic
import api.enums as _enums

class LogRequest(_pydantic.BaseModel):    
    id: int
    data: _dt.datetime
    sistema: _enums.LogSistema
    endpoint: str
    request: str
    response: str
    status_code: str
    
    class Config:
        orm_mode = True

class LogRequestCreate(_pydantic.BaseModel): 
    sistema: _enums.LogSistema
    endpoint: str
    request: str
    response: str
    status_code: str
    
    class Config:
        orm_mode = True