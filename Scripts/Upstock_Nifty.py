import requests
import json

IndexList = ['Nifty%2050','Nifty%20Bank']

for i in IndexList:
    IndInd = []
# url = "https://api.upstox.com/v2/historical-candle//NSE_INDEX%7CNifty%2050/1minute/2024-08-06/2024-08-06"
    url = f"https://api.upstox.com/v2/historical-candle/NSE_INDEX%7C{i}/1minute/2024-08-13/2024-08-13"
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
