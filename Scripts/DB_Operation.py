'''
Created on Sep 6, 2020

@author: DELL
'''

import pyodbc
import datetime
from pytest import fixture


    
# conn = pymssql.connect(user='sa',password='password',host='.\\SQLEXPRESS', database='Bse_Results',port='1433')
# cur=conn.cursor()
class DB_Operation():
    
    def __init__(self,sql_Query=""):
        self.sql_Query = sql_Query
    

       
    def Rdb_ConnectionObject(self):
        # conn = pymssql.connect(user='sa',password='password',host='.\\SQLEXPRESS', database='Bse_Results',port='1433')
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-IFK6D8L3\\SQLEXPRESS;DATABASE=StockQuote;UID=sa;PWD=password')
        return conn
#         
    def db_select(self):
        conn = DB_Operation.Rdb_ConnectionObject(self)
        cur = conn.cursor()
        cur.execute(self.sql_Query)
#         ret_Row_Val = cur.fetchall()
        ret_Row_Val = cur.fetchone()
        conn.close()
        return ret_Row_Val
    def db_selectAll(self):
        conn = DB_Operation.Rdb_ConnectionObject(self)
        cur = conn.cursor()
        cur.execute(self.sql_Query)
        ret_Row_Val = cur.fetchall()
        
        conn.close()
        return ret_Row_Val
    def Insert_data(self,objInsert,sql_Query):
#         conn = DB_Operation.db_ConnectionObject(self)
        conn = objInsert
        cur = conn.cursor()
        cur.execute(sql_Query)
        print("Data inserted {}".format(sql_Query))
#         conn.commit()
#         print("Transaction commited")
#         conn.close()
#         print("connection close")
    
    def Update_data(self,objUpdate,sql_Query):
        conn = objUpdate
        cur =conn.cursor()
        cur.execute(sql_Query)
        print(sql_Query)
        
        
    def sqlCommit(self,objCommit):
        """This will commit the transaction"""
        conn = objCommit
        conn.commit()
        print("Transaction commit successful")

    def sqlRollBack(self,objRollBack):
        """This will rollback the transaction """
        conn = objRollBack
        conn.rollback()
        print("Transaction rollback successful")
        