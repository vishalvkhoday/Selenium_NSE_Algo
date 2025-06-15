
""" Exploring chg values (NIFTY 50)

...

VK project

Indicators that are based on change values are implemente on past data here.


Vishal Khoday sir:
    -> ~ 840-860 values to derive std
    -> chg_i = bar value in hourly bar chart
    

Author(s)
---------
Gaurav S Hegde (grv.hegde@gmail.com)
Sugamya/CodeSāmarthya, SAfE
"""

import pandas as pd
pd.set_option("display.max.columns", None)

import numpy as np
import datetime
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from  DB_Connection_V1 import DB_Connect as db

connectionParms = {"DATABASE":"Bse_Results"}
MSSQLConnect = db.connectStr(**connectionParms)
SQL_NiftyTicker = "select top 840 * from Nifty_Ticker where Script_Name = 'Nifty 50' order by [DateTime] desc "
# NiftyTickerSql = MSSQLConnect.execute(SQL_NiftyTicker)
# nifty = pd.DataFrame()
nifty = pd.read_sql(SQL_NiftyTicker, MSSQLConnect)

# Reading data
# nifty = pd.read_excel(r"C:\\Users\\Vishal\\Downloads\\NiftyDataTest.xlsx",
#     usecols = ["DateTime", "SpotPrice", "chg", "IndOpen", "IndHigh", "IndLow", "IndPreClose"],
# )


window_size = 840

nifty["max_chg"] = nifty["chg"].rolling(window= 800).max()
nifty["std_chg (target)"] = nifty["chg"].rolling(window= 800).std()
nifty["avg_chg"] = nifty["chg"].rolling(window= 800).sum()/window_size

print(nifty.head()) 


# Animations
no_frames = nifty.shape[0] - window_size


fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize=(10, 6.15))
ax[0].set_xlabel(r'DateTime')
ax[0].set_ylabel(r'$Nifty$ SpotPrice')
ax[1].set_xlabel(r'DateTime')
ax[1].set_ylabel(r'$chg$')
fig.suptitle('Movement of Tgt & Max')


spot_plot, = ax[0].plot(
    nifty.loc[:window_size]["DateTime"],
    nifty.loc[:window_size]["SpotPrice"],
    color = 'b'
)
ax[0].set_xlim(auto = True)

chg_plot, = ax[1].plot(
    nifty.loc[:window_size]["DateTime"],
    nifty.loc[:window_size]["chg"],
    color = 'r'
)
ax[1].set_xlim(auto = True)

hl_tgt_1 = ax[1].axhline(
    nifty.loc[window_size]["avg_chg"] + nifty.loc[window_size]["std_chg (target)"], color='g', linestyle = '-', label = 'tgt_1'
)
hl_avg = ax[1].axhline(
    nifty.loc[window_size]["avg_chg"], color='k', linestyle = '-', label = 'avg'
)
hl_tgt_2 = ax[1].axhline(
    nifty.loc[window_size]["avg_chg"] -1*nifty.loc[window_size]["std_chg (target)"], color='g', linestyle = '-', label = 'tgt_2'
)
hl_max = ax[1].axhline(nifty.loc[window_size]["max_chg"], color='m', linestyle = '-', label = 'max')

ann_text = fig.text(
    .85, .90,
    f'tgt = {nifty.loc[window_size]["std_chg (target)"]} \n'+
    f'max = {nifty.loc[window_size]["max_chg"]}',
    fontsize=15
)

# updater function for the animation
def update(frame):
    
    # update the background plots
    spot_plot.set_data(
        nifty.loc[frame: frame + window_size]["DateTime"],
        nifty.loc[frame: frame + window_size]["SpotPrice"]
    )
    ax[0].set_xlim(
        nifty.loc[frame]["DateTime"],
        nifty.loc[frame + window_size]["DateTime"],
    )
    ax[0].set_ylim(
        nifty.loc[frame: frame + window_size]["SpotPrice"].min()-100,
        nifty.loc[frame: frame + window_size]["SpotPrice"].max() + 100,
    )
    
    chg_plot.set_data(
        nifty.loc[frame: frame + window_size]["DateTime"],
        nifty.loc[frame: frame + window_size]["chg"]
    )
    ax[1].set_xlim(
        nifty.loc[frame]["DateTime"],
        nifty.loc[frame + window_size]["DateTime"],
    )
    ax[1].set_ylim(
        nifty.loc[frame: frame + window_size]["chg"].min()-0.5,
        nifty.loc[frame: frame + window_size]["chg"].max() + 0.5,
    )
    ax[1].legend()
    
    # update the horizontal lines
    hl_tgt_1.set_ydata(
        nifty.loc[window_size]["avg_chg"] + nifty.loc[window_size + frame]["std_chg (target)"]
    )
    hl_tgt_2.set_ydata(
        nifty.loc[window_size]["avg_chg"] -1*nifty.loc[window_size + frame]["std_chg (target)"]
    )
    hl_avg.set_ydata(
        nifty.loc[window_size]["avg_chg"]
    )
    
    hl_max.set_ydata(nifty.loc[window_size + frame]["max_chg"])
    
    #update the text annotation
    ann_text.set_text(
        f'tgt = {nifty.loc[window_size + frame]["std_chg (target)"]:.2f} \n'+
        f'max = {nifty.loc[window_size + frame]["max_chg"]}',
    )
    
    return (ax[0],ax[1],hl_tgt_1, hl_tgt_2, hl_avg, hl_max, ann_text)

ani = animation.FuncAnimation(
    fig = fig, func = update,
    frames = no_frames, interval = 200, repeat = False
)

plt.show()
