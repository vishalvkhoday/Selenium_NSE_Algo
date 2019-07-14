'''
Created on Aug 13, 2018

@author: khoday
'''
import pymssql
import datetime



class DB_Operation():
    
    def __init__(self,sql_Query=""):
        self.sql_Query = sql_Query
    
    
    def db_connection_str(self):
        conn = pymssql.connect(user='sa',password='password',host='.\\SQLEXPRESS', database='StockQuote',port='1433')
        cur=conn.cursor()
        
        return cur
    
    def db_select(self):
        obj = DB_Operation.db_connection_str(self)
        obj.execute(self.sql_Query)
        ret_Row_Val = obj.fetchall()
        return ret_Row_Val
    
    def Insert_data(self):
        conn = pymssql.connect(user='sa', password='password', host='.\\SQLEXPRESS', database='StockQuote',port='1433')
#                 conn = pymssql.connect(user='sa', password='password', host='.\\SQLEXPRESS', database='StockQuote',port='1433')
        cur = conn.cursor()
        cur.execute(self.sql_Query)
        conn.commit()
        
class Stock_Info():
    
    def __init__(self,script="",st_High_Dt="",st_Low_Dt=""):
        self.script= script
        self.st_High_Dt=st_High_Dt
        self.st_Low_Dt = st_Low_Dt
        
        
    def date_Diff(self,frm_Dt,to_Dt):
        spl_frm_Dt = frm_Dt.split('-')
        spl_to_Dt = to_Dt.split('-')
        
        dt_frm_Dt = datetime.datetime(int(spl_frm_Dt[0]),int(spl_frm_Dt[1]),int(spl_frm_Dt[2]))
        dt_to_Dt = datetime.datetime(int(spl_to_Dt[0]),int(spl_to_Dt[1]),int(spl_to_Dt[2]))
        dt_Diff =  (dt_to_Dt - dt_frm_Dt)
        return int((dt_Diff).days)
    
    
    