from decimal import *


class CoinContainer:
    _coins_format_list = (0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50)

    def __init__(self):
        self.coins_list = []
        self.value = 0

    def addCoin(self, value):
        if value in self._coins_format_list:
            self.value = Decimal(str(value))
            self.coins_list.append(value)
        else:
            self.value = Decimal('0')
            print("NIEZNANA MONETA PRZYPISANO WARTOSC 0zł") #TODO:string do zmiany

    def sumOfCoins(self):
        return sum(self.coins_list)

    def chargeCoin(self, value): #TODO: to najprawodpodobniej bede musial zmeinic
        if value in self.coins_list:
            self.coins_list.remove(value)
            return self.value
        else:
            print("nie ma takiej monety")
