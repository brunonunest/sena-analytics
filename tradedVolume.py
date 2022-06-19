import pymongo
import requests
import json
import datetime
import pandas as pd

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
            ts1 = obj["timestamp"]/1000
            ts = datetime.datetime.fromtimestamp(ts1).isoformat()
            ts1 = ts.split("T")
            tsf = ts1[0]     
            amount = float(obj["contract"][0]["parameter"]["amount"])
            asset = obj["contract"][0]["parameter"]["assetId"].upper()
            rawdata.append({"amount": amount, "assetbytime": asset + " " + tsf})

#calculate total amount for assetbytime and add on mongodata
df = pd.DataFrame(rawdata)
dfsum = df.groupby(df.assetbytime)['amount'].sum()
flist = dfsum.to_dict()
mongodata.append(flist)

#add data to mongodb
client = pymongo.MongoClient("mongodb+srv://senadbnew:11223344@clusternft.7fhtj.mongodb.net/?retryWrites=true&w=majority")
db = client.test
nftvolumebyasset = db["nftvolumebyasset"]
x = nftvolumebyasset.insert_many(mongodata)