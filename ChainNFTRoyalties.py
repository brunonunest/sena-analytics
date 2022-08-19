import pymongo
import requests
import json
import datetime
import pandas as pd
import ssl
from decouple import config

ssl._create_default_https_context = ssl._create_unverified_context

#change condition from NFT address to NFT assetId
#remove ASSET= filter and get all data by asset, Also remove env for the ROYALTIES_ADDRESS
#get listdata from klever raw response
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36'}
mongourl = config('MONGO_URL')
url = config('PROXY_PROVIDER')
#asset = config('SENA_ASSET_ID')
address = config('ROYALTIES_ADDRESS')
rs = requests.get(url + "/transaction/list?type=17&status=success", headers=headers)
data = {'data': {'transactions': []}, 'pagination': {'self': 1, 'next': 0, 'previous': 1, 'perPage': 10, 'totalPages': 0, 'totalRecords': 0}, 'error': '', 'code': 'successful'}

try:
    data = json.loads(rs.text)
    print(data)
    print("Request response OK")
except:
    print("Request response error")

#set variables for the lists
rawdata = []
mongodata = []

#loop in data to get royalties
#if len(data) > 1: #TODO: Maior que 0 
for obj in data["data"]["transactions"]:
    try:
        ts1 = obj["timestamp"]/1000
        ts = datetime.datetime.fromtimestamp(ts1).isoformat()
        ts1 = ts.split("T")
        tsf = ts1[0]
        print("Timestamp defined")
    except:
        print("Timestamp not found")
    for obj2 in obj["receipts"]:
        try:
            #Remove or change this condition, we need RY by NFT asset
            if obj2["to"] == address:
                rawdata.append({"value": obj2["value"], "date": tsf})
                print("Data added to list")
        except:
            print("Invalid or no Data")

#start iteration to calculate SENA NFT total ry
df = dfsum = pd.DataFrame()
try:
    df = pd.DataFrame(rawdata)
    dfsum = df.groupby(df.datetime).sum()
    print("Pandas Dataframe created")
except:
    print("Pandas Dataframe error")

#transpose keys to match dict type
try:
    for k, v in dfsum.iterrows():
        mongodata.append({"amount": float(v[0]), "datetime": k})
    print("Data added to flist")
except:
    print("Error trying to iterate df and adding data to list")

#upload data to mongo
try:
    client = pymongo.MongoClient(mongourl)
    db = client.prodmainnet
    senanftrybyday = db["senanftrybyday"]
    x = senanftrybyday.insert_many(mongodata)
    print("MongoDB Updated")
except:
    print("Error trying to upload data")

#TODO: Adicionar págination
#CHECAR ASSET ID DO SENA