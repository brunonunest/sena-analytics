import pymongo
import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#get listdata from klever raw response
senaddress = 'klv17e8zzgn73h6ehe3c6q9vlt77kuxk5euddmhymy5uhv2rhv0dc0nqlfp0ap'
listdata = [
    {
        "hash": "4b6aa4a5b95d08146f800d3879ebffa32a846ad91ef027afb8a4b03eb625c6a7",
        "blockNum": 71,
        "sender": "klv122hvtd77uvqlsanmq3dcfpwtmjhm7j0yreygff20scycw0dx3dpsn2mkat",
        "nonce": 0,
        "timestamp": 1655831553000,
        "kAppFee": 1000000,
        "bandwidthFee": 1000000,
        "status": "success",
        "resultCode": "Ok",
        "version": 1,
        "chainID": "420420",
        "signature": [
            "2cf51b6e15e6ea8a2ac799295d778d8e6e4d94086c233e336edc75d56326e5f9dcc78aac35856a3fb8412cd9a45471dcce4d4fa741740cfffcadf0fa0083b40f"
        ],
        "searchOrder": 0,
        "receipts": [
            {
                "klv122hvtd77uvqlsanmq3dcfpwtmjhm7j0yreygff20scycw0dx3dpsn2mkat": "1",
                "type": 19
            },
            {
                "assetId": "KLV",
                "from": "klv122hvtd77uvqlsanmq3dcfpwtmjhm7j0yreygff20scycw0dx3dpsn2mkat",
                "marketplaceId": "491c84d66327c54a",
                "orderId": "14b0e70d7cf3fec7",
                "to": "klv1qqqqqqqqqqqqqqqpqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqylllsymmgky",
                "type": 14,
                "value": 1000
            },
            {
                "assetId": "KLV",
                "from": "klv1qqqqqqqqqqqqqqqpqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqylllsymmgky",
                "marketplaceId": "491c84d66327c54a",
                "orderId": "14b0e70d7cf3fec7",
                "to": "klv1pkvnm3sjwklm2q95knfs0sgxa9ufy8u0fflqma83stjpg5fude4qn75suu",
                "type": 14,
                "value": 10
            },
            {
                "assetId": "KLV",
                "from": "klv1qqqqqqqqqqqqqqqpqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqylllsymmgky",
                "marketplaceId": "491c84d66327c54a",
                "orderId": "14b0e70d7cf3fec7",
                "to": "klv17e8zzgn73h6ehe3c6q9vlt77kuxk5euddmhymy5uhv2rhv0dc0nqlfp0ap",
                "type": 14,
                "value": 100
            },
            {
                "assetId": "KLV",
                "from": "klv1qqqqqqqqqqqqqqqpqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqylllsymmgky",
                "marketplaceId": "491c84d66327c54a",
                "orderId": "14b0e70d7cf3fec7",
                "to": "klv17e8zzgn73h6ehe3c6q9vlt77kuxk5euddmhymy5uhv2rhv0dc0nqlfp0ap",
                "type": 14,
                "value": 0
            },
            {
                "assetId": "KLV",
                "from": "klv1qqqqqqqqqqqqqqqpqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqylllsymmgky",
                "marketplaceId": "491c84d66327c54a",
                "orderId": "14b0e70d7cf3fec7",
                "to": "klv17e8zzgn73h6ehe3c6q9vlt77kuxk5euddmhymy5uhv2rhv0dc0nqlfp0ap",
                "type": 14,
                "value": 890
            },
            {
                "assetId": "SENA-0b4819/1",
                "from": "klv1qqqqqqqqqqqqqqqpqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqylllsymmgky",
                "marketplaceId": "491c84d66327c54a",
                "orderId": "14b0e70d7cf3fec7",
                "to": "klv122hvtd77uvqlsanmq3dcfpwtmjhm7j0yreygff20scycw0dx3dpsn2mkat",
                "type": 14,
                "value": 1
            }
        ],
        "contract": [
            {
                "type": 17,
                "typeString": "BuyContractType",
                "parameter": {
                    "amount": 1000,
                    "buyType": "MarketBuy",
                    "currencyID": "KLV",
                    "id": "14b0e70d7cf3fec7"
                }
            }
        ]
    },
    {
        "hash": "4b6aa4a5b95d08146f800d3879ebffa32a846ad91ef027afb8a4b03eb625c6a7",
        "blockNum": 71,
        "sender": "klv122hvtd77uvqlsanmq3dcfpwtmjhm7j0yreygff20scycw0dx3dpsn2mkat",
        "nonce": 0,
        "timestamp": 1655831553000,
        "kAppFee": 1000000,
        "bandwidthFee": 1000000,
        "status": "success",
        "resultCode": "Ok",
        "version": 1,
        "chainID": "420420",
        "signature": [
            "2cf51b6e15e6ea8a2ac799295d778d8e6e4d94086c233e336edc75d56326e5f9dcc78aac35856a3fb8412cd9a45471dcce4d4fa741740cfffcadf0fa0083b40f"
        ],
        "searchOrder": 0,
        "receipts": [
            {
                "klv122hvtd77uvqlsanmq3dcfpwtmjhm7j0yreygff20scycw0dx3dpsn2mkat": "1",
                "type": 19
            },
            {
                "assetId": "KLV",
                "from": "klv122hvtd77uvqlsanmq3dcfpwtmjhm7j0yreygff20scycw0dx3dpsn2mkat",
                "marketplaceId": "491c84d66327c54a",
                "orderId": "14b0e70d7cf3fec7",
                "to": "klv1qqqqqqqqqqqqqqqpqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqylllsymmgky",
                "type": 14,
                "value": 1000
            },
            {
                "assetId": "KLV",
                "from": "klv1qqqqqqqqqqqqqqqpqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqylllsymmgky",
                "marketplaceId": "491c84d66327c54a",
                "orderId": "14b0e70d7cf3fec7",
                "to": "klv1pkvnm3sjwklm2q95knfs0sgxa9ufy8u0fflqma83stjpg5fude4qn75suu",
                "type": 14,
                "value": 10
            },
            {
                "assetId": "KLV",
                "from": "klv1qqqqqqqqqqqqqqqpqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqylllsymmgky",
                "marketplaceId": "491c84d66327c54a",
                "orderId": "14b0e70d7cf3fec7",
                "to": "klv17e8zzgn73h6ehe3c6q9vlt77kuxk5euddmhymy5uhv2rhv0dc0nqlfp0ap",
                "type": 14,
                "value": 100
            },
            {
                "assetId": "KLV",
                "from": "klv1qqqqqqqqqqqqqqqpqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqylllsymmgky",
                "marketplaceId": "491c84d66327c54a",
                "orderId": "14b0e70d7cf3fec7",
                "to": "klv17e8zzgn73h6ehe3c6q9vlt77kuxk5euddmhymy5uhv2rhv0dc0nqlfp0ap",
                "type": 14,
                "value": 0
            },
            {
                "assetId": "KLV",
                "from": "klv1qqqqqqqqqqqqqqqpqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqylllsymmgky",
                "marketplaceId": "491c84d66327c54a",
                "orderId": "14b0e70d7cf3fec7",
                "to": "klv17e8zzgn73h6ehe3c6q9vlt77kuxk5euddmhymy5uhv2rhv0dc0nqlfp0ap",
                "type": 14,
                "value": 890
            },
            {
                "assetId": "SENA-0b4819/1",
                "from": "klv1qqqqqqqqqqqqqqqpqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqylllsymmgky",
                "marketplaceId": "491c84d66327c54a",
                "orderId": "14b0e70d7cf3fec7",
                "to": "klv122hvtd77uvqlsanmq3dcfpwtmjhm7j0yreygff20scycw0dx3dpsn2mkat",
                "type": 14,
                "value": 1
            }
        ],
        "contract": [
            {
                "type": 17,
                "typeString": "BuyContractType",
                "parameter": {
                    "amount": 1000,
                    "buyType": "MarketBuy",
                    "currencyID": "KLV",
                    "id": "14b0e70d7cf3fec7"
                }
            }
        ]
    },
    {
        "hash": "4b6aa4a5b95d08146f800d3879ebffa32a846ad91ef027afb8a4b03eb625c6a7",
        "blockNum": 71,
        "sender": "klv122hvtd77uvqlsanmq3dcfpwtmjhm7j0yreygff20scycw0dx3dpsn2mkat",
        "nonce": 0,
        "timestamp": 1655831553000,
        "kAppFee": 1000000,
        "bandwidthFee": 1000000,
        "status": "success",
        "resultCode": "Ok",
        "version": 1,
        "chainID": "420420",
        "signature": [
            "2cf51b6e15e6ea8a2ac799295d778d8e6e4d94086c233e336edc75d56326e5f9dcc78aac35856a3fb8412cd9a45471dcce4d4fa741740cfffcadf0fa0083b40f"
        ],
        "searchOrder": 0,
        "receipts": [
            {
                "klv122hvtd77uvqlsanmq3dcfpwtmjhm7j0yreygff20scycw0dx3dpsn2mkat": "1",
                "type": 19
            },
            {
                "assetId": "KLV",
                "from": "klv122hvtd77uvqlsanmq3dcfpwtmjhm7j0yreygff20scycw0dx3dpsn2mkat",
                "marketplaceId": "491c84d66327c54a",
                "orderId": "14b0e70d7cf3fec7",
                "to": "klv1qqqqqqqqqqqqqqqpqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqylllsymmgky",
                "type": 14,
                "value": 1000
            },
            {
                "assetId": "KLV",
                "from": "klv1qqqqqqqqqqqqqqqpqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqylllsymmgky",
                "marketplaceId": "491c84d66327c54a",
                "orderId": "14b0e70d7cf3fec7",
                "to": "klv1pkvnm3sjwklm2q95knfs0sgxa9ufy8u0fflqma83stjpg5fude4qn75suu",
                "type": 14,
                "value": 10
            },
            {
                "assetId": "KLV",
                "from": "klv1qqqqqqqqqqqqqqqpqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqylllsymmgky",
                "marketplaceId": "491c84d66327c54a",
                "orderId": "14b0e70d7cf3fec7",
                "to": "klv17e8zzgn73h6ehe3c6q9vlt77kuxk5euddmhymy5uhv2rhv0dc0nqlfp0ap",
                "type": 14,
                "value": 100
            },
            {
                "assetId": "KLV",
                "from": "klv1qqqqqqqqqqqqqqqpqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqylllsymmgky",
                "marketplaceId": "491c84d66327c54a",
                "orderId": "14b0e70d7cf3fec7",
                "to": "klv17e8zzgn73h6ehe3c6q9vlt77kuxk5euddmhymy5uhv2rhv0dc0nqlfp0ap",
                "type": 14,
                "value": 0
            },
            {
                "assetId": "KLV",
                "from": "klv1qqqqqqqqqqqqqqqpqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqylllsymmgky",
                "marketplaceId": "491c84d66327c54a",
                "orderId": "14b0e70d7cf3fec7",
                "to": "klv17e8zzgn73h6ehe3c6q9vlt77kuxk5euddmhymy5uhv2rhv0dc0nqlfp0ap",
                "type": 14,
                "value": 890
            },
            {
                "assetId": "SENA-0b4819/1",
                "from": "klv1qqqqqqqqqqqqqqqpqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqylllsymmgky",
                "marketplaceId": "491c84d66327c54a",
                "orderId": "14b0e70d7cf3fec7",
                "to": "klv122hvtd77uvqlsanmq3dcfpwtmjhm7j0yreygff20scycw0dx3dpsn2mkat",
                "type": 14,
                "value": 1
            }
        ],
        "contract": [
            {
                "type": 17,
                "typeString": "BuyContractType",
                "parameter": {
                    "amount": 1000,
                    "buyType": "MarketBuy",
                    "currencyID": "KLV",
                    "id": "14b0e70d7cf3fec7"
                }
            }
        ]
    }
]

#start iteration to calculate SENA NFT total ry
total = 0
datatopd = []
for obj in listdata:
    if obj["receipts"]:
        for value in obj["receipts"]:
            datatopd.append(value)
df = pd.DataFrame(datatopd)
for obj in df.iterrows():
    if obj[1]["to"] == senaddress:
        total += obj[1]["value"]

#upload total for SENA NFT Royalties
client = pymongo.MongoClient("mongodb+srv://senadbnew:11223344@clusternft.7fhtj.mongodb.net/?retryWrites=true&w=majority")
db = client.prod
#db = client.test
senanftry = db["senanftry"]
x = senanftry.insert_one({"total": total})
print("MongoDB Updated")