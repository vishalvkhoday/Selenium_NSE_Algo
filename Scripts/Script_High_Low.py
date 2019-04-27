from Algo_classes import DB_Operation
from datetime import datetime
from datetime import date
 

def Date_diff(script):
    h_dt = str(script[2]).split("-")
    l_dt = str(script[4]).split("-")
    frnt_H_dt = date(int(h_dt[0]),int(h_dt[1]),int(h_dt[2]))
    frnt_L_dt = date(int(l_dt[0]),int(l_dt[1]),int(l_dt[2]))
    days_diff = (frnt_H_dt-frnt_L_dt).days
    return days_diff


def DB_select(sql_query):
    DB = DB_Operation(sql_query)
    scr =DB.db_select()
    return tuple(scr)
    



sql_hig_low = """
select sh.script_name,sh.High,sh.Trnx_date High_Dt,sl.Low,sl.Trnx_date Low_dt  from script_high sh inner join Script_Low sl on
sl.script_name = sh.script_name
where sh.script_name not in('LIQUIDETF','ICICINXT50','ICICIMCAP','_ADVANCE','_DECLINE','_UNCHANGED')
and sh.trnx_date >=getdate()- 200
"""
down_list = {}
up_list = {}
dt_frmt = "%YYYY%mm%dd"

All_script = DB_select(sql_hig_low)
for script in All_script:
    days_diff=Date_diff(script)
    scr_sql_hig_low =sql_hig_low + " and sh.script_name = '{}'".format(str(script[0]))
    if (days_diff)>=1:
        if str(script[0]) not in  up_list:
            up_list.update({str(script[0]):str(days_diff)})
            print("Script name : {} in uptrend".format(script[0]))
            scr_res = DB_select(scr_sql_hig_low)
            if (len(scr_res))>1:
                print("Script as multiple values: \n{}".format(scr_res))
            else:
                print("Script has single value \n{}".format(scr_res))
                
    else:
        if str(script[0]) not in down_list:                        
            down_list.update({str(script[0]):str(days_diff)})
            print("Script name : {} in downtrend".format(script[0]))
            scr_res = DB_select(scr_sql_hig_low)
            if (len(scr_res))>1:
                print("Script as multiple values \n{}".format(scr_res))
            else:
                print("Script has single value \n{}".format(scr_res))


with open ("C:\\Data_Backup\\scriptName.json","w+") as file:
    up_f_wrt = str(up_list).replace("'", '"')
    dw_f_wrt = str(down_list).replace("'",'"')
    file.write('{"Up List category":'+up_f_wrt+',\n"Downlist":'+dw_f_wrt+'}')
    
