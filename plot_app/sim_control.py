from csv_data_trans import get_symbols_from_csv
from user import User


class Simulation_Controller:
    # validate before the simulation gets the data.
    user = {
        "symbol": "",
        "symbol_list": {},

        "bank": 0.0,
        "invest_amt": 0.0,
        "take_profit": 0.0,
        "stop_loss": 0.0,
    }

    def __init__(self):
        self.create_position()

    # create new user  todo refactor to use position/ balance
    def create_position(self):
        user = position(self.user["symbol"])
        return user

    def stop_loss(self):
        stop_loss_flag = input("Do you want to set a Stop Loss amount? Y/N").upper()
        if stop_loss_flag == "Y":
            set_stop_loss = float(input("Enter Stop Loss dollar amount: $ "))
            self.user["stop_loss"] = set_stop_loss
        else:
            self.user["stop_loss"] = 0.0

    #  get take profit
    def take_profit(self):
        take_profit_flag = input("Do you wish to set a Take Profit Order? Y/N").upper()
        if take_profit_flag == "Y":
            set_stop_loss = float(input("Enter Take Profit dollar amount: $ "))
            self.user["take_profit"] = set_stop_loss
        else:
            self.user["take_profit"] = 0.0

    # ask user to make trades,
    # todo see stock_utils.py purchase_stocks()
    # cash out,
    #
    # or advance time
    #
    # continue loop
