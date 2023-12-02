import pandas as pd
import pyodbc
import sqlalchemy


connNSE = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-IFK6D8L3\\SQLEXPRESS;DATABASE=StockQuote;UID=sa;PWD=password')
StockSQL = "select Script_Name, [Close], Trnx_date  from NSE_EOD where Trnx_date >= getdate()-150  " #  and Script_Name='GSFC'

# nseEOD = connNSE2.execute(StockSQL)
dfStock = pd.read_sql(con=connNSE,sql=StockSQL)
ScriptEMA =pd.DataFrame()
tempScriptEMA = pd.DataFrame()
dfGrouped = dfStock.groupby(['Script_Name','Trnx_date'])
ScriptEMA['MA5'] = round(dfGrouped.mean().rolling(window=5).mean(),2)
ScriptEMA['MA9'] = dfGrouped.mean().rolling(window=9).mean()
ScriptEMA['MA12'] = dfGrouped.mean().rolling(window=12).mean()
ScriptEMA['MA21'] = dfGrouped.mean().rolling(window=21).mean()
ScriptEMA['MA25'] = dfGrouped.mean().rolling(window=25).mean()
ScriptEMA['MA26'] = dfGrouped.mean().rolling(window=26).mean()
# ScriptEMA['Min14'] = dfGrouped['Close'].rolling(window=14).min()
# dfStock['Max14']
print(dfGrouped)

dfStock = round(dfStock.merge(ScriptEMA['MA5'],how="left", on=['Script_Name','Trnx_date']),2)
dfStock = round(dfStock.merge(ScriptEMA['MA9'],how="left", on=['Script_Name','Trnx_date']),2)
dfStock = round(dfStock.merge(ScriptEMA['MA12'],how="left", on=['Script_Name','Trnx_date']),2)
dfStock = round(dfStock.merge(ScriptEMA['MA21'],how="left", on=['Script_Name','Trnx_date']),2)
dfStock = round(dfStock.merge(ScriptEMA['MA25'],how="left", on=['Script_Name','Trnx_date']),2)
dfStock = round(dfStock.merge(ScriptEMA['MA26'],how="left", on=['Script_Name','Trnx_date']),2)

dfStock.dropna(axis=0,inplace=True)


# dfStock['EMA5']= round(dfStock.apply(lambda x: (x.Close*(2/(5+1))) + (x.uprow5*(1-(2/(5+1)))),axis=1 ),2)
# dfStock['EMA5']= round(dfStock.apply(lambda x: (x.Close*(2/(5+1))) + (x.uprow5*(1-(2/(5+1)))),axis=1 ),2)
dfStock['EMA5'] = round(dfStock['Close'].ewm(span=5,adjust=False).mean(),2)
dfStock['EMA9'] = round(dfStock['Close'].ewm(span=9,adjust=False).mean(),2)
dfStock['EMA12']= round(dfStock['Close'].ewm(span=12,adjust=False).mean(),2)
dfStock['EMA21']= round(dfStock['Close'].ewm(span=21,adjust=False).mean(),2)
dfStock['EMA25']= round(dfStock['Close'].ewm(span=25,adjust=False).mean(),2)
dfStock['EMA26']= round(dfStock['Close'].ewm(span=26,adjust=False).mean(),2)
dfStock['MACD'] = round(dfStock.apply(lambda x: (x.EMA12 - x.EMA26),axis=1),2)
dfStock['Signal'] = round(dfStock['MACD'].rolling(window=9).mean(),2)
# dfStock.dropna(axis=0,inplace=True)
#dfStock['SignalPreVal'] = dfStock['Signal'].shift(1)
dfStock['Signal2'] = round(dfStock['MACD'].ewm(span=9,adjust=False).mean(),2)
dfStock['MACD-X'] = round(dfStock['MACD'] - dfStock['Signal'],2)
# LatestDate = dfStock['Trnx_date'].max()
# dfStock['MACD-X'] = dfStock.apply(lambda x: x.MACD - x.Signal)

# uncomment to get date specific
LatestDate =pd.DataFrame()
LatestDate['Trnx_date'] = dfStock['Trnx_date'].unique()
LatestDate.astype('datetime64[ns]')

print(LatestDate['Trnx_date'].unique())
LatestDate.sort_values(by='Trnx_date',ascending = False,inplace=True)
LatestDate.head(10)
print(LatestDate.head(51).min())
LatestDate.head(51).min()

dfStock.dropna(axis=0,inplace=True)
# print(dfStock)

dfStock =dfStock.loc[dfStock['Trnx_date'] >= LatestDate['Trnx_date'].head(51).min()]

# dfStock.to_csv('c:/EMA/ema.csv',index=False)

# dfStock['EMA'] = dfStock['Close'].ewm(span=21,adjust=False).mean()
# dfStock['MA50'] = dfStock['Close'].rolling(window=50).mean()
# dfStock.set_index('Script_Name')
# dfStock.reset_index(drop=True)
print(dfStock)


conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-IFK6D8L3\\SQLEXPRESS;DATABASE=StockQuote;UID=sa;PWD=password')
cur = conn.cursor()

dfSql = "INSERT INTO [dbo].[tbl_Signals] ([Script_Name],[Cls],[Trnx_Date] ,[MA5] ,[MA9],[MA12] ,[MA21] ,[MA25] ,[MA26] ,[EMA5] ,[EMA9],[EMA12] ,[EMA21]  ,[EMA25]  ,[EMA26] ,[MACD],[Signal] ,[Signal-2] ,[MACD-X])  VALUES ("


for row in dfStock.iterrows():
     trnx = str(row[1][2].year)+"/"+str(row[1][2].month)+"/"+str(row[1][2].day)
     val = f"'{row[1][0]}',{row[1][1]},'{trnx}',{row[1][3]},{row[1][4]},{row[1][5]},{row[1][6]},{row[1][7]},{row[1][8]},{row[1][9]},{row[1][10]},{row[1][11]},{row[1][12]},{row[1][13]},{row[1][14]},{row[1][15]},{row[1][16]},{row[1][17]},{row[1][18]})"
     insSQL = dfSql + val
     print(insSQL)
     try:
          cur.execute(insSQL)
     except Exception as e:
          print(e)
     cur.commit()
print("Signals calculation completed!!!")
connNSE.close()
conn.close()
