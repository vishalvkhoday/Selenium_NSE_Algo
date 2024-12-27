import sys,openpyxl
import pandas as pd

filepath = "C:\\Users\\Vishal\\Downloads\\StockPE.xlsx"
pdstock = pd.read_excel(filepath,sheet_name='Sheet1')
pdstock.to_csv("C:\\Users\\Vishal\\Downloads\\StockPE.csv")
