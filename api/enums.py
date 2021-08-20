import enum

class Status(enum.Enum):
    Ativo = 'Ativo'
    Inativo = 'Inativo'
    Suspenso = 'Suspenso'

class StatusPesquisa(enum.Enum):
    Ativo = 'Ativo'
    Inativo = 'Inativo'
    Suspenso = 'Suspenso'
    Todos = 'TODOS'

class LogSistema(enum.Enum):
    OMIE = 'OMIE'
    BITRIX = 'BITRIX'
    MXF = 'MXF'

class LogSistemaPesquisa(enum.Enum):
    OMIE = 'OMIE'
    BITRIX = 'BITRIX'
    MXF = 'MXF'
    TODOS = 'TODOS'