'''
Created on June 10, 2017

@author: khoday
'''

#    Version 1.0 : Base version 

import os
import sys
import exceptions
import openpyxl
import re
import datetime
from datetime import date


str_file_path = raw_input("Enter the path : ")
#str_file_path = "C:\\Users\\khoday\\workspace\\Python_codes\\Wave-8\\USCreate_Res_10072017"
int_file_cnt = 0
str_file_res = ""
if os.listdir(str_file_path):
    for str_file_name in os.listdir(str_file_path):
        file = open(str_file_path + "\\"+str_file_name,"r")
        #print str_file_name +"\t"
        try:
            f_file_line =file.readlines()
        except StandardError :
            print "unable to read the file ."
            continue     
        #print f_file_line
        str_file_content = str(f_file_line)
        str_Res_no = re.findall(r'RES NO.*', str_file_content, re.MULTILINE)
        #print str_Res_no
        if len(str_Res_no) > 0 :
            temp_res = str(str_Res_no).replace("\\n", "").split(",")
            str_get_res_no = temp_res[0].replace("\\", "").replace("[", "").replace('"','').replace("\'","").strip()
            #print str_file_name + "\t\t\t" + str(str_get_res_no) + "\n"
            int_file_cnt = int_file_cnt + 1
            
            str_file_res = str_file_res + str(int_file_cnt) +"\t\t" + str_file_name + "\t\t\t" + str(str_get_res_no) + "\n"
            file.close()
    print str_file_res
    print "end"
    str_filepart = str(datetime.datetime.now())
    str_filepart=  str_filepart.replace(" ","").replace(":", "").replace(".","")
    str_file_path = str_file_path+"\\"+"Res_list.txt"
    file_res = open(str_file_path,"w+")
    file_res.write(str_file_res)
    file_res.close()
    
     
