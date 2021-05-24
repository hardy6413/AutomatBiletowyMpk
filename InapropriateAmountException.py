from tkinter import messagebox


class InapropriateAmountException(Exception):
    def __init__(self, info):
        super().__init__(info)
        self.errorMessagebox(info)

    def errorMessagebox(self, info):
        messagebox.showerror("", info)
