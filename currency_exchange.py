class CurrencyExchanger:

    def __init__(self):
        self.amount = None
        self.rates = {
            'ARS': 0.82,
            'HNL': 0.17,
            'AUD': 1.9622,
            'MAD': 0.208,
        }

    def get_currency_amount(self):
        return float(input('Please, enter the number of mycoins you have: > '))

    # def get_currency_exchange_rate(self):
    #     return float(input('Please, enter the exchange rate: > '))

    def show_result(self):
        for curr, rate in self.rates.items():
            print(f'I will get {round(self.amount * rate, 2):.2f} {curr} from the sale of {self.amount:.2f} mycoins.')

    def start(self):
        self.amount = self.get_currency_amount()
        self.show_result()

if __name__ == '__main__':
    ex = CurrencyExchanger()
    ex.start()