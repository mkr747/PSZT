import Currency from Currency

class Memeber:
    _id = 0
    Change = 0

    def __init__(self, currency):
        Memeber._id = Memeber._id + 1
        self.id = Memeber._id
        self.fitnessValue = -1
        self.change = Member.Change
        self.coins = { value: 0 for value in currency.coins }

    def setChange(value):
        Memeber.Change = value