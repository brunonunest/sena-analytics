import pymongo
import requests
import json
import datetime
import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

#step1 get klever api.devnet data and parse .json
rs = requests.get("https://api.devnet.klever.finance/v1.0/transaction/list?type=0")
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
                asset = obj["receipts"][1]["assetId"].upper()
                rawdata.append({"amount": amount, "assetbytime": asset + " " + tsf})
            except:
                pass

#calculate total amount for assetbytime and add on mongodata
df = pd.DataFrame(rawdata)
dfsum = df.groupby(df.assetbytime).min()
for k, v in dfsum.iterrows():
    k2 = k.split(" ")
    mongodata.append({"asset": k2[0], "amount": v[0], "datetime": k2[1]})


#add data to mongodb
client = pymongo.MongoClient("mongodb+srv://senadbnew:11223344@clusternft.7fhtj.mongodb.net/?retryWrites=true&w=majority")
db = client.prod
#db = client.test
tradedvolumebyday = db["tradedvolumebyday"]
x = tradedvolumebyday.insert_many(mongodata)
print("MongoDB Updated")
