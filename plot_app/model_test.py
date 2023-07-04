import yfinance as yf
import pandas as pd
import datetime
# period: data period to download (Either Use period parameter or use start and end) Valid periods are: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max

# interval: data interval (intraday data cannot extend last 60 days) Valid intervals are: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo

# start: If not using period - Download start date string (YYYY-MM-DD) or datetime.
# end: If not using period - Download end date string (YYYY-MM-DD) or datetime.

# prepost: Include Pre and Post market data in results? (Default is False)

# auto_adjust: Adjust all OHLC automatically? (Default is True)

# actions: Download stock dividends and stock splits events? (Default is True)

################################################################################

#  create a main loop that user can interact with
# this loop takes user input to:
    # set company symbol
    # set .history() period

print("Welcome!")
company_symbol = input("Select a company using their stock symbol:")
company = yf.Ticker(company_symbol)
print(company.info)
print("<===================================================>")

print("do you have a start and end date?")
use_period = input('Y or N')
if use_period.capitalize() == 'N':
    print("Available timeframes are:")
    print("1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max")
    period = input("your period:")
    company.history(period=period)
else:
    start_date = input("enter the start date:")
    end_date = input("enter the end date:")
    company.history(start=start_date, end=end_date)

