import os
import jwt as _jwt
import sqlalchemy.orm as _orm
import api.models as _models

from fastapi import status
from api.services import usuarios as _services
from api.schemas import usuarios as _schemas

from dotenv import load_dotenv
load_dotenv()
JWT_SECRET = os.getenv("JWT_SECRET")


async def authenticate_user(email: str, password: str, db: _orm.Session):
    user = await _services.get_user_by_email(db=db, email=email)

    if not user:
        return False

    if not _services.verify_password(password):
        return False

    return user


async def create_token(user: _models.Usuario):
    user_obj = _schemas.User.from_orm(user)
    token = _jwt.encode(user_obj.dict(), JWT_SECRET)
    return dict(access_token=token, token_type="bearer")
    
