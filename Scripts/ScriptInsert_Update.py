'''
Created on Jul 13, 2018

@author: khoday
'''

import pytest
from DB_Operation import DB_Operation
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os
import datetime


    

options = webdriver.ChromeOptions()
options.add_argument("disable-infobars")
options.add_argument("start-maximized")
# options.add_argument("headless")
# driver = webdriver.Chrome(chrome_options=chrome_options)
driver = webdriver.Chrome(chrome_options=options,executable_path='C:/Users/DELL/git/Selenium_NSE_Algo/Additonal_Utility/chromedriver_242', service_args=["--verbose", "--log-path=C:/Users/DELL/git/Selenium_NSE_Algo/Additonal_Utility/Script.log","w+"])
driver.get("https://www.moneycontrol.com/")


def Navigate_ScriptPage(scr,INIE):
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"(//input[@id='search_str'])[1]")), "Waiting for search textfield...")
        driver.find_element_by_xpath("(//input[@id='search_str'])[1]").click()
        driver.find_element_by_xpath("(//input[@id='search_str'])[1]").send_keys(INIE)
        ActionChains(driver).send_keys(Keys.ENTER).perform()
        wait = WebDriverWait(driver, 10)
        if driver.find_element_by_xpath('//*[@id="proceed-button"]').is_displayed() ==True:
            driver.find_element_by_xpath('//*[@id="proceed-button"]').click()
            # if driver.find_element_by_xpath("//p[@class='b_20 PT10 FL']").is_displayed() ==True :
            #     return False
            
            WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"(//ul[@class='comdetl'])[3]/li[4]/p[1]")), "Waiting for page")
            expINIE = driver.find_element_by_xpath("(//ul[@class='comdetl'])[3]/li[4]/p[1]").get_attribute('innerText')
            print("Actual {} vs Expected {}".format(INIE, expINIE))
            return True
            
    except:
        try:
            driver.find_element_by_xpath("(//input[@id='search_str'])[1]").click()
            driver.find_element_by_xpath("(//input[@id='search_str'])[1]").send_keys(scr)
            ActionChains(driver).send_keys(Keys.ENTER).perform()
            wait = WebDriverWait(driver, 10)
            if driver.find_element_by_xpath('//*[@id="proceed-button"]').is_displayed() ==True:
                driver.find_element_by_xpath('//*[@id="proceed-button"]').click()
            WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"(//ul[@class='comdetl'])[3]/li[4]/p[1]")), "Waiting for page")
            expINIE = driver.find_element_by_xpath("(//ul[@class='comdetl'])[3]/li[4]/p[1]").get_attribute('innerText')
            if INIE == expINIE :
                print(expINIE)
                return True
            else:
                return False
                
        
            
        except Exception as e:
            print (e)
            if driver.find_element_by_xpath('//*[@id="proceed-button"]').is_displayed() ==True:
                driver.find_element_by_xpath('//*[@id="proceed-button"]').click()
                WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"(//input[@id='search_str'])[1]")), "Waiting for search textfield...")
            return False
    

def objExist(obj):
    try:
        obj.is_displayed()
        return True
    except NoSuchElementException:
        return False

def clear_Temp ():
    try:
        os.system('del /f/s/q %temp%\*')
    except AssertionError as ae:
        print('Unable to delete temp files')

def getScriptName():
    get_script="select * from tbl_ShareHolderScriptList where ToExecute='Yes' and IsLocked='No' order by Script_Name"
    objDb =DB_Operation(get_script)
    ArryScrLst = objDb.db_select()
    return ArryScrLst
def WinHandlers():
    arrWin =driver.window_handles
    if len(arrWin)>1:
        driver.switch_to_window(arrWin[1])
        driver.close()
        driver.switch_to_window(arrWin[0])


sqlTablereset ="update tbl_ShareHolderScriptList set IsLocked='No' where ToExecute='Yes'"
objTblreset = DB_Operation().db_ConnectionObject()
DB_Operation().Update_data(objTblreset,sqlTablereset)
DB_Operation().sqlCommit(objTblreset)
while(True):
    try:
        WinHandlers()
        script_name = getScriptName()
        if script_name ==None:
            print("No more script to execute")
            sqlTablereset ="update tbl_ShareHolderScriptList set IsLocked='No' where ToExecute='Yes'"
            objTblreset = DB_Operation().db_ConnectionObject()
            DB_Operation().Update_data(objTblreset,sqlTablereset)
            DB_Operation().sqlCommit(objTblreset)
            break
        else:
            sql_UpdateLock = "update tbl_ShareHolderScriptList set IsLocked='Yes' where Script_Name = '{}'".format(script_name[0])
            ObjUpdatelock = DB_Operation().db_ConnectionObject()
            DB_Operation().Update_data(ObjUpdatelock,sql_UpdateLock)
            DB_Operation().sqlCommit(ObjUpdatelock)
            if Navigate_ScriptPage(script_name[0],script_name[1]) == True:
                sector =driver.find_element_by_xpath('//*[@id="stockName"]/span[1]/strong/a[1]').get_attribute('innerText')
                print(sector)
                sqlSector = "update sector set sector = '{}' where ISIN='{}' ".format(sector,script_name[1])
                objSectorUpdate = DB_Operation().db_ConnectionObject()
                DB_Operation().Update_data(objSectorUpdate,sqlSector)
                DB_Operation().sqlCommit(objSectorUpdate)
                print (sqlSector)
                sqlExecuteFlag = "update tbl_ShareHolderScriptList set ToExecute='No' where Script_Name = '{}'".format(script_name[0])
            elif Navigate_ScriptPage(script_name[0],script_name[1]) == False: 
                sqlExecuteFlag = "update tbl_ShareHolderScriptList set ToExecute='Yes' where Script_Name = '{}'".format(script_name[0])
            sqlUpdateEXE = DB_Operation().db_ConnectionObject()
            DB_Operation().Update_data(sqlUpdateEXE,sqlExecuteFlag)
            DB_Operation().sqlCommit(sqlUpdateEXE)
                
    except:
        try:
            if driver.find_element_by_xpath('//*[@id="proceed-button"]').is_displayed() ==True:
                driver.find_element_by_xpath('//*[@id="proceed-button"]').click()
        except:
            continue
        

    
    
if __name__ =="__main__":
    getScriptName()