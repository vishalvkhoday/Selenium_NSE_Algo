'''
Created on Aug 8, 2018

@author: khoday
'''
import pymssql
import datetime
from datetime import timedelta
import time
import os



class Stock_info():
    def __init__(self,script="",st_High_dt="",st_Low_dt=""):
        self.script =script
        self.st_High_dt=st_High_dt
        self.st_Low_dt=st_Low_dt
        
        
    def get_Pattern(self,script,obj,f_Path):
        try:
            f_status =os.path.exists(f_Path+'Stock_pattern.txt')
        
        except:
            print ('unexpected error')
        if f_status == True:
            trend_file = open(f_Path+'Stock_pattern.txt','a')
        else:
            trend_file = open(f_Path+'Stock_pattern.txt','w')
        print'Execute script individually {} '.format(script)        
        ind_stock =obj.connect_DB()        
        ini_Opn = int(ind_stock[0][1])
        ini_high = int(ind_stock[0][2])
        ini_low = int(ind_stock[0][3])
        ini_cls = int(ind_stock[0][4])
        end_Opn = int(ind_stock[1][1])
        end_high = int(ind_stock[1][2])
        end_low = int(ind_stock[1][3])
        end_cls = int(ind_stock[1][4])
        st_Opn = int(ind_stock[2][1])
        st_High = int(ind_stock[2][2])
        st_low = int(ind_stock[2][3])
        st_cls = int(ind_stock[2][4])
        ls_Opn = int(ind_stock[3][1])
        ls_high = int(ind_stock[3][2])
        ls_low = int(ind_stock[3][3])
        ls_cls = int(ind_stock[3][4])
        
        st_High_dt =  str(ind_stock[2][8]).strip()
#         spl_st_High_dt =st_High_dt.split('-')        
        st_Low_dt = str(ind_stock[3][8]).strip()
#         spl_st_Low_dt = st_Low_dt.split('-')
#         H_day = datetime.datetime(int(spl_st_High_dt[0]),int(spl_st_High_dt[1]),int(spl_st_High_dt[2]))
#         L_day = datetime.datetime(int(spl_st_Low_dt[0]),int(spl_st_Low_dt[1]),int(spl_st_Low_dt[2]))
#         
#         day_Diff =(L_day-H_day).days
        res_dt_Diff = self.date_Diff_res(st_High_dt,st_Low_dt)

        avg_opn =(ini_Opn +end_Opn+st_Opn+ls_Opn)/4
        avg_hig =(ini_high+end_high+st_High+ls_high)/4
        avg_low =(ini_low+end_low+st_low+ls_low)/4
        avg_cls =(ini_cls+end_cls+st_cls+ls_cls)/4
        trnd = ""
        if res_dt_Diff <=0:
            print str(ind_stock[0][0]) +', Down Trend \n'
            trend_file.write(str(ind_stock[0][0]) +', Down Trend \n')
            trnd ='Down Trend'
        else:
            print str(ind_stock[0][0]) + ', Up Trend \n'
            trend_file.write(str(ind_stock[0][0]) +', Up Trend \n')
            trnd = 'Up Trend'
            
        trend_file.close()
        return trnd
        
    def date_Diff_res(self,frm_Dt,to_Dt):
        spl_frm_Dt = frm_Dt.split('-')
        spl_to_Dt = to_Dt.split('-')
        
        dt_frm_Dt = datetime.datetime(int(spl_frm_Dt[0]),int(spl_frm_Dt[1]),int(spl_frm_Dt[2]))
        dt_to_Dt = datetime.datetime(int(spl_to_Dt[0]),int(spl_to_Dt[1]),int(spl_to_Dt[2]))
        
        dt_Diff =  (dt_frm_Dt-dt_to_Dt)
        return (dt_Diff).days
            
        
        
        
        
class DB_operation():
    
    def __init__(self,execute_sql=""):
        self.execute_sql = execute_sql
        
    def connect_DB(self):
        conn = pymssql.connect(user='sa', password='password', host='.\\SQLEXPRESS', database='StockQuote',port='1433')
        cur = conn.cursor()
        cur.execute(self.execute_sql)
        ls_all_Row =cur.fetchall()
#         time.sleep(1)
#         conn.close()
        return tuple(ls_all_Row)
    def Insert_data(self):
        conn = pymssql.connect(user='sa', password='password', host='.\\SQLEXPRESS', database='StockQuote',port='1433')
        cur = conn.cursor()
        cur.execute(self.execute_sql)
        conn.commit()

    
f_Path = "c:\\test\\"
stockInfo = Stock_info()
db = DB_operation('EXEC     [dbo].[Alog_List_Stock]')
 
obj_all_row =db.connect_DB()
up_Tr_cnt = 0
dw_Tr_cnt = 0
for ls_row_stock in obj_all_row:
    script_code = str(ls_row_stock[0]).strip()
    st_pattern = DB_operation("EXEC     [dbo].[Alog_Patterns] @Coname = '"+script_code+"'")
    rep_trend =stockInfo.get_Pattern(script_code,st_pattern,f_Path)
     
    if rep_trend =='Up Trend':
        up_Tr_cnt+=1
    else:
        dw_Tr_cnt+=1      
         
         
     
print ('Completed Total Up Trend = %d & Down trend = %d') %(up_Tr_cnt,dw_Tr_cnt)
        
    
    
        

    

    