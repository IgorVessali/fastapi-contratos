import sqlalchemy as _sql
import api.database as _database

class OmieCategorias(_database.Base):
    __tablename__ = "omie_categorias"
    
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    empresa_id = _sql.Column(_sql.Integer)
    codigo = _sql.Column(_sql.String(10), unique=True)
    nome = _sql.Column(_sql.String(50))
    nome_omie = _sql.Column(_sql.String(50))
    abreviacao = _sql.Column(_sql.String(3))
    tipo = _sql.Column(_sql.String(1))