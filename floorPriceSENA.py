from genericpath import exists
import pymongo
import requests
import json
import datetime
import pandas as pd
import ssl
from decouple import config

ssl._create_default_https_context = ssl._create_unverified_context

#step1 get klever api.devnet data and parse .json
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36'}
mongourl = config('MONGO_URL')
url = config('PROXY_PROVIDER')
asset = config('SENA_ASSET_ID')
rs = requests.get(url + "/transaction/list?type=17&asset=" + asset, headers=headers)
data = dict()
try:
    data = json.loads(rs.text)
    print("Request response OK")
except:
    print("Request response error")

#set variables for the lists
rawdata = []
mongodata = []

#loop between klever .json and filter data to mongodata, if response is valid
if len(data) > 1:
    for obj in data["data"]["transactions"]:
        try:
            ts1 = obj["timestamp"]/1000
            ts = datetime.datetime.fromtimestamp(ts1).isoformat()
            ts1 = ts.split("T")
            tsf = ts1[0]
            price = float(obj["contract"][0][ "parameter"]["price"])
            rawdata.append({"price": price, "datetime": tsf}) 
            print("Data added to list")
        except:
            print("Invalid or no Data")
else:
    print("Request returned no data")

#calculate floorprice on data
df = dfmin = pd.DataFrame()
try:
    df = pd.DataFrame(rawdata)
    dfmin = df.groupby(df.datetime).min()
    print("Pandas Dataframe created")
except:
    print("Pandas Dataframe error")

#loop dataframe to filter and clean data
for k, v in dfmin.iterrows():
    try:
        mongodata.append({"floorprice": v["price"], "datetime": k})
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

#floorPrice SENA
#TODO: Alterar busca para contrato de SELL
#! ADC PÁGINAÇÃO EM TODOS OS SCRIPTS
#! SEPARAR POR PASTA OS SCRIPTS DO SENA