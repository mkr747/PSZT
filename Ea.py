from Currency import Currency
from Member import Member
from collections import defaultdict
import operator
import random
import numpy as np

class EvolutionaryAlgorithm:
    
    def __init__(self, currency, pop_size, crossRate, mutationRate):
        self.currency = currency
        self.crossRate = crossRate
        self.mutationRate = mutationRate
        self.population = []
        self.pop_size = pop_size
        self.best_value = 0
        for _ in range(pop_size):
            member = Member(currency)
            for coin in currency.coins:
                member.coins[coin] = np.random.randint(Member.Change)
            self.population.append(member)

    def getFitness(self, member):
        fitness = 0
        for coin in self.currency.coins:
            fitness += abs(self.minimal[coin] - member.coins[coin]) * coin
        
        return 1/(fitness + 1e-4)
        
    def getAllFitness(self):
        fitness = []
        for member in self.population:
            fitness.append(self.getFitness(member))
        
        return fitness

    def select(self):
        fitness = self.getAllFitness()
        self.best_value = max(fitness)
        print(f"The best solution : {self.population[fitness.index(max(fitness))].coins} with fitness : {self.best_value}")
        idx = np.random.choice(np.arange(self.pop_size), size=self.pop_size, replace=True, p=self.probability(fitness))
        newGeneration = []
        for index in idx:
            newGeneration.append(self.population[index])

        self.population = newGeneration

        return self.population

    def probability(self, fitness):
        sum = 0
        for value in fitness:
            sum += value

        prob = []
        for value in fitness:
            probVal = value/sum
            prob.append(probVal)

        return prob

    def crossover(self, parent, population):
        if np.random.rand() < self.crossRate:
            randomMemberIndex = random.randint(0, self.pop_size - 1)
            child = Member(self.currency)
            for coin in self.currency.coins:
                num = np.random.randint(2)
                if num:
                    child.coins[coin] = parent.coins[coin]
                else:
                    child.coins[coin] = population[randomMemberIndex].coins[coin]

            return child

        return parent

    def mutate(self, child):
        if random.randint(0, self.pop_size) < self.mutationRate:
            coin = random.choice(self.currency.coins)
            child.coins[coin] += 1 if random.random() < 0.5 or child.coins[coin] == 0 else -1

        return child

    def evolve(self):
        population = self.select()
        population_copy = population.copy()
        for i in range(len(population)):
            child = self.crossover(population[i], population_copy)
            child = self.mutate(child)
            population[i] = child

        self.population = population

    #Run after init
    def countMinimalCoins(self):
        change = Member.Change
        dictionary = { value: 0 for value in self.currency.coins }
        for coin in self.currency.coins:
            remainder = change % coin
            dictionary[coin] = (change - remainder) / coin
            change = remainder

        print(f"Minimal {dictionary}")
        self.minimal = dictionary
        
                