from tkinter import *
from GUI.MainMenuGUI import MainMenuGUI
from GUI.SignInGUI import SignInGUI
from GUI.Validator.InputDataValidator import InputDataValidator
from Model.DB import DB
from Model.User import User


class LoginGUI:

    '''LoginGUI create GUI and manages the login process.'''

    def __init__(self):
        self.root = Tk()
        self.entry_login = None
        self.entry_password = None
        self.start()

    def start(self):
        self.root.title('Login')
        self.init_login_entry()
        self.init_password_entry()
        self.init_buttons()
        self.root.mainloop()

    def init_login_entry(self):
        self.entry_login = Entry(self.root, width=35, borderwidth=7)
        self.entry_login.insert(1, 'Login')
        self.entry_login.grid(row=1, column=0, columnspan=3)

    def init_password_entry(self):
        self.entry_password = Entry(self.root, width=35, borderwidth=7, show = "*")
        self.entry_password.insert(1, 'Password')
        self.entry_password.grid(row=2, column=0, columnspan=3)

    def init_buttons(self):
        button_log_in = Button(self.root, text='Log in', padx=15, pady=5, command=self.click_log_in)
        button_sign_in = Button(self.root, text='Sign in', padx=15, pady=5, command=self.click_sign_in)
        button_exit = Button(self.root, text='Exit', command=self.root.quit)
        button_sign_in.grid(row=3, column=1)
        button_log_in.grid(row=3, column=0)
        button_exit.grid(row=3, column=2)

    def click_sign_in(self):
        self.root.withdraw()
        SignInGUI().start()
        self.root.deiconify()

    def click_log_in(self):

        '''The log_in method check correctness login and password.
         In the next step it set currently logged user and run main menu.'''

        input_login = self.entry_login.get()
        input_password = self.entry_password.get()
        if InputDataValidator.login_validator(input_login, input_password):
            User.current_logged = DB().get_user_from_db(input_login)
            self.root.destroy()
            MainMenuGUI().start()




