'''
Created on Aug 16, 2018

@author: khoday
'''

'''
Created on Mar 8, 2012

@author: khoday
'''

import os
#import datetime
import pymssql
#import _mssql 

conn=pymssql.connect(user='sa', password='password', host='.\\SQLEXPRESS', database='StockQuote',port='1433')
#conn=pymssql.connect(user='sa', password='password', host='KHODAY3\\SQLEXPRESS', database='StockQuote',port='1433')


#fpath = "D:\\Vishal\\NSE_EOD"
fpath = "c:\\test"
Pre_dt =''
for filename in os.listdir(fpath):
    file= open(fpath+"\\"+filename)
    cur = conn.cursor()
    Sql_preDt = ("""select top 1 trnx_date from NSE_EOD where Trnx_date in (
                        select distinct  top 2 (trnx_date)Trnx_Date from NSE_EOD order by Trnx_date desc)
                order by Trnx_date desc""")
    cur.execute(Sql_preDt)
    row = cur.fetchall()
    while row:
        Pre_dt= "%s" % (row[0])
        row = cur.fetchone()
                
    if Pre_dt == '':
        Pre_dt='2007/01/01'
               
    while 1:
        line =file.readline()
        if not line:
            break
        Templine_sp = str(line).strip()
        line_sp = Templine_sp.split(',')
        cklen = len(line_sp)
        if( cklen !=8):
            break
        else:
            tempDt= str(line_sp[1])
            yr =tempDt[0:4]
            MM=tempDt[4:6]
            DD=tempDt[6:8]
            Dt= yr.strip()+"/"+MM.strip()+"/"+DD.strip()
            script_name = str(line_sp[0])
            T_Open =str(line_sp[2])
            T_High =str(line_sp[3])
            T_Low=str(line_sp[4])
            T_Close=str(line_sp[5])
            T_Vol=str(line_sp[6])
            cur = conn.cursor()
            
            Sql_cmd= ("EXEC    [dbo].[NSE_EOD_Insert] @script = '%s', @Open = %s, @High = %s, @Low = %s, @Close = %s, @vol = %s, @Trn_date = '%s' ") %(script_name,T_Open,T_High,T_Low,T_Close,T_Vol,Dt)
            
            Sql_update = ("EXEC    [dbo].[Update_preClose] @ScriptName = '%s',@Pre_dt ='%s'") %(script_name,Pre_dt)
            
            Sql_Chg_update = ("update dbo.NSE_EOD set Change = round(((([Close] -Pre_Close  )/Pre_Close )*100),2) where Trnx_date= '%s' and Pre_Close != 0") %(Dt)
#            print Sql_cmd
            print (Sql_update)
#            print Sql_Chg_update
            Sql_Inst = """insert into DBO.Actual_NSE_EOD (Script_Name, [Open], High, Low, [Close], Volume, Pre_Close, Change, Trnx_date)
                select Script_Name, [Open], High, Low, [Close], Volume, Pre_Close, Change, Trnx_date from NSE_EOD where Trnx_date = (
                select max(Trnx_date) from dbo.NSE_EOD )"""
            cur.execute(Sql_cmd)
            cur.execute(Sql_update)
            #cur.execute(Sql_Chg_update)
            
    cur.execute(Sql_Chg_update)
    conn.commit() 
    cur.execute("EXEC    [dbo].[DMA5Days]")
    cur.execute("EXEC    [dbo].[DMA20Days]")
    cur.execute("EXEC    [dbo].[DMA50Days]")
    cur.execute(Sql_Inst)
#    cur.execute("EXEC     [dbo].[SP_Hotpick]")
    conn.commit()
    print filename           
print "End"
os.system('pause')