import requests

url = "https://api.upstox.com/v2/market-quote/NSE_INDEX%7CINE148I07TW3"

payload={}
headers = {
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)