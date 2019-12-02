from Currency import Currency

class Member:
    Change = 0

    def __init__(self, currency):
        self.fitnessValue = -1
        self.change = Member.Change
        self.coins = { value: 0 for value in currency.coins }

    @staticmethod
    def setChange(value):
        Member.Change = value