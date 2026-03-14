import requests,fnc
import pandas as pd

# Endpoint
url = "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%2050"

# Headers required
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://www.nseindia.com/"
}

# Session for cookies
session = requests.Session()
session.headers.update(headers)

# Request
response = session.get(url)

if response.status_code == 200:
    json_data = response.json()
    
    # Extract the 'data' list into a DataFrame
    df = pd.DataFrame(json_data['data'])
    trnxDT = json_data['time']
    df = df[df['priority'] == 0]
    # Nifty50Stock = list(fnc.map(('symbol','lastPrice','previousClose','pChange','open','dayHigh','dayLow','previousClose','totalTradedVolume'),df))
    Nifty50Stock = list(fnc.map(('symbol','lastPrice','previousClose','pChange','open','dayHigh','dayLow','previousClose',
                                 'totalTradedVolume','meta.industry'),json_data["data"]))
    
    print(Nifty50Stock)
    print("✅ DataFrame created successfully!")
    print(df.head())  # Show first 5 rows
else:
    print(f"❌ Failed with status code {response.status_code}")