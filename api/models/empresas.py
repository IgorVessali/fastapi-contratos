
import sqlalchemy as _sql
import api.database as _database
import api.models.enuns.database as _enums

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