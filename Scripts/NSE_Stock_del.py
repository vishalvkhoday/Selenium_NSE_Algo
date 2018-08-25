'''
Created on Aug 11, 2018

@author: khoday
'''
from selenium import webdriver
# import unittest
from datetime import date
# from Algo_Patterns import DB_operation
import time

from openpyxl import Workbook
from openpyxl.reader.excel import load_workbook

xl_F_name ='C:\\Users\\khoday\\workspace\\Selenium_AVIS\\Additonal_Utility\\Top_script.xlsx'
Wb =load_workbook(xl_F_name)
Ws=Wb.get_sheet_by_name('Sheet1')

scr_row = Ws.max_row
# db = DB_operation('EXEC     [dbo].[Alog_List_Stock]')
# script =db.connect_DB()


driver = webdriver.Chrome('C:\\Python37\\chromedriver')
nse_Del_url = 'https://www.nseindia.com/products/content/equities/equities/eq_security.htm'
x_txt_symbol = '//*[@id="symbol"]'
x_bt_GetData = '//*[@id="get"]'
x_rd_bt_duration ='//*[@id="rdDateToDate"]'
x_cal_From_Dt = '//*[@id="fromDate"]'
x_cal_To_Dt = '//*[@id="toDate"]'
x_cal_From_Dt_month = '//*[@id="ui-datepicker-div"]/div/div/select[1]'
x_cal_text = '//*[@id="fromDate"]'
x_lk_dt_file = '//*[@id="historicalData"]/div[1]/span[2]/a'

end_Dt= str(date.today()).split('-')
driver.maximize_window()
driver.get(nse_Del_url)
driver.set_page_load_timeout(5)
driver.find_element_by_xpath(x_rd_bt_duration).click()
pic_dt_from =driver.find_element_by_xpath(x_cal_From_Dt)
pic_dt_from.send_keys('01-01-2018')
pic_dt_to = driver.find_element_by_xpath(x_cal_To_Dt)
pic_dt_to.send_keys(end_Dt[2]+'-'+end_Dt[1]+'-'+end_Dt[0])

for x in range(2,scr_row):
    try:
        script = Ws[str('A' + str(x))].value
        exe_st = Ws[str('C' +str(x) )].value
        if exe_st =='Yes':            
            driver.find_element_by_xpath(x_txt_symbol).click()
            driver.find_element_by_xpath(x_txt_symbol).clear()
            driver.find_element_by_xpath(x_txt_symbol).send_keys(script)    
            driver.find_element_by_xpath(x_bt_GetData).click()
            driver.set_page_load_timeout(2)
            time.sleep(5)
            driver.find_element_by_xpath(x_lk_dt_file).click()
            Ws['C' +str(x) ]= str('No')
            print ('{} download completed'.format(script))
            
            Wb.save(xl_F_name)
        else:
            continue
    except:
        continue
print('Done')

