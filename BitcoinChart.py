""" Program to plot the fluctuations in the price of bitcoin"""

from pycoingecko import CoinGeckoAPI
    #Imported CoinGeckoAPI class from pycoingecko library
import pandas as pd
import matplotlib.pyplot as plt


cg = CoinGeckoAPI()
    #Created a CoinGeckoAPI object

#use a method in this class to get info about bitcoin for the last 30 days:
bit_info = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)
#'bit_info' is a dictionary of lists
print(bit_info.keys())


#Get the values at 'prices' key:
bit_prices = bit_info['prices']
print(type(bit_prices))

#Convert the list into a dataframe:
bit_df = pd.DataFrame(bit_prices, columns= ['Timestamp', 'Price'])
print(bit_df)
#(instead of casting the entire dictionary, just the list at one of its keys is cast into a DF)

plt.plot(bit_df.Timestamp[0:100], bit_df.Price[0:100])
plt.show()


'''
#Get the list of all coins in CoinGeckoAPI:
L = cg.get_coins_list()
print(L) #it is a list of dictionaries


#convert the list into a DataFrame for convenience:
df = pd.DataFrame(L)
print(df)
'''
