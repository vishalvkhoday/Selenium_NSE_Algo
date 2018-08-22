'''
Created on June 13, 2017

@author: khoday
'''

#    Version 1.0 : Base version 

import os
import sys
import exceptions
import re


str_path = "C:\\Wave-8"
str_basefile = "C:\\Wave-8\\Base_File\\"
str_new_code = "C:\\Wave-8\\New_Code\\"
str_results = str_path + "\\Results"


def format_file(fileinfo):
    str_File = fileinfo
    print filename
    


if os.path.exists(str_results) == False:
    os.mkdir(str_results)
    
if os.listdir(str_basefile):
    str_full_base_msg=''
    for file in os.listdir(str_basefile):
        
        try:                
            f_base_file = open(str_basefile + file)
            l_basefile = f_base_file.readlines()
            
            f_NewCode_file = open (str_new_code + file)
            l_NewCode = f_NewCode_file.readlines()
            
            int_base_f_len = len(l_basefile)
            int_NewC_f_len = len(l_NewCode)
            
            if int_base_f_len > int_NewC_f_len :
                iter = int_base_f_len
            else:
                iter = int_NewC_f_len
            
            x=0
            for x in range(iter):
                #print l_basefile[x]
                #print l_NewCode[x]
                try:
                    str_base_line = str(l_basefile[x])
                except:
                    str_base_line=""
                
                try:
                    str_NewCode_line = str(l_NewCode[x])
                except :
                    str_NewCode_line=""
                
                str_Base_res = re.findall(r'(RES NO.*)', str_base_line,re.IGNORECASE)
                str_New_res = re.findall(r'(RES NO.*)',str_base_line,re.IGNORECASE)
                
                
                if str_Base_res:
                    for b_res in str_Base_res:
                        #print b_res
                        print str(l_basefile[x]).replace(b_res,'')
                        
                
                if str_New_res:
                    for n_res in str_New_res:
                        #print n_res
                        print str(l_basefile[x]).replace(n_res, '')       
                
                
                
                
                if l_basefile[x] != l_NewCode[x] :
                    print " Expected : %s \n Actual : %s" %(str_base_line,str_NewCode_line)
                
                str_full_base_msg = str(str_full_base_msg)+"\n"+str(str_base_line)
            
            # print str_newCode_cont
            print "\n\n\n%s file complete -" %(file)
            print str_full_base_msg
            
            print "**/"*20
            
            f_base_file.close()
            f_NewCode_file.close()
        except :
            print "file not found or unable to read file :-\t %s" % (file)
            continue
    
