from django import forms
from stock import Stock

POST_data = ""
validate_POST_data(POST_data)  # todo create this validation function.
user_data = POST_data['stuff']
default_period = "1mo"
symbol = user_data
stock = Stock(symbol, period=user_data['period'] | default_period, start='', end='')

# variables passed to process_stock.html
symbol = user_data['stonk-select']
date = user_data.date
open = user_data.open
high = user_data.high
low = user_data.low
close = user_data.close
volume = user_data.volume
dividends = user_data.dividends
splits = user_data.splits
period = user_data.period | default_period