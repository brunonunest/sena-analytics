import pymongo
import requests
import json
import datetime
import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

#params = {'q': 'requests+language:python'}

#step1 get klever api.devnet data and parse .json
#rs = requests.get("https://api.devnet.klever.finance/v1.0/transaction/list?type=0")
#rs = requests.get("https://api.testnet.klever.finance/v1.0/transaction/list?type=0", params = {'q': 'requests+language:python'})
#data = json.loads(rs.text)
data = [{
				"hash": "50849de5400f6928238cfbc1e6d77b098a10aec0dcd19707aa9460accb09dafb",
				"blockNum": 57315,
				"sender": "klv1pz2qmsd6tuta2dplfk5j8dt5wwapfhdasu78j5e8mlpuvvlf5frsyyfe0r",
				"nonce": 5,
				"data": [
					""
				],
				"timestamp": 1656330060000,
				"kAppFee": 10000000,
				"bandwidthFee": 1000000,
				"status": "success",
				"resultCode": "Ok",
				"version": 1,
				"chainID": "100420",
				"signature": [
					"52e544c0a0e79362a1b54762d0c69c2d759878aec593adfa0c6877444ddf82bc93fed78ce8b7a977707864836ebeb8c06ffa548726ebf24e951f11862509cf02"
				],
				"searchOrder": 0,
				"receipts": [
					{
						"klv1pz2qmsd6tuta2dplfk5j8dt5wwapfhdasu78j5e8mlpuvvlf5frsyyfe0r": "1",
						"type": 19
					},
					{
						"assetId": "SENA-1QHB/3",
						"from": "klv1pz2qmsd6tuta2dplfk5j8dt5wwapfhdasu78j5e8mlpuvvlf5frsyyfe0r",
						"marketplaceId": "bbbb822493fa5a71",
						"orderId": "e32962c63c7c509c",
						"to": "klv1qqqqqqqqqqqqqqqpqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqylllsymmgky",
						"type": 14,
						"value": 1
					},
					{
						"marketplaceId": "bbbb822493fa5a71",
						"orderId": "e32962c63c7c509c",
						"type": 15
					}
				],
				"contract": [
					{
						"type": 18,
						"typeString": "SellContractType",
						"parameter": {
							"assetId": "SENA-1QHB/3",
							"currencyID": "KLV",
							"endTime": 1666618293,
							"marketType": "BuyItNowMarket",
							"marketplaceID": "bbbb822493fa5a71",
							"price": 100,
							"reservePrice": 100
						}
					}
				]
			}]


#set variables for the lists
mongodata = []

#loop between klever .json and filter data to rawdata
for k, v in data[0]["contract"][0]["parameter"].items():
    if k == "price":
        mongodata.append(v)

#add data to mongodb
client = pymongo.MongoClient("mongodb+srv://senadbnew:11223344@clusternft.7fhtj.mongodb.net/?retryWrites=true&w=majority")
db = client.prod
#db = client.test
senanftvolume = db["senanftvolume"]
x = senanftvolume.insert_one({"senavolume": mongodata[0]})
print("MongoDB Updated")
