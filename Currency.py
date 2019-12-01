class Currency:
    def __init__(self, name, values):
        self.name = name
        self.coins = sorted(set(values), reverse=True)