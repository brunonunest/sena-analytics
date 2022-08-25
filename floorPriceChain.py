import pymongo
import requests
import json
import datetime
import pandas as pd
import ssl
from decouple import config

ssl._create_default_https_context = ssl._create_unverified_context

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36'}
mongourl = config('MONGO_URL')
url = config('PROXY_PROVIDER')
rs = requests.get(url + "/transaction/list?type=18&status=success", headers=headers)
data = {'data': {'transactions': []}, 'pagination': {'self': 1, 'next': 0, 'previous': 1, 'perPage': 10, 'totalPages': 0, 'totalRecords': 0}, 'error': '', 'code': 'successful'}

try:
    data = json.loads(rs.text)
    print("Request response OK")
except:
    print("Request response error")

#set variables for the lists
rawdata = []
mongodata = []

#loop between klever .json and filter data to mongodata, if response is valid
for obj in data["data"]["transactions"]:
    try:
        ts1 = obj["timestamp"]/1000
        ts = datetime.datetime.fromtimestamp(ts1).isoformat()
        ts1 = ts.split("T")
        tsf = ts1[0]
        assetId = obj["contract"][0]["parameter"]["assetId"].split("/")
        currency = obj["contract"][0]["parameter"]["currencyID"]
        #talvez fzer um loop aqui em obj["contract"], checar retorno exemplo**
        price = float(obj["contract"][0][ "parameter"]["price"])
        rawdata.append({"value": price, "date": tsf, "currency": currency, "asset": assetId[0]}) 
        print("Data added to list")
    except:
        print("Invalid or no Data")

#calculate floorprice on data
df = dfmin = pd.DataFrame()
try:
    df = pd.DataFrame(rawdata)
    dfmin = df.groupby(df.asset).min()
    print("Pandas Dataframe created")
except:
    print("Pandas Dataframe error")

#loop dataframe to filter and clean data
for k, v in dfmin.iterrows():
    try:
        mongodata.append({"value": v["value"], "date": v["date"], "currency": v["currency"], "asset": k})
        print("Data added to flist")
    except:
        print("Error trying to iterate df and adding data to list")

#upload data to mongodb
try:
    client = pymongo.MongoClient(mongourl)
    db = client.prodmainnet
    floorpricebyday = db["floorpricebyday"]
    x = floorpricebyday.insert_many(mongodata)
    print("MongoDB Updated")
except:
	print("Error trying to upload data")
