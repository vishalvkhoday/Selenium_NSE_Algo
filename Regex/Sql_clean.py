
import os
import pymssql



Conn = pymssql.connect(user='sa',password='password',host='.\\SQLEXPRESS',databases='StockQuote',port='1433')

