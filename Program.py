from Currency import Currency
from DataProvider import DataProvider
from Ea import EvolutionaryAlgorithm
from Member import Member

CROSS_RATE = 0.2
MUTATION_RATE = 0.05
POP_SIZE = 200
CHANGE = 57
NON_ZERO_FITNESS = 1e-4

def main():
    Member.setChange(CHANGE)
    ea = EvolutionaryAlgorithm(DataProvider.setUpCurrency(), POP_SIZE, CROSS_RATE, MUTATION_RATE )
    ea.countMinimalCoins()
    generation = 0
    while ea.best_value != 1/NON_ZERO_FITNESS:
        print(f"Generation {generation}:", end = " ")
        generation += 1
        ea.evolve()

if __name__ == "__main__":
    main()