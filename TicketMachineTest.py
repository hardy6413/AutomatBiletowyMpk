import unittest
import tkinter
from decimal import *
from tkinter import messagebox
from CoinContainer import CoinContainer
from TicketMachine import TicketMachine
from tkinter import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        #given
        ticketMachine = TicketMachine()
        userCoinContainer =CoinContainer()
        ticketMachine.ticketsPrice = ticketMachine.avaiableTickets["reduced40mTicket"]
        userCoinContainer.addCoin(2)
        userCoinContainer.addCoin(0.2)
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
