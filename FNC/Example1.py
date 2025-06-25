import fnc,requests,time,json
import pandas as pd
from functools import partial

# def getNSE_Index_Data():
#     url ='https://iislliveblob.niftyindices.com/jsonfiles/LiveIndicesWatch.json?{}&_='
#     session = int(time.time())
#     url = url+ str(session)
#     # head = {'Accept':'application/json' ,':method': 'GET'}
#     try:
#         res = requests.get(url=url,timeout=5).text
#         return json.loads(res)
    
#     except Exception as e:
#         print(e,res.status_code)
# mappedData =list(fnc.map(('indexName','timeVal','last','percChange','open','high','low','previousClose'),getNSE_Index_Data()["data"]))
# # print(mappedData)
# NonZero = list(fnc.filter(lambda x: str(x[3]).replace('-','0') ,mappedData))
# ValidVal = list(fnc.filter(lambda x: float(x[3]) !=0 ,NonZero))
# print(ValidVal)
# mappedData = list(map(lambda x: str(x).replace(',',''),mappedData))

from datetime import datetime
timestamp = 1744880459
