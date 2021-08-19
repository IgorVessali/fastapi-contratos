import os
import fastapi as _fastapi
import fastapi.security as _security
import sqlalchemy.orm as _orm
import passlib.hash as _hash
import jwt as _jwt

from fastapi import status
from api.models import usuarios as _models
from api.schemas import usuarios as _schemas
import api.database as _database


from dotenv import load_dotenv
load_dotenv()

oauth2schema = _security.OAuth2PasswordBearer(tokenUrl="/auth/token")

JWT_SECRET = os.getenv("JWT_SECRET")


async def get_user_by_email(email: str, db: _orm.Session):
    return db.query(_models.User).filter(_models.User.email == email).first()


async def get_all_users(db: _orm.Session):
    users = db.query(_models.User).all()
    return list(map(_schemas.UserList.from_orm, users))


async def create_user(user: _schemas.UserCreate, db: _orm.Session):
    user_obj = _models.User(
        email=user.email, password=_hash.bcrypt.hash(user.password),
        nome=user.nome, ativo=user.ativo
    )
    try:        
        db.add(user_obj)
        db.commit()
    except:
        db.rollback()
        raise _fastapi.HTTPException(status_code=status.HTTP_304_NOT_MODIFIED, 
                                    detail="Ocorreu um erro ao cadastrar o usuário.")

    db.refresh(user_obj)
    return user_obj


async def authenticate_user(email: str, password: str, db: _orm.Session):
    user = await get_user_by_email(db=db, email=email)

    if not user:
        return False

    if not user.verify_password(password):
        return False

    return user



async def get_current_user(
    db: _orm.Session = _fastapi.Depends(_database.get_db),
    token: str = _fastapi.Depends(oauth2schema),
):
    try:
        payload = _jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        user = db.query(_models.User).get(payload["id"])
    except:
        raise _fastapi.HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="E-mail ou senha inválido."
        )

    return _schemas.User.from_orm(user)