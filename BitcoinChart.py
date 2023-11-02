"""Candlestick chart - Bitcoin price data"""

from pycoingecko import CoinGeckoAPI
import pandas as pd
#import matplotlib.pyplot as plt
import plotly.graph_objects as go
from datetime import datetime as dt

def unix_to_date(x):
    """Converts Unix Time to string of format dd-mm-yyyy hh:mm:ss"""
    return dt.fromtimestamp(x/1000).strftime("%d-%m-%Y %H:%M:%S")

cg = CoinGeckoAPI()
        #Created a CoinGeckoAPI client object
ohlcList = cg.get_coin_ohlc_by_id(id='bitcoin', vs_currency='usd', days= 7)
        #ohlc list of bitcoin for the last 7 days
ohlcDF = pd.DataFrame(ohlcList, columns= ["Date", "Open", "High", "Low", "Close"])
        #Casting into a dataframe
ohlcDF.Date = list(map( unix_to_date, ohlcDF.Date))
ohlcDF.set_index('Date', inplace= True)
#print(ohlcDF)

fig = go.Figure(data= [go.Candlestick(x= ohlcDF.index, open= ohlcDF.Open,
                                      high= ohlcDF.High, low= ohlcDF.Low,
                                    close= ohlcDF.Close)])
        #Created candlestick chart using plotly
#fig.write_html("C:/Users/Aravind R/Desktop/Bitcoin.html")

with open('C:/Users/Aravind R/Desktop/Bitcoin2.html', 'w') as f:
    """Saving the candlestick chart as a small size html file"""
    f.write(fig.to_html(full_html=False, include_plotlyjs='cdn'))
f.close()

#fig.show()
