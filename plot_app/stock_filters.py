
def purchase_stocks(bank, invest, stock_units, comp_hist_df, ):
    ask = True
    while ask:
        invest = float(input('How much do you wish to invest? '))
        if invest > bank:
            print("You don't have enough funds!")
            ask = True
        else:
            bank -= invest
            print('you have ' + str(bank) + ' remaining.')
            ask = False
    opens = comp_hist_df['Open']  # need to use bracket notation to create a Series
    # print(opens)
    for values in opens:
        if invest - values >= 0.0:
            invest -= values
            stock_units += 1
    bank += invest
    print(str(stock_units) + " Stock Units.")
    print('$' + str(invest) + ' remaining')
    print('$' + str(bank) + ' remaining')
    return bank


def stop_loss_filter(comp_hist_df):
    stop_loss = 0
    print("do you want to set a Stop Loss Order? ")
    set_stop_loss = input('Y or N: ')
    if set_stop_loss.capitalize() == 'Y':
        stop_loss = float(input("Set your Stop Loss Order amount: $ "))
    else:
        stop_loss = None

    if stop_loss:
        print('match on stop_loss')
        stop_match = comp_hist_df[comp_hist_df.Open == stop_loss]
        if stop_match.empty:
            print('Stop loss set but no matching values.')

        print(stop_match['Open'])
        print(stop_match.High)
        print(stop_match.Low)
        print(stop_match.Close)

        print(stop_match)
        print("<===================== Stop Loss set! ==========================>")
        return stop_match
    else:
        print('no match - stop_loss')
        print("<===================== Unable to set Stop Loss! ==========================>")
        return 'Unable to set Stop Loss!'


def take_profit_filter(comp_hist_df):
    take_profit = None
    print("do you want to set a Take Profit Order? ")
    set_take_profit = input('Y or N: ')
    if set_take_profit.capitalize() == 'Y':
        take_profit = float(input("Set your Take Profit Order amount: $ "))
    else:
        take_profit = None

    # todo data validation is required for input large values cause an error in take profit
    if take_profit:
        print('match on take profit')
        print(comp_hist_df[comp_hist_df.Open >= take_profit])
    # this outputs a dataframe can also use this syntax comp_hist_df.loc[comp_hist_df.Open >= take_profit]
    # can search for multiple columns using the condition as swell
    # dataframe.loc[dataframe.label, 'other_column', 'another column', ...]
    #                           |                   |
    #                .label refers to           These are a comma separated list of
    #                row OR column name             column names
    #             you can also pass a lists
    #                         OR
    #               use conditional logic
    # dataframe.loc[(dataframe.label  >= value) "&&" OR "|" (value, 'other_column', 'another column', ...)]
    #
    else:
        print('no match - take_profit')
    print("<===================== take profit works ==========================>")