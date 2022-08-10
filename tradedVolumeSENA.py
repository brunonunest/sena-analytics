import pymongo
import requests
import json
import ssl
from decouple import config

ssl._create_default_https_context = ssl._create_unverified_context

#step1 get klever api.devnet data and parse .json
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36'}
mongourl = config('MONGO_URL')
url = config('PROXY_PROVIDER')
asset = config('SENA_ASSET_ID')
rs = requests.get(url + "/transaction/list?type=17&status=success&asset=" + asset, headers=headers)
data = {'data': {'transactions': []}, 'pagination': {'self': 1, 'next': 0, 'previous': 1, 'perPage': 10, 'totalPages': 0, 'totalRecords': 0}, 'error': '', 'code': 'successful'}
try:
	data = json.loads(rs.text)
	print("Request response OK")
except:
    print("Request response error")

#set variables for the lists
mongodata = []
total = 0

#loop between klever .json and filter data to rawdata
for obj in data["data"]["transactions"]:
	for obj2 in obj["contract"]:
		try:
			total += obj2["parameter"]["price"]
			print("Data added to flist")
		except:
			print("Error trying to iterate df and adding data to list")

#add data to mongodb
try:
	client = pymongo.MongoClient(mongourl)
	db = client.prodmainnet
	senatotalvolume = db["senatotalvolume"]
	senatotalvolume.drop()
	senatotalvolume = db["senatotalvolume"]
	x = senatotalvolume.insert_one({"total": total})
	print("MongoDB Updated")
except:
    print("Error trying to upload data")

#TODO: Adicionar págination