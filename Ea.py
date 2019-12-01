from Currency import Currency
from Member import Member
from collections import defaultdict
import operator
import random

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
    
    def coinFlip(self):
        num = random.choice(["Heads", "Tails"])
        return num

    def crossover(self, parent1, parent2):
        children = [Member(self.currency), Member(self.curenccy)]
        for child in children:
            for coin in currency.coins:
                num = coinflip()
                if num == "Heads":
                    children.coins[coin] = parent1.coins
                else:
                    children.coins[coin] = parent2.coins
        return children


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
        
                