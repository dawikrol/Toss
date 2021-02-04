from tkinter import *
from tkinter import ttk
from Functionality.MessageManager import MessageManager
from GUI.ListCreatorGUI import ListCreatorGUI
from GUI.InfoBoxGUI import InfoBoxGUI
from Model.DB import DB
from Model.User import User


class EditListGUI(ListCreatorGUI.ProductsInserterGUI):

    def __init__(self, clicked, users_lists, id_users_lists):
        super().__init__()
        self.clicked = clicked
        self.users_lists = users_lists
        self.id_users_lists = id_users_lists
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
        self.root.mainloop()

    def init_buttons(self):
        add_products_buttons = Button(self.frame2, text='Add product', width=22,
                                             command=self.click_add_products_button)
        add_products_buttons.grid(row=0, column=0, sticky='w')

        delete_buttons = Button(self.frame2, text='Delete product', width=24,
                                       command=self.click_delete_button)
        delete_buttons.grid(row=0, column=1)

        back = Button(self.frame2, text='Back', command=self.click_back, width=22)
        back.grid(row=0, column=2)

    def click_add_products_button(self):
        if self.name_checker() and self.number_checker() and self.price_checker():
            query = f"INSERT INTO items VALUES (NULL, {self.current_list_id}, '{self.entry_product.get()}', {self.entry_num_of_products.get()}, {self.entry_price.get()})"
            DB().execute_query(query)
            self.name_of_products.append(self.entry_product.get())
            self.number_of_products.append(self.entry_num_of_products.get())
            self.prices_of_products.append(self.entry_price.get())
            self.add_record_to_add_products_tree()
            self.init_entry_product()

    def click_delete_button(self):
        current_items = self.products_tree.selection()
        try:
            current_product = self.products_tree.item(current_items).get('values')[0]
            index = self.name_of_products.index(current_product)
            self.name_of_products.pop(index)
            self.number_of_products.pop(index)
            self.prices_of_products.pop(index)
            self.add_record_to_add_products_tree()
            query = f"DELETE FROM items WHERE list_id={self.current_list_id} and item='{current_product}'"
            DB().execute_query(query)
        except Exception as e:
            pass

    # def click_send_list(self):
    #     MessageManager().send_list(self.clicked, self.items)

    def click_back(self):
        from GUI.MainMenuGUI import MainMenuGUI
        self.root.destroy()
        MainMenuGUI().start()




