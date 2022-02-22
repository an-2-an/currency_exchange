import requests

class CurrencyExchanger:

    def __init__(self):
        self.amount = None
        self.currency_name = None
        self.rates = {
            'USD': None,
            'EUR': None,
        }

    def get_currency_name(self):
        return input('Please, enter the name of currency: > ')

    def get_currency_amount(self):
        return float(input(f'Please, enter the number of {self.currency_name} you have: > '))

    # def get_currency_exchange_rate(self):
    #     return float(input('Please, enter the exchange rate: > '))

    def show_result(self):
        for curr, rate in self.rates.items():
            print(f'I will get {round(self.amount * rate, 2):.2f} {curr} from the sale of {self.amount:.2f} {self.currency_name}.')

    def get_data(self):
        return requests.get(f'http://www.floatrates.com/daily/{self.currency_name}.json').json()

    def start(self):
        self.currency_name = self.get_currency_name()
        self.amount = self.get_currency_amount()
        data = self.get_data()
        # print(data)
        for key in self.rates.keys():
            self.rates[key] = data[key.lower()].get('rate')
        self.show_result()


if __name__ == '__main__':
    ex = CurrencyExchanger()
    ex.start()