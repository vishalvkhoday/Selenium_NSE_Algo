'''
Created on Aug 10, 2018

@author: khoday
'''


#from cPAMIE import PAMIE
import string 
import msvcrt
import urllib
 

#ie = PAMIE()
for i in range (1,31):
    url = 'http://www.nseindia.com/content/historical/EQUITIES/2018/MAY/'
    #url = 'http://nseindia.com/archives/equities/mto/MTO_09042008.DAT'
    if i < 10:
        i = str(i)
        #print(url+'0'+i+'012007'+'.DAT')
        #ie.navigate(url+'cm0'+i+'SEP2007bhav.csv')
        url1 = str(url+'cm0'+i+'MAY2018bhav.csv')
        try:
            # urllib.urlretrieve(url1,"C:\\NSE_Bhav\\"+i+'MAY.txt')
            urllib.urlretrieve(url1,'C:\\NSE_Bhav\\'+i+'MAY.txt')
            #ie.navigate(url+'cm0'+i+'MAY2006bhav.csv')
        except:
            break
        i = int(i)     
    if i >=10 :
        i = str(i)
        url1 = str(url+'cm'+i+'MAY2018bhav.csv')
        try:
            #ie.navigate(url+'cm'+i+'MAY2006bhav.csv')
            urllib.urlretrieve(url1,"C:\\NSE_Bhav\\"+i+'MAY.txt')
        except:
            break
    
print "Task Completed !!!"
#    if ( ie.findText('The webpage cannot be found') == True):
#            exit
#   
#ie.quit()


