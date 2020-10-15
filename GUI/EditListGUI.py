from tkinter import *
from tkinter import ttk

from Functionality.MessageManager import MessageManager
from GUI.ListCreatorGUI import ListCreatorGUI
from GUI.InfoBoxGUI import InfoBoxGUI
from Model.DB import DB
from Model.User import User


class EditListGUI(ListCreatorGUI.ProductsInserterGUI):

    def __init__(self, clicked):
        super().__init__()
        self.clicked = clicked
        self.items = []

    def start(self):
        self.root.title('Add products')
        Label(self.root, text="Add products to list:").grid(row=0, column=0, padx=50, pady=10)
        self.init_frames()
        self.init_product_treeview()
        self.get_data_with_database(self.clicked)
        self.get_data_to_Treeview(None)
        self.init_entry_product()
        self.init_buttons()
        print(self.name_of_products, self.number_of_products)

        self.root.mainloop()

    def init_buttons(self):
        add_products_buttons = Button(self.frame2, text='Add product', width=22,
                                             command=self.click_add_products_button)
        add_products_buttons.grid(row=0, column=0, sticky='w')

        send_list = Button(self.frame2, text='Send list', command=self.click_send_list, width=22)
        send_list.grid(row=0, column=2)

        delete_buttons = Button(self.frame2, text='Delete', width=24,
                                       command=self.click_delete_button)
        delete_buttons.grid(row=0, column=1)

        add_member = Button(self.frame2, text='Add member', command=self.click_add_member, width=22)
        add_member.grid(row=1, column=0)

        delete_member = Button(self.frame2, text='Delete member', command=self.click_delete_member, width=24)
        delete_member.grid(row=1, column=1)

        complete_list = Button(self.frame2, text='Complete a list', command=self.click_complete_list, width=22)
        complete_list.grid(row=1, column=2)

        back = Button(self.frame2, text='Back', command=self.click_back, width=22)
        back.grid(row=2, column=2)

    def click_send_list(self):
        MessageManager().send_list(self.clicked, self.items)

    def click_back(self):
        from GUI.MainMenuGUI import MainMenuGUI
        self.root.destroy()
        MainMenuGUI().start()

    def click_add_member(self):
        pass

    def click_delete_member(self):
        pass

    def click_complete_list(self):
        pass

