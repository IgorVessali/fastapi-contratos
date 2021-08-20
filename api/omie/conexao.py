import requests
# from ..utils import gravaLog

def buscaDados(url, data):
	headers = {'Content-type': 'application/json',}
	response = requests.post(url, headers=headers, data=data)
	# gravaLog('OMIE', data, url, response.content.decode('UTF-8'), response.status_code)
	
	return response