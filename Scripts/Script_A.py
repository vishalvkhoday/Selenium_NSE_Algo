'''
Created on Jul 13, 2018

@author: khoday
'''

import  time
from selenium import webdriver
from openpyxl import load_workbook
import os
import shutil
import datetime

def Table_Value (str_val):
    temp_tble_Val = str(str_val).split('\\n')
    temp_tble_Val = str(temp_tble_Val[0]).replace('\\n\\n', '').split('\n')
    temp_str = ""
    for i in temp_tble_Val:
        if len(str(i).strip()) > 0:
            i = str(i).strip()
            temp_str += i + '\n'
    return temp_str


def clear_Temp ():
    temp_path = 'C:\\Users\\khoday\\AppData\\Local\\Temp\\'
    ls_dir = os.listdir(temp_path)
    for fol in ls_dir:
        try:
            shutil.rmtree(temp_path + fol)            
        except OSError as e:
#             print (e.filename + '\t' + e.strerror)
            continue

def get_Sector():
    Head_Inner_Val = driver.find_element_by_class_name('PB10').get_attribute('innerText')
    splt_header = str(Head_Inner_Val).split('|')
    t_bse_code = str(splt_header[0]).split(':')
    bse_code = str(t_bse_code[1]).strip()
    t_nse_code = str(splt_header[1]).split(':')
    nse_code = str(t_nse_code[1]).strip()    
    t_ISIN = str(splt_header[2]).split(':')
    ISIN = str(t_ISIN[1]).strip()    
    t_sector = str(splt_header[3]).split(":")
    Sector = str(t_sector[1]).strip()
    print (splt_header)    
    return Sector

def Stock_info (str_tbl,f_Name):    
    Ws = Wb['Sheet1']
    try:
        Tbl_InnerText_Val = driver.find_element_by_id(str_tbl).get_attribute('innerText')
    except:
        quit
    All_val = Table_Value(Tbl_InnerText_Val)
#     print All_val
    spt_All_val = str(All_val).split('\n')
    M_cap = str(spt_All_val[0]).strip()
    M_cap = str(M_cap.replace('MARKET CAP (RS CR)', '')).strip()        
    PE = str(spt_All_val[1]).strip()
    PE = str(PE.replace('P/E', '')).strip()
    Bookvalue = str(spt_All_val[2]).strip()
    Bookvalue = str(Bookvalue.replace('BOOK VALUE (RS)', '')).strip()
    Div = str(spt_All_val[3]).strip()
    Div = str(Div.replace('DIV (%)', '')).strip()
    Ind_PE = str(spt_All_val[5]).strip()
    Ind_PE = str(Ind_PE.replace('INDUSTRY P/E', '')).strip()
    EPS = str(spt_All_val[6]).strip()
    EPS = str(EPS.replace('EPS (TTM)', '')).strip()        
    Face_val = str(spt_All_val[10]).strip()
    Face_val = str(Face_val.replace('FACE VALUE (RS)', '')).strip()
    Sector = get_Sector()         
    Ws['C' + str(row)] = M_cap
    Ws['D' + str(row)] = EPS
    Ws['E' + str(row)] = PE
    Ws['F' + str(row)] = ''
    Ws['G' + str(row)] = Bookvalue
    Ws['I' + str(row)] = Div
    Ws['K' + str(row)] = Face_val
    Ws['L' + str(row)] = Ind_PE
    Ws['M' + str(row)] = Sector
    Ws['N' + str(row)] = 'No'
#     Wb.save(f_Name)
    M_cap = ""
    EPS = ""
    PE = ""
    Bookvalue = ""
    Div = ""
    Face_val = ""
    Ind_PE = ""
    Sector = ""

