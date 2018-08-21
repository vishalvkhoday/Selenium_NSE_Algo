'''
Created on Aug 10, 2018

@author: khoday
'''

import pymssql
import urllib
import msvcrt
import urllib2
from urlparse import urlparse
from selenium import webdriver
import os
from time import sleep

driver = webdriver.Chrome('C:\\Python27\\chromedriver')

sql_Trnx_date = "select distinct CONVERT(varchar(12),Trnx_date,106) trnx_Dt from NSE_EOD where year(Trnx_date) ='2018' order by 1"

conn=pymssql.connect(user='sa', password='password', host='.\\SQLEXPRESS', database='StockQuote',port='1433')
cur = conn.cursor()
cur.execute(sql_Trnx_date)

# https://www.nseindia.com/content/historical/EQUITIES/2018/AUG/cm09AUG2018bhav.csv.zip
# https://www.nseindia.com/content/historical/EQUITIES/2018/AUG/cm01AUG2018bhav.csv.zip

ls_trn_dt = tuple(cur.fetchall())

for r in ls_trn_dt:
    print str(r[0]).strip()
    split_dt = str(r[0]).split()
    dd = split_dt[0]
    mm = str(split_dt[1]).upper()
    yy = split_dt[2]
    bhav_dt =str(r[0]).replace("", '')
    url = str('https://www.nseindia.com/content/historical/EQUITIES/'+yy+'/'+mm+'/'+'cm'+dd+mm+yy+'bhav.csv.zip')
    driver.get(url)
    sleep(3)
#     os.system('C:\\Users\\khoday\\workspace\\Selenium_AVIS\\Additonal_Utility\\Enter_alt4.vbs')
    
#     urllib.urlretrieve(url, "C://NSE_Bhav//"+"cm"+dd+mm+yy+"bhav.csv",reporthook=None, data=None)    
#     f =urllib.urlopen(url)
#     print f.read()
#     urllib2.urlopen(url, "C:\\NSE_Bhav\\"+"cm"+dd+mm+yy+"bhav.csv.zip")
#     urllib2.OpenerDirector.open(url, "C:\\NSE_Bhav\\"+"cm"+dd+mm+yy+"bhav.csv.zip")
    
