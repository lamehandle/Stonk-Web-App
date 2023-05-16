from stock import Stock

POST_data = ''
validate_POST_data(POST_data)  # todo create this validation function.
user_data = POST_data['stuff']
default_period = "1mo"
symbol = user_data
stock = Stock(symbol, period=user_data['period'] | default_period, start='', end='')



