import pymongo
import requests
import json
from datetime import datetime
import pandas as pd
import ssl
from decouple import config

ssl._create_default_https_context = ssl._create_unverified_context

#CHECK API LIST AND RECHECK CODE
#set variables for the lists
rawdata = []
assetlist = []

rawstartdate = str(datetime.now()).split(" ")[0]

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36'}
url = config('PROXY_PROVIDER')
mongourl = config('MONGO_URL')
rs = requests.get(url + "/assets/kassets", headers=headers)
datalist = {'data': {'transactions': []}, 'pagination': {'self': 1, 'next': 0, 'previous': 1, 'perPage': 10, 'totalPages': 0, 'totalRecords': 0}, 'error': '', 'code': 'successful'}

try:
    datalist = json.loads(rs.text)
except:
    print("Request response error")

#check pagination
pages = datalist["pagination"]["totalPages"]

if pages == 1:
    for obj in datalist["data"]["assets"]:
        assetlist.append(obj["assetId"])
elif pages > 1:
    for index in range(1, pages + 1):
        rs = requests.get(url + "/assets/kassets?page=" + str(index), headers=headers)
        #assetlist.append()
        for obj in datalist["data"]["assets"]:
            assetlist.append(obj["assetId"])

#defining the pipeline as function
def uniqueHolders():
    rawdata = []
    for asset in assetlist:
        rs = requests.get(url + "/assets/holders/" + asset, headers=headers)
        try:
            data = json.loads(rs.text)
        except:
            print("Request response error")
        #loop between klever .json and filter data to rawdata
        try:
            holders = data["pagination"]["totalRecords"]
            rawdata.append({"asset": asset, "amount": holders, "date": rawstartdate})
        except:
            print("Invalid or empty data")
    df = pd.DataFrame(rawdata)
    df = df.drop_duplicates()
    #add data to mongodb
    for k,v in df.iterrows():
        try:
            client = pymongo.MongoClient(mongourl)
            db = client.ktestnet
            uniqueholders = db["uniqueholders"]
            x = uniqueholders.insert_one({"asset": v["asset"], "amount": v["amount"], "date": v["date"]})
        except:
            print("Error trying to upload data")
            print("--------------")

uniqueHolders()