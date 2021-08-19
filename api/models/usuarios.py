import datetime as _dt
import sqlalchemy as _sql
import passlib.hash as _hash
import api.database as _database


class User(_database.Base):
    __tablename__ = "users"
    
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    nome = _sql.Column(_sql.String())
    email = _sql.Column(_sql.String(128), unique=True, index=True)
    password = _sql.Column(_sql.String(128), nullable=False)
    ativo = _sql.Column(_sql.Boolean, default=False)
    created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    updated = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow, onupdate=_dt.datetime.utcnow)

    def verify_password(self, password_plain: str):
        return _hash.bcrypt.verify(password_plain, self.password)