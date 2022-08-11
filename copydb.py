import pymongo
import requests
import json
import datetime
import pandas as pd
import ssl
from decouple import config

ssl._create_default_https_context = ssl._create_unverified_context

url = "mongodb+srv://senadbnew:112233445566@clusternft.7fhtj.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(url)
#db = client.prod
#floorpricebyday = db["floorpricebyday"]
#db2 = client.dev
#floorpricebyday2 = db2["floorpricebyday"]

client.admin.command('copydb',fromdb='prod',todb='dev',fromhost=url)
