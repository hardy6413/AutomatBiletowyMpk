from decimal import *
from CoinContainer import CoinContainer
from TicketMachine import TicketMachine
import math
from tkinter import *


def showFrame(frame):
    frame.tkraise()


class StartPage(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        global pageOne
        pageOne = PageOne()


class PageOne(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

        self.grid_rowconfigure(0, weight=0)
        self.grid_columnconfigure(0, weight=0)
        self.grid(row=0, column=0, sticky="NSEW")
        entries = []
        entry1 = IntVar()
        entry2 = IntVar()
        entry3 = IntVar()
        entry4 = IntVar()
        entry5 = IntVar()
        entry6 = IntVar()
        entries.append(entry1)
        entries.append(entry2)
        entries.append(entry3)
        entries.append(entry4)
        entries.append(entry5)
        entries.append(entry6)

        E1 = Entry(self, bd=5, textvariable=entry1)
        E1.grid(row=0, column=1)
        E2 = Entry(self, bd=5, textvariable=entry2)
        E2.grid(row=1, column=1)
        E3 = Entry(self, bd=5, textvariable=entry3)
        E3.grid(row=2, column=1)
        E4 = Entry(self, bd=5, textvariable=entry4)
        E4.grid(row=3, column=1)
        E5 = Entry(self, bd=5, textvariable=entry5)
        E5.grid(row=4, column=1)
        E6 = Entry(self, bd=5, textvariable=entry6)
        E6.grid(row=5, column=1)

        def button_command():
            i = 0
            for ticket in ticketMachine.avaiableTickets:
                if entries[i].get() != 0:
                    ticketMachine.addTicket(ticket, entries[i].get())
                    entries[i].set("0")
                i += 1
            ticketMachine.showCostOfTickets()  # zeby mi pokaalo do sprawdzenia  pozniej usuanc
            pageTwo = PageTwo()
            showFrame(pageTwo)

        i = 0
        for ticket in ticketMachine.avaiableTickets:
            Label(self,
                  text=str(ticket) + " price  " + str(ticketMachine.avaiableTickets[str(ticket)]),
                  height=1, width=30).grid(row=i, column=0)

            Button(self,
                   text="Add",
                   command=button_command, height=1, width=30).grid(row=i, column=2)
            i += 1


class PageTwo(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

        self.grid_rowconfigure(0, weight=0)
        self.grid_columnconfigure(0, weight=0)
        self.grid(row=0, column=0, sticky="NSEW")

        amountOfCoins = IntVar()
        entryAmountOfCoins = Entry(self, bd=5, textvariable=amountOfCoins)
        entryAmountOfCoins.grid(row=3, column=3, columnspan=3, sticky="nsew")
        amountOfCoins.set(1)

        i = 0
        for coin in userCoinContainer._coins_format_list:
            Button(self,
                   text=coin,
                   command=lambda coin=coin: submitCoin(coin, submitAmount()), height=2, width=4).grid(row=1,
                                                                                                       column=i,
                                                                                                       sticky="nsew")
            i += 1

        labelDodaj = Label(self, text="dodaj monete klikając", height=0, width=20).grid(row=0, column=3, columnspan=3,
                                                                                        sticky="nsew")
        labelDodaj = Label(self, text="ilość", height=0, width=6).grid(row=3, column=1, columnspan=1,
                                                                       sticky="nsew")
        Button(self, text="czy chcesz dodać kolejne bilety?", command=lambda: showFrame(pageOne), height=2,
               width=25).grid(row=5, column=1, columnspan=6, sticky="nsew")
        Button(self, text="Zakończ transakcje", command=lambda: finishTransaction(), height=2,
               width=15).grid(row=6, column=1, columnspan=6, sticky="nsew")

        def finishTransaction():
            ticketMachine.ticketsPrice = round(ticketMachine.ticketsPrice,1)
            sumOfUsersCoins=round(userCoinContainer.sumOfCoins(),1)
            if ticketMachine.ticketsPrice > sumOfUsersCoins: #TODO porownywaniue ulamkowych rzeczy
                return None
            window = Tk()
            window.title("")
            if ticketMachine.ticketsPrice == sumOfUsersCoins:  # TODO:to musze pozniej ogarnac
                ticketMachine.coins_list = ticketMachine.coins_list + userCoinContainer.coins_list
                Label(window, text="dziękujemy za transakcję", command=None, height=2,
                      width=25).grid(row=1, column=1, columnspan=1, sticky="nsew")
            elif ticketMachine.ticketsPrice < sumOfUsersCoins:
                ticketMachine.coins_list = ticketMachine.coins_list + userCoinContainer.coins_list
                returnList = []
                remainder = Decimal(0)
                remainder = userCoinContainer.sumOfCoins() - ticketMachine.ticketsPrice
                remainder = round(remainder,1)
                ticketMachine.coins_list.sort(reverse=True)
                for value in ticketMachine.coins_list:
                    if value == remainder:
                        remainder -=value
                        returnList.append(value)
                    elif round((float(value) % float(remainder)),1) == float(value):
                        remainder =  round(float(remainder) - float(value),1)
                        returnList.append(value)
                    if remainder == 0:
                        print(returnList)
                        return returnList
                if sum(returnList) != round(sumOfUsersCoins - ticketMachine.ticketsPrice,1):
                    print("nie mnozna wydac reszty przeprasamy")
                    for coin in userCoinContainer.coins_list:
                        if coin in ticketMachine.coins_list:
                            ticketMachine.coins_list.remove(coin)



        def submitCoin(coin, amount):
            userCoinContainer.addCoin(coin, amount)

        def submitAmount() -> int:
            amount = amountOfCoins.get()
            amountOfCoins.set(1)
            return amount


if __name__ == '__main__':
    userCoinContainer = CoinContainer()
    ticketMachine = TicketMachine()

    root = Tk()

    start = StartPage(root)
    root.title("Automat Biletowy Mpk")
    root.mainloop()
