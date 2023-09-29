

class Balance:
    bank = 0.0
    invest_amt = 0.0
    unit_cost = 0.0
    stock_units = 0
    errors = {}

    def __init__(self, bank, invest):
        self.bank = bank
        self.invest_amt = invest

    def bank_amt(self):
        return self.bank

    def invest(self, invest):
        self.invest_amt = invest

    def purchase_stocks(self, position):
        if self.invest_amt <= self.bank:
            self.unit_cost = position["Open"].loc[0]
            self.stock_units = self.invest_amt // position["Open"].loc[0]
            # print(str(stock_units) + ' units.')
            cost = self.stock_units * position["Open"].loc[0]
            # print('$' + str(cost))
            self.bank = (self.bank - cost)
            # print('$' + str(bank) + 'mid-func')
            remaining = self.invest_amt - cost

        else:
            self.errors = {"funds": "Not enough funds!"}

    def value_held(self):
        return self.stock_units * self.unit_cost

    def cash_out(self):
        pass




