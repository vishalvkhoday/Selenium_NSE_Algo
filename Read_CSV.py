import cx_Oracle
import csv
# from _csv import reader, writer
import time
import datetime
import os
from openpyxl import Workbook

str_path = "C:\\Program Files (x86)\Manav\\NSE Tracker\\NSE Bhav Copy\\"

for scr_csvfile in os.listdir(str_path):
    print scr_csvfile
    #New_file = open(def_path,'a')
    with open (str_path+scr_csvfile,'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            str_col1 = str(row['SYMBOL']).strip()
            str_col2 = str(row['SERIES']).strip()
            
            split_row =str(row).strip()
            temp_split_col = split_row.split(',')
            int_noOfCol = len( split_row.split(','))
            
            x=1
            for x in range(int_noOfCol) :
                print temp_split_col[x]
            
            
    
    
