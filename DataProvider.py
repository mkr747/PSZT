from Currency import Currency
from Change import Change
import random

class DataProvider:
    ChosenCurrency = None
    @staticmethod
    def setUpCurrency():
        if not DataProvider.ChosenCurrency:
            pln = Currency("PLN", [1, 2, 5])
        
        return pln

    @staticmethod
    def initialPopulation(popSize, changeValue):
        population = []
        DataProvider.setUpCurrency()
        
        for _ in range(0, popSize):
            population.append(
                Change(DataProvider.createChanges(changeValue),
                       DataProvider.ChosenCurrency))
        return population

    @staticmethod
    def createChanges(changeValue):
        result = []
        coins = DataProvider.ChosenCurrency.getCoins()
        for coin in coins:
            coins_amount = random.sample(range(0,changeValue), 1)
            result.append(coins_amount*coin)
        
        return result

