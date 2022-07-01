import pymongo
import ssl
from decouple import config

ssl._create_default_https_context = ssl._create_unverified_context

#index for floorprice (datetime unique)
mongourl = config('MONGO_URL')
client = pymongo.MongoClient(mongourl)
db = client.prod
index1 = db.floorpricebyday.create_index([('datetime', pymongo.DESCENDING)],unique=True)
index2 = db.nftvolumes.create_index([('asset', pymongo.ASCENDING)],unique=True)
index3 = db.senanftrybyday.create_index([('datetime', pymongo.DESCENDING)],unique=True)
index4 = db.senanftvolumebyday.create_index([('datetime', pymongo.DESCENDING)],unique=True)
index5 = db.totaltransactions.create_index([('datetime', pymongo.DESCENDING)],unique=True)
index6 = db.tradedvolumebyday.create_index([('datetime', pymongo.DESCENDING)],unique=True)