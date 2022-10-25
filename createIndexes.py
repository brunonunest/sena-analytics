import pymongo
import ssl
from decouple import config

ssl._create_default_https_context = ssl._create_unverified_context

#Update before creating new database and automate on Heroku
#indexes for mongodb
try:
    mongourl = config('MONGO_URL')
    client = pymongo.MongoClient(mongourl)
    db = client.kmainnet
    #index1 = db.dailyusers.create_index([('datetime', pymongo.DESCENDING)],unique=True)
    #index2 = db.nftprices.create_index([('datetime', pymongo.DESCENDING)],unique=True)
    #index3 = db.nftprices.create_index([('datetime', pymongo.DESCENDING)],unique=True)
    #index4 = db.nftroyalties.create_index([('datetime', pymongo.DESCENDING)],unique=True)
    #index5 = db.nfttransactions.create_index([('datetime', pymongo.DESCENDING)],unique=True)
    #index6 = db.topsales.create_index([('datetime', pymongo.DESCENDING)],unique=True)
    #index7 = db.totaltx24.create_index([('datetime', pymongo.DESCENDING)],unique=True)
    #index8 = db.uniqueholders.create_index([('datetime', pymongo.DESCENDING)],unique=True)
    print("Indexes created/updated")
except:
    print("Error trying to create some indexes, check on MongoDB")
