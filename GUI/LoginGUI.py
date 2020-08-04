from tkinter import Tk, Label, Entry, Button

from Functionality.LoginManager import LoginManager
from GUI.MainMenuGUI import MainMenuGUI
from GUI.SignInGUI import SignInGUI
from GUI.Validator.InputDataValidator import InputDataValidator


class LoginGUI:

    def __init__(self):
        self.root = Tk()
        self.entry_login = None
        self.entry_password = None
        self.start()


    def start(self):
        self.root.title('Start page')
        Label(self.root, text="Welcome in Toss!").grid(row=0, column=0, columnspan=2)
        self.init_login_entry()
        self.init_password_entry()
        self.init_buttons()
        self.root.mainloop()

    def init_login_entry(self):
        self.entry_login = Entry(self.root, width=35, borderwidth=7)
        self.entry_login.insert(1, 'Login')
        self.entry_login.grid(row=1, column=0, columnspan=3)

    def init_password_entry(self):
        self.entry_password = Entry(self.root, width=35, borderwidth=7)
        self.entry_password.insert(1, 'Password')
        self.entry_password.grid(row=2, column=0, columnspan=3)

    def init_buttons(self):
        button_log_in = Button(self.root, text='Log in', padx=15, pady=5, command=self.log_in)
        button_sign_in = Button(self.root, text='Sign in', padx=15, pady=5, command=self.sign_in)
        button_exit = Button(self.root, text='Exit', command=self.root.quit)
        button_sign_in.grid(row=3, column=1)
        button_log_in.grid(row=3, column=0)
        button_exit.grid(row=3, column=2)

    def sign_in(self):
        self.root.withdraw()
        SignInGUI().start()
        self.root.deiconify()

    def log_in(self):
        input_login = self.entry_login.get()
        input_password = self.entry_password.get()
        if InputDataValidator.login_validator(input_login, input_password):

            LoginManager.log_in()
            self.root.withdraw()
            MainMenuGUI().start()
            self.root.destroy()
            self.__init__()
            self.root.deiconify()

