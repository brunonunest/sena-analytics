import pymongo
import requests
import json
import ssl
from decouple import config

ssl._create_default_https_context = ssl._create_unverified_context

#step1 get klever api.devnet data and parse .json
mongourl = config('MONGO_URL')
url = config('PROXY_PROVIDER')
asset = config('SENA_ASSET_ID')
rs = requests.get(url + "/transaction/list?type=17&asset=" + asset)
data = json.loads(rs.text)

#set variables for the lists
mongodata = []
total = 0

#loop between klever .json and filter data to rawdata
for obj in data:
	for obj2 in obj["contract"]:
		total += obj2["parameter"]["price"]

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
