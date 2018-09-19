'''
Created on Aug 13, 2018

@author: khoday
'''

from Algo_classes import DB_Operation


sql ='select * from ListOfScrips'

DB = DB_Operation(sql)
all_row =DB.db_select()
for x  in all_row:
    print (x[1])
    
print ('done')