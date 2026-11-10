#data-link="https://nsearchives.nseindia.com/content/indices/ind_close_all_23102026.csv"

from selenium.webdriver import ChromeOptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from datetime import datetime, timedelta
Options = ChromeOptions()
Options.add_argument("start-maximized")

Options.add_argument("disable-infobar")
serviceObj = Service('C:/Vishal/git/Bse_Extractor/src/WebDriver/chromedriver.exe')
browChrome =  webdriver.Chrome(service=serviceObj,options=Options) #Driver

# Define start and end dates (YYYY-MM-DD format)
start_date_str = "2026-10-25"
end_date_str   = "2026-11-02"

# Convert strings to datetime objects
start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
end_date   = datetime.strptime(end_date_str, "%Y-%m-%d")

# Loop through each day
current_date = start_date
while current_date <= end_date:        
    current_date += timedelta(days=1)
    date_str = current_date.strftime("%d%m%Y")  # format as DDMMYYYY
    url = f"https://nsearchives.nseindia.com/content/indices/ind_close_all_{date_str}.csv"
    browChrome.get(url)
    print(f"Downloaded data for {current_date.strftime('%Y-%m-%d')}")  # format as YYYY-MM-DD

print("All data downloaded successfully.")