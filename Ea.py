from Fitness import Fitness
from Member import Member
import Currency from Currency
import operator
import random

class GeneticAlgorithm:
    def __init__(self, goal_value):
        self.goal_value = goal_value

    def rankRoutes(self, population):
        fitnessResults = {}

        for i in range(0, len(population)):
            fitness = Fitness(population[i], self.goal_value)
            fitnessResults[i] = fitness.countFitness()
        
        return sorted(fitnessResults.items(), key = operator.itemgetter(1), reverse = True)

    @staticmethod
    def selection(popRanked, eliteSize):
        pass

    @staticmethod
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