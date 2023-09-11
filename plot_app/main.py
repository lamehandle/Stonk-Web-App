from balance import Balance
from position import Position
from plot import Plot
################################################################################
# from front-end grab user data
# allow drop down and text entry,
# sanitize/ validate user data

# further the simulation needs to start with an amount of money
# Allow purchasing of stocks based on current Open price.
# dummy data
data = {
    "symbol": 'AAPL',
    "symbol_list": {"Apple": 'AAPL', },
    "stock_units": 0,
    "bank": 10000.00,
    "invest_amt": 2000.00,
    "take_profit": 200.00,
    "stop_loss": 100.00,

}


# create a main loop
# sim = Sim_Ctrl()
position = Position(data['symbol'])

# print(position.position_series)
# take profit order
profit = position.take_profit(data["take_profit"])
# # stop loss order
stop_loss = position.stop_loss(data["stop_loss"])

balance = Balance(data['bank'], data['invest_amt'])
balance.invest(data['invest_amt'])

print("<========Sim Start=========>")
print('<======== Total Bank Amount: ========>$')
print('             $ ' + str(balance.bank_amt()))
print("<=================>")
# print(position.history)
# print("<=================>")
balance.purchase_stocks(position.history)

print("Total units purchased: " + str(balance.stock_units) + " units of " + str(position.symbol))
print("<=================>")
print('<======== Remaining Bank Amount: ========>')
print('             $ ' + str(balance.bank_amt()))
print("<========= Advance the Sim 1 Day ========>")
# advance the loop 1 day
position.advance_time()

plot = Plot(position).plot_position()
# # on each round of the simulation add or subtract funds based on the bets.

print(plot)
# # add or subtract value of the match from bank.
#
# todo Plot ticker history
# todo plot take profit/stop loss on top of plot to show where those amounts land.


# Chart main stock data
# x-axis should be the date labeled.
# y-axis should be stock price. labeled.
# removed slider from layout.
# Chart filtered rows over original data.
#

