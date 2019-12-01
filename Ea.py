from Fitness import Fitness
import operator

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

    def corssover(self):
        pass

    def mutatePopulation(self):
        pass