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
    print(csvVal.dtypes)
    csvVal.dropna(axis=0,inplace=True)
    csvVal['Open Index Value']=pd.to_numeric(csvVal['Open Index Value'],downcast="float")
    csvVal['Index Date'] = pd.to_datetime(csvVal['Index Date'])
    print(csvVal.dtypes)
    csvVal['Index Date'] = csvVal.apply(lambda x: x['Index Date'].strftime('%Y%m%d'),axis=1)

    dfAll = pd.concat([dfAll,csvVal],ignore_index=False)
    # dfAll = pd.concat([dfAll,readCSV(f)],ignore_index=False)

print(dfAll)

dfAll.to_csv(fPath+"/"+"Mergeall.csv",index=False)

print("Merge done !!!")