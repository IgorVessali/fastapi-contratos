
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