def ShareHolding(f_Name):
    driver.find_element_by_id(id_shr_prt).click()
    driver.set_page_load_timeout(1)
    sh_Prnt_tbl =str(driver.find_element_by_xpath(x_shr_tbl).get_attribute('innerText').strip())
    sh_Prnt_tbl_ary = str(sh_Prnt_tbl).split('\n')
    r_count = ws_Shr.max_row
    r_count = r_count+1
    for i in range(0,4):
        Col = str(sh_Prnt_tbl_ary[i]).split('\t')
        if len(Col) ==4 :
            try:
                ws_Shr['A'+str(r_count)] = str(Script_code)
                ws_Shr['B'+str(r_count)] = Col[0]
                ws_Shr['C'+str(r_count)] = Col[1]
                ws_Shr['D'+str(r_count)] = Col[2]
                ws_Shr['E'+str(r_count)] = Col[3]
                r_count = r_count+1
            except:
                r_count = r_count+1
                continue
        elif len(Col)==3:
            try:
                ws_Shr['A'+str(r_count)] = str(Script_code)
                ws_Shr['B'+str(r_count)] = Col[0]
                ws_Shr['C'+str(r_count)] = Col[1]
                ws_Shr['D'+str(r_count)] = Col[2]
                r_count = r_count+1
            except:
                r_count = r_count+1
                continue
            
        else:
            try:
                ws_Shr['A'+str(r_count)] = str(Script_code)
                ws_Shr['B'+str(r_count)] = Col[0]
                ws_Shr['C'+str(r_count)] = Col[1]
                ws_Shr['D'+str(r_count)] = Col[2]
                ws_Shr['E'+str(r_count)] = Col[3]
                ws_Shr['F'+str(r_count)] = Col[4]
                r_count=r_count+1
            except:
                r_count = r_count+1
                continue 
#     Wb.save(f_Name)

def MF_Holding (f_Name):
    driver.set_page_load_timeout(5)
    MF_holding_tbl =str(driver.find_element_by_xpath(x_MF_holding).get_attribute('outerText').strip())
    MF_holding_row = MF_holding_tbl.split('\n')
    MF_Row_cnt = int(len(MF_holding_row))
    mf_row = Ws_MF_Holding.max_row
    mf_row = mf_row+1
    for mf_R in range(1,MF_Row_cnt):
        MF_holding_Split = str(MF_holding_row[mf_R]).split('\t')
        Ws_MF_Holding['A'+str(mf_row)] = str(Script_code)
        Ws_MF_Holding['B'+str(mf_row)] = str(MF_holding_Split[0])
        Ws_MF_Holding['C'+str(mf_row)] = str(MF_holding_Split[1])
        mf_row =mf_row +1
#     Wb.save(f_Name)

