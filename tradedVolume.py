import pymongo
import requests
import json
import datetime
import pandas as pd
import ssl
from decouple import config

ssl._create_default_https_context = ssl._create_unverified_context

#step1 get klever api.devnet data and parse .json
url = config('PROXY_PROVIDER')
mongourl = config('MONGO_URL')
rs = requests.get(url + "/transaction/list?type=17&status=success")
data = json.loads(rs.text)

#set variables for the lists
rawdata = []
mongodata = []

#loop between klever .json and filter data to rawdata
for k, v in data.items():
    if k == "data":
        for obj in v["transactions"]:
            try:
                ts1 = obj["timestamp"]/1000
                ts = datetime.datetime.fromtimestamp(ts1).isoformat()
                ts1 = ts.split("T")
                tsf = ts1[0]
                amount = float(obj["receipts"][1]["value"])
                rawdata.append({"amount": amount, "datetime": tsf})
                print("Data added to list")
            except:
                print("Invalid or empty data")

#calculate total amount for assetbytime and add on mongodata
df = pd.DataFrame(rawdata)
dfsum = df.groupby(df.datetime).sum()

#iterate in df to fix keys and add to mongodata
for k, v in dfsum.iterrows():
    try:
        #k2 = k.split(" ")
        mongodata.append({"amount": v[0], "datetime": k})
        print("Data added to flist")
    except:
        print("Error trying to iterate df and adding data to list")

#add data to mongodb
try:
    client = pymongo.MongoClient(mongourl)
    db = client.prod
    tradedvolumebyday = db["tradedvolumebyday"]
    x = tradedvolumebyday.insert_many(mongodata)
    print("MongoDB Updated")
except:
    print("Error trying to upload data")
