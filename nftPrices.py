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
def averagePrice(rs):
    rawdata = []
    mongodata = []
    try:
        data = json.loads(rs.text)
    except:
        print("Request response error")
    #loop between klever .json and filter data to mongodata, if response is valid
    for obj in data["data"]["transactions"]:
        try:
            ts1 = obj["timestamp"]/1000
            ts = datetime.datetime.fromtimestamp(ts1).isoformat()
            ts1 = ts.split("T")
            tsf = ts1[0]
            assetId = obj["contract"][0]["parameter"]["assetId"].split("/")
            currency = obj["contract"][0]["parameter"]["currencyID"]
            marketType = obj["contract"][0]["parameter"]["marketType"]
            if marketType == "BuyItNowMarket":
                #talvez fzer um loop aqui em obj["contract"], checar retorno exemplo**
                price = float(obj["contract"][0][ "parameter"]["price"])
                rawdata.append({"value": price, "currency": currency, "assetdate": assetId[0] + "<>" + tsf})
            else:
                continue
        except:
            print("Invalid or no Data")
    #calculate floorprice on data
    df, dfmin, dfmax, dfmean = (pd.DataFrame() for i in range(4))
    try:
        df = pd.DataFrame(rawdata)
        dfmin = df.groupby(df.assetdate).min()
        dfmax = df.groupby(df.assetdate).max()
        dfmean = df.groupby(df.assetdate).mean()
        dfmerge1 = dfmin.merge(dfmax, left_on='assetdate', right_on='assetdate', suffixes=('_min', '_max'))
        dfmerge2 = dfmerge1.merge(dfmean, left_on='assetdate', right_on='assetdate')
    except:
        print("Pandas Dataframe error")
    #loop dataframe to filter and clean data
    for k, v in dfmerge2.iterrows():
        try:
            splitdata = k.split("<>")
            mongodata.append({"average": v["value"], "min": v["value_min"], "max": v["value_max"], "date": splitdata[1], "currency": v["currency_max"], "asset": splitdata[0]})
        except:
            print("Error trying to iterate df and adding data to list")
    #upload data to mongodb
    try:
        client = pymongo.MongoClient(mongourl)
        db = client.ktestnet
        pricesbyday = db["pricesbyday"]
        x = pricesbyday.insert_many(mongodata)
    except:
        print("Error trying to upload data")
        print("--------------")

#step1 get klever api.devnet data and parse .json
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36'}
mongourl = config('MONGO_URL')
url = config('PROXY_PROVIDER')
rs = requests.get(url + "/transaction/list?type=18&status=success", headers=headers)
data = {'data': {'transactions': []}, 'pagination': {'self': 1, 'next': 0, 'previous': 1, 'perPage': 10, 'totalPages': 0, 'totalRecords': 0}, 'error': '', 'code': 'successful'}

try:
    data = json.loads(rs.text)
except:
    print("Request response error")

#check pagination
pages = data["pagination"]["totalPages"]

if pages == 1:
    averagePrice(rs)
elif pages > 1:
    for index in range(1, pages + 1):
        rs = requests.get(url + "/transaction/list?type=18&status=success&page=" + str(index), headers=headers)
        averagePrice(rs)
