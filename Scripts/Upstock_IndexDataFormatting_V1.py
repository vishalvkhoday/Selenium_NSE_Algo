import pandas as pd
import os

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
        df = pd.read_csv('C:\\Test\\'+i)
        df.columns = Cols
        
        df['DateTime'] = pd.to_datetime(df['DateTime'])
        df['Min'] = df['DateTime'].dt.minute
        df['Mod'] = df['Min'] % 2        
        df = df[df['Mod']==1]
        df['Chg'] =None
        DaysHigh = df['High'].max()
        DaysLow = df['Low'].min()
        df['High'] = DaysHigh
        df['Low'] = DaysLow
        df = df.sort_values(by=['DateTime'])
        DaysOpen = df.iloc[0]['Open']
        df['DaysOpen'] = DaysOpen
        df.rename(columns={'Open':'SpotPrice','Min':'Chg','Mod':'Pre_Close'},inplace=True)
        df['Pre_Close'] = None
        df = df[NewCols]
        IndexName = IndexVal[df['Script_Name'].unique()[0]]
        
        df['Script_Name'] = IndexName
        j = i.replace('.txt','.csv')
        df.to_csv('C:\\Test\\'+j,index=False)
        os.remove('C:\\Test\\'+i)
    else:
        continue
print('Done')