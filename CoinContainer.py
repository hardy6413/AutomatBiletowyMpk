from decimal import *
from InapropriateAmountException import InapropriateAmountException


class CoinContainer:
    '''class asociated with correct coin formats and coin container for both user and ticket machine'''
    _coins_format_list = ("0.01", "0.02", "0.05", "0.1", "0.2", "0.5", "1", "2", "5", "10", "20", "50")

    def __init__(self):
        self.coins_list = []
        self.value = 0

    def addCoin(self, value, amount=1):
        if value in self._coins_format_list:
            self.value = Decimal(str(value))
            for i in range(amount):
                self.coins_list.append(self.value)
        print(" wpłacono " + str(self.sumOfCoins()))

    def sumOfCoins(self):
        return Decimal(sum(self.coins_list))


    def submitAmount(self,entry) -> int:
        '''method that checks if the correct amount was submitted'''
        try:
            amount = int(entry)
            if (amount <= 0):
                raise InapropriateAmountException("Zła ilość monet")
            return amount
        except ValueError:
            raise InapropriateAmountException("Zła ilość monet")
