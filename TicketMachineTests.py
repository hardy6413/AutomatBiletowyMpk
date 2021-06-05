import unittest
from decimal import Decimal

from CoinContainer import CoinContainer
from InapropriateAmountException import InapropriateAmountException
from TicketMachine import TicketMachine


class MyTestCase(unittest.TestCase):
    def test_shouldRetunrNoRemainder(self):
        # given
        ticketMachine = TicketMachine()
        userCoinContainer = CoinContainer()
        ticket = "Bilet ulgowy20m"
        ticketMachine.addTicket(ticket)
        userCoinContainer.addCoin("2")
        userCoinContainer.addCoin("0.2")
        # when
        returnList = ticketMachine.remainderCalculator(userCoinContainer)

        #then
        self.assertEqual(0, sum(returnList))

    def test_shouldReturnRemainder(self):
        # given
        ticketMachine = TicketMachine()
        userCoinContainer = CoinContainer()
        ticket = "Bilet ulgowy20m"
        ticketMachine.addTicket(ticket)
        userCoinContainer.addCoin("2")
        userCoinContainer.addCoin("0.2")
        userCoinContainer.addCoin("0.2")
        userCoinContainer.addCoin("0.5")
        expectedReturnList=[]
        expectedReturnList.append(Decimal(0.5))
        expectedReturnList.append(Decimal(0.2))


        # when
        returnList = ticketMachine.remainderCalculator(userCoinContainer)

        # then
        self.assertEqual(sum(returnList), round(sum(expectedReturnList),1))

    def test_shouldReturnCantReturnRemainder(self):
        # given
        ticketMachine = TicketMachine()
        userCoinContainer = CoinContainer()
        ticket = "Bilet ulgowy20m"
        ticketMachine.addTicket(ticket)
        userCoinContainer.addCoin("50")

        expectedReturnList = []
        expectedReturnList.append(Decimal(50))
        # when
        returnList = ticketMachine.remainderCalculator(userCoinContainer)

        #then
        self.assertEqual(returnList, expectedReturnList)

    def test_shouldCorrectlySumCoins(self):
        # given
        ticketMachine = TicketMachine()
        userCoinContainer = CoinContainer()
        ticket = "Bilet ulgowy20m"
        for i in range (0,220):
            userCoinContainer.addCoin("0.01")
        ticketMachine.addTicket(ticket)

        # when
        returnList = ticketMachine.remainderCalculator(userCoinContainer)
        #then

        self.assertEqual(sum(returnList),0)

    def test_shouldSumTicketsPriceCorrectly(self):
        # given
        ticketMachine = TicketMachine()
        firstTicket = "Bilet ulgowy20m"
        secondTicket = "Bilet ulgowy60m"
        ticketMachine.addTicket(firstTicket)
        ticketMachine.addTicket(secondTicket)

        # when
        sumOfTickets = round(Decimal(ticketMachine.avaiableTickets[firstTicket] + ticketMachine.avaiableTickets[secondTicket]) ,1)
        ticketMachine.ticketsPrice= round(ticketMachine.ticketsPrice,1)

        # then
        self.assertEqual(sumOfTickets,ticketMachine.ticketsPrice)





    def test_shouldNotResetCoinsListAfterAddingTicket(self):
        # given
        ticketMachine = TicketMachine()
        userCoinContainer = CoinContainer()
        ticket = "Bilet ulgowy20m"
        otherTicket = "Bilet 20m"
        ticketMachine.addTicket(ticket)
        userCoinContainer.addCoin("2")
        userCoinContainer.addCoin("0.2")
        ticketMachine.addTicket(otherTicket)
        userCoinContainer.addCoin("1")
        userCoinContainer.addCoin("0.2")
        userCoinContainer.addCoin("0.5")
        userCoinContainer.addCoin("2")

        # when
        returnList = ticketMachine.remainderCalculator(userCoinContainer)

        # then

        self.assertEqual(sum(returnList), 0)


    def test_shouldRaiseIncorrectValueErrorWhenAmountIsNotInteger(self):
        # given
        userCoinContainer = CoinContainer()

        # when

        # then

        with self.assertRaises(InapropriateAmountException,) as context:
            userCoinContainer.submitAmount(0.3)


    def test_shouldRaiseIncorrectValueErrorWhenAmountIsNegative(self):
        # given
        userCoinContainer = CoinContainer()

        # when

        # then

        with self.assertRaises(InapropriateAmountException,) as context:
            userCoinContainer.submitAmount(-5)


if __name__ == '__main__':
    unittest.main()
