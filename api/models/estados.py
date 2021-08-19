import sqlalchemy as _sql

import api.database as _database


class UF(_database.Base):
    __tablename__ = "estados"
    
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    codigo = _sql.Column(_sql.String(2), unique=True)
    descricao = _sql.Column(_sql.String(128))
    sigla = _sql.Column(_sql.String(128), unique=True)