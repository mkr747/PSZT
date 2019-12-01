from Currency import Currency
from Member import Member
from collections import defaultdict
import operator
import random
import numpy as np

CROSS_RATE = 0.2
MUTATION_RATE = 0.01
POP_SIZE = 200

class EvolutionaryAlgorithm:

    def __init__(self, currency, pop_size):
        self.currency = currency

        for i in range(pop_size):
            member = Member(currency)
            for coin in coins:
                member.coins[coin] = np.randint(Member.Change)
            self.population.append(member)

    def select(self):
        fitness = self.getAllFitness() + 1e-4
        idx = np.random.choice(np.arange(len(self.population), size=len(self.population), replace=True, p=1-(fitness/fitness.sum())))
        return self.population[idx]
    

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

    def getAllFitness(self):
        fitness = []
        for member in self.population:
            #member.fitnessValue = getFitness(member)
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
        
                