import pymongo
import requests
import json
import datetime
import pandas as pd
import ssl
from decouple import config

ssl._create_default_https_context = ssl._create_unverified_context

#dados por asset!!!!!!
#add index loop for more than 1 item on contracts
#step1 get klever api.devnet data and parse .json
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36'}
url = config('PROXY_PROVIDER')
mongourl = config('MONGO_URL')
rs = requests.get(url + "/transaction/list?type=17&status=success", headers=headers)
data = {'data': {'transactions': []}, 'pagination': {'self': 1, 'next': 0, 'previous': 1, 'perPage': 10, 'totalPages': 0, 'totalRecords': 0}, 'error': '', 'code': 'successful'}

try:
    data = json.loads(rs.text)
    print("Request response OK")
except:
    print("Request response error")

#set variables for the lists
rawdata = []
mongodata = []

#loop between klever .json and filter data to rawdata
for obj in data["data"]["transactions"]:
    try:
        ts1 = obj["timestamp"]/1000
        ts = datetime.datetime.fromtimestamp(ts1).isoformat()
        ts1 = ts.split("T")
        tsf = ts1[0]
        buyType = obj["contract"][0]["parameter"]["buyType"]
        if buyType == 'MarketBuy' and len(obj["receipts"]) == 3:
            print(len(obj["receipts"]))
            print(obj["contract"][0]["parameter"]["buyType"])
        amount = obj["contract"][0]["parameter"]["amount"]
        assetId = obj["contract"][0]["parameter"]["id"]
        #amount = float(obj["receipts"][1]["value"])
        #assetId = float(obj["receipts"][1]["assetId"])
        currency = obj["contract"][0]["parameter"]["currencyID"]
        #print(currency)
        #print(assetId)
        #print(amount)
        #rawdata.append({"value": amount, "date": tsf})
        print("Data added to list")
    except:
        print("Invalid or empty data")

#calculate total amount for assetbytime and add on mongodata
df = dfsum = pd.DataFrame()
try:
    df = pd.DataFrame(rawdata)
    dfsum = df.groupby(df.date).sum()
    print("Pandas Dataframe created")
except:
    print("Pandas Dataframe error")

#iterate in df to fix keys and add to mongodata
for k, v in dfsum.iterrows():
    try:
        mongodata.append({"value": v[0], "date": k})
        print("Data added to flist")
    except:
        print("Error trying to iterate df and adding data to list")

#add data to mongodb
try:
    client = pymongo.MongoClient(mongourl)
    db = client.prodmainnet
    tradedvolumebyday = db["tradedvolumebyday"]
    #x = tradedvolumebyday.insert_many(mongodata)
    #print("MongoDB Updated")
except:
    print("Error trying to upload data")

#TODO: Adicionar págination