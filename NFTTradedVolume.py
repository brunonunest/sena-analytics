import pymongo
import requests
import json
import ssl
from decouple import config

ssl._create_default_https_context = ssl._create_unverified_context

#step1 get klever api.devnet data and parse .json
url = config('PROXY_PROVIDER')
mongourl = config('MONGO_URL')
rs = requests.get(url + "/transaction/list?type=17&status=success")
data = dict()
try:
    data = json.loads(rs.text)
    print("Request response OK")
except:
    print("Request response error")

#set list variables
mongodata = []

#loop in receipts and contract to get data
if len(data) > 1: #TODO: Data tem que ser maior que 0 não 1 (ver em outras partes do código)
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
else:
    print("Request returned no data")

# add data to mongodb
try:
    client = pymongo.MongoClient(mongourl)
    db = client.prodmainnet
    nftvolumes = db["nftvolumes"]
    x = nftvolumes.insert_many(mongodata)
    print("MongoDB Updated")
except:
    print("Error trying to upload data")

#TODO: Adicionar páginação para caso tenha mais páginas 
#TODO: Está somando ou gravando o dado por transação? 
#TODO: Loop ta incorreto, precisa revisar (está buscando contrato dentro do receipt)
#! Verificar se todas as queries são por success transactions
#! Criar teste unitários com JSON estáticos