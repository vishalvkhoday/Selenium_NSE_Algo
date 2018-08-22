'''
Created on Jun 19, 2018

@author: khoday
'''


try:
    alist = [1,2,3,4,5]
    print alist[5]
    
except IndexError:
    print ("Index doest not exist")
except:
    print("Unknown error")