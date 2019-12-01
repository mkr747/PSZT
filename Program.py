from Currency import Currency
from DataProvider import DataProvider
from Ea import EvolutionaryAlgorithm
from Member import Member

N_GENERATIONS = 20
CROSS_RATE = 0.2
MUTATION_RATE = 0.01
POP_SIZE = 200

def main():

    Member.Change = 38
    ea = EvolutionaryAlgorithm(DataProvider.setUpCurrency(), POP_SIZE, CROSS_RATE, MUTATION_RATE )
    ea.countMinimalCoins()
    for generation in range(N_GENERATIONS):
        ea.evolve()

if __name__ == "__main__":
    main()