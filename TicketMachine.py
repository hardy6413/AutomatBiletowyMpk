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
