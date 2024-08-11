import requests
import json

url = "https://api.upstox.com/v2/historical-candle//NSE_INDEX%7CNifty%2050/1minute/2024-08-06/2024-08-06"

payload={}
headers = {
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)

josonText = json.loads(response.text)
for i in josonText['data']['candles']:
    print(i)
    
