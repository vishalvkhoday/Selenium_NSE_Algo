import cx_Oracle
import csv
# from _csv import reader, writer
import time
import datetime
import os
from pip._vendor.requests.exceptions import ConnectionError


print "Start"
respath = raw_input("Enter the path to save the report : ")
#res_path ='c:\\Test_results'
temp_dt=time.strftime("%c")
dt= str(temp_dt).replace('/','').replace(' ','').replace(':', '')
ttemp = datetime.datetime.now()
temp_filename = str(ttemp).replace('-', '_').replace(' ','_').replace(':', '')
temp_filename = temp_filename[0:15]
def_path =respath+"results_"+temp_filename+".txt"

if (os.path.exists(respath)) == False :
    os.mkdir(respath)
    

New_file = open(def_path,'a')

with open('C:\\Test_Sheet.csv','rb') as csvfile:
    reader = csv.DictReader(csvfile)        
    for row in reader:

        str_sql =str(row['SCR_SQL_Query']).strip()
        str_sqlDes = str(row['Description']).strip()
#         print str_sql
        try:
            con = cx_Oracle.connect('main_user','main_user','CCB20BZ3')
            cur = con.cursor()
            cur.execute(str_sql)
            
        except ConnectionError:
            print "Unable to connect to database please check the connection..."
            break
#         int_colLen= str(cur.description)
        print (str_sql)
        Full_colName =[]
        for col in range(len(cur.description)):
#             print cur.description[col]
            New_file = open(def_path,'a')
            Temp_str_colName = cur.description[col]
            str_colName = Temp_str_colName[0]
            
            Full_colName.append(str_colName)
        Col_header=str(Full_colName).replace("[","").replace("]","").replace("'", "")
        New_file.write('Description :'+str_sqlDes +"\n")
        New_file.write('SQL :' +str_sql+"\n\n")
        New_file.write(Col_header +"\n")
        Int_counter =0    
            
        for result in cur:
            if Int_counter< 8:    #set counter for number of records to write                        
                Dt_Rows =str(result).replace("(","").replace(")","")
                print(Dt_Rows)        
                New_file.write(Dt_Rows+"\n")
                Int_counter = Int_counter+1
            else:
                break
                
        tem_sep = "--*" * 100
        New_file.write("\n" +tem_sep+"\n\n")
        cur.close()
        con.close()
        New_file.close()
        print "\n\n\n\n"
print ("Execution completed!!!!")
    #SCR_Result    Tgt_Result