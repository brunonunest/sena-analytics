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
def dailyUsers(rs):
    rawdata = []
    mongodata = []
    try:
        data = json.loads(rs.text)
        print("Request response OK")
    except:
        print("Request response error")
    #loop between klever .json and filter data to rawdata
    for obj in data["data"]["transactions"]:
        try:
            ts1 = obj["timestamp"]/1000
            ts = datetime.datetime.fromtimestamp(ts1).isoformat()
            ts1 = ts.split("T")
            tsf = ts1[0]
            buyType = obj["contract"][0]["parameter"]["buyType"]
            amount = obj["contract"][0]["parameter"]["amount"]
            assetId = obj["contract"][0]["parameter"]["id"]
            user = obj["sender"]
            if buyType == 'MarketBuy' and len(obj["receipts"]) == 3:
                continue
            elif buyType == 'MarketBuy' and len(obj["receipts"]) >= 5:
                assetId = obj["receipts"][-1]["assetId"]
                assetId = assetId.split("/")
                assetId = assetId[0]
            rawdata.append({"assetdate": assetId + "<>" + tsf, "value": amount, "user": user})
            print("Data added to list")
        except:
            print("Invalid or empty data")
    #calculate daily users on data
    df = pd.DataFrame()
    try:
        df = pd.DataFrame(rawdata)
        df = df.groupby(df.assetdate)
        df = df.user.nunique()
        print("Pandas Dataframe created")
        #dfmerge1 = dfmin.merge(dfmax, left_on='assetdate', right_on='assetdate', suffixes=('_min', '_max'))
        #dfmerge2 = dfmerge1.merge(dfmean, left_on='assetdate', right_on='assetdate')
        #print(dfmerge2)
    except:
        print("Pandas Dataframe error")
    #loop dataframe to filter and clean data
    for k, v in df.items():
        try:
            splitdata = k.split("<>")
            mongodata.append({"date": splitdata[1], "count": v, "asset": splitdata[0]})
            print("Data added to flist")
        except:
            print("Error trying to iterate df and adding data to list")
    #add data to mongodb
    print(mongodata)
    try:
        client = pymongo.MongoClient(mongourl)
        db = client.ktestnet
        dailyusers = db["dailyusers"]
        x = dailyusers.insert_many(mongodata)
        print("MongoDB Updated")
        print("--------------")
    except:
        print("Error trying to upload data")
        print("--------------")


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

#check pagination
pages = data["pagination"]["totalPages"]
print(pages)
if pages == 1:
    dailyUsers(rs)
elif pages > 1:
    for index in range(1, pages + 1):
        rs = requests.get(url + "/transaction/list?type=17&status=success&page=" + str(index), headers=headers)
        dailyUsers(rs)
