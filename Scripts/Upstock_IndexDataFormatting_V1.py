import pandas as pd
import os
import pyodbc
import numpy as np

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

connectionParms = {"DATABASE":"Bse_Results"}


IndexVal = {'Nifty50':'NIFTY 50','IndiaVIX':'INDIA VIX','Nifty100':'NIFTY 100',
            "Nifty200":"NIFTY 200","Nifty500":"NIFTY 500","NIFTYAlpha50":"NIFTY ALPHA 50","NiftyAuto":"NIFTY AUTO",
            "NiftyBank":"NIFTY BANK","NiftyCPSE":"NIFTY CPSE","NiftyEnergy":"NIFTY ENERGY","NiftyFMCG":"NIFTY FMCG",
            "NIFTYINDIAMFG":"NIFTY INDIA MFG","NiftyInfra":"NIFTY INFRA","NiftyIT":"NIFTY IT","NiftyMedia":"NIFTY MEDIA",
            "NiftyMetal":"NIFTY METAL","NiftyMidcap50":"NIFTY MIDCAP 50","NiftyMNC":"NIFTY MNC","NiftyMultiMfg":"NIFTY MULTI MFG",
            "NiftyNext50":"NIFTY NEXT 50","NiftyPharma":"NIFTY PHARMA","NiftyPSE":"NIFTY PSE","NiftyPSUBank":"NIFTY PSU BANK",
            "NiftyPvtBank":"NIFTY PVT BANK","NiftyRealty":"NIFTY REALTY","NIFTYTOTALMKT":"NIFTY TOTAL MKT","NIFTYMIDCAP150":"NIFTY MIDCAP 50"}
FileNames = os.listdir('C:\\Test')
Cols = ['Script_Name','DateTime', 'Open', 'High', 'Low', 'Close','Min','Mod']
NewCols = ['Script_Name','DateTime','SpotPrice','Chg', 'DaysOpen', 'High', 'Low', 'Pre_Close']

for i in FileNames:
    if (i.endswith('.txt')):    
        try:
            df = pd.read_csv('C:\\Test\\'+i)
            
        except:
            continue
        df.columns = Cols
        
        df['DateTime'] = pd.to_datetime(df['DateTime'])
        Trnx_date = df["DateTime"].dt.strftime("%Y-%m-%d")[0]
        # Trnx_date = '2024-12-05'  # Add previous for all new inserts
        df['Min'] = df['DateTime'].dt.minute
        df['Mod'] = df['Min'] % 2        
        df = df[df['Mod']==1]
        df =df.drop(columns=['Mod'])
        # df['Chg'] =None
        DaysHigh = df['High'].max()
        DaysLow = df['Low'].min()
        df['High'] = DaysHigh
        df['Low'] = DaysLow
        df = df.sort_values(by=['DateTime'])
        DaysOpen = df.iloc[0]['Open']
        df['DaysOpen'] = DaysOpen
        df.rename(columns={'Open':'SpotPrice','Min':'Chg','Mod':'Pre_Close'},inplace=True)
        IndexName = IndexVal[df['Script_Name'].unique()[0]]
        TicketVal =f"select top 1 IndPreClose from Nifty_Ticker where Script_Name = '{IndexName}' and cast([DateTime] as date) = '{Trnx_date}' order by [DateTime] desc"
        
        
        MSSQLConnect = connect(**connectionParms)
        dfSQL = pd.read_sql(TicketVal,MSSQLConnect)
        df['Pre_Close'] = dfSQL.values[0][0]
        df['Chg'] =((df['SpotPrice'] - df['Pre_Close'])/df['Pre_Close']*100).round(2)
        df = df[NewCols]
                
        df['Script_Name'] = IndexName
        sqlCursor = MSSQLConnect.cursor()
        
        for row in df.iterrows():
            SqlInsert = f"INSERT INTO Nifty_Ticker (Script_Name, [DateTime], SpotPrice, chg, IndOpen, IndHigh, IndLow, IndPreClose) values ('{row[1].Script_Name}','{str(row[1].DateTime)}','{row[1].SpotPrice}',{row[1].Chg},'{row[1].DaysOpen}','{row[1].High}','{row[1].Low}','{row[1].Pre_Close}')"
            try:
                sqlCursor.execute(SqlInsert)
                print(SqlInsert)
            except Exception as e:
                pass
        MSSQLConnect.commit()
        MSSQLConnect.close()
        j = i.replace('.txt','.csv')
        df.to_csv('C:\\Test\\'+j,index=False)
        os.remove('C:\\Test\\'+i)
    else:
        continue
print('Done')