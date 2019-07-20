'''
Created on May 4, 2019

@author: DELL
'''

from Algo_classes import DB_Operation
import pandas 
from pandas import DataFrame
import numpy as np


def getScrList():        
    UniqueScript = "select distinct Script_Name from Bse_Results order by Script_Name"
    db= DB_Operation(UniqueScript)
    DbScrList=list(db.db_select())
    ScrList = []
    for x in DbScrList:
        ScrList.append(x[0])
    return(ScrList)

def ScrScan():
    ScrQuery = """
    select  Script_Name, convert(date,[Quarter],104)[Qtr] ,Net_Profit, Other_Income, Total_Income,
round((Net_Profit/Total_Income)*100,2) Proft_age from Bse_Results 
where Total_Income >0 and Script_Name = '{}'
order by Script_Name,[Quarter]
"""
    ScrList = getScrList()
    for i in ScrList:
        ScrQueryExe=ScrQuery.format(i)
        db=DB_Operation(ScrQueryExe)
        row=DataFrame(db.db_select(),columns=['ScrName','Quarter','Net_Profit', 'Other_Income', 'Total_Income','ProfitAge'])
        rowFour= (row.tail(4))
        NetProfit = rowFour['Net_Profit'].real
        print(rowFour)
    
ScrScan()