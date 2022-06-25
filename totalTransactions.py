#get listdata data from https://api.testnet.klever.finance/v1.0/transaction/list?startdate=1651287651000&enddate=1659287651000
listdata2 = []
import pandas as pd
total = 0
datatopd = []
for obj in listdata2:
    total += obj["pagination"]["totalRecords"]
print(total)