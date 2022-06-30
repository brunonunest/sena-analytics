import pymongo
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

#index for floorprice (datetime unique)
client = pymongo.MongoClient("mongodb+srv://senadbnew:11223344@clusternft.7fhtj.mongodb.net/?retryWrites=true&w=majority")
db = client.prod
index = db.floorpricebyday.create_index([('datetime', pymongo.DESCENDING)],unique=True)