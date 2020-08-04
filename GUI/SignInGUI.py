from tkinter import *

from Functionality.UserManager import UserManager
from GUI.InfoBoxGUI import InfoBoxGUI

from GUI.Validator.InputDataValidator import InputDataValidator


class SignInGUI:

    def __init__(self):

        self.root = Tk()
        self.frame = None
        self.entry_nick_name = None
        self.entry_firstname = None
        self.entry_surname = None
        self.entry_email = None
        self.entry_password = None
        self.entry_repeat_password = None

    def __del__(self):
        self.root.destroy()





    def start(self):
        self.root.title('Sign in page')
        Label(self.root, text="Sign up now!").grid(row=0, column=0, columnspan=2, padx=50, pady=10)
        self.init_frame()
        self.init_entry_nick_name()
        self.init_entry_firstname()
        self.init_entry_surname()
        self.init_entry_email()
        self.init_entry_password()
        self.init_entry_return_password()
        self.init_buttons()
        self.root.mainloop()

    def init_frame(self):
        self.frame = LabelFrame(self.root, padx=10, pady=10)
        self.frame.grid(row=1, column=0)

    def init_entry_nick_name(self):
        self.entry_nick_name = Entry(self.frame, width=35, borderwidth=7)
        self.entry_nick_name.insert(1, 'Nick name')
        self.entry_nick_name.grid(row=2, column=0)

    def init_entry_firstname(self):
        self.entry_firstname = Entry(self.frame, width=35, borderwidth=7)
        self.entry_firstname.insert(1, 'First name')
        self.entry_firstname.grid(row=3, column=0)

    def init_entry_surname(self):
        self.entry_surname = Entry(self.frame, width=35, borderwidth=7)
        self.entry_surname.insert(1, 'Surname')
        self.entry_surname.grid(row=4, column=0)

    def init_entry_email(self):
        self.entry_email = Entry(self.frame, width=35, borderwidth=7)
        self.entry_email.insert(1, 'Email address')
        self.entry_email.grid(row=5, column=0)

    def init_entry_password(self):
        self.entry_password = Entry(self.frame, width=35, borderwidth=7)
        self.entry_password.insert(1, 'Password')
        self.entry_password.grid(row=6, column=0)

    def init_entry_return_password(self):
        self.entry_repeat_password = Entry(self.frame, width=35, borderwidth=7)
        self.entry_repeat_password.insert(1, 'Repeat the password')
        self.entry_repeat_password.grid(row=7, column=0)

    def init_buttons(self):
        create_account_buttons = Button(self.root, text='Create an account!', padx=15, pady=5,
        command=self.click_create_account_button)
        create_account_buttons.grid(row=8, column=0, sticky=W+E)

    def click_create_account_button(self):
        nick = self.entry_nick_name.get()
        firstname = self.entry_firstname.get()
        surname = self.entry_surname.get()
        email = self.entry_email.get()
        password = self.entry_password.get()
        r_password = self.entry_repeat_password.get()

        if InputDataValidator.sign_up_validator(nick, firstname, surname, email, password, r_password):
            UserManager.create_new_user(nick, firstname, surname, email, password)

        else:
            InfoBoxGUI().info_box(message='The entered data are incorrect')
        self.root.withdraw()
        self.root.quit()

