import Currency from Currency

class Memeber:
    _id = 0
    Change = 0

    def __init__(self, currency):
        Memeber._id += 1
        self.id = Memeber._id
        self.fitnessValue = -1
        self.change = Member.Change
        for coin in currency.coins:
            self.coins[coin] = 0

    def setChange(value):
        Memeber.Change = value