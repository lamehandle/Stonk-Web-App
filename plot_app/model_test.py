import yfinance as yf
import pandas as pd
from datetime import date

################################################################################
#  create a main loop that user can interact with
# this loop takes user input to:
    # set company symbol
    # set .history() period

print('''<===================================================>
                    Welcome!
<===================================================>''')
company_symbol = input("Select a company using their stock symbol: ")
company = yf.Ticker(company_symbol)
# pd.DataFrame(company.info)
# print(pd.DataFrame(company.info['quoteSourceName']))
print("<===================================================>")

# determine if user has dates or a period
comp_hist_df = {}
print("do you have a start and end date?")
use_period = input('Y or N: ')
if use_period.capitalize() == 'N':
    print("Available timeframes are:")
    # period: data period to download (Either Use period parameter or use start and end) Valid periods are: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
    # interval: data interval (intraday data cannot extend last 60 days) Valid intervals are: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
    print("1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max")
    period = input("your period: ")
    comp_hist = company.history(period=period)
    comp_hist_df = pd.DataFrame(comp_hist).reset_index()
    print(comp_hist_df)
else:
    # start: If not using period - Download start date string (YYYY-MM-DD) or datetime.
    start_date = date.fromisoformat(input("enter the start date (YYYY-MM-DD): "))
    # end: If not using period - Download end date string (YYYY-MM-DD) or datetime.
    end_date = date.fromisoformat(input("enter the end date (YYYY-MM-DD): "))
    comp_hist = company.history(start=start_date, end=end_date)
    comp_hist_df = pd.DataFrame(comp_hist).reset_index()
    print(comp_hist_df)
print("<===================== Good ==========================>")

# stop loss order logic
stop_loss = 0
print("do you want to set a Stop Loss Order? ")
set_stop_loss = input('Y or N: ')
if set_stop_loss.capitalize() == 'Y':
    stop_loss = float(input("Set your Stop Loss Order amount: $ "))
else:
    stop_loss = None

if stop_loss:
    print('match on stop_loss')
    print(comp_hist_df[comp_hist_df.Open <= stop_loss])
else:
    print('no match - stop_loss')

print("<===================== Stop Loss works ==========================>")

# take profit order logic
take_profit = 0
print("do you want to set a Take Profit Order? ")
set_take_profit = input('Y or N: ')
if set_take_profit.capitalize() == 'Y':
    take_profit = float(input("Set your Take Profit Order amount: $ "))
else:
    take_profit = None

if take_profit:
    print('match on take profit')
    print(comp_hist_df[comp_hist_df.Open <= take_profit])
else:
    print('no match - take_profit')
    