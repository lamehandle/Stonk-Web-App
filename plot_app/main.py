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
    "take_profit": 180.00,
    "stop_loss": 166.00,

}


# create a main loop
# sim = Sim_Ctrl()
position = Position(data['symbol'])
# print(position.position_series)

# # stop loss order


balance = Balance(data['bank'], data['invest_amt'])
balance.invest(data['invest_amt'])

print("<========Sim Start=========>")
print('<======== Total Bank Amount: ========>$')
print('             $ ' + str(balance.bank_amt()))
print("<=================>")

balance.purchase_stocks(position.history)
print("Total units purchased: " + str(balance.stock_units) + " units of " + str(position.symbol))
print("<=================>")

print('<======== Remaining Bank Amount: ========>')
print('             $ ' + str(balance.bank_amt()))
print("<========= Advancing the Sim ========>")
# advance the loop 1 day
position.advance_record()

print("<========= Plotting the Sim ========>")
plot = Plot(position)
# plot.plot_history(position)

# # on each round of the simulation add or subtract funds based on the bets.
position.advance_record()
position.advance_record()
position.advance_record()
plot.update_position(position)
position.advance_record()
position.advance_record()
plot.update_position(position)

# take profit order
position.set_take_profit(data["take_profit"])
position.take_profit(balance)

position.set_stop_loss(data["stop_loss"])
position.stop_loss(balance)

plot.update_position(position)
# todo plot take profit/stop loss on top of plot to show where those amounts land.
