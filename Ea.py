from Currency import Currency
from Member import Member
from collections import defaultdict
import operator

class EvolutionaryAlgorithm:

    def __init__(self, currency):
        self.currency = currency

    def rankRoutes(self, population):
        pass

    def selection(popRanked, eliteSize):
        pass

    def matingPool(population, selectionResults):
        matingpool = []
        for i in range(0, len(selectionResults)):
            index = selectionResults[i]
            matingpool.append(population[index])
        return matingpool

    def corssover(self):
        pass

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
        
                