import yfinance as yf
import pandas as pd
import numpy as np
from datetime import date
from company import retrieve_single_day
import stock_utils as sf
from user import User

################################################################################
# from front-end grab user data
# allow drop down and text entry,
# sanitize/ validate user data

ask = True
bank = 10000.00
invest = 500.00
symbol = 'AAPL'
stop_loss = None
take_profit = None
stock_units = 0
# comp_hist_df = retrieve_single_day()

user = User(bank, invest, symbol)
user.retrieve_single_day()
user.purchase_stocks(bank, invest)
# create a main loop that user can interact with
# further the simulation needs to start with an amount of money
# Allow purchasing of stocks based on current Open price.
# bank = sf.purchase_stocks(bank, invest, stock_units, comp_hist_df)
# print('$' + str(bank) + ' end')

# stop loss order logic
print("do you want to set a Stop Loss Order? ")
stop_loss = float(input("Set your Stop Loss Order amount: $ "))

# # take profit order logic
print("do you want to set a Take Profit Order? ")
take_profit = float(input("Set your Take Profit Order amount: $ "))
# take_profit = sf.take_profit_filter(comp_hist_df)

# advance the loop 1 day
user.advance_time()
# sf.advance_time(comp_hist_df)
# works

# on each round of the simulation add or subtract funds based on the bets.
# add or subtract value of the match from bank.





# Chart main stock data
# x-axis should be the date labeled.
# y-axis should be stock price. labeled.
# removed slider from layout.
# Chart filtered rows over original data.
#

