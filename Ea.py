from Currency import Currency
from Member import Member
from collections import defaultdict
import operator
import random

CROSS_RATE = 0.2
MUTATION_RATE = 0.01

class EvolutionaryAlgorithm:

    def __init__(self, currency, population):
        self.currency = currency
        self.population = population

    def getFitness(self, member):
        fitness = 0
        for coin in self.currency.coins:
            fitness += (self.minimal[coin] - member.coins[coin]) * coin
        return fitness

    def select(self):
        fitness = self.getAllFitness() + 1e-4
        idx = np.random.choice(np.arange(len(self.population), size=len(self.population), replace=True, p=1-fitness/fitness.sum())
        return self.population[idx]

    def crossover(self, parent, population):
        if random.rand() < CROSS_RATE:
            i_ = random.randint(0, len(population))
            child = Member(self.currency)
            for coin in currency.coins:
                num = random.choice(["Heads", "Tails"])
                if num == "Heads":
                    child.coins[coin] = parent.coins
                else:
                    child.coins[coin] = population[i_].coins
            return child
        return parent

    def mutate(self, child):
        if random.randint(0, len(self.population)):
            coin = random.choice(self.currency)
            child.coins[coin] = random.randint(0, Member.change)
        return child

    def evolve(self):
        population = self.select()
        population_copy = population.copy()
        for parent in population:
            child = self.crossover(parent)
            child = self.mutate(child)
            parent[:] = child
        self.population = population



    def getAllFitness(self):
        fitness = []
        for member in self.population:
            fitness.append(getFitness(member))
        
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
        
                