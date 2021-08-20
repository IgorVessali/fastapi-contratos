import requests
import sqlalchemy.orm as _orm
import api.services.log_request as _log
import api.enums as _enums

async def buscaDados(url, data, db: _orm.Session):
	headers = {'Content-type': 'application/json',}
	response = requests.post(url, headers=headers, data=data)
	values = {
		"sistema": _enums.LogSistema.OMIE, 
		"endpoint": url, 
		"request": data, 
		"response": response.content.decode('UTF-8'), 
		"status_code": response.status_code
	}
	await _log.create_log(values, db)
	
	return response