from company import *


class User:
    bank = 10000.00
    invest = 0
    stock_units = 0
    comp_hist_df = retrieve_single_day()
    print(comp_hist_df)

