from CoinContainer import CoinContainer
from decimal import *


class TicketMachine(CoinContainer):
    '''Class that helps me to do everyting around tickets'''
    avaiableTickets = {
        "Bilet ulgowy20m": 2.20,
        "Bilet ulgowy40m": 4.70,
        "Bilet ulgowy60m": 7.50,
        "Bilet 20m": 3.70,
        "Bilet 40m": 6.20,
        "Bilet 60m": 10.2
    }

    ticketsPrice = 0

    def __init__(self):
        super().__init__()

    def addTicket(self, ticket, amount=1):
        self.ticketsPrice = Decimal(self.ticketsPrice+ Decimal(self.avaiableTickets[str(ticket)]) * amount)

    def showCostOfTickets(self):
        print("total cost of tickets :", self.ticketsPrice)

    def remainderCalculator(self,userCoinContainer):
        '''Method that calculates the change when user paid more than he should for a ticket'''
        self.ticketsPrice = (round(Decimal(self.ticketsPrice), 1))
        sumOfUsersCoins = round(userCoinContainer.sumOfCoins(), 1)
        returnList = []
        if self.ticketsPrice > sumOfUsersCoins:
            return None
        if self.ticketsPrice == sumOfUsersCoins:
            self.coins_list = self.coins_list + userCoinContainer.coins_list
            return returnList

        elif self.ticketsPrice < sumOfUsersCoins:
            self.coins_list = self.coins_list + userCoinContainer.coins_list
            remainder = userCoinContainer.sumOfCoins() - self.ticketsPrice
            remainder = round(remainder, 1)
            self.coins_list.sort(reverse=True)
            for value in self.coins_list:
                value = round(Decimal(value), 1)
                remainder = round(Decimal(remainder), 1)
                if value == remainder:
                    remainder -= value
                    returnList.append(value)
                elif remainder - value > 0:
                    remainder = round(Decimal(remainder - value), 1)
                    returnList.append(value)
                if remainder == 0:
                    return returnList

            if sum(returnList) != round(sumOfUsersCoins - self.ticketsPrice, 1):
                for coin in userCoinContainer.coins_list:
                    if coin in self.coins_list:
                        self.coins_list.remove(coin)
                return userCoinContainer.coins_list

