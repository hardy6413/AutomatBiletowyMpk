from CoinContainer import CoinContainer
from TicketMachine import TicketMachine
from tkinter import *
import tkinter as tk

def button_command():
    text=entry1.get()
    print(text)
    return None



if __name__ == '__main__':

    userCoinContainer = CoinContainer()
    ticketMachine = TicketMachine()
    ticketMachine.addCoin("5", 2)
    ticketMachine.addCoin("2", 2)
    userCoinContainer.addCoin("5")
    userCoinContainer.addCoin("2")
    print(ticketMachine.sumOfCoins())
    root =tk.Tk()
    root.title("Automat Biletowy Mpk")
    root.geometry('800x600')



    i = 0
    for ticket in ticketMachine.avaiableTickets:
        tk.Label(root,
                 text=str(ticket) + " price  " + str(ticketMachine.avaiableTickets[str(ticket)]),
                 fg='White',
                 bg='dark green', height=1, width=30).pack()

        entry1 = tk.Entry(root, width=20)
        entry1.pack()

        tk.Button(root,
                  text="Add",
                  fg='White',
                  bg='dark green', command=button_command, height=1, width=30).pack()
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
