
import re
import os




file1 = open("C:\\Wave_8_Reservation_Transactons-DC_Wave8_AVIS_CR001-CR_ECAR_Daily-0-FAILED.txt")
F1_all = str(file1.readlines())
print F1_all

str_res_text = "---------------- Response --------------------------"
int_res_ind = F1_all.find(str_res_text)
intfilelen = len(F1_all)
str_resp = F1_all[int_res_ind+55:intfilelen]
print str_resp

str_getConfid = re.findall(r'<Conf.*', str_resp, re.MULTILINE)
if str_getConfid:
    for ConfID in str_getConfid:
        ConfID = str(ConfID.strip().split('\n'))
        print ConfID[3:27]
    

marchObj2 = re.findall(r'<ConfID ID=".*', F1_all, re.MULTILINE)
counter = 0
if marchObj2:
    for x in marchObj2:
        print str(len(x.strip(' '))) + "\t" + x
        print "|---"*15
        counter = counter + 1
    print counter
else:
    print "Nothing matched in marchObj2"
