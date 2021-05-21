
from decimal import *
from tkinter import messagebox
from CoinContainer import CoinContainer
from TicketMachine import TicketMachine
from tkinter import *

class InapropriateAmountException(Exception):
    def __init__(self, info):
        super().__init__(info)
        self.errorMessagebox(info)

    def errorMessagebox(self,info):
        messagebox.showerror("", info)

def showFrame(frame):
    frame.tkraise()


def resetState():
    userCoinContainer.coins_list = []
    ticketMachine.ticketsPrice = 0


class StartPage(Frame):
    global userCoinContainer
    global ticketMachine
    userCoinContainer = CoinContainer()
    ticketMachine = TicketMachine()

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        ticketMachine.coins_list += [0.01, 0.01, 0.02, 0.05, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.5, 1, 2, 5]  # STARTOWE MONETY DLA AUTOMATU
        global pageOne
        pageOne = PageOne()


class PageOne(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

        self.grid_rowconfigure(0, weight=0)
        self.grid_columnconfigure(0, weight=0)
        self.grid(row=0, column=0, sticky="NSEW")
        entries = []
        entry1 = StringVar()
        entry2 = StringVar()
        entry3 = StringVar()
        entry4 = StringVar()
        entry5 = StringVar()
        entry6 = StringVar()
        entry1.set(0)
        entry2.set(0)
        entry3.set(0)
        entry4.set(0)
        entry5.set(0)
        entry6.set(0)
        E1 = Entry(self, bd=5,textvariable=entry1)
        E1.grid(row=0, column=1)
        E2 = Entry(self, bd=5,textvariable=entry2)
        E2.grid(row=1, column=1)
        E3 = Entry(self, bd=5,textvariable=entry3)
        E3.grid(row=2, column=1)
        E4 = Entry(self, bd=5,textvariable=entry4)
        E4.grid(row=3, column=1)
        E5 = Entry(self, bd=5,textvariable=entry5)
        E5.grid(row=4, column=1)
        E6 = Entry(self, bd=5,textvariable=entry6)
        E6.grid(row=5, column=1)

        entries.append(E1)
        entries.append(E2)
        entries.append(E3)
        entries.append(E4)
        entries.append(E5)
        entries.append(E6)
        entries.append(entry1)
        entries.append(entry2)
        entries.append(entry3)
        entries.append(entry4)
        entries.append(entry5)
        entries.append(entry6)

        def ticketsAdder():
            i = 0
            for ticket in ticketMachine.avaiableTickets:
                try:
                    amount = int(entries[i].get())
                    if amount > 0 :
                        ticketMachine.addTicket(ticket, amount)
                    elif amount < 0 :
                        raise InapropriateAmountException("Zła ilość biletów")
                except ValueError:
                    raise InapropriateAmountException("Zła ilość biletów")
                entries[6+i].set("0")
                i += 1
            if ticketMachine.ticketsPrice == 0:
                raise InapropriateAmountException("Nie wybrałeś żadnego biletu")
            ticketMachine.showCostOfTickets()  # zeby mi pokaalo do sprawdzenia  pozniej usuanc
            pageTwo = PageTwo()
            showFrame(pageTwo)

        i = 0
        for ticket in ticketMachine.avaiableTickets:
            Label(self,text=str(ticket) + "   price  " + str(ticketMachine.avaiableTickets[str(ticket)]),height=1, width=30, font=10)\
                .grid(row=i, column=0)

            Button(self, text="Add",command=ticketsAdder, height=1, width=10, font="16")\
                .grid(row=i, column=2)

            i += 1


class PageTwo(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

        self.grid(row=0, column=0, sticky="NSEW")

        amountOfCoins = StringVar()
        entryAmountOfCoins = Entry(self, bd=5, textvariable=amountOfCoins, width=5, font=16)
        entryAmountOfCoins.grid(row=3, column=4, columnspan=4, sticky="nsew")
        amountOfCoins.set(1)

        i = 0
        for coin in userCoinContainer._coins_format_list:
            Button(self,text=coin,command=lambda coin=coin: submitCoin(coin, submitAmount()), height=2, width=4, font=16)\
                .grid(row=1,column=i,sticky="nsew")
            i += 1

        labelDodaj = Label(self, text="dodaj monete klikając", height=2, width=15, font=16)\
            .grid(row=0, column=3,columnspan=5,sticky="nsew")

        labelDodaj = Label(self, text="ilość", height=0, width=6, font=16)\
            .grid(row=3, column=2, columnspan=2,sticky="nsew")

        Button(self, text="czy chcesz dodać kolejne bilety?", command=lambda: showFrame(pageOne), height=2,width=20)\
            .grid(row=5, column=4, columnspan=4, sticky="nsew")

        Button(self, text="Zakończ transakcje", command=lambda: finishTransaction(), height=2,width=10).\
            grid(row=6, column=4, columnspan=4, sticky="nsew")

        def finishTransaction():
            ticketMachine.ticketsPrice = round(ticketMachine.ticketsPrice, 1)
            sumOfUsersCoins = round(userCoinContainer.sumOfCoins(), 1)
            if ticketMachine.ticketsPrice > sumOfUsersCoins:  # TODO porownywaniue ulamkowych rzeczy
                return None

            if ticketMachine.ticketsPrice == sumOfUsersCoins:  # TODO:to musze pozniej ogarnac
                ticketMachine.coins_list = ticketMachine.coins_list + userCoinContainer.coins_list
                info = "Dziękujemy za transakcję"
                printChange(info)
            elif ticketMachine.ticketsPrice < sumOfUsersCoins:
                ticketMachine.coins_list = ticketMachine.coins_list + userCoinContainer.coins_list
                returnList = []
                remainder = userCoinContainer.sumOfCoins() - ticketMachine.ticketsPrice
                remainder = round(remainder, 1)
                ticketMachine.coins_list.sort(reverse=True)
                for value in ticketMachine.coins_list:
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
                        printChange(info)
                        return
                if sum(returnList) != round(sumOfUsersCoins - ticketMachine.ticketsPrice, 1):
                    info = "Tylko odliczona kwota \n" + str(
                        ",".join([str(float(x)) for x in userCoinContainer.coins_list]))
                    printChange(info)
                    for coin in userCoinContainer.coins_list:
                        if coin in ticketMachine.coins_list:
                            ticketMachine.coins_list.remove(coin)

        def submitCoin(coin, amount):
            userCoinContainer.addCoin(coin, amount)

        def submitAmount() -> int:
            try:
                amount = int(entryAmountOfCoins.get())
                if(amount < 0):
                    raise InapropriateAmountException("Zła ilość monet")
                amountOfCoins.set(1)
                return amount
            except ValueError:
                raise InapropriateAmountException("Zła ilość monet")


        def printChange(info):
            messagebox.showinfo("", info)
            showFrame(pageOne)
            resetState()

