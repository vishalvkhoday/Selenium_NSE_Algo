'''
Created on Mar 8, 2012

@author: khoday
'''

#    Version 1.0 : Base version 
#    Version 1.2 : File handing with appropriate error message
#    Version 1.3 : Handling string length incase of any extra string write to error log.
#    Version 1.4 : Handling case sensetive 
#    Version 1.5 : Ignore session ID in the outbound mesage



import os
import  sys
import exceptions

def CheckLength (Base, C_code, fname):
    Base_length = len (Base)
    C_codeLen = len (C_code)
    if Base_length == C_codeLen :
        print "length of the file same"
        return 1
    else :
        print "File length failed please check file manually"
        if Base_length > C_codeLen :
            str_Basediff = Base[C_codeLen:Base_length]
            print str_Basediff
            Error_log(fname, "Extra text in Base line => \t" + str_Basediff)
            Check_Tag_value (Base, C_code, fname)
        
        else :
            str_C_coddiff = C_code[Base_length:C_codeLen]
            print str_C_coddiff
            Error_log(fname, "Extra text in  C code => \t" + str_C_coddiff)
            Check_Tag_value (Base, C_code, fname)
            
        return 0

def Check_tag (Base, C_code):
    Base_tag = Base.split('/')
    C_Code_tag = C_code.split('/')    
    Base_Tag_len = len(Base_tag)
    C_code_Tag_len = len(C_Code_tag)
    if Base_Tag_len == C_code_Tag_len :
        print "Tag length same Pass"
        return 1
    else :
        print "Tag length mismatch fail!!!"
        # ckh_tag = "Base_Code Tag length : " +Base_Tag_len +"\t\t"+"C_Code Tag length : "+ C_code_Tag_len 
        return 0 
        
    
def Check_Tag_value (Base, C_code, filename):
    Base_Outbound = Base.split('/')
    C_code_Outbound = C_code.split('/')
    Base_Outboundlen = len(Base_Outbound)
    C_code_Outboundlen = len(C_code_Outbound)
    OutBoundLen = 0
    if Base_Outboundlen > C_code_Outboundlen:
        OutBoundLen = C_code_Outboundlen
    else :
        OutBoundLen = Base_Outboundlen
    
    Tag_val_all = ''
    for OutBound_len in range (0, OutBoundLen) :
        try:
            Base_Tag = str(Base_Outbound[OutBound_len]).strip()
            C_code_Tag = str(C_code_Outbound[OutBound_len]).strip()
            Base_Tag = Split_tag(Base_Tag)
            C_code_Tag = Split_tag(C_code_Tag)
        except :
            print 'File length error verify manually !!!'
            break
        
        if len (Base_Tag) !=0 :            
            if  Base_Tag.upper() == C_code_Tag.upper() :
                print ("\n BaseLine : %s \t C Code : %s") % (Base_Tag, C_code_Tag)
            else:
                Tag_val = ("Actual :  %s \t Expected : %s") % (C_code_Tag, Base_Tag)
                Tag_val_all += Tag_val + '\n'
        else :
            continue
    
    if len(Tag_val_all) > 0:
        Error_log(filename, "Tag mismatch :\n" + Tag_val_all)
        return 0
    else:
        return 1

def Split_tag(Tag):
    Temp_tag = Tag.split('-')
    if Temp_tag[0].upper().strip() !='WZ':
        Temp_att = ''
        if (len (Temp_tag) > 1) :
            Temp_att = Temp_tag[0].strip() + '-' + Temp_tag[1].strip()
    #         print Temp_att
            return Temp_att
            
        else:
            return Tag
    
    else :
        Temp_att =''
        return Temp_att             

def Error_log(Fname, Err_Outbound):
    Err_file = open(Fname, "a")
    Err_file.write('\n***************************Error Log*************************** \n\n')
    Err_file.write(Err_Outbound + '\n\n')
    Err_file.close()
    
def log_transaction (Fname, Outbound_msg):
    Log_file = open(Fname, "a")
    Log_file.write('\n***************************Log*************************** \n\n\n')
    Log_file.write(Outbound_msg + '\n\n\n')
    Log_file.close()



msg = ''' The Following script will compare results of base code with C code
Before executing the script please place all the results file in the respective folder
ie Baseline in Baseline folder etc.... \n\n\n Usage :<baseline> <C Code> <Results>
'''

print msg

# Uncomment to execute in run more

# FPath= raw_input(" Enter Assembler Code path : ")
# C_Path= raw_input("\n Enter C Code path : ")
# Results=raw_input("\n Enter Results path :")
   

#    Uncomment to execute in the below path 

