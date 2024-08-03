import pandas as pd
from  DB_Operation import DB_Operation as dbo

sql_Query = """     select * from Actual_NSE_EOD where Script_Name = '{}' order by Trnx_date """
ScrName = "Smartlink"
sql_Query = sql_Query.format(ScrName)

conn = dbo().Rdb_ConnectionObject()
df = pd.read_sql(sql_Query,conn)
conn.close()

def Sqr(x,y):
    x =str(x)
    y = float(y).__round__(2)
    x =str(x).replace('-','')
    y =str(y).replace('-','')
    return '-'.join([x,y]),x,y

df['Vol21MA'] = df['Volume'].rolling(window=21).apply(lambda x:sum(x)/21).round(0)
df['ChgMedian21'] = df['Change'].rolling(window=21).median()
df['UpbandVal'] = (df['Close'] * (df['ChgMedian21']/100)).round(2)
df['HiPredictVal'] = df['UpbandVal'].round(2) + df['Close'].round(2)
df['LowPredictVals'] =df['Close'] +( df['UpbandVal'].abs() * -1).round(2)
df['Trnx_date'] = pd.to_datetime(df['Trnx_date'])
# df['A'] = df['Trnx_date'].dt.day_name()

# groupedby = df.groupby(['Script_Name','ChgMedian21','Trnx_date']).median()
df= df.dropna()
df['Min21'] = df['Change'].rolling(window=14).min()
df['Max21'] = df['Change'].rolling(window=14).max()
df['minmaxChg_'] = df['Min21'] - df['Max21']
df['minmaxChg'] = df['Min21'] + df['Max21']
df['minmaxChg'] = df['minmaxChg'].round(2)
df['Nechg'] = df['Change'].map(lambda x:x+1)
df['Sq'] = list(map(Sqr,df['Script_Name'],df['Change']))
df['Sq1'] = df['Sq'].apply(lambda x:x[0] )
df.eval('Sq2 = Sq1.str.split("-")',inplace=True)
df['Sq2'] = df['Sq2'].apply(lambda x:x[1] )
df.assign(Sq3=pd.to_numeric(df['Sq2']),inplace=True)
df['Sq2'] = df['Sq2'].round(2)





# print(df)
# groupedby.sort_values(by=['Trnx_date'], ascending=[True])
# print(groupedby)
fpath = 'c:\\Test\\{}.csv'
fpath = fpath.format(ScrName)
df.to_csv(fpath,mode='w',index=False)