from tkinter import messagebox


class InapropriateAmountException(Exception):
    '''Exception that is used when inapropriate amount as input was given'''
    def __init__(self, info):
        super().__init__(info)
        self.errorMessagebox(info)

    def errorMessagebox(self, info):
        messagebox.showerror("", info)
