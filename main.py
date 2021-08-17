import fastapi as _fastapi
import sqlalchemy.orm as _orm
from os import path
from typing import List

import api.routers.auth as _auth
import api.routers.users as _users
import api.database as _database


app = _fastapi.FastAPI()


_database.create_database()


app.include_router(_auth.router)
app.include_router(_users.router)

# if __name__ == '__main__':
#     import sys
#     sys.path.append(path.join(path.dirname(__file__), '..'))

# @app.post("/api/leads", response_model=_schemas.Lead)
# async def create_lead(
#     lead: _schemas.LeadCreate,
#     user: _schemas.User = _fastapi.Depends(_services.get_current_user),
#     db: _orm.Session = _fastapi.Depends(_services.get_db),
# ):
#     return await _services.create_lead(user=user, db=db, lead=lead)


# @app.get("/api/leads", response_model=List[_schemas.Lead])
# async def get_leads(
#     user: _schemas.User = _fastapi.Depends(_services.get_current_user),
#     db: _orm.Session = _fastapi.Depends(_services.get_db),
# ):
#     return await _services.get_leads(user=user, db=db)


# @app.get("/api/leads/{lead_id}", status_code=200)
# async def get_lead(
#     lead_id: int,
#     user: _schemas.User = _fastapi.Depends(_services.get_current_user),
#     db: _orm.Session = _fastapi.Depends(_services.get_db),
# ):
#     return await _services.get_lead(lead_id, user, db)


# @app.delete("/api/leads/{lead_id}", status_code=204)
# async def delete_lead(
#     lead_id: int,
#     user: _schemas.User = _fastapi.Depends(_services.get_current_user),
#     db: _orm.Session = _fastapi.Depends(_services.get_db),
# ):
#     await _services.delete_lead(lead_id, user, db)
#     return {"message", "Successfully Deleted"}


# @app.put("/api/leads/{lead_id}", status_code=200)
# async def update_lead(
#     lead_id: int,
#     lead: _schemas.LeadCreate,
#     user: _schemas.User = _fastapi.Depends(_services.get_current_user),
#     db: _orm.Session = _fastapi.Depends(_services.get_db),
# ):
#     await _services.update_lead(lead_id, lead, user, db)
#     return {"message", "Successfully Updated"}


# @app.get("/api")
# async def root():
#     return {"message": "Awesome Leads Manager"}