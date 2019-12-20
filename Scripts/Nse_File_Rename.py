'''
Created on Nov 29, 2019

@author: DELL
'''

import os 
 
 
def GetMonth(Month):
    if Month =='JAN':
        return '01'
    elif Month =='FEB':
        return '02'
    elif Month =='MAR':
        return '03'
    elif Month =='APR':
        return '04'
    elif Month =='MAY':
        return '05'
    elif Month =='JUN':
        return '06'
    elif Month =='JUL':
        return '07'
    elif Month =='AUG':
        return '08'
    elif Month =='SEP':
        return '09'
    elif Month =='OCT':
        return '10'
    elif Month =='NOV':
        return '11'
    elif Month =='DEC':
        return '12'
    
    
    
filPath = 'C:/Users/DELL/Downloads/NSE EOD Data Downloader v3.3/Equity'
allFiles=os.listdir(filPath) 
for fil in allFiles :
    try:
        if str(fil).startswith('EQ_')==True:        
            yrs = str(fil[8:len(fil)])
            yrs = yrs.replace('.txt', '')
            mon = fil[5:8]
            mon = str(mon).upper()
            monVal = GetMonth(mon)
            dd = fil[3:5]            
            newfil = (str(yrs)+str(monVal)+str(dd)+'.txt')
            print (fil+"\t\t"+newfil)
            os.rename(filPath+'/'+fil, filPath+'/'+newfil)
        
        elif str(fil[2:5]).isalpha()==True: # and len(fil)==13
            yrs = str(fil[5:len(fil)])
            yrs = yrs.replace('.txt', '')
            mon = fil[2:5]
            mon = str(mon).upper()
            monVal = GetMonth(mon)
            dd = fil[0:2]            
            newfil = (str(yrs)+str(monVal)+str(dd)+'.txt')
#             print (fil+"\t\t"+newfil)
            print("Old file name {} new file name {}".format(fil,newfil))
            os.rename(filPath+'/'+fil, filPath+'/'+newfil)
        
        else:
            print(fil)
    except:
        print("duplicate file found removed {}".format(fil))
        os.remove(filPath+'/'+fil)
    
