from csv_data_trans import get_symbols_from_csv
from user import User


class Simulation_Controller:

    #  take user company stock symbol
    raw_stock = input("Enter your stock symbol. ")
    raw_bank = input("How much funds are in the bank? ")
    raw_invest_amt = input("How much are you investing? ")
    # validate against list
    symbol_list = get_symbols_from_csv()
    symbol = ''
    bank = 0.0
    invest_funds = 0.0

    if raw_stock in symbol_list:
        symbol = raw_stock

    # create new user
    user = User(bank, symbol)

    #  retreive initial history
    user.retrieve_single_day()
    # prompt user for stop loss... y/n?

#