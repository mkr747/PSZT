class Currency:
    def __init__(self, name):
        self.name = name
        self.coins = []

    def addCoins(self, values):
        for coin in values:
            self.coins.append(coin)

    def getCoins(self):
        return self.coins