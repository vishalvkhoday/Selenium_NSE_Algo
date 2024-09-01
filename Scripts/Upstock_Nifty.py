import requests
import json

IndexList = ['India%20VIX','Nifty%20100','Nifty%20200','Nifty%2050','Nifty%20500','NIFTY%20Alpha%2050',
             'Nifty%20Bank','Nifty%20Auto','India%20VIX','Nifty%20Infra','Nifty%20Pharma','NIFTY%20MIDCAP%20150',
             'Nifty%20CPSE','Nifty%20Energy','Nifty%20FMCG','NIFTY%20INDIA%20MFG','Nifty%20IT','Nifty%20Media',
             'Nifty%20Metal','Nifty%20Midcap%2050','Nifty%20MNC','Nifty%20Multi%20Mfg','Nifty%20Next%2050',
             'Nifty%20Pharma','Nifty%20PSE','Nifty%20PSU%20Bank','Nifty%20Pvt%20Bank','Nifty%20Realty',
             'NIFTY%20TOTAL%20MKT']

for i in IndexList:
    IndInd = []
# url = "https://api.upstox.com/v2/historical-candle//NSE_INDEX%7CNifty%2050/1minute/2024-08-06/2024-08-06"
    url = f"https://api.upstox.com/v2/historical-candle/NSE_INDEX%7C{i}/1minute/2024-08-30/2024-08-30"
    # url = f"https://api.upstox.com/v2/historical-candle/{i}/1minute/2024-08-29/2024-08-29"
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
        fContent = ""
        for k in FormatJson:
            # f"{i},{k}"7
            fContent = fContent +f"{i},{k[1:-1]}\n"
        fName = f"c:/Test/{i}_Index_{TrnxDate}.txt"
        with open(fName,'w') as f:
            f.write(str(fContent))
        
        print(fName)
    else:
        print(response.status_code)
        continue
