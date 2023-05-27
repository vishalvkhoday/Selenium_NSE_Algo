import pandas as pd
import os

def ReadXlValue(strFile):
    FilePath = 'C:/Users/Vishal/OneDrive/Desktop/Nagraj/{}'.format(strFile)
    strRow = pd.read_excel(FilePath,sheet_name=0)
    Sheet1 = pd.DataFrame(strRow)
    Sheet1['Filename']= strFile
    return Sheet1

df =pd.DataFrame()
strOutputPath = 'C:/Users/Vishal/OneDrive/Desktop/Nagraj'
FileList = os.listdir(strOutputPath)  # ['PROFORMA_INVOICE_769824','PROFORMA_INVOICE_769823']
for i in FileList:
    df = df.append(ReadXlValue(i))
    
with pd.ExcelWriter('C:/Users/Vishal/OneDrive/Desktop/OutPut.xlsx',mode='a') as writer:
        df.to_excel(writer, sheet_name='Performa')
print(df)
print("Done")

