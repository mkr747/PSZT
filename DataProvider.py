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