def Financial(f_Name):
    driver.find_element_by_id(id_fin_prt).click()
    Fin_tbl = str(driver.find_element_by_xpath(x_fin_tbl).get_attribute('innerText').strip())
    fin_tbl_QoQ = str(driver.find_element_by_xpath('//*[@id="findet_1"]/table/tbody/tr[1]').get_attribute('innerText').strip())
    fin_tbl_QoQ = fin_tbl_QoQ.replace('\n','')
    print (fin_tbl_QoQ)
    ary_fin_tbl_QoQ = fin_tbl_QoQ.split('\t')
    NetSales_fin_tbl = str(driver.find_element_by_xpath('//*[@id="findet_1"]/table/tbody/tr[2]').get_attribute('innerText').strip())
    Other_Income_fin_tbl = str(driver.find_element_by_xpath('//*[@id="findet_1"]/table/tbody/tr[3]').get_attribute('innerText').strip())
    PBDIT_fin_tbl = str(driver.find_element_by_xpath('//*[@id="findet_1"]/table/tbody/tr[4]').get_attribute('innerText').strip())
    Net_Profit_fin_tbl = str(driver.find_element_by_xpath('//*[@id="findet_1"]/table/tbody/tr[5]').get_attribute('innerText').strip())
    ary_NetSales_fin_tbl = NetSales_fin_tbl.split('\t')
    ary_Other_Income_fin_tbl = Other_Income_fin_tbl.split('\t')
    ary_PBDIT_fin_tbl =PBDIT_fin_tbl.split('\t')
    ary_Net_Profit_fin_tbl = Net_Profit_fin_tbl.split('\t')
    Fin_row_cnt = Ws_Fin.max_row
    Fin_row_cnt =Fin_row_cnt+1
    Ws_Fin['A'+str(Fin_row_cnt)] = str(Script_code)
    Ws_Fin['B'+str(Fin_row_cnt)] = str(ary_fin_tbl_QoQ[0])
    Ws_Fin['C'+str(Fin_row_cnt)] = str(ary_fin_tbl_QoQ[1])
    Ws_Fin['D'+str(Fin_row_cnt)] =str(ary_fin_tbl_QoQ[2])
    Ws_Fin['E'+str(Fin_row_cnt)] =str(ary_fin_tbl_QoQ[3])
    Ws_Fin['F'+str(Fin_row_cnt)] =str(ary_fin_tbl_QoQ[4])
    Fin_row_cnt =Fin_row_cnt+1
    Ws_Fin['A'+str(Fin_row_cnt)] = str(Script_code)
    Ws_Fin['B'+str(Fin_row_cnt)] = str(ary_NetSales_fin_tbl[0])
    Ws_Fin['C'+str(Fin_row_cnt)] = str(ary_NetSales_fin_tbl[1])
    Ws_Fin['D'+str(Fin_row_cnt)] =str(ary_NetSales_fin_tbl[2])
    Ws_Fin['E'+str(Fin_row_cnt)] =str(ary_NetSales_fin_tbl[3])
    Ws_Fin['F'+str(Fin_row_cnt)] =str(ary_NetSales_fin_tbl[4])
    Fin_row_cnt =Fin_row_cnt+1
    Ws_Fin['A'+str(Fin_row_cnt)] = str(Script_code)
    Ws_Fin['B'+str(Fin_row_cnt)] = str(ary_Other_Income_fin_tbl[0])
    Ws_Fin['C'+str(Fin_row_cnt)] = str(ary_Other_Income_fin_tbl[1])
    Ws_Fin['D'+str(Fin_row_cnt)] =str(ary_Other_Income_fin_tbl[2])
    Ws_Fin['E'+str(Fin_row_cnt)] =str(ary_Other_Income_fin_tbl[3])
    Ws_Fin['F'+str(Fin_row_cnt)] =str(ary_Other_Income_fin_tbl[4])
    Fin_row_cnt =Fin_row_cnt+1
    Ws_Fin['A'+str(Fin_row_cnt)] = str(Script_code)
    Ws_Fin['B'+str(Fin_row_cnt)] = str(ary_PBDIT_fin_tbl[0])
    Ws_Fin['C'+str(Fin_row_cnt)] = str(ary_PBDIT_fin_tbl[1])
    Ws_Fin['D'+str(Fin_row_cnt)] =str(ary_PBDIT_fin_tbl[2])
    Ws_Fin['E'+str(Fin_row_cnt)] =str(ary_PBDIT_fin_tbl[3])
    Ws_Fin['F'+str(Fin_row_cnt)] =str(ary_PBDIT_fin_tbl[4])
    Fin_row_cnt =Fin_row_cnt+1
    Ws_Fin['A'+str(Fin_row_cnt)] = str(Script_code)
    Ws_Fin['B'+str(Fin_row_cnt)] = str(ary_PBDIT_fin_tbl[0])
    Ws_Fin['C'+str(Fin_row_cnt)] = str(ary_PBDIT_fin_tbl[1])
    Ws_Fin['D'+str(Fin_row_cnt)] =str(ary_PBDIT_fin_tbl[2])
    Ws_Fin['E'+str(Fin_row_cnt)] =str(ary_PBDIT_fin_tbl[3])
    Ws_Fin['F'+str(Fin_row_cnt)] =str(ary_PBDIT_fin_tbl[4])
    Fin_row_cnt =Fin_row_cnt+1
    Ws_Fin['A'+str(Fin_row_cnt)] = str(Script_code)
    Ws_Fin['B'+str(Fin_row_cnt)] = str(ary_Net_Profit_fin_tbl[0])
    Ws_Fin['C'+str(Fin_row_cnt)] = str(ary_Net_Profit_fin_tbl[1])
    Ws_Fin['D'+str(Fin_row_cnt)] =str(ary_Net_Profit_fin_tbl[2])
    Ws_Fin['E'+str(Fin_row_cnt)] =str(ary_Net_Profit_fin_tbl[3])
    Ws_Fin['F'+str(Fin_row_cnt)] =str(ary_Net_Profit_fin_tbl[4])
