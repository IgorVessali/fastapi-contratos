import datetime as _dt
import sqlalchemy as _sql
import api.database as _database
import api.enums as _enums

class Empresa(_database.Base):
    __tablename__ = "empresas"
    
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    status = _sql.Column(_sql.Enum(_enums.Status))
    razao = _sql.Column(_sql.String(50))
    fantasia = _sql.Column(_sql.String(50))
    cnpj = _sql.Column(_sql.String(20), unique=True)
    omie_key = _sql.Column(_sql.String(15))
    omie_secret = _sql.Column(_sql.String(50))
    alq_imposto = _sql.Column(_sql.Numeric(10,2))


class LogRequests(_database.Base):
    __tablename__ = "log_requests"
    
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    data = _sql.Column(_sql.DateTime, default=_dt.datetime.now)
    sistema = _sql.Column(_sql.Enum(_enums.LogSistema))
    endpoint = _sql.Column(_sql.Text)
    request = _sql.Column(_sql.Text)
    response = _sql.Column(_sql.Text)
    status_code = _sql.Column(_sql.String(5))


class OmieCategorias(_database.Base):
    __tablename__ = "omie_categorias"
    
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    empresa_id = _sql.Column(_sql.Integer)
    codigo = _sql.Column(_sql.String(10), unique=True)
    nome = _sql.Column(_sql.String(50))
    nome_omie = _sql.Column(_sql.String(50))
    abreviacao = _sql.Column(_sql.String(3))
    tipo = _sql.Column(_sql.String(1))
    

class OmieCidades(_database.Base):
    __tablename__ = "omie_cidades"
    
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    ccod = _sql.Column(_sql.String(50))
    nome = _sql.Column(_sql.String(50))
    uf = _sql.Column(_sql.String(2))
    ibge = _sql.Column(_sql.Integer)
    siafi = _sql.Column(_sql.Integer)


class OmieEstado(_database.Base):
    __tablename__ = "omie_estados"
    
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    codigo = _sql.Column(_sql.String(2), unique=True)
    descricao = _sql.Column(_sql.String(30))
    sigla = _sql.Column(_sql.String(2), unique=True)
    


class Usuario(_database.Base):
    __tablename__ = "usuarios"
    
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    nome = _sql.Column(_sql.String())
    email = _sql.Column(_sql.String(128), unique=True, index=True)
    password = _sql.Column(_sql.String(128), nullable=False)
    ativo = _sql.Column(_sql.Boolean, default=False)
    created = _sql.Column(_sql.DateTime, default=_dt.datetime)
    updated = _sql.Column(_sql.DateTime, default=_dt.datetime, onupdate=_dt.datetime)