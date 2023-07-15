import yfinance as yf
import pandas as pd
from datetime import date
from company import retrieve_company_data
import stock_filters as sf
################################################################################
# from front-end grab user data
# allow drop down and text entry,
# sanitize/ validate user data

# create a main loop that user can interact with
comp_hist_df = retrieve_company_data()

# stop loss order logic
sf.stop_loss_filter(comp_hist_df)

# take profit order logic
sf.take_profit_filter(comp_hist_df)

# Chart main stock data8
# x-axis should be the date labled.
# y-axis should be stock price. labled.
# removed slider from layout.
# Chart filtered rows over original data.
#

