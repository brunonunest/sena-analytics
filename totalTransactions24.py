import pymongo
import requests
import json
import time
import datetime
import ssl
from decouple import config

ssl._create_default_https_context = ssl._create_unverified_context

# step1 API ref and dates, code takes 24 hours before run total txs count, run on correct time!
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36'}
rawstartdate = str(time.time()).split(".")
startdate = (int(rawstartdate[0]) - 86400)
enddate = (int(rawstartdate[0]) - 1)
url = config('PROXY_PROVIDER')
mongourl = config('MONGO_URL')
furl = url + "/transaction/list?status=success&startdate=" + str(startdate) + "000" + "&enddate=" + str(enddate) + "000"
rs = requests.get(furl, headers=headers)
data = {'data': {'transactions': []}, 'pagination': {'self': 1, 'next': 0, 'previous': 1, 'perPage': 10, 'totalPages': 0, 'totalRecords': 0}, 'error': '', 'code': 'successful'}

try:
    data = json.loads(rs.text)
except:
    print("Request response error")

#set variable for total
total = 0

#loop to get total
for k, v in data.items():
    try:
        if k == "pagination":
            total = v["totalRecords"]
    except:
        print("Invalid or no Data")

#convert timestamp to date
tsf = 0
try:
    ts1 = startdate
    ts = datetime.datetime.fromtimestamp(ts1).isoformat()
except:
    print("Datetime lib error")

#upload total for transactions count
try:
    client = pymongo.MongoClient(mongourl)
    db = client.ktestnet
    totaltransactions24 = db["totaltransactions24"]
    x = totaltransactions24.insert_one({"value": total, "datetime": ts})
except:
    print("Error trying to upload data")
