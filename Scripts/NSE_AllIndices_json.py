import requests,fnc,time,random,json
import pandas as pd
from  DB_Connection_V1 import DB_Connect as db

# DB name to connect
connectionParms = {"DATABASE":"Bse_Results"}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
webURL = "https://www.nseindia.com/api/NextApi/apiClient?functionName=getIndexData&&type=All"

def getNseData():
    response = requests.get(url=webURL, headers=headers, timeout=10)
    
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return []
    response = response.json()
    IndexData = list(fnc.map(('indexName','timeVal','last','percChange','open','high','low','previousClose'),response['data']))
    dfIndex = pd.DataFrame(IndexData,columns=['indexName','timeVal','last','percChange','open','high','low','previousClose'])
    dfIndex = dfIndex[dfIndex['previousClose'] != '-']
    dfIndex = list(fnc.filter(lambda x: x[0] !='-', dfIndex.values.tolist()))
    return dfIndex

def insertDataToDB(mssqlConnect):
        dfIndex = getNseData()
        for i in dfIndex:    
            try:                
                sqlIndex_Data = f""" insert into Nifty_Ticker (Script_Name, [DateTime], SpotPrice, chg,
                IndOpen, IndHigh,IndLow, IndPreClose)
                    values ( '{i[0]}',CONVERT(datetime,'{i[1]}'),'{i[2]}','{i[3]}','{i[4]}','{i[5]}','{i[6]}','{i[7]}')"""
                print(sqlIndex_Data)
                mssqlConnect.execute(sqlIndex_Data)
                mssqlConnect.commit()
            except Exception as e:
                print(e)
                mssqlConnect.rollback()
        mssqlConnect.close()
        

while True:
    # #returns connection object and cursor object
    dbCursor = db.connect(**connectionParms)
    insertDataToDB(dbCursor)
    iRant = random.randint(59,80)    
    for i in range(iRant,-1,-1):            
        print("Next refresh in {} seconds   ".format(i), end = "\r")
        time.sleep(1)

    

    
    