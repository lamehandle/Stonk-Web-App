from sim_control import Sim_Ctrl
from balance import Balance
from position import Position

################################################################################
# from front-end grab user data
# allow drop down and text entry,
# sanitize/ validate user data

# further the simulation needs to start with an amount of money
# Allow purchasing of stocks based on current Open price.

data = {
    "symbol": 'AAPL',
    "symbol_list": {"Apple": 'AAPL', },
    "stock_units": 0,
    "bank": 100000.00,
    "invest_amt": 2000.00,
    "take_profit": 200.00,
    "stop_loss": 100.00,
}


# create a main loop
# sim = Sim_Ctrl()
balance = Balance(data['bank'], data['invest_amt'])
position = Position(data['symbol'])

print(balance.bank_amt())
print("<=================>")
print(position.comp_hist_df)
print(balance.purchase_stocks(position.comp_hist_df))
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

