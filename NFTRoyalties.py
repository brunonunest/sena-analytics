# get listdata data from klever api.... brandon did not send it to me
listdata = []
import pandas as pd
total = 0
datatopd = []
for obj in listdata:
    if obj["receipts"]:
        for value in obj["receipts"]:
            datatopd.append(value)
df = pd.DataFrame(datatopd)
for obj in df.iterrows():
    #if obj[1]["to"] == senaddress:
        total += obj[1]["value"]
total