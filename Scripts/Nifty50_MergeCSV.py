import pandas as pd
import csv
import os
import dateutil.parser as dp
import datetime
import numpy as np

# datetime.datetime.now().str

fPath ='C:/Users/Vishal/OneDrive/Desktop/New folder'
def getFilename():
    fNames = os.listdir(fPath)
    return fNames


def readCSV(fName):    
    dfCSV = pd.DataFrame()    
    fName = fPath+"/"+fName
    dfCSV = pd.read_csv(fName,na_values=["-"])
    return dfCSV


allFiles = getFilename()
dfAll = pd.DataFrame()
for f in allFiles:
    csvVal = readCSV(f)
    # print(csvVal.dtypes)
    csvVal.dropna(axis=0,inplace=True)
    csvVal['Open Index Value']=pd.to_numeric(csvVal['Open Index Value'],downcast="float")
    # csvVal['Index Date'] = pd.to_datetime(csvVal['Index Date'])
    # csvVal['Index Date'] = csvVal['Index Date'].dt.strftime('%Y%d%m')


    # print(csvVal.dtypes)
    csvVal['Open Index Value'] = csvVal.apply(lambda x:round(x['Open Index Value'],2),axis=1)
    csvVal['Index Name'] = csvVal.apply(lambda x:str(x['Index Name']).replace(" ",""),axis=1)
    # csvVal['Index Date'] = csvVal.apply(lambda x: x['Index Date'].strftime('%Y%d%m'),axis=1)
    csvVal['Index Date'] = str(f[18:-4])+str(f[16:-8])+str(f[14:-10])
    # str(f[18:-4])+str(f[16:-8])+str(f[14:-10])
    csvVal['Turnover (Rs. Cr.)'] = csvVal.apply(lambda y: y['Turnover (Rs. Cr.)'] *100,axis=1)
    csvVal.drop(['Points Change','Change(%)','P/E','P/B','Div Yield','Volume'],axis=1,inplace=True)
    csvVal['IO'] =0

    dfAll = pd.concat([dfAll,csvVal],ignore_index=False)
    # dfAll = pd.concat([dfAll,readCSV(f)],ignore_index=False)

print(dfAll)

dfAll.to_csv(fPath+"/Mergeall.csv",index=False)

print("Merge done !!!")