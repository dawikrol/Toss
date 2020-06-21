from tkinter import Tk, Label, Entry, Button

from Functionality.LoginManager import LoginManager
from GUI.SignInGUI import SignInGUI


class LoginGUI:

    def __init__(self):
        self.root = Tk()


    def start(self):
        self.root.title('Start page')
        Label(self.root, text="Welcome in Toss!").grid(row=0, column=0, columnspan=2)
        self.init_login_entry()
        self.init_password_entry()
        self.init_buttons()
        self.root.mainloop()

    def init_login_entry(self):
        entry_login = Entry(self.root, width=35, borderwidth=7)
        entry_login.insert(1, 'Login')
        entry_login.grid(row=1, column=0, columnspan=3)

    def init_password_entry(self):
        entry_password = Entry(self.root, width=35, borderwidth=7)
        entry_password.insert(1, 'Password')
        entry_password.grid(row=2, column=0, columnspan=3)

    def init_buttons(self):
        button_log_in = Button(self.root, text='Log in', padx=15, pady=5, command=LoginManager.log_in)
        button_sign_in = Button(self.root, text='Sign in', padx=15, pady=5, command=self.sign_in)
        button_exit = Button(self.root, text='Exit', command=self.root.quit)
        button_sign_in.grid(row=3, column=1)
        button_log_in.grid(row=3, column=0)
        button_exit.grid(row=3, column=2)

    def sign_in(self):
        self.root.destroy()
        SignInGUI().start()
