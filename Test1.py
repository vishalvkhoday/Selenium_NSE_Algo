'''
Created on Aug 20, 2018

@author: khoday
'''

import math
import pymssql

def myFunc(x):
    if math.ceil(x) < 20:
        return False
    else:
        return True
 

conn = pymssql.connect(user='sa',password='password',host='.\\SQLEXPRESS', database='StockQuote',port='1433')
cur = conn.cursor()
# cur.execute('EXEC     [dbo].[Alog_List_Stock]')
cur.execute('select [Close] from NSE_EOD where Trnx_date in (select max(Trnx_date) from NSE_EOD)')
new_list=[]
All_script = cur.fetchall()
list_build_sc = iter(All_script)
try:
    while True:
        temp_ls = next(list_build_sc)
        new_list.append(temp_ls[0])
        print (temp_ls[0])
except:
    
    print ('next')
sc = filter(myFunc, new_list)
for x in sc:
    print (x)