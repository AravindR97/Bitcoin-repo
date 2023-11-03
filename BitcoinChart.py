"""Candlestick chart - Bitcoin price data"""

from pycoingecko import CoinGeckoAPI
import pandas as pd
#import matplotlib.pyplot as plt
import plotly.graph_objects as go
from datetime import datetime as dt

def unix_to_date(x):
    """Converts Unix Time to string of readable format dd-mm-yyyy hh:mm:ss"""
    return dt.fromtimestamp(x/1000).strftime("%d-%m-%Y %H:%M:%S")

def coin_select(L,x):
    """To find the ID of a specific cryptocurency"""
    coinsDF = pd.DataFrame(L)
    #print(coinsDF.head())
    coinsDF = coinsDF.loc[coinsDF.name == x]
    coinID = coinsDF.iat[0,0]
    return coinID

cg = CoinGeckoAPI()
"""    Created a CoinGeckoAPI client object"""
coinList = cg.get_coins_list()
crypto = input("Enter the name of the Cryptocurrency that has to be plotted\n")

ohlcList = cg.get_coin_ohlc_by_id(id= coin_select(coinList,crypto), vs_currency='usd', days= 7)
"""    ohlc list of chosen crypto for the last 7 days"""
ohlcDF = pd.DataFrame(ohlcList, columns= ["Date", "Open", "High", "Low", "Close"])
ohlcDF.Date = list(map( unix_to_date, ohlcDF.Date))
ohlcDF.set_index('Date', inplace= True)
print(ohlcDF)

fig = go.Figure(data= [go.Candlestick(x= ohlcDF.index, open= ohlcDF.Open,
                    high= ohlcDF.High, low= ohlcDF.Low, close= ohlcDF.Close)])
"""     pyplot candlestick chart"""
#fig.write_html("C:/Users/Aravind R/Desktop/Bitcoin.html")
"""     save pyplot candlestick figure as a large html file"""

with open(f'C:/Users/Aravind R/Desktop/{crypto}{ohlcDF.index[len(ohlcDF)-1][:10]}.html', 'w') as f:
    #Saving the pyplot candlestick figure as a small size html file
    f.write(fig.to_html(full_html=False, include_plotlyjs='cdn'))
f.close()


#fig.show()
"""     display the figure on an interactive environment"""
