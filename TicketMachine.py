from CoinContainer import CoinContainer
from decimal import *


class TicketMachine(CoinContainer):
    avaiableTickets = {
        "reduced20mTicket": 2.20,
        "reduced40mTicket": 4.70,
        "reduced60mTicket": 7.50,
        "normal20mTicket": 3.70,
        "normal40mTicket": 6.20,
        "normal60mTicket": 10.2
    }

    ticketsPrice = 0

    def __init__(self):
        super().__init__()

    def addTicket(self, ticket, amount=1):
        self.ticketsPrice = Decimal(self.ticketsPrice+ Decimal(self.avaiableTickets[str(ticket)]) * amount)

    def showCostOfTickets(self):
        print("total cost of tickets :", self.ticketsPrice)

    def remainderCalculator(self,userCoinContainer):
        self.ticketsPrice = round(self.ticketsPrice, 1)
        sumOfUsersCoins = round(userCoinContainer.sumOfCoins(), 1)
        if self.ticketsPrice > sumOfUsersCoins:
            return None
        if self.ticketsPrice == sumOfUsersCoins:
            self.coins_list = self.coins_list + userCoinContainer.coins_list
            info = "Dziękujemy za transakcję"
            return info

        elif self.ticketsPrice < sumOfUsersCoins:
            self.coins_list = self.coins_list + userCoinContainer.coins_list
            returnList = []
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
                    info = "Reszta \n " + str(",".join([str(float(x)) for x in returnList]))
                    return info

            if sum(returnList) != round(sumOfUsersCoins - self.ticketsPrice, 1):
                info = "Tylko odliczona kwota \n" + str(
                    ",".join([str(float(x)) for x in userCoinContainer.coins_list]))

                for coin in userCoinContainer.coins_list:
                    if coin in self.coins_list:
                        self.coins_list.remove(coin)
                return info

