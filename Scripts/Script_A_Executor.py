'''
Created on Jan 25, 2019

@author: DELL
'''

import os
import time
from selenium import webdriver

for i in range(1,15):
    os.system('python C:/Users/DELL/git/Selenium_NSE_Algo/Scripts/Script_A.py')
    time.sleep(300)
#     driver = webdriver.Chrome(executable_path='C:/Users/DELL/git/Selenium_NSE_Algo/Additonal_Utility/chromedriver_242')
#     driver.quit()
    os.system("taskkill /im Chrome.exe /f")
    