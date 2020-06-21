from tkinter import *


class MainMenuGUI:

    def __init__(self):
        self.root = Tk()

    def start(self):
        self.root.title('Main page')
        self.root.geometry('200x400')
        Label(self.root, text='Main page').grid(row=0, column=0, padx=50, pady=10)
        self.frame()
        self.buttons()
        self.root.mainloop()

    def frame(self):
        self.main_frame = LabelFrame(self.root, padx=50, pady=100)
        self.main_frame.grid(row=1, column=0)

    def buttons(self):
        my_profile_button = Button(self.main_frame, text='My profile', padx=50, pady=20)
        my_profile_button.grid(row=1, column=0)

        my_lists_button = Button(self.main_frame, text='My lists', padx=50, pady=20)
        my_lists_button.grid(row=2, column=0)

        create_new_list_button = Button(self.main_frame, text='Create new list', padx=50, pady=20)
        create_new_list_button.grid(row=3, column=0)

        log_out_button = Button(self.root, text='Log out', padx=50, pady=20)
        log_out_button.grid(row=2, column=0)


print(MainMenuGUI().start())