import pymongo
import requests
import json
import datetime
import ssl
from decouple import config

ssl._create_default_https_context = ssl._create_unverified_context

#TIRAR FILTRO ASSET= DA URL, PUXAR TODOS os dados POR ASSET
#step1 get klever api.devnet data and parse .json
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36'}
mongourl = config('MONGO_URL')
url = config('PROXY_PROVIDER')
rs = requests.get(url + "/transaction/list?type=17&status=success&asset=", headers=headers)
data = {'data': {'transactions': []}, 'pagination': {'self': 1, 'next': 0, 'previous': 1, 'perPage': 10, 'totalPages': 0, 'totalRecords': 0}, 'error': '', 'code': 'successful'}

try:
	data = json.loads(rs.text)
	print("Request response OK")
except:
	print("Request response error")

#set variables for the lists
mongodata = []

#loop between klever .json and filter data to mongodata
for obj in data["data"]["transactions"]:
	try:
			ts = datetime.datetime.fromtimestamp(obj["timestamp"]/1000).isoformat()
			ts1 = ts.split("T")
			tsf = ts1[0]
			#talvez fzer um loop aqui em obj["contract"], checar retorno exemplo**
			mongodata.append({"value": obj["contract"][0][ "parameter"]["price"], "date": tsf})
			print("Data added to list")
	except:
		print("Invalid or no Data")

#upload data to mongodb
try:
	client = pymongo.MongoClient(mongourl)
	db = client.testnet
	senanftvolumebyday = db["senanftvolumebyday"]
	x = senanftvolumebyday.insert_many(mongodata)
	print("MongoDB Updated")
except:
	print("Error trying to upload data")

#---------------------
# Daily Traded Volume
# TODO:  Considerar mais de um contrato na transação - pode ter mais de um buy dentro de uma transação! **OK, MAS ISSO SERIA 1 KEY CONTRACT COM +1 OBJETO, OU 2+ KEYS?