import pymongo
import requests
import json
import time
import datetime
import ssl
from decouple import config

ssl._create_default_https_context = ssl._create_unverified_context

# step1 API ref and dates, code MUST RUN at midnight first second
rawstartdate = str(time.time()).split(".")
startdate = (int(rawstartdate[0]) - 86400)
enddate = (int(rawstartdate[0]) - 1)
url = config('PROXY_PROVIDER')
mongourl = config('MONGO_URL')
furl = url + "/transaction/list?startdate=" + str(startdate) + "000" + "&enddate=" + str(enddate) + "000"
rs = requests.get(furl)
data = json.loads(rs.text)

#set variable for total
total = 0

#loop to get total
for obj in data:
    try:
        total += obj["pagination"]["totalRecords"]
        print("Data added to list")
    except:
        print("Invalid or no Data")

#convert timestamp to date
ts1 = startdate
ts = datetime.datetime.fromtimestamp(ts1).isoformat()
ts1 = ts.split("T")
tsf = ts1[0]

#upload total for transactions count
try:
    client = pymongo.MongoClient(mongourl)
    db = client.prodmainnet
    totaltransactions = db["totaltransactions"]
    x = totaltransactions.insert_one({"total": total, "datetime": tsf})
    print("MongoDB Updated")
except:
    print("Error trying to upload data")
