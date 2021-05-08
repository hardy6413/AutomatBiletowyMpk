import tkinter

from CoinContainer import CoinContainer
from TicketMachine import TicketMachine

from tkinter import *




def button_command():
    i = 0
    for ticket in ticketMachine.avaiableTickets:
        if entries[i].get()!=0:
            ticketMachine.addTicket(ticket,entries[i].get())
            entries[i].set("0")
        i+=1
    ticketMachine.showCostOfTickets()

if __name__ == '__main__':

    userCoinContainer = CoinContainer()
    ticketMachine = TicketMachine()

    root = Tk()
    root.title("Automat Biletowy Mpk")
    entries=[]
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

    E1 = Entry(root, bd=5,textvariable = entry1)
    E1.grid(row=0, column=1)
    E2 = Entry(root, bd=5,textvariable = entry2)
    E2.grid(row=1, column=1)
    E3 = Entry(root, bd=5,textvariable = entry3)
    E3.grid(row=2, column=1)
    E4 = Entry(root, bd=5,textvariable = entry4)
    E4.grid(row=3, column=1)
    E5 = Entry(root, bd=5,textvariable = entry5)
    E5.grid(row=4, column=1)
    E6 = Entry(root, bd=5,textvariable = entry6)
    E6.grid(row=5, column=1)

    i = 0
    for ticket in ticketMachine.avaiableTickets:
        Label(root,
              text=str(ticket) + " price  " + str(ticketMachine.avaiableTickets[str(ticket)]),
               height=1, width=30).grid(row=i, column=0)

        Button(root,
               text="Add",
               command=button_command, height=1, width=30).grid(row=i, column=2)
        i += 1

    root.mainloop()

    # ticketMachine.change(userCoinContainer.coins_list)

    '''for ticket in ticketMachine.avaiableTickets:
        # jakis amount do tych ticketow
        ticketMachine.addTicket(ticket, 2)
        ticketMachine.showCostOfTickets()
        if userCoinContainer.sumOfCoins() >= TicketMachine.ticketsPrice:
            ticketMachine.change(userCoinContainer.coins_list)
        else:
            print("test")'''
