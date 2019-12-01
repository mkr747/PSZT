from Currency import Currency
from Member import Member
from collections import defaultdict
import operator
import random

CROSS_RATE = 0.4

class EvolutionaryAlgorithm:

    def __init__(self, currency, crossRate, population):
        self.currency = currency
        self.crossRate = crossRate
        self.population = population

    def rankRoutes(self, population):
        pass

    def select(self):
        fitness = self.getAllFitness() + 1e-4
        idx = np.random.choice(np.arange(len(self.population), size=len(self.population), replace=True, p=fitness/fitness.sum())
        return self.population[idx]
    
    def coinFlip(self):
        num = random.choice(["Heads", "Tails"])
        return num

    def crossover(self, parent):
        if random.rand() < self.crossRate:
            i_ = random.randint(0, len(self.population - 1))
            child = Member(self.currency)
            for coin in currency.coins:
                num = coinflip()
                if num == "Heads":
                    child.coins[coin] = parent.coins
                else:
                    child.coins[coin] = population[i_].coins
            return child
        return parent


    def mutatePopulation(self):
        pass    

    def getAllFitness(self):
        fitness = []
        for member in self.population:
            fitness.append(getFitness(member))
        
        return fitness

    def getFitness(self, member):
        fitness = 0
        for coin in self.currency.coins:
            fitness += (self.minimal[coin] - member.coins[coin]) * coin

        return fitness

    #Run after init
    def countMinimalCoins(self):
        change = Member.Change
        dictionary = { value: 0 for value in self.currency.coins }
        for coin in self.currency.coins:
            remainder = change % coin
            dictionary[coin] = (change - remainder) / coin
            change = remainder

        self.minimal = dictionary
        
                