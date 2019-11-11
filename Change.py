class Change:
    def __init__(self, pileOfCoins, currency):
        self.pileOfCoins = pileOfCoins
        self.currency = currency

    def coins(self):
        return self.pileOfCoins

    def getValue(self):
        result = 0
        for coin in self.pileOfCoins:
            result += coin
        return result

    def amountOfCoins(self):
        return len(self.pileOfCoins)
        
    def amountOfChosenCoin(self, value):
        if value not in self.currency.coins:
            return 0
        
        counter = 0
        for val in self.pileOfCoins:
            if val == value:
                counter+=1
        return counter

    def __repr__(self):
        return f"This is {self.__class__} and it's value is {self.coins()} using {self.amountOfCoins()}" 