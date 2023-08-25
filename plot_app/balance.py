

class Balance:
    bank = 0.0
    invest_funds = 0.0
    stock_units = 0
    errors = {}

    def __init__(self):
        self.bank_amt()
        self.invest_amt()

    def bank_amt(self):
        self.bank = float(input("How much are you starting with in the bank? $ "))

    def invest_amt(self):
        self.invest_funds = float(input("How much are you investing in this stock? $ "))
        self.purchase_stocks()

    def purchase_stocks(self):
        if self.invest_funds <= self.bank:
            stock_units = self.invest_funds // self.comp_hist_df["Open"].loc[0]
            # print(str(stock_units) + ' units.')
            cost = stock_units * self.comp_hist_df["Open"].loc[0]
            # print('$' + str(cost))
            self.bank = (self.bank - cost)
            # print('$' + str(bank) + 'mid-func')
            remaining = self.invest_funds - cost
        else:
            self.errors = {"fund": "Not enough funds!"}




