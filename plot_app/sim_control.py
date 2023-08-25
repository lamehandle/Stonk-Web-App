from csv_data_trans import get_symbols_from_csv
from position import Position
from balance import Balance


class Sim_Ctrl:
    #  validate before the simulation gets the data.
    position = None
    balance = None

    def __init__(self):
        self.create_position()
        self.create_balance()

    def create_position(self):
        self.position = Position().retrieve_single_day()

    def create_balance(self):
        self.balance = Balance()

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
