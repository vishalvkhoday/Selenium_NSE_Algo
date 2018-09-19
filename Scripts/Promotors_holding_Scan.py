'''
Created on Jul 24, 2018

@author: khoday
'''

 
from Algo_classes import DB_Operation

# 
# 
# conn = pymssql.connect(user='sa',password='password',host='.\\SQLEXPRESS', database='StockQuote',port='1433')
# cur =conn.cursor()
# ls_script=cur.execute(Script_list_Sql)
# for x in ls_script:
#     print (x)
sql_list_script = "select Script_Name from NSE_EOD where Trnx_date in(select MAX(trnx_Date) from NSE_EOD)"
sql_Prom_holding = ("select * from Share_Pattern where Script_Name ='{}' order by [Quarter]")
DB= DB_Operation(sql_list_script)
All_script = DB.db_select()
Promo_holding=[]
Co_name =[]
for x in All_script:
    print (x[0])
#     sql_Prom_holding_exe= sql_Prom_holding +(x[0])+"' order by [Quarter]"
    print (sql_Prom_holding_exe.format(x[0]))
    DB1 = DB_Operation(sql_Prom_holding_exe.format(x[0]))
    Rows = DB1.db_select()
    for y in Rows:
#         print (y[0],y[1],y[2],y[3])
        Promo_holding.append(y[2])
        
    print(Promo_holding)
    if len(Promo_holding) > 1:
        if Promo_holding[0]<= Promo_holding[1] and Promo_holding[0] > 35 :
            if len(Promo_holding) >2 : 
                if Promo_holding[1]< Promo_holding[2]:
                    if len(Promo_holding)> 3:
                        if Promo_holding[2] <= Promo_holding[3]:
                            Co_name.append(x[0])
                        else:
                            if Promo_holding[0] <= Promo_holding[3]:
                                Co_name.append(x[0])
                    else:                        
                        if Promo_holding[0] <= Promo_holding[3]:
                            Co_name.append(x[0]) 
                    
    Promo_holding=[]
print (Co_name)
