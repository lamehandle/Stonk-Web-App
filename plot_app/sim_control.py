from csv_data_trans import get_symbols_from_csv
from user import User


class Simulation_Controller:
    # validate before the simulation gets the data.
    user = {
        "symbol" : "",
        "symbol_list" : {},
        "bank" : 0.0,
        "invest_amt" : 0.0,
        "take_profit" : 0.0,
        "stop_loss" : 0.0,
    }

    def __init__(self):
       self.create_user()

    # create new user
    def create_user(self):
        user = User(self.user["bank"], self.user["symbol"])
        return user

    def stop_loss(self):
        set_stop_loss = float(input("Do you want to set a Stop Loss amount?"))
        if set_stop_loss:
            self.user["stop_loss"] = set_stop_loss
    #  get take profit
    def take_profit(self):
        set_take_profit = float(input("Do you wish to set a Take Profit Order?"))
        if set_take_profit:
            self.user["take_profit"]
    #  advance time

    # continue loop