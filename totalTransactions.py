import pymongo
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

listdata = [{"data":{"transactions":[{"hash":"b70be36e790d5d002245d2a072490dfdc9930e08b3b31afd623f3aeb955b0162","blockNum":56455,"sender":"klv1epfu9z52gpsy65y3hs7q5l5t5gfhfk8x2j442cvuhq4ue6xrtecq8tyml7","nonce":159,"timestamp":1656326620000,"kAppFee":500000,"bandwidthFee":1000000,"status":"success","resultCode":"Ok","version":1,"chainID":"100420","signature":["4a17bd76a78c5f5a0c1ab2006ca2023631da76610beb6f9263cee3f018ea6c79878b1cdc2361f0be719fe9cebdb10a311b0f1bb7befeb5892944327fc40f5405"],"searchOrder":0,"receipts":[{"klv1epfu9z52gpsy65y3hs7q5l5t5gfhfk8x2j442cvuhq4ue6xrtecq8tyml7":"1","type":19},{"assetId":"KLV","from":"klv1epfu9z52gpsy65y3hs7q5l5t5gfhfk8x2j442cvuhq4ue6xrtecq8tyml7","to":"klv1w8apl6mkaup6t86ck9ddlcj442jruglj00ey2waf6maj8zcle6tswtl52u","type":0,"value":50000000000}],"contract":[{"type":0,"typeString":"TransferContractType","parameter":{"amount":50000000000,"toAddress":"klv1w8apl6mkaup6t86ck9ddlcj442jruglj00ey2waf6maj8zcle6tswtl52u"}}]},{"hash":"3c2f31d19864f88457bde1b86c15de6088471b3940de7e8e42e2ef4b25f288b5","blockNum":56020,"sender":"klv17jtut9hsgutu0ldlmuvkvzv936n9yn0h50w3j9vl29n2xltmlx8qq2wqfe","nonce":168,"timestamp":1656324880000,"kAppFee":500000,"bandwidthFee":1000000,"status":"success","resultCode":"Ok","version":1,"chainID":"100420","signature":["b2e1c50c715cb6e9071a0147a4fa074847c074b572ba663c6431ec945445a627c78d86050a6d21d651cd437996fcbc18b4608fe5e60fdb53e3e4bdb22b80c90f"],"searchOrder":0,"receipts":[{"klv17jtut9hsgutu0ldlmuvkvzv936n9yn0h50w3j9vl29n2xltmlx8qq2wqfe":"1","type":19},{"assetId":"KLV","from":"klv17jtut9hsgutu0ldlmuvkvzv936n9yn0h50w3j9vl29n2xltmlx8qq2wqfe","to":"klv13zg2ehyvfejrk3y2edw0285sn3j9tlu8r9av7jpu5s9tfy7cns7qn9efx8","type":0,"value":50000000000}],"contract":[{"type":0,"typeString":"TransferContractType","parameter":{"amount":50000000000,"toAddress":"klv13zg2ehyvfejrk3y2edw0285sn3j9tlu8r9av7jpu5s9tfy7cns7qn9efx8"}}]},{"hash":"60fd2686e4400a5d1c32309eec0b8131266df4b4b761dce88d761687e8897753","blockNum":55941,"sender":"klv17jtut9hsgutu0ldlmuvkvzv936n9yn0h50w3j9vl29n2xltmlx8qq2wqfe","nonce":167,"timestamp":1656324564000,"kAppFee":500000,"bandwidthFee":1000000,"status":"success","resultCode":"Ok","version":1,"chainID":"100420","signature":["f3b05b2c91d09540c4d7fe55645775ec77f907fa500cc1a367e1ec845ac2e5c8afa6532290fd20c59c64dcdc54c379073ab103dfbfd739016b9b6e9d389ced0c"],"searchOrder":0,"receipts":[{"klv17jtut9hsgutu0ldlmuvkvzv936n9yn0h50w3j9vl29n2xltmlx8qq2wqfe":"1","type":19},{"assetId":"KLV","from":"klv17jtut9hsgutu0ldlmuvkvzv936n9yn0h50w3j9vl29n2xltmlx8qq2wqfe","to":"klv1w4jzh8srfpku46l58hmf50du73mcdgr0kprq7zdunzn3g98k00rswmyvem","type":0,"value":50000000000}],"contract":[{"type":0,"typeString":"TransferContractType","parameter":{"amount":50000000000,"toAddress":"klv1w4jzh8srfpku46l58hmf50du73mcdgr0kprq7zdunzn3g98k00rswmyvem"}}]},{"hash":"5d5f9bb868b53e27d5b468e2b65f13bde5628a02f61d8438c6f996f88935fd68","blockNum":55262,"sender":"klv17jtut9hsgutu0ldlmuvkvzv936n9yn0h50w3j9vl29n2xltmlx8qq2wqfe","nonce":166,"timestamp":1656321848000,"kAppFee":500000,"bandwidthFee":1000000,"status":"success","resultCode":"Ok","version":1,"chainID":"100420","signature":["46b9c38b7692a33774dee6b73ba6595918b245b9374fee5eb7056af4dc247828cc4ceecad4fb8a1944b0bd156372b13655b7b889fe2e28539abe607229abd30e"],"searchOrder":0,"receipts":[{"klv17jtut9hsgutu0ldlmuvkvzv936n9yn0h50w3j9vl29n2xltmlx8qq2wqfe":"1","type":19},{"assetId":"KLV","from":"klv17jtut9hsgutu0ldlmuvkvzv936n9yn0h50w3j9vl29n2xltmlx8qq2wqfe","to":"klv13q8st4etj8ell69xa4j7z5rq62acg6txa7plhj4fllfnds6kvmmsczs6nw","type":0,"value":50000000000}],"contract":[{"type":0,"typeString":"TransferContractType","parameter":{"amount":50000000000,"toAddress":"klv13q8st4etj8ell69xa4j7z5rq62acg6txa7plhj4fllfnds6kvmmsczs6nw"}}]},{"hash":"b248d8e7addabc145c4ffdf704bb937794d695ad5bae1593a407acdb060847af","blockNum":55186,"sender":"klv1epfu9z52gpsy65y3hs7q5l5t5gfhfk8x2j442cvuhq4ue6xrtecq8tyml7","nonce":158,"timestamp":1656321544000,"kAppFee":500000,"bandwidthFee":1000000,"status":"success","resultCode":"Ok","version":1,"chainID":"100420","signature":["b205f480329d27fcf16388fa01e736ad18f0404c3e00ef14f02e2138f34eef218d5cfe1bcecc1f517662631ff7d233d57f580a72f206420cf285b0933a11b109"],"searchOrder":0,"receipts":[{"klv1epfu9z52gpsy65y3hs7q5l5t5gfhfk8x2j442cvuhq4ue6xrtecq8tyml7":"1","type":19},{"assetId":"KLV","from":"klv1epfu9z52gpsy65y3hs7q5l5t5gfhfk8x2j442cvuhq4ue6xrtecq8tyml7","to":"klv1fh4ay8extgg4latea3q0r6369rrvzkpyd03tatvyqqzqhzl623rsfv3u0m","type":0,"value":50000000000}],"contract":[{"type":0,"typeString":"TransferContractType","parameter":{"amount":50000000000,"toAddress":"klv1fh4ay8extgg4latea3q0r6369rrvzkpyd03tatvyqqzqhzl623rsfv3u0m"}}]},{"hash":"e8b9582bc3959501e430cd8f198ba1253e9d25187db3bf4594176cb54f5fbe00","blockNum":55156,"sender":"klv17jtut9hsgutu0ldlmuvkvzv936n9yn0h50w3j9vl29n2xltmlx8qq2wqfe","nonce":165,"timestamp":1656321424000,"kAppFee":500000,"bandwidthFee":1000000,"status":"success","resultCode":"Ok","version":1,"chainID":"100420","signature":["960c8919d24adafa4017e253ebc43ea97d2f294e39c72535a56fb224c2e5d9e0c368e652fd1102b0a6636bee407cb958a00044e2290d009347786d780eb8640f"],"searchOrder":0,"receipts":[{"klv17jtut9hsgutu0ldlmuvkvzv936n9yn0h50w3j9vl29n2xltmlx8qq2wqfe":"1","type":19},{"assetId":"KLV","from":"klv17jtut9hsgutu0ldlmuvkvzv936n9yn0h50w3j9vl29n2xltmlx8qq2wqfe","to":"klv1a0sn8068u97t2pg7a97rqcwnjp59fj4x3xtxl94xm2pszrgvtahqqx38cz","type":0,"value":50000000000}],"contract":[{"type":0,"typeString":"TransferContractType","parameter":{"amount":50000000000,"toAddress":"klv1a0sn8068u97t2pg7a97rqcwnjp59fj4x3xtxl94xm2pszrgvtahqqx38cz"}}]},{"hash":"df78567ca76e40a3c0fa2d5611c930c5c5beaba875d33443f97a4ce120eec5cf","blockNum":54963,"sender":"klv1epfu9z52gpsy65y3hs7q5l5t5gfhfk8x2j442cvuhq4ue6xrtecq8tyml7","nonce":157,"timestamp":1656320652000,"kAppFee":500000,"bandwidthFee":1000000,"status":"success","resultCode":"Ok","version":1,"chainID":"100420","signature":["9965750fcfb75d11ed5c28bccc9dc476c95fa449d250a78f3cb69b12aa071f72d3d1361b4bdc565d471b18494cc38bfb537e9073862eed1bf9e869db7eadf809"],"searchOrder":0,"receipts":[{"klv1epfu9z52gpsy65y3hs7q5l5t5gfhfk8x2j442cvuhq4ue6xrtecq8tyml7":"1","type":19},{"assetId":"KLV","from":"klv1epfu9z52gpsy65y3hs7q5l5t5gfhfk8x2j442cvuhq4ue6xrtecq8tyml7","to":"klv18t62e7fvustuw7rzaj2098l0fjufl24ef29gwpd0axc5le5shj4qnhxg3x","type":0,"value":50000000000}],"contract":[{"type":0,"typeString":"TransferContractType","parameter":{"amount":50000000000,"toAddress":"klv18t62e7fvustuw7rzaj2098l0fjufl24ef29gwpd0axc5le5shj4qnhxg3x"}}]},{"hash":"981b6777bb8dbb0faf173dfc794a090bed62df1076f50ecbc1c6a067c123573f","blockNum":54844,"sender":"klv1pz2qmsd6tuta2dplfk5j8dt5wwapfhdasu78j5e8mlpuvvlf5frsyyfe0r","nonce":2,"data":[""],"timestamp":1656320176000,"kAppFee":2000000,"bandwidthFee":1000000,"status":"success","resultCode":"Ok","version":1,"chainID":"100420","signature":["1222690754776a757d1be432ff3e875913eb6af007f38a696f0821ff5da2b9fb56c5270e83b6f500f8f288934888cffaf14974cc51cc1292e8a0e9f7972d9209"],"searchOrder":0,"receipts":[{"klv1pz2qmsd6tuta2dplfk5j8dt5wwapfhdasu78j5e8mlpuvvlf5frsyyfe0r":"1","type":19},{"assetId":"SENA-1QHB","type":2},{"assetId":"SENA-1QHB/3","from":"klv1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqpgm89z","to":"klv1pz2qmsd6tuta2dplfk5j8dt5wwapfhdasu78j5e8mlpuvvlf5frsyyfe0r","type":0,"value":1}],"contract":[{"type":11,"typeString":"AssetTriggerContractType","parameter":{"amount":1,"assetId":"SENA-1QHB","logo":"","toAddress":"klv1pz2qmsd6tuta2dplfk5j8dt5wwapfhdasu78j5e8mlpuvvlf5frsyyfe0r","triggerType":"Mint","uris":"null"}}]},{"hash":"a776a1053ea5047d53c5bd151753f4c9f108f23037c4a0d368f6e5417635972a","blockNum":54843,"sender":"klv1pz2qmsd6tuta2dplfk5j8dt5wwapfhdasu78j5e8mlpuvvlf5frsyyfe0r","nonce":1,"data":[""],"timestamp":1656320172000,"kAppFee":2000000,"bandwidthFee":1000000,"status":"success","resultCode":"Ok","version":1,"chainID":"100420","signature":["fd1a1c2bc4628cc98e5468fd5264f2473f43a1dfbf5126b382f72f33449e27347fca2ccf4a1fcd78014b522df5617da70f2518c8a350c8cae763593f3dc7940b"],"searchOrder":0,"receipts":[{"klv1pz2qmsd6tuta2dplfk5j8dt5wwapfhdasu78j5e8mlpuvvlf5frsyyfe0r":"1","type":19},{"assetId":"SENA-1QHB","type":2},{"assetId":"SENA-1QHB/2","from":"klv1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqpgm89z","to":"klv1pz2qmsd6tuta2dplfk5j8dt5wwapfhdasu78j5e8mlpuvvlf5frsyyfe0r","type":0,"value":1}],"contract":[{"type":11,"typeString":"AssetTriggerContractType","parameter":{"amount":1,"assetId":"SENA-1QHB","logo":"","toAddress":"klv1pz2qmsd6tuta2dplfk5j8dt5wwapfhdasu78j5e8mlpuvvlf5frsyyfe0r","triggerType":"Mint","uris":"null"}}]},{"hash":"bdd1dcd446ccab0c44f760882fed3d1d0dd369975786b1f96d69b4f88e34ff0b","blockNum":54835,"sender":"klv1pz2qmsd6tuta2dplfk5j8dt5wwapfhdasu78j5e8mlpuvvlf5frsyyfe0r","nonce":0,"data":[""],"timestamp":1656320140000,"kAppFee":2000000,"bandwidthFee":1000000,"status":"success","resultCode":"Ok","version":1,"chainID":"100420","signature":["24d4ad02a0fcd5087d6ae709e7b40c3b8a7d19f6cfd74d112597ad313773cef64bf5ca197bfa22f69cefb8ce9bcdabac18b077599e7491ea669abab3db8e3509"],"searchOrder":0,"receipts":[{"klv1pz2qmsd6tuta2dplfk5j8dt5wwapfhdasu78j5e8mlpuvvlf5frsyyfe0r":"1","type":19},{"assetId":"SENA-1QHB","type":2},{"assetId":"SENA-1QHB/1","from":"klv1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqpgm89z","to":"klv1pz2qmsd6tuta2dplfk5j8dt5wwapfhdasu78j5e8mlpuvvlf5frsyyfe0r","type":0,"value":1}],"contract":[{"type":11,"typeString":"AssetTriggerContractType","parameter":{"amount":1,"assetId":"SENA-1QHB","logo":"","toAddress":"klv1pz2qmsd6tuta2dplfk5j8dt5wwapfhdasu78j5e8mlpuvvlf5frsyyfe0r","triggerType":"Mint","uris":"null"}}]}]},"pagination":{"next":1,"previous":0,"perPage":10,"totalPages":48,"totalRecords":486},"error":"","code":"successful"}]
#get listdata data from https://api.testnet.klever.finance/v1.0/transaction/list?startdate=1651287651000&enddate=1659287651000
total = 0
datatopd = []
for obj in listdata:
    total += obj["pagination"]["totalRecords"]

#upload total for transactions count
client = pymongo.MongoClient("mongodb+srv://senadbnew:11223344@clusternft.7fhtj.mongodb.net/?retryWrites=true&w=majority")
db = client.prod
#db = client.test
totaltransactions = db["totaltransactions"]
x = totaltransactions.insert_one({"total": total})
print("MongoDB Updated")