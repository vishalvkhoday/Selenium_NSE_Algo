import requests,fnc,json
import pandas as pd

url = "https://api.upstox.com/v2/historical-candle/intraday/NSE_INDEX%7CIndia%20VIX/1minute"

payload={}
headers = {
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

jsonText = response.text
jsonText = json.loads(response.text)

FormatJson =list(map(lambda x:str(x).replace('+05:30',''),jsonText['data']['candles']))
FormatJson =list(map(lambda x:str(x).replace('T',' '),FormatJson))
# FormatJson =list(map(lambda x:str(x).replace("'", ""),FormatJson))
dfIndex = pd.DataFrame(FormatJson)
dfIndex = dfIndex.apply(lambda x:str(x).split(','))

dfIndex.columns = ['DateTime','Open','High','Low','Close','Volume']

print(dfIndex)
