from Change import Change

class Fitness:
    def __init__(self, change, goal_value):
        self.change = change
        self.goal_value = goal_value
        self.fitness = 0.0

    def amountOfChange(self):
        return self.change.amountOfCoins()
    
    def countFitness(self):
        currentValue = self.change.getValue()
        diff =  self.goal_value - currentValue
        self.fitness = 1 / float(self.amountOfChange() + diff)
        return self.fitness
