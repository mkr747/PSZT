from Currency import Currency
from Member import Member
from collections import defaultdict
import operator
import random

CROSS_RATE = 0.2
MUTATION_RATE = 0.01

class EvolutionaryAlgorithm:

    def __init__(self, currency):
        self.currency = currency
        

    def rankRoutes(self, population):
        pass

    def select(self):
        fitness = self.getFitness()
        idx = random()
        parent = population[idx]
        return parent

    def crossover(self, parent):
        if random.rand() < CROSS_RATE:
            i_ = random.randint(0, len(population), size=1)
            child = Member(self.currency)
            for coin in currency.coins:
                num = random.choice(["Heads", "Tails"])
                if num == "Heads":
                    child.coins[coin] = parent.coins
                else:
                    child.coins[coin] = population[i_].coins
            return child
        return parent


    def mutatePopulation(self):
        if random.randint(O, len(population), sieze=1):


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
        
                