#     Wb.save(f_Name)

def Bal_Sheet(f_Name):
    Bal_rown_cnt = Ws_Bal_sheet.max_row
    Bal_rown_cnt =Bal_rown_cnt+1
    Bal_Tbl = str(driver.find_element_by_xpath(x_Bal_Sheet).get_attribute('innerText')).strip()
    Bal_dur = str(driver.find_element_by_xpath(x_bal_dur).get_attribute('innerText')).strip()
    Bal_dur = Bal_dur.replace('\n','') #(In Rs Cr)
    Bal_Tbl =Bal_Tbl .replace(',','')
    Bal_Tbl = Bal_Tbl.replace('\n\n\t\t\t\t\t\t\t\t\t\t\t','\t')
    Bal_Tbl = Bal_Tbl.replace('\n\n\t\t\t\t\t\t\t\t\t\t\t','\t')
    Bal_Tbl = Bal_Tbl.replace('\n\n\t\t\t\t\t\t\t\t\t\t\t','\n')
    Bal_Tbl = Bal_Tbl.replace('\n\n\t\t\t\t\t\t\t\t\t\t\t','\n')
    ary_Bal_Tbl = Bal_Tbl.split('\n')
    for y in ary_Bal_Tbl:
        ary_y= str(y).split('\t')
        Ws_Bal_sheet['A'+str(Bal_rown_cnt)]= str(Script_code)
        Ws_Bal_sheet['B'+str(Bal_rown_cnt)]= str(ary_y[0])
        Ws_Bal_sheet['C'+str(Bal_rown_cnt)]= str(ary_y[1])
        Ws_Bal_sheet['D'+str(Bal_rown_cnt)]= str(Bal_dur)
        Bal_rown_cnt=Bal_rown_cnt+1
#     Wb.save(f_Name)
    
    
x_M_cap = '//*[@id="mktdet_1"]/div[1]/div[1]/div[2]'
x_EPS = '//*[@id="mktdet_1"]/div[2]/div[1]/div[2]'
x_PE = '//*[@id="mktdet_1"]/div[1]/div[2]/div[2]'
x_BookValue = '//*[@id="mktdet_1"]/div[1]/div[3]/div[2]'
x_PriceBook = '//*[@id="mktdet_1"]/div[2]/div[3]/div[2]'
x_Div = '//*[@id="mktdet_1"]/div[1]/div[4]/div[2]'
x_Div_yeild = '//*[@id="mktdet_1"]/div[2]/div[4]/div[2]'
x_Facevalue = '//*[@id="mktdet_1"]/div[2]/div[5]/div[2]'
x_Ind_Pe = '//*[@id="mktdet_1"]/div[1]/div[6]/div[2]'
x_error_msg = '//*[@id="mc_mainWrapper"]/div[3]/div[2]/div/p[1]'
x_promo_link = '//*[@id="newsn"]/div/div[2]/p/a'
x_error_msg_tag = '//*[@id="mc_mainWrapper"]/div[3]/div[2]/div/div[3]/p/strong'
f_Name = 'C:\\Users\\khoday\\git\\Selenium_NSE_Algo\\Selenium_NSE_Algo\\Additonal_Utility\\NSE_Script_codes.xlsx'
x_shr_tbl = '//*[@id="acc_hd7"]/div/div[1]/table'
id_shr_prt = 'acc_pm7'
id_fin_prt = 'acc_pm5'

