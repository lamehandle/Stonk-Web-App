import yfinance as yf
import pandas as pd
import numpy as np
from datetime import date
from company import retrieve_single_day
import stock_utils as sf
from sim_control import Sim_Ctrl
from user import User

################################################################################
# from front-end grab user data
# allow drop down and text entry,
# sanitize/ validate user data

# further the simulation needs to start with an amount of money
# Allow purchasing of stocks based on current Open price.

user_data = {
    "symbol": 'AAPL',
    "symbol_list": {},
    "stock_units": 0,
    "bank": 0.0,
    "invest_amt": 0.0,
    "take_profit": 0.0,
    "stop_loss": 0.0,
}


# create a main loop
sim = Sim_Ctrl()

#
# # stop loss order logic
# print("do you want to set a Stop Loss Order? ")
# user.stop_loss = float(input("Set your Stop Loss Order amount: $ "))
#
# # # take profit order logic
# print("do you want to set a Take Profit Order? ")
# user.take_profit = float(input("Set your Take Profit Order amount: $ "))
#
# # advance the loop 1 day
# user.advance_time()
# # works
#
# # on each round of the simulation add or subtract funds based on the bets.
# # add or subtract value of the match from bank.
#
# #  todo Plot ticker history
# # todo plot take profit/stop loss on top of plot to show where those amounts land.



# Chart main stock data
# x-axis should be the date labeled.
# y-axis should be stock price. labeled.
# removed slider from layout.
# Chart filtered rows over original data.
#

