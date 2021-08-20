import json, time
import sqlalchemy.orm as _orm
import api.omie.conexao as _omie_conexao


from fastapi import status
from api.models import omie_estados as _models
from api.schemas import omie_estados as _schemas


async def get_all_estados(db: _orm.Session):
    estados = db.query(_models.Estado).all()
    return list(map(_schemas.EstadoList.from_orm, estados))


async def verifica_se_existe(uf, db: _orm.Session):
    estado = (db.query(_models.Estado).filter_by(sigla=uf).first())
    if estado:
        return estado


async def sincronizar_estado(db):
    total_registros = 0
    inicio = time.time()
    # empresa = _database._orm.query(_models.Estado).get()
    url = 'http://app.omie.com.br/api/v1/geral/estados/'

    data ='{"call":"ListarEstados", \
        "app_key":"%s", \
        "app_secret":"%s", \
        "param":[{"filtrar_por_codigo": "", "filtrar_por_descricao": "", "filtrar_por_sigla": ""}]}' \
            %('7029851648', 'c7660d828028b59724f6cb1cfc105804')

    response = _omie_conexao.buscaDados(url,data)

    if response.status_code == status.HTTP_200_OK:
        dados = json.loads(response.content)
        estados = dados['lista_estados']
        
        for estado in estados:
            await cadastraEstado(estado, db)
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
	

async def cadastraEstado(estado, db: _orm.Session):
    values = {
        'sigla':estado['cSigla'],
        'codigo':estado['cCodigo'],
        'descricao':estado['cDescricao'],
    }

    obj = await verifica_se_existe(estado['cSigla'], db)
    if obj:
        obj(**values)
        # obj.sigla = estado['cSigla']
        # obj.codigo = estado['cCodigo']
        # obj.descricao = estado['cDescricao']

        db.commit()
        db.refresh(obj)
    else:
        obj = _models.Estado(**values)
        db.add(obj)
        db.commit()
        db.refresh(obj)


