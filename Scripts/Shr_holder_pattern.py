'''
Created on Jul 24, 2018

@author: khoday
'''

from selenium import webdriver


driver = webdriver.Chrome('C:\\Python27\\chromedriver')

x_shr_tbl = '//*[@id="acc_hd7"]/div/div[1]/table'
id_shr_prt = 'acc_pm7'

driver.get('https://www.moneycontrol.com/india/stockpricequote/auto-ancillaries/shanthigears/SG04')

driver.find_element_by_id(id_shr_prt).click()
sh_Prnt_tbl =driver.find_element_by_xpath(x_shr_tbl).get_attribute('innerText')
sh_Prnt_tbl_ary = sh_Prnt_tbl.split('\n')
for sh_row in sh_Prnt_tbl_ary:
    print sh_row 