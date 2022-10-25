import pymongo
import requests
import json
import datetime
import pandas as pd
import ssl
from decouple import config

ssl._create_default_https_context = ssl._create_unverified_context

#set variables for the lists
rawdata = []
mongodata = []

#defining the pipeline as function
def nftRoyalties(rs):
    rawdata = []
    mongodata = []
    try:
        data = json.loads(rs.text)
    except:
        print("Request response error")
    #loop in data to get royalties
    for obj in data["data"]["transactions"]:
        try:
            ts1 = obj["timestamp"]/1000
            ts = datetime.datetime.fromtimestamp(ts1).isoformat()
            ts1 = ts.split("T")
            tsf = ts1[0]
            currency = obj["contract"][0]["parameter"]["currencyID"]
        except:
            print("Timestamp not found")
        if obj["contract"][0]["parameter"]["buyType"] == "MarketBuy" and len(obj["receipts"]) == 3:
            continue
        for obj2 in obj["receipts"]:
            try:
                if obj2["assetId"] != "KLV":
                    rawdata.append({"assetdate": obj2["assetId"] + "<>" + tsf, "value": obj2["value"], "currency": currency})
            except:
                print("Invalid or no Data")
    #start iteration to calculate NFT total ry
    df = dfsum = pd.DataFrame()
    try:
        df = pd.DataFrame(rawdata)
        dfsum = df.groupby(df.assetdate).agg({'value':'sum','currency':'first'})
    except:
        print("Pandas Dataframe error")
    #transpose keys to match dict type
    try:
        for k, v in dfsum.iterrows():
            splitdata = k.split("<>")
            asset = splitdata[0].split("/")
            mongodata.append({"asset": asset[0], "value": float(v[0]), "date": splitdata[1], "currency": v[1]})
    except:
        print("Error trying to iterate df and adding data to list")
    #upload data to mongo
    try:
        client = pymongo.MongoClient(mongourl)
        db = client.ktestnet
        nftrybyday = db["nftrybyday"]
        x = nftrybyday.insert_many(mongodata)
    except:
        print("Error trying to upload data")
        print("--------------")

#step1 get klever api.devnet data and parse .json
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36'}
mongourl = config('MONGO_URL')
url = config('PROXY_PROVIDER')
rs = requests.get(url + "/transaction/list?type=17&status=success", headers=headers)
data = {'data': {'transactions': []}, 'pagination': {'self': 1, 'next': 0, 'previous': 1, 'perPage': 10, 'totalPages': 0, 'totalRecords': 0}, 'error': '', 'code': 'successful'}

try:
    data = json.loads(rs.text)
except:
    print("Request response error")

#check pagination
pages = data["pagination"]["totalPages"]

if pages == 1:
    nftRoyalties(rs)
elif pages > 1:
    for index in range(1, pages + 1):
        rs = requests.get(url + "/transaction/list?type=17&status=success&page=" + str(index), headers=headers)
        nftRoyalties(rs)
