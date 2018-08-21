'''
Created on Aug 14, 2018

@author: khoday
'''

from Algo_classes import DB_Operation
from Algo_classes import Stock_Info
import os

st_Pick_path = 'c:\\vishal\\Stock_pickup.txt'
f_status = os.path.exists(st_Pick_path)


if f_status == False:
    st_pick_file = open(st_Pick_path,'w')
    st_pick_file.write('Scriptname,Change,Recovered,Std_Div_Val,Last_close,comments\n')
else:
    st_pick_file = open(st_Pick_path,'a')
    

SI = Stock_Info()
DB = DB_Operation('EXEC     [dbo].[Alog_List_Stock]')
row =DB.db_select()
up_stock_cnt = 0
dw_Stock_cnt = 0
for x in row:
    str_script_name= str(x[0])
    stk_Pattern = DB_Operation("EXEC     [dbo].[Alog_Patterns] @Coname = '"+str_script_name+"'")
    stk_Row = stk_Pattern.db_select()
    st_H_Dt= str(stk_Row[2][8])
    st_L_Dt =str(stk_Row[3][8])
    st_L_cls = float(stk_Row[3][4])
    end_cls = float(stk_Row[1][4])
    end_Dt = str(stk_Row[1][8])
    Hi_cls = float(stk_Row[2][4])
    days_Diff =SI.date_Diff(st_H_Dt, st_L_Dt)
    start_Dt = str(stk_Row[0][8])
    end_Dt = str(stk_Row[1][8])
    chg_age = 0
    print 'Stock analysis of  {} Started!!!'.format(str_script_name)
    if days_Diff >= 0:
        chg_age =float(end_cls-st_L_cls)/st_L_cls * 100
        chg_age = ("%.2f")%chg_age
        dw_Stock_cnt = dw_Stock_cnt+1
        if float(chg_age) >= 20:
            sql_low_to_cls= str("select count(*)Duration from NSE_EOD where Script_Name ='" + str_script_name+"' and Trnx_date >= '" + st_L_Dt +"'")
            low_to_cls = DB_Operation(sql_low_to_cls)
            low_to_cls_Diff = low_to_cls.db_select()
            Hi_low_recovery = float(Hi_cls - end_cls)/Hi_cls * 100 
            Hi_low_recovery = ("%.2f")% Hi_low_recovery
            sql_std_div = str("select round(avg([close]),2) from NSE_EOD where  Script_Name ='" + str_script_name+"' and Trnx_date between '" +st_H_Dt +"' and '"+st_L_Dt+"'")          
            std_Div = DB_Operation(sql_std_div)
            std_Div_Val = std_Div.db_select()
            if float(std_Div_Val[0][0]) < float(end_cls):
                std_Div_age = float(end_cls - float(std_Div_Val[0][0]))/float(std_Div_Val[0][0])*100
                if float(std_Div_age) <=10 :
                    try:
                        str_msg = str(str_script_name +','+str(chg_age)+','+str(Hi_low_recovery)+ ','+str(std_Div_Val[0][0])+','+str(end_cls))
                        st_pick_file.write(str_msg+'\n')
                        print 'Stock analysis of  {} completed!!!'.format(str_script_name)
                        str_msg=""
#                         st_pick_file.close()
                    except:
                        st_pick_file.close()
            
            
    else:
        up_stock_cnt =up_stock_cnt+1
        chg_age =float(Hi_cls -end_cls)/end_cls * 100
        chg_age = ("%.2f")%chg_age
        if float(chg_age) <= 20:
            sql_Hi_to_cls= str("select count(*)Duration from NSE_EOD where Script_Name ='" + str_script_name+"' and Trnx_date >= '" + st_L_Dt +"'")
            Hi_to_cls = DB_Operation(sql_Hi_to_cls)
            Hi_to_cls_Diff = Hi_to_cls.db_select()
            int_Dur = SI.date_Diff(st_H_Dt, end_Dt)
            if int_Dur <= 5 :
                comments = str("currently trading at High during scanned duration from " +start_Dt + " To " + end_Dt)
#                 print  comments
                str_msg = str(str_script_name +','+str(chg_age)+','+str(Hi_to_cls_Diff[0][0])+ str(',0,')+str(end_cls)+comments)
                
                try:
                    st_pick_file.write(str_msg+'\n')
                    print 'Stock analysis of  {} completed!!!'.format(str_script_name)
                    str_msg=""

                except :
                    st_pick_file.close()
                    
                    
                

        
        elif float(chg_age)>=21 and float(chg_age)<=40:
            print('')    
        
st_pick_file.close()            
print('Completed')