str_Path = 'C:\\Projects\\AVIS\\Wave_7\\Note_Pad_Wave_7\\Test\\'
FPath = str_Path + 'Base_line'
C_Path = str_Path + 'C_Code'
Results = str_Path + "Results"


if os.path.exists(Results) == False :
    os.mkdir(Results)

for filename in os.listdir(FPath) :
    if os.path.isdir(FPath + "\\" + filename) == True:
        break
    try:
        b_file = open(FPath + "\\" + filename)
        c_file = open(C_Path + "\\" + filename)
    except StandardError :
        print "File not found error %s !!!" % (filename)
        continue 

    while 1:
        try :
            line = b_file.readlines()
        except  StandardError:
            print "File read error !!!"
            break
        print str(line)
        if  len(line) == 0 :
            break
        else :
            Split1 = str(line).replace('\\n', '').replace('\r', '').replace('\t','').strip()
            print Split1
            split2 = str(Split1).replace('",', '')
            print split2
            split3 = str(split2).replace('\\', '').replace("'", "").replace(']', '').strip()
            print split3
            field = str(split3).strip().split(',')
            str_Baselint_Input_str = ""
            for i in range (0, (len(field))):
                if len(field[i].strip()) != 0 :
                    str_recom = field[i].strip().replace('  ', '')
                    str_Baselint_Input_str = str_Baselint_Input_str.strip() + str_recom.strip()                 
                    
#             print FPath+"\\"+filename+str_Baselint_Input_str
            str_Base_OutBound_Ind = str(str_Baselint_Input_str).find('OUTBOUND MESSAGE:')
            str_Base_OutBound = str_Baselint_Input_str[str_Base_OutBound_Ind:len(str_Baselint_Input_str)]
            print str_Base_OutBound
            
            
# C Code comparsion starts from here 
        
    while 1:
        try:
            C_line = c_file.readlines()
        except :
            print "File not found or error in reading !!!"
            # break
        print C_line
        if len(C_line) == 0:
            break
        else :
            c_Split1 = str(C_line).replace('\\n', '').replace('\r', '').strip()
            c_split2 = str(c_Split1).replace('",', '')
            c_split3 = str(c_split2).replace('\\', '').replace("'", "").replace(']', '').strip()
            c_field = str(c_split3).strip().split(',')
            str_C_code_Input_str = ""
            for i in range (0, (len(c_field))):
                if len(c_field[i].strip()) != 0 :
                    c_str_recom = c_field[i].strip().replace('  ', '')
                    str_C_code_Input_str = str_C_code_Input_str.strip() + c_str_recom.strip()
                
            str_C_code_OutBound_Ind = str(str_C_code_Input_str).find('OUTBOUND MESSAGE:')
            str_C_code_OutBound = str_C_code_Input_str[str_C_code_OutBound_Ind:len(str_C_code_Input_str)]
            print str_C_code_OutBound
                        
            # print C_Path+"\\"+filename+str_C_code_Input_str
            fname = str(Results + "\\Failed_" + filename)
            if CheckLength(str_Base_OutBound, str_C_code_OutBound, fname) == 0:
                Error_log(Results + "\\Failed_" + filename, "Check Length failed \n\n\n Base_Code :" + str_Base_OutBound + "\n\n\n C_Code :" + str_C_code_OutBound)
                print "Check length"
                break
            
            else :
                # log_transaction(Results+"\\Pass_"+filename,str_Base_OutBound,str_C_code_OutBound)
                str_Checklen_log = "Base_Code :" + str_Base_OutBound + "\n\n\n " + str_C_code_OutBound
                
                
            if Check_tag(str_Base_OutBound, str_C_code_OutBound) == 0 :
                Error_log(Results + "\\Failed_" + filename, "Check Tag failed \n\n\n Base_Code :" + str_Base_OutBound + "\n\n\n C_Code :" + str_C_code_OutBound)
                print "Check tag"
                break
            else :
                str_Checklen_log = "Base_Code :" + str_Base_OutBound + "\n\n\n" + str_C_code_OutBound
            
#             fname= str(Results+"\\Failed_"+filename)
            if Check_Tag_value(str_Base_OutBound, str_C_code_OutBound, fname) == 0:
                Error_log(Results + "\\Failed_" + filename, "Base_Code :" + str_Base_OutBound + "\n\n\n C_Code :" + str_C_code_OutBound)
            else :
                
                log_transaction(Results + "\\Pass_" + filename, "Base_Code :" + str_Base_OutBound + "\n\n\n C_Code :" + str_C_code_OutBound)
            
os.system('pause')
