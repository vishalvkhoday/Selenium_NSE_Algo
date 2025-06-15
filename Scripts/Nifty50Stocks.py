import requests
from  DB_Connection_V1 import DB_Connect as db
import fnc
import time

# DB name to connect
connectionParms = {"DATABASE":"Bse_Results"}


def StockIndexInsertintoDB(Nifty50StockJson):
    MSSQLConnect = db.connect(**connectionParms)
    Nifty50Stock = list(fnc.map(('symbol','ltP','iislPercChange','open','high','low','previousClose','cAct'),Nifty50StockJson["data"]))
        
    for i in Nifty50Stock:
        i = list(map(lambda x: str(x).replace(',',''),i))
        NiftyStockSql = f"insert into Nifty_Stock (Script_Name, [DateTime], SpotPrice, chg, StkOpen, StkHigh, StkLow, StkPreClose, Announcement) values ( '{i[0]}',CONVERT(datetime,'{Nifty50StockJson['time']}'),'{i[1]}','{i[2]}','{i[3]}','{i[4]}','{i[5]}','{i[6]}','{i[7]}')"
        # print(NiftyStockSql)
        try:
            MSSQLConnect.execute(NiftyStockSql)
            MSSQLConnect.commit()
        except Exception as e:
            print("\n","***-***"*18,"\n",e)
            MSSQLConnect.rollback()
    MSSQLConnect.close()   
    

def getIndexResponse():    
    index = ["500","MIDSML%20400","LARGEMID250","SMALLCAP%20250"]    
    for i in index:        
        Weburl = f"https://iislliveblob.niftyindices.com/jsonfiles/equitystockwatch/EquityStockWatchNIFTY%20{i}.json?"+"{}&_="+str(int(time.time()))        
        try:
            IndexMapping = requests.get(url = Weburl,timeout=5)
        except requests.exceptions.RequestException as e:
            print("\n","***-***"*18,"\n",e)
            print("Error in fetching data from NSE")
            print("Retrying in 5 seconds...")
            time.sleep(5)
            continue
        if IndexMapping.status_code == 200:
            IndexMappingJson = IndexMapping.json()
            StockIndexInsertintoDB(IndexMappingJson)
            
while True: 
    try:
        getIndexResponse()           
        iRant = 120
        for i in range(iRant,-1,-1):
            print("Next refresh in {} seconds    ".format(i), end = "\r")
            time.sleep(1)
    except Exception as e:
        print("\n","***-***"*18,"\n",e)
        time.sleep(5)
