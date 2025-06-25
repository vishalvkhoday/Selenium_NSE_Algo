
from  DB_Connection_V1 import DB_Connect as db
import time, json,datetime as dt
from selenium.webdriver import ChromeOptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

Options = ChromeOptions()
Options.add_argument("start-maximized")
Options.add_argument("disable-infobar")
serviceObj = Service('C:/Vishal/git/Bse_Extractor/src/WebDriver/chromedriver.exe')

connectionParms = {"DATABASE":"StockQuote"}
MSSQLConnect = db.connect(**connectionParms)

browChrome =  webdriver.Chrome(service=serviceObj,options=Options)
def getScriptName():
    get_script="select replace(script_name,'&','%26') from v_Current_NSE_EOD except select Script_Name from Nse_Stock_PE_V1 "
    # get_script="select Script_Name from NSE_Stock_PE_Archive_V1  except select Script_Name from  Nse_Stock_PE_V1 "
    objDb =MSSQLConnect.execute(get_script).fetchall()
    MSSQLConnect.close()
    ArryScrLst = objDb
    return ArryScrLst

getscriptcode = getScriptName()
browChrome.get("https://www.nseindia.com")
for script in getscriptcode:
    MSSQLConnect = db.connect(**connectionParms)
    
    # time.sleep(5)
    weburl = f"https://www.nseindia.com/api/quote-equity?symbol={script[0]}"
    browChrome.get(weburl)
    time.sleep(1)
    try:
        resJson = browChrome.find_element("xpath", "/html/body/pre").text
        resJson = json.loads(resJson)
        # print(resJson["metadata"])
    except Exception as e:
        print("\n","***-***"*18,"\n",e)
        print("Error in fetching data from NSE")
        print("Retrying in 5 seconds...")
        time.sleep(5)
        MSSQLConnect.close()
        continue
    try:
        symbol = resJson["metadata"]["symbol"]
        peAdjusted = resJson["metadata"]["pdSectorPe"]
        peSymbol = resJson["metadata"]["pdSymbolPe"]
        industry = resJson["metadata"]["industry"]
        isin = resJson["metadata"]["isin"]
        lastupdated = dt.datetime.now().strftime("%Y-%m-%d")   # Change the date here 

        #Sector & industry section
        macro = resJson["industryInfo"]["macro"]
        sector = resJson["industryInfo"]["sector"]
        industry = resJson["industryInfo"]["industry"]
        basicIndustry = resJson["industryInfo"]["basicIndustry"]

        if peAdjusted == 'NA':
            peAdjusted = 0
        if peSymbol == 'NA':
            peSymbol = 0
        sql_insertQuery = f"insert into Nse_Stock_PE_V1 (Script_Name, PE_Adjusted, PE_Symbol, Industry,LastUpdated, INIS) values ('{symbol}','{peAdjusted}','{peSymbol}','{industry}','{lastupdated}','{isin}')"
        # sql_IndustryQuery = f"insert into Sector_Industry (Script_Name,[BasicIndustry] ,[Industry] ,[Sector] ,[Macro]  ,[ISIN]) values ('{symbol}','{basicIndustry}','{industry}','{sector}','{macro}','{isin}')"
        print(sql_insertQuery)    
        MSSQLConnect.execute(sql_insertQuery)
        # MSSQLConnect.execute(sql_IndustryQuery)
        MSSQLConnect.commit()
    except Exception as e:
        MSSQLConnect.rollback()
        print("\n","***-***"*18,"\n",e)
    MSSQLConnect.close()