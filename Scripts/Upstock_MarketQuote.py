import requests,json
import pandas as pd

url = "https://api.upstox.com/v3/historical-candle/NSE_EQ%7CINE848E01016/minutes/1/2022-01-08"

payload={}
headers = {
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

jsonText = json.loads(response.text)
FormatJson =list(map(lambda x:str(x).replace('+05:30',''),jsonText['data']['candles']))
FormatJson =list(map(lambda x:str(x).replace('T',' '),FormatJson))
FormatJson =list(map(lambda x:str(x).replace("'", ""),FormatJson))
print(response)