import pandas as pd
from  DB_Operation import DB_Operation as dbo
import matplotlib.pyplot as plt
import mplfinance as mpf

listComp = ['HAL','ABBOTINDIA','TATAMOTORS']

def plotChart(ScrName):
    sql_Query = """     select top 120 * from NSE_EOD where Script_Name = '{}' order by Trnx_date desc """
    # ScrName = "HAL"
    sql_Query = sql_Query.format(ScrName)

    conn = dbo().Rdb_ConnectionObject()
    df = pd.read_sql(sql_Query,conn)
    conn.close()

    df['Trnx_date'] = pd.to_datetime(df['Trnx_date'])
    df.sort_values(by='Trnx_date',inplace=True)
    df.set_index('Trnx_date',inplace=True)

    mpf.plot(df,type='candle',style='yahoo',volume=True,title=ScrName,ylabel_lower='Volume')
    plt.show()


for ScrName in listComp:
    plotChart(ScrName)

