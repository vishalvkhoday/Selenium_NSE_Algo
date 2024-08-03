import pandas as pd
import pyodbc
from  sqlalchemy import create_engine
from DB_Operation import DB_Operation as dbo
from matplotlib import pyplot as plt

engine = create_engine('mssql+pyodbc://sa:password@LAPTOP-IFK6D8L3\\SQLEXPRESS/StockQuote')


SqlScriptName = """
select distinct Script_Name from NSE_EOD order by 1
"""

def calculate_RSI(data,window=14):
    delta = (data.diff)
    gain = delta.where(delta >0,0).rolling(window=window).mean().round(2)
    loss =(-delta).where (delta<0,0).rolling(window=window).mean().round(2)
    rsi = gain/loss
    rsi = 100 - (100/(1/+rsi))
    return rsi

def SignalsMACD(ScrName):
    sql_Query = """
    select Script_Name,Change,[Close],trnx_date from NSE_EOD where Script_Name = '{}' order by Trnx_date  
    """
    ScrName = 'HAL'
    sql_Query = sql_Query.format(ScrName)

    conn = dbo().Rdb_ConnectionObject()
    df = pd.read_sql(sql_Query,conn)
    conn.close()
    
    df['Scale'] = df['Close'].round(-1)
    # df['MA7']    = df['Close'].rolling(window=7).apply(lambda x: x.sum()/7).round(-2)
    # df['MA21']    = df['Close'].rolling(window=21).apply(lambda x: x.sum()/21).round(2)
    # df['EMA5'] = df['Close'].ewm(span=5).mean().round(2)
    # df['EMA9'] = df['Close'].ewm(span=9).mean().round(2)
    # df['EMA12'] = df['Close'].ewm(span=12).mean().round(2)
    # df['EMA21'] = df['Close'].ewm(span=21).mean().round(2)
    # df['EMA25'] = df['Close'].ewm(span=25).mean().round(2)
    # df['EMA26'] = df['Close'].ewm(span=26).mean().round(2)
    # df['MACD']  = df.apply(lambda x : x['EMA12'] - x['EMA26'],axis=1)
    # df['Signal'] = df['MACD'].rolling(window=9).apply(lambda y:y.sum()/9).round(2)
    # df['Signal2'] = df['MACD'].ewm(span=9).mean().round(2)
    # df['MACD-X'] = df.apply(lambda z:z['MACD'] - z['Signal'],axis=1)
    df['Change'] = df.groupby('Scale')['Change'].sum().round(2)
    
    df['Low'] = df.groupby('Scale')['Change'].min().round(2)
    # df['Open'] = df.groupby('Scale')['Open'].first().round(2)
    # df['Close'] = df.groupby('Scale')['Close'].last().round(2)

    df = df.reset_index()
    df = df.reset_index(drop=True)
    print(df)
    # rsi_val   = calculate_RSI(df['Close'])
    # df['RSI'] = rsi_val
    df = df.dropna()
    fPath =  "c:\\Test\\{}.csv"
    fPath = fPath.format(ScrName)
    df.to_csv(fPath,index=False)
    # df = df.drop('Change',axis=1)
    df = df.reset_index(drop=True)
    print(df)
    
    plt.plot(df['trnx_date'],df['Signal2'],label='Signal2')
    plt.plot(df['trnx_date'],df['Signal'],label='Signal')
    plt.plot(df['trnx_date'],df['MACD-X'] ,label='MACD-X')
    plt.plot(df['trnx_date'],df['MACD'] ,label='MACD')
    plt.axhline(0,color='black',linestyle='--',label='Zline')
    
    plt.legend()
    plt.title(df['Script_Name'].unique()[0])
    plt.show()
    plt.close()
    # conn = dbo().Rdb_ConnectionObject()
    # df.to_sql('tbl_Signals',engine,if_exists='replace',index=False)
    # engine.dispose()

conn = dbo().Rdb_ConnectionObject()
dfScr = pd.read_sql(SqlScriptName,conn)
conn.close()

for i in range(len(dfScr.values)):
    print(dfScr.values[i][0])
    ScrName = dfScr.values[i][0]
    SignalsMACD(ScrName)


