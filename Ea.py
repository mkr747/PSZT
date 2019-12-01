from Currency import Currency
from Member import Member
from collections import defaultdict
import operator
import random

CROSS_RATE = 0.4

class EvolutionaryAlgorithm:

    def __init__(self, currency, crossRate):
        self.currency = currency
        self.crossRate = crossRate

    def rankRoutes(self, population):
        pass

    def select(self):
        fitness = self.getFitness()

        return parent


    
    
    def coinFlip(self):
        num = random.choice(["Heads", "Tails"])
        return num

    def crossover(self, parent):
        if random.rand() < self.crossRate:
            i_ = random.randint(0, len(population))
            child = Member(self.currency)
            for coin in currency.coins:
                num = coinflip()
                if num == "Heads":
                    child.coins[coin] = parent.coins
                else:
                    child.coins[coin] = population[i_].coins
        return child


    def mutatePopulation(self):
        pass    

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
        
                