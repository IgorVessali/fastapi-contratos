import json, time
import sqlalchemy.orm as _orm
import api.models as _models
import api.omie.request as _omie

from fastapi import status
from api.schemas import omie_estados as _schemas

async def get_all_estados(db: _orm.Session):
    estados = db.query(_models.OmieEstado).all()
    return list(map(_schemas.EstadoList.from_orm, estados))


async def verifica_se_existe(uf, db: _orm.Session):
    estado = (db.query(_models.OmieEstado).filter_by(sigla=uf).first())
    if estado:
        return estado

async def sincronizar_estado(db: _orm.Session):
    total_registros = 0
    inicio = time.time()
    emp = db.query(_models.Empresa).get(1)
    url = 'http://app.omie.com.br/api/v1/geral/estados/'

    data ='{"call":"ListarEstados", \
        "app_key":"%s", \
        "app_secret":"%s", \
        "param":[{"filtrar_por_codigo": "", "filtrar_por_descricao": "", "filtrar_por_sigla": ""}]}' \
            %(emp.omie_key, emp.omie_secret)

    response = await _omie.buscaDados(url, data, db)

    if response.status_code == status.HTTP_200_OK:
        dados = json.loads(response.content)
        estados = dados['lista_estados']
        
        for estado in estados:
            values = {
                'sigla':estado['cSigla'],
                'codigo':estado['cCodigo'],
                'descricao':estado['cDescricao'],
            }
            await cadastraEstado(values, db)
            total_registros +=1

        fim = time.time()
        return {'status_code': response.status_code,
                'status': 'Processo concluído com sucesso!',
                'total': total_registros,
                'time': '%.2f seg' % (fim - inicio)}
    else:
        fim = time.time()
        return {'status_code': response.status_code,
                'total': 0,
                'time': '%.2f seg' % (fim - inicio)}
	

async def cadastraEstado(values: dict, db: _orm.Session):
    obj = await verifica_se_existe(values['sigla'], db)
    if obj:
        values['id'] = obj.id
        db.merge(_models.OmieEstado(**values))
    else:
        db.add(_models.OmieEstado(**values))
        db.commit()


