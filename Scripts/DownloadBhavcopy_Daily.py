import requests
import datetime
import zipfile,os
import pandas as pd


url = "https://nsearchives.nseindia.com/content/cm/BhavCopy_NSE_CM_0_0_0_{}_F_0000.csv.zip"

# url = "https://nsearchives.nseindia.com/content/cm/BhavCopy_NSE_CM_0_0_0_20240708_F_0000.csv.zip"

def BhavToText(fpath):
    dfbhav = pd.DataFrame()
    dfbhav = pd.read_csv(fpath)
    dfbhav = dfbhav.filter(items=['TckrSymb','TradDt','OpnPric','HghPric',	'LwPric',	'ClsPric','TtlTradgVol','SctySrs'])
    
    dfbhav['TradDt'] = dfbhav['TradDt'].apply(lambda x: str(x).replace('-',''))
    dfbhav['OpnPric'] = pd.to_numeric(dfbhav['OpnPric']).round(2)
    dfbhav = dfbhav[dfbhav['SctySrs'].isin(['EQ','BE'])]
    dfbhav = dfbhav.sort_values(by=['TckrSymb'])
    dfbhav['SctySrs'] = 0
    dfbhav.to_csv('c:/test/'+fpath[30:38]+".txt",index=False,header=False)
    print(dfbhav)



curDate = datetime.datetime.now().strftime("%Y%m%d")
url = url.format(curDate)
print(url)
filename = "{curDate}.txt".format(curDate=curDate)
print(filename)
listFilaename = os.listdir("c:/test/")
print(listFilaename)
for f in listFilaename:
    if f.endswith(".zip"):
        print(f)
        compressfile = "c:/test/"+f
        
        zipref = zipfile.ZipFile(compressfile)
        zipref.extractall("c:/test/")
        zipref.close()
        
        compressfile = "c:/test/"+f.replace(".zip","")
        BhavToText(compressfile)
        os.remove(compressfile)
        os.remove(compressfile+'.zip')
        print("done")
    # else:
    #     os.remove("c:\\test\\"+f)