x_MF_holding = '//*[@id="acc_hd7"]/div/div[2]/table'
x_fin_tbl = '//*[@id="findet_1"]/table'
x_Bal_Sheet = '//*[@id="findet_11"]/table'
x_bal_dur = '//*[@id="findet_11"]/div/div[2]/div'

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--disable-infobars")
# driver = webdriver.Chrome(chrome_options=chrome_options)
driver = webdriver.Chrome('C:\\Python37\\chromedriver')

try:
    driver.get('https://www.moneycontrol.com/')
#     driver.get('https://www.moneycontrol.com/india/stockpricequote/mining-minerals/20microns/2M')
    driver.find_element_by_xpath(x_promo_link).click()
except:
    print('')
    
driver.set_page_load_timeout(5)
driver.maximize_window()

Wb = load_workbook(f_Name)
Wb.get_sheet_names()
Ws = Wb['Sheet1']
sht1_Row = Ws.max_row
print (sht1_Row)
ws_Shr =Wb.get_sheet_by_name('Share_pattern')
# Wsheet_partner= Wb.active
r_count = ws_Shr.max_row

if r_count ==1 :
    r_count=2
Ws_MF_Holding =Wb.get_sheet_by_name('MF_Holding')
mf_row =Ws_MF_Holding.max_row 
if mf_row ==1 :
    mf_row=2
    
Ws_Fin = Wb.get_sheet_by_name('Financial')
Ws_Bal_sheet = Wb.get_sheet_by_name('Bal_Sheet')
row = 1
clear_Temp ()
int_cnt = 1
for row in range(2, 1576):
    Col_Script_code = 'A' + str(row)
    Col_INIE = 'B' + str(row)
    Col_status = 'N' + str(row)
    Script_code = Ws[Col_Script_code].value
    INIE = Ws[Col_INIE].value
    Exe_status = Ws[Col_status].value
    
    if str(Exe_status).upper() == 'YES': 
        print ('Row number : '+ str(r_count))       
#         driver.find_element_by_id("search_str").send_keys(INIE)
        driver.find_element_by_id("search_str").send_keys(Script_code)
        time.sleep(2)        
        os.system('C:\\Users\\khoday\\git\\Selenium_NSE_Algo\\Selenium_NSE_Algo\\Additonal_Utility\\Enter.vbs')
        driver.set_page_load_timeout(15)
        time.sleep(10)   

        try:  
            str_error_msg = ""
            str_error_msg = driver.find_element_by_xpath(x_error_msg).get_attribute('textContent')
        except:
            print('Company Found')
        
        try:
            str_no_Com = ""
            str_no_Com = driver.find_element_by_xpath(x_error_msg_tag).get_attribute('innerText')             
        except:
            print('Company Found')
        if int_cnt > 12:
            clear_Temp ()
            int_cnt = 0
        int_cnt = int_cnt + 1
        if len(str_error_msg.strip()) > 0 or len(str(str_no_Com).strip()) > 0:            
            print ('Company code not found')
            continue              
        else:
            try:
                driver.find_element_by_id('mktdet_nav_2').get_attribute('innerText')
                Stock_info('mktdet_2',f_Name)
                time.sleep(2)
            except:
                try:
                    Stock_info('mktdet_1',f_Name)
                    time.sleep(2)
                    driver.set_page_load_timeout(2)
                except:
                    continue
                
            str_error_msg = ""            
            
            time.sleep(2)
            driver.set_page_load_timeout(5)
            try:
                Financial(f_Name)
                Bal_Sheet(f_Name)
                
                ShareHolding(f_Name)
                MF_Holding(f_Name)
                print (datetime.datetime.now())
            except:
                print('unknown error occured')
                Wb.save(f_Name)
                continue
                
            Wb.save(f_Name)
            
