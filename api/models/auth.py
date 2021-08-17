import datetime as _dt

import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import passlib.hash as _hash

import api.database as _database


class User(_database.Base):
    __tablename__ = "users"
    
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    email = _sql.Column(_sql.String, unique=True, index=True)
    password = _sql.Column(_sql.String)


    def verify_password(self, password_plain: str):
        return _hash.bcrypt.verify(password_plain, self.password)


# class Lead(_database.Base):
#     __tablename__ = "leads"
#     id = _sql.Column(_sql.Integer, primary_key=True, index=True)
#     owner_id = _sql.Column(_sql.Integer, _sql.ForeignKey("users.id"))
#     first_name = _sql.Column(_sql.String, index=True)
#     last_name = _sql.Column(_sql.String, index=True)
#     email = _sql.Column(_sql.String, index=True)
#     company = _sql.Column(_sql.String, index=True, default="")
#     note = _sql.Column(_sql.String, default="")
#     date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
#     date_last_updated = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)

#     owner = _orm.relationship("User", back_populates="leads")
