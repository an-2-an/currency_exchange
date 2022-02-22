class CurrencyExchanger:

    def __init__(self):
        self.amount = None

    def get_currency_amount(self):
        return float(input('Please, enter the number of mycoins you have: > '))

    def get_currency_exchange_rate(self):
        return float(input('Please, enter the exchange rate: > '))

    def show_result(self):
        print(f'The total amount of dollars: {self.amount}')

    def start(self):
        c = self.get_currency_amount()
        r = self.get_currency_exchange_rate()
        self.amount = round(c * r, 2)
        self.show_result()

if __name__ == '__main__':
    ex = CurrencyExchanger()
    ex.start()