'''
Created on Aug 11, 2018

@author: khoday
'''

import os
import csv
# from Algo_Patterns import DB_operation
from Algo_classes import DB_Operation


f_Path = 'C:\\Users\\khoday\\Downloads\\stock_Del'


for csv_File in os.listdir(f_Path):
    print (f_Path + '\\' + csv_File)
    f_full_Path= str(f_Path )+ str( '\\' + csv_File)
    
    try:
        with open(f_full_Path,'rb') as csv_File:
            reader = csv.DictReader(csv_File)
            for row in reader:
                script_name = str(row['Symbol']).strip()
                ser =str(row['Series']).strip()
                trnx_dt = str(row['Date']).strip()
                trd_Qty = str(row['Total Traded Quantity']).strip()
                del_Qty = str(row['Deliverable Qty']).strip()            
                no_of_trd = str(row['No. of Trades']).strip()
                
                del_page = str(row['% Dly Qt to Traded Qty']).strip()
                if del_Qty =='-':
                    del_Qty=trd_Qty
    
                    
                if del_page =='-':
                    del_page=100
                specul = int(trd_Qty)- int(del_Qty)          
                
                if ser =='EQ' or ser =='BE':
                    sql_Stock_del_ins = ("EXEC    [dbo].[Stock_del_Insert] @Script = '%s',@Series = '%s',@Trd_qty = %s,@Spec = %s,@Del_Qty = %s,@NoOf_Trd = %s,@Del_PAge =%s,@Trn_dt = '%s'")%(script_name,ser,trd_Qty,specul,del_Qty,no_of_trd,del_page,trnx_dt)
                    try:
                        db_inst =DB_Operation(sql_Stock_del_ins)
                        db_inst.Insert_data()
                        print(script_name +' inserted successfully for trade on '+trnx_dt+'!!!')
                                            
                    except:
                        continue
            
    except:
        continue
