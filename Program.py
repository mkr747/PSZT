from Currency import Currency
from DataProvider import DataProvider

def main():
    currency = DataProvider.setUpCurrency()
    print(currency.coins[0])

if __name__ == "__main__":
    main()