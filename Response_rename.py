'''
Created on Apr 12, 2012

@author: khoday
'''
import os
import datetime
import string
import zipfile

Filepath ="C:\\GetNewCoMigrationStatus\\"
rr= string.capitalize("sssssss")
for filename in os.listdir(Filepath):
    f = open (Filepath + filename,'r')
    for line in f.readlines():
        print line
    
    
    print file
 