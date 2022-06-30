import pymongo
import requests
import json
import pandas as pd
import ssl
from decouple import config

ssl._create_default_https_context = ssl._create_unverified_context

#step1 get klever api.devnet data and parse .json
url = config('PROXY_PROVIDER')
mongourl = config('MONGO_URL')
rs = requests.get(url + "/transaction/list?type=17&status=success")
data = json.loads(rs.text)

#set list variables
mongodata = []

#loop in receipts and contract to get data
for obj in data["data"]["transactions"]:
    for obj2 in obj["receipts"]:
        for k, v in obj2.items():
            if k == "assetId":
                if v != "KLV":
                    for obj4 in obj["contract"]:
                        try:
                            mongodata.append({"asset": v, "amount": obj4["parameter"]["amount"]})
                            print("Data added to list")
                        except:
                            print("Invalid or no Data")

# add data to mongodb
try:
    client = pymongo.MongoClient(mongourl)
    db = client.prodmainnet
    nftvolumes = db["nftvolumes"]
    x = nftvolumes.insert_many(mongodata)
    print("MongoDB Updated")
except:
    print("Error trying to upload data")
