import requests
import json
import pandas as pd
import csv

IndexList = ['India%20VIX','Nifty%20100','Nifty%20200','Nifty%2050','Nifty%20500','NIFTY%20Alpha%2050',
             'Nifty%20Bank','Nifty%20Auto','India%20VIX','Nifty%20Infra','Nifty%20Pharma','NIFTY%20MIDCAP%20150',
             'Nifty%20CPSE','Nifty%20Energy','Nifty%20FMCG','NIFTY%20INDIA%20MFG','Nifty%20IT','Nifty%20Media',
             'Nifty%20Metal','Nifty%20Midcap%2050','Nifty%20MNC','Nifty%20Multi%20Mfg','Nifty%20Next%2050',
             'Nifty%20Pharma','Nifty%20PSE','Nifty%20PSU%20Bank','Nifty%20Pvt%20Bank','Nifty%20Realty',
             'NIFTY%20TOTAL%20MKT','Nifty%20IPO','Nifty%20Housing','Nifty%20Commodities','Nifty%20Consumption',
             'Nifty%20EV','Nifty%20Mobility','Nifty%20Rural','Nifty%20Services','Nifty%20SME','Nifty%20TMT']

## list of trnx date to download in bulk
TDate = ['2025-03-13']    

for x in TDate:
    for i in IndexList:                
    # url = "https://api.upstox.com/v2/historical-candle//NSE_INDEX%7CNifty%2050/1minute/2024-08-06/2024-08-06"
        # url = f"https://api.upstox.com/v2/historical-candle/NSE_INDEX%7C{i}/1minute/2024-07-22/2024-07-22"
        url = f"https://api.upstox.com/v2/historical-candle/NSE_INDEX%7C{i}/1minute/{x}/{x}"
        TrnxDate = url[-10:]
        payload={}
        headers = {
        'Accept': 'application/json'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        if (response.status_code == 200):
            jsonText = json.loads(response.text)
            FormatJson =list(map(lambda x:str(x).replace('+05:30',''),jsonText['data']['candles']))
            FormatJson =list(map(lambda x:str(x).replace('T',' '),FormatJson))
            FormatJson =list(map(lambda x:str(x).replace("'", ""),FormatJson))
            i = i.replace("%20","")
            # FormatJson = list(map(lambda x:str(x.split(',')).replace("[", "").replace("]", "").strip(),FormatJson))
            
            xx  = list(map(lambda x:f"{i},"+x[1:-1],FormatJson))
            dfIndex = pd.DataFrame(xx)
            # dfIndex = pd.DataFrame(xx)
            dfIndex = dfIndex.apply(lambda x:x[1].strip() if isinstance(x,str) else x)        
            print(dfIndex[1:-1])
            dfIndex.to_csv(f"c:/Test/{i}_Index_{TrnxDate}.txt",index=False,header=False,sep='"',quoting=csv.QUOTE_NONE)
            fName = f"{i}_Index_{TrnxDate}.txt"
            print(fName)
        else:
            print(response.status_code)
            continue
print("Done")