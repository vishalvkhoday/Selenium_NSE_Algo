
import requests
import json
import datetime as dt
from DB_Connection_V1 import DB_Connect as db

connectionParms = {"DATABASE": "StockQuote"}
MSSQLConnect = db.connect(**connectionParms)

def get_script_names():
    get_script = "SELECT REPLACE(script_name, '&', '%26') FROM v_Current_NSE_EOD EXCEPT SELECT Script_Name FROM Nse_Stock_PE_V1  order by 1  "
    objDb = MSSQLConnect.execute(get_script).fetchall()
    return [row[0] for row in objDb]

def fetch_data(symbol):
    urls = [
        f"https://www.nseindia.com/api/NextApi/apiClient/GetQuoteApi?functionName=getSymbolData&marketType=N&series=EQ&symbol={symbol}",
        f"https://www.nseindia.com/api/NextApi/apiClient/GetQuoteApi?functionName=getSymbolData&marketType=N&series=BE&symbol={symbol}",
        f"https://www.nseindia.com/api/NextApi/apiClient/GetQuoteApi?functionName=getSymbolData&marketType=G&series=BE&symbol={symbol}"
    ]
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    for url in urls:
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            if data.get('equityResponse') and data['equityResponse'][0].get('metaData'):
                return data
        except (requests.RequestException, json.JSONDecodeError, KeyError):
            continue
    return None

def process_script(symbol):
    data = fetch_data(symbol)
    if not data:
        print(f"Failed to fetch data for {symbol}")
        return
    
    try:
        meta = data['equityResponse'][0]['metaData']
        sec_info = data['equityResponse'][0]['secInfo']
        
        symbol_name = meta['symbol']
        pe_adjusted = sec_info.get('pdSectorPe', 0)
        pe_symbol = sec_info.get('pdSymbolPe', 0)
        industry = sec_info.get('industryInfo', '')
        isin = meta.get('isinCode', '')
        last_updated = dt.datetime.now().strftime("%Y-%m-%d")
        
        macro = sec_info.get('macro', '')
        sector = sec_info.get('sector', '')
        basic_industry = sec_info.get('basicIndustry', '')
        
        if not macro:
            return
        
        if pe_adjusted in ('NA', None):
            pe_adjusted = 0
        if pe_symbol in ('NA', None):
            pe_symbol = 0
        
        # Use parameterized queries
        insert_pe_query = """
        INSERT INTO Nse_Stock_PE_V1 (Script_Name, PE_Adjusted, PE_Symbol, Industry, LastUpdated, INIS)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        MSSQLConnect.execute(insert_pe_query, (symbol_name, pe_adjusted, pe_symbol, industry, last_updated, isin))
        
        insert_industry_query = """
        INSERT INTO Sector_Industry (Script_Name, BasicIndustry, Industry, Sector, Macro, ISIN)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        try:
            MSSQLConnect.execute(insert_industry_query, (symbol_name, basic_industry, industry, sector, macro, isin))
        except Exception:
            print(f"Data already exists for {symbol_name}")
        
        MSSQLConnect.commit()
        print(f"Processed {symbol_name}")
    
    except Exception as e:
        MSSQLConnect.rollback()
        print(f"Error processing {symbol}: {e}")

def main():
    script_names = get_script_names()
    for symbol in script_names:
        process_script(symbol)
    MSSQLConnect.close()

if __name__ == "__main__":
    main()