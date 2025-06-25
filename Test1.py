'''
Created on Aug 20, 2018

@author: khoday
'''

import requests,time
import fnc,json,pyodbc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from selenium import webdriver
import pyodbc
import win32gui,win32ui,win32con,win32api
import datetime as dt

Options = ChromeOptions()
Options.add_argument("start-maximized")
Options.add_argument("disable-infobar")
serviceObj = Service('C:/Vishal/git/Bse_Extractor/src/WebDriver/chromedriver.exe')

print(dt.datetime.now().strftime("%Y-%m-%d"))
def MSSQLConnectStr(**kwargs):
    driver =kwargs.get("DRIVER","ODBC Driver 17 for SQL Server")
    server =kwargs.get('SERVER',"LAPTOP-IFK6D8L3\\SQLEXPRESS")
    database =kwargs.get('DATABASE',"")
    user = kwargs.get("UID","sa")
    password = kwargs.get("PWD","password")
    return f"DRIVER={driver};SERVER={server};DATABASE={database};UID={user};PWD={password}"

def connect(**kwargs):
    try:
        connection_string = MSSQLConnectStr(**kwargs)
        return   pyodbc.connect(connection_string)
    except pyodbc.Error as e:
        print(e)


def Get_Res_data(url):
    browChrome.get(url)
    counter = 0
    while(True):
        try:
            res = browChrome.find_element(By.XPATH,"/html/body/pre")
            jsonRes = json.loads(res.text)
            print(jsonRes)
            return jsonRes['metadata']
        except:
            browChrome.refresh()
            time.sleep(1)
            counter=counter+1
            if counter >= 5:
                break
            continue

connectionParms = {"DATABASE":"StockQuote"}
MSSQLConnect = connect(**connectionParms)
sqlCursor = MSSQLConnect.cursor()
SQLScriptList = "select distinct Script_Name  from NSE_EOD where Trnx_date >= getdate()-2 and Script_Name like 'A%'"
ScriptList = sqlCursor.execute(SQLScriptList).fetchall()
browChrome =  webdriver.Chrome(service=serviceObj,options=Options) #Driver

for i in ScriptList:
    url = f"https://www.nseindia.com/api/quote-equity?symbol={i[0]}"
    JsonResponse = Get_Res_data(url)
    if JsonResponse == None:
        continue
    try:
        SqlInsert_SectorPE = f"insert into NSE_Stock_PE values('{JsonResponse['symbol']}','{JsonResponse['isin']}','{JsonResponse['industry']}','{JsonResponse['pdSectorPe']}','{JsonResponse['pdSymbolPe']}','{JsonResponse['lastUpdateTime']}')"
        print(SqlInsert_SectorPE)
        sqlCursor.execute(SqlInsert_SectorPE)
        MSSQLConnect.commit()
    except:
        pass

MSSQLConnect.close()


# conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-IFK6D8L3\\SQLEXPRESS;DATABASE=Bse_Results;UID=sa;PWD=password')
# cur = conn.cursor()

# Nseurl = "https://www.nseindia.com/api/quote-equity?symbol=GRINDWELL"
# header = {"content-type":"application/json; charset=utf-8"}

# # Nseurl = "https://iislliveblob.niftyindices.com/jsonfiles/equitystockwatch/EquityStockWatchNIFTY%20500.json?{}"
# header = {"content-Type":"application/json; charset=utf-8"}

# Res = requests.get(url=Nseurl,headers=header,timeout=3)
# # print(Res.text)
# jRes = json.loads(Res.text)
# Nifty50Stock = list(fnc.map(('symbol','ltP','per','open','high','low','previousClose','cAct'),jRes["data"]))
# # Nifty50Stock = list(fnc.map(('symbol','time','ltP','per','open','high','low','previousClose'),jRes["data"]))

# for ii in Nifty50Stock:
#     i = list(map(lambda x: x.replace(',',''),ii))
#     NiftyStockSql = f"insert into Nifty_Stock (Script_Name, [DateTime], SpotPrice, chg, StkOpen, StkHigh, StkLow, StkPreClose, Announcement) values ( '{i[0]}',CONVERT(datetime,'{jRes['time']}'),'{i[1]}','{i[2]}','{i[3]}','{i[4]}','{i[5]}','{i[6]}','{i[7]}')"
#     print(NiftyStockSql)
#     try:
#         cur.execute(NiftyStockSql)        
#     except Exception as e:
#         print(e)
#     cur.commit()
    
# cur.close()
# conn.close()