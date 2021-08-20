import json, time
import sqlalchemy.orm as _orm
import api.models as _models
import api.omie.request as _omie

from fastapi import status
from api.schemas import omie_cidades as _schemas

async def get_all_estados(db: _orm.Session):
    cidades = db.query(_models.Cidades).all()
    return list(map(_schemas.CidadeList.from_orm, cidades))


async def verifica_se_existe(uf, db: _orm.Session):
    cidade = (db.query(_models.Cidades).filter_by(sigla=uf).first())
    if cidade:
        return cidade

async def sincronizaCidades():	
	pagina = 1
	updated = 0
	created = 0
	inicio = time.time()
	empresa = buscaEmpresa(1)
	url = 'https://app.omie.com.br/api/v1/geral/cidades/'

	for n in range(1000000000):
		data ='{"call":"PesquisarCidades", \
				"app_key":"%s", \
				"app_secret":"%s", \
				"param":[{"pagina":%s,"registros_por_pagina":100}]}' \
					%(empresa.omie_key, empresa.omie_secret, pagina)

		response = buscaDados(url, data)
		
		if response.status_code == 200:
			dados = json.loads(response.content)
			cidades = dados['lista_cidades']	
			total_paginas = dados['total_de_paginas']

			for cidade in cidades:
				ret = cadastraCidade(cidade)
				if ret == 'C':
					created +=1
				elif ret == 'U':
					updated +=1
			
			pagina +=1
		else:
			fim = time.time()
			return {'status_code': response.status_code,
					'created': 0,
					'updated': 0,
					'total': 0,
					'time': '%.2f seg' % (fim - inicio)}

		if n+1 == total_paginas:
			break

	fim = time.time()
	return {'status_code': response.status_code,
			'status': 'Processo concluído com sucesso!',
			'created': created,
			'updated': updated,
			'total': int(dados['total_de_registros']),
			'time': '%.2f seg' % (fim - inicio)}

async def cadastraEstado(values: dict, db: _orm.Session):
    obj = await verifica_se_existe(values['sigla'], db)
    if obj:
        values['id'] = obj.id
        db.merge(_models.Cidades(**values))
    else:
        db.add(_models.Cidades(**values))
        db.commit()


