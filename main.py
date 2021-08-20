import fastapi as _fastapi
import api.database as _database
import api.routers.auth as _auth
import api.routers.estados as _estados
import api.routers.empresas as _empresas
import api.routers.usuarios as _usuarios

from fastapi_pagination import add_pagination
from fastapi.openapi.utils import get_openapi

app = _fastapi.FastAPI()
_database.create_database()

app.include_router(_auth.router)
app.include_router(_estados.router)
app.include_router(_empresas.router)
app.include_router(_usuarios.router)

add_pagination(app)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Sistema de Contratos.",
        version="1.0",
        description="Sistema de contratos e calculo de comissão da Mix Fiscal.",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://www.mixfiscal.com.br/wp-content/uploads/2021/01/logo-mixfiscal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


# if __name__ == '__main__':
#     import sys
#     sys.path.append(path.join(path.dirname(__file__), '..'))