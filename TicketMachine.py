from CoinContainer import CoinContainer
from decimal import *


class TicketMachine(CoinContainer):
    avaiableTickets = {
        "reduced20mTicket": 2.20,
        "reduced40mTicket": 4.70,
        "reduced60mTicket": 7.50,
        "normal20mTicket ": 3.70,
        "normal40mTicket ": 6.20,
        "normal60mTicket ": 10.2
    }

    ticketsPrice = 0

    def __init__(self):
        super().__init__()

    def addTicket(self, ticket, amount=1):
        print("testasdf")
        self.ticketsPrice = Decimal(self.ticketsPrice+ self.avaiableTickets[str(ticket)] * amount)

    def showCostOfTickets(self):
        print("total cost of tickets :", self.ticketsPrice)

    def change(self, userListOfCoins):  # generalnie podaje mu liste monet wrzuconą przez usera
        if self.ticketsPrice == Decimal(sum(userListOfCoins)):
            print("Thank you citzen!")
            self.coins_list = self.coins_list + userListOfCoins
        elif self.ticketsPrice < self.sumOfCoins():  # wydaje reszte
            change = Decimal(sum(userListOfCoins)) - Decimal(self.ticketsPrice)
            self.coins_list.sort(reverse=True) #TODO:to musze dokonczyc
            print(self.coins_list)
            # while change > 0 :

        elif self.ticketsPrice > self.sumOfCoins():
            print("Tylko odliczona kwota")
            return userListOfCoins
