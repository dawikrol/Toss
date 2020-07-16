from tkinter import *



class MainMenuGUI:

    def __init__(self):
        self.root = Tk()

    def start(self):
        self.root.title('Main page')
        Label(self.root).grid(row=0, column=0)
        self.root.geometry('270x250')
        self.init_drop_down_list()
        self.init_listbox()
        self.init_buttons()
        self.root.mainloop()

    def init_drop_down_list(self):

        lists = [
                    'test', 'test1', 'test2'
                ]
        clicked = StringVar()
        clicked.set(lists[0])
        drop = OptionMenu(self.root, clicked, *lists)
        drop.config(width=20)
        drop.grid(row=1, column=0, columnspan=3)

    def init_listbox(self):
        list_of_items = Listbox(self.root)
        list_of_items.config(width=26)
        list_of_items.insert(0, 'test')
        list_of_items.insert(1, 'test1')
        list_of_items.grid(row=2, column=0, columnspan=3)

    def init_buttons(self):
        add_item = Button(self.root, text='+', padx=12).grid(row=3, column=0, sticky='w')
        delete_item = Button(self.root, text='-', padx=12).grid(row=3, column=1, sticky='w')
        edit_list = Button(self.root, text='Edit list', padx=14).grid(row=3, column=2)
        create_new_list = Button(self.root, text='Create new list', padx=2).grid(row=1, column=3)
        my_profile = Button(self.root, text='  My profile ', padx=8).grid(row=2, column=3, sticky='n')
        log_out = Button(self.root, text='   Log out   ', padx=10).grid(row=3, column=3, sticky='s')
