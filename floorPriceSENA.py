import pymongo
import requests
import json
import datetime
import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

#rs = requests.get("https://api.testnet.klever.finance/v1.0/transaction/list?type=18&asset=SENA-1QHB")
#data = json.loads(rs.text)

#set variables for the lists
rawdata = []
mongodata = []

listdata = {"data":{"transactions":[{"hash":"50849de5400f6928238cfbc1e6d77b098a10aec0dcd19707aa9460accb09dafb","blockNum":57315,"sender":"klv1pz2qmsd6tuta2dplfk5j8dt5wwapfhdasu78j5e8mlpuvvlf5frsyyfe0r","nonce":5,"data":[""],"timestamp":1656330060000,"kAppFee":10000000,"bandwidthFee":1000000,"status":"success","resultCode":"Ok","version":1,"chainID":"100420","signature":["52e544c0a0e79362a1b54762d0c69c2d759878aec593adfa0c6877444ddf82bc93fed78ce8b7a977707864836ebeb8c06ffa548726ebf24e951f11862509cf02"],"searchOrder":0,"receipts":[{"klv1pz2qmsd6tuta2dplfk5j8dt5wwapfhdasu78j5e8mlpuvvlf5frsyyfe0r":"1","type":19},{"assetId":"SENA-1QHB/3","from":"klv1pz2qmsd6tuta2dplfk5j8dt5wwapfhdasu78j5e8mlpuvvlf5frsyyfe0r","marketplaceId":"bbbb822493fa5a71","orderId":"e32962c63c7c509c","to":"klv1qqqqqqqqqqqqqqqpqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqylllsymmgky","type":14,"value":1},{"marketplaceId":"bbbb822493fa5a71","orderId":"e32962c63c7c509c","type":15}],"contract":[{"type":18,"typeString":"SellContractType","parameter":{"assetId":"SENA-1QHB/3","currencyID":"KLV","endTime":1666618293,"marketType":"BuyItNowMarket","marketplaceID":"bbbb822493fa5a71","price":100,"reservePrice":100}}]},{"hash":"44ce305a2d9e8b3593bdba9da89df20cf204d448efe4749819c7ea40d3a352e6","blockNum":57312,"sender":"klv1pz2qmsd6tuta2dplfk5j8dt5wwapfhdasu78j5e8mlpuvvlf5frsyyfe0r","nonce":4,"data":[""],"timestamp":1656330048000,"kAppFee":10000000,"bandwidthFee":1000000,"status":"success","resultCode":"Ok","version":1,"chainID":"100420","signature":["c47fd317b57ebd0817fb598d65921a0261936cba5d81f04bda6b03ecf3b6985ecafc5e76bca2a5bb1c26ab5e03c5c829b29a76400b9cee57af8ba41c19ee1b0f"],"searchOrder":0,"receipts":[{"klv1pz2qmsd6tuta2dplfk5j8dt5wwapfhdasu78j5e8mlpuvvlf5frsyyfe0r":"1","type":19},{"assetId":"SENA-1QHB/2","from":"klv1pz2qmsd6tuta2dplfk5j8dt5wwapfhdasu78j5e8mlpuvvlf5frsyyfe0r","marketplaceId":"bbbb822493fa5a71","orderId":"29bb194bd676b031","to":"klv1qqqqqqqqqqqqqqqpqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqylllsymmgky","type":14,"value":1},{"marketplaceId":"bbbb822493fa5a71","orderId":"29bb194bd676b031","type":15}],"contract":[{"type":18,"typeString":"SellContractType","parameter":{"assetId":"SENA-1QHB/2","currencyID":"KLV","endTime":1666618293,"marketType":"BuyItNowMarket","marketplaceID":"bbbb822493fa5a71","price":80,"reservePrice":80}}]},{"hash":"37b5060e2dc81dd76aea56237fc419e7df0bda5f7b1954dca53fd8da03050ef6","blockNum":57305,"sender":"klv1pz2qmsd6tuta2dplfk5j8dt5wwapfhdasu78j5e8mlpuvvlf5frsyyfe0r","nonce":3,"data":[""],"timestamp":1656330020000,"kAppFee":10000000,"bandwidthFee":1000000,"status":"success","resultCode":"Ok","version":1,"chainID":"100420","signature":["b93f23d8058679f8d60e0591d50c951d2ac577af25503c0b381abd2ecc3672fbcbd498b199a2ebf34fcd2dee8bf215158c7aeefe6d7782c673ba42b3ca2b020b"],"searchOrder":0,"receipts":[{"klv1pz2qmsd6tuta2dplfk5j8dt5wwapfhdasu78j5e8mlpuvvlf5frsyyfe0r":"1","type":19},{"assetId":"SENA-1QHB/1","from":"klv1pz2qmsd6tuta2dplfk5j8dt5wwapfhdasu78j5e8mlpuvvlf5frsyyfe0r","marketplaceId":"bbbb822493fa5a71","orderId":"153abac656b47470","to":"klv1qqqqqqqqqqqqqqqpqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqylllsymmgky","type":14,"value":1},{"marketplaceId":"bbbb822493fa5a71","orderId":"153abac656b47470","type":15}],"contract":[{"type":18,"typeString":"SellContractType","parameter":{"assetId":"SENA-1QHB/1","currencyID":"KLV","endTime":1666618293,"marketType":"BuyItNowMarket","marketplaceID":"bbbb822493fa5a71","price":50,"reservePrice":50}}]}]},"pagination":{"next":0,"previous":0,"perPage":10,"totalPages":0,"totalRecords":3},"error":"","code":"successful"}

for obj in listdata["data"]["transactions"]:
    try:
        ts1 = obj["timestamp"]/1000
        ts = datetime.datetime.fromtimestamp(ts1).isoformat()
        ts1 = ts.split("T")
        tsf = ts1[0]
        price = float(obj["contract"][0][ "parameter"]["price"])
        rawdata.append({"price": price, "datetime": tsf})
    except:
        pass

#calculate floorprice on data
df = pd.DataFrame(rawdata)
dfmin = df.groupby(df.datetime).min()
for k, v in dfmin.iterrows():
    mongodata.append({"floorprice": v["price"], "datetime": k})



client = pymongo.MongoClient("mongodb+srv://senadbnew:11223344@clusternft.7fhtj.mongodb.net/?retryWrites=true&w=majority")
db = client.prod
#db = client.test
floorpricebyday = db["floorpricebyday"]
#setup index, once only
#index = db.floorpricebyday.create_index([('datetime', pymongo.DESCENDING)],unique=True)
x = floorpricebyday.insert_many(mongodata)
print("MongoDB Updated")
