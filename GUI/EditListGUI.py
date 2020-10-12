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
        self.init_frame()
        self.init_entry_product()
        self.init_buttons()
        self.init_products_treeview()
        self.add_record_to_add_products_tree()
        self.root.mainloop()

    def add_date_to_lists(self):
        query = f"SELECT list_id FROM lists WHERE tittle='{self.clicked}' AND owner='{User.current_logged.nickname}'"
        list_id = DB().get_data_from_db(query)[0][0]
        query = f"SELECT item, count_of_item, prise_per_item FROM items WHERE list_id='{list_id}'"
        self.list_of_products.append(DB().get_data_from_db(query)[0])


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



        #self.root = Tk()
    #     self.frame1 = None
    #     self.frame2 = None
    #     self.frame3 = None
    #     self.entry_product = None
    #     self.entry_num_of_products = None
    #     self.entry_price = None
    #     self.style = None
    #     self.add_products_tree = None
    #     self.style = None
    #     self.list_of_products = []
    #     self.num_of_products = []
    #     self.prise_of_products = []
    #     self.counter = 0
    #     self.clicked = clicked
    #     self.style = ttk.Style()
    #     self.style.theme_use("clam")
    #     self.items = []
    #
    # def __del__(self):
    #     self.root.destroy()
    #
    # def start(self):
    #     self.root.title('Add products')
    #     Label(self.root, text="Add products to list:").grid(row=0, column=0, padx=50, pady=10)
    #     self.init_frame()
    #     self.init_entry_product()
    #     self.init_buttons()
    #     self.init_products_treeview()
    #     self.get_data_to_Treeview()
    #     self.root.mainloop()
    #
    #
    # def init_frame(self):
    #     self.frame1 = LabelFrame(self.root, padx=10, pady=10)
    #     self.frame1.grid(row=1, column=0)
    #     self.frame2 = LabelFrame(self.root)
    #     self.frame2.grid(row=3, column=0)
    #     self.frame3 = LabelFrame(self.root, padx=10, pady=10)
    #     self.frame3.grid(row=4, column=0)
    #
    # def init_entry_product(self):
    #     # creating labels
    #     label1 = Label(self.frame1, text='Name of product', width=30)
    #     label1.grid(row=0, column=0, sticky='w')
    #     label2 = Label(self.frame1, text='Number of product', width=18, anchor=CENTER)
    #     label2.grid(row=0, column=1, sticky='w')
    #     label3 = Label(self.frame1, text='Price per product', width=18, anchor=CENTER)
    #     label3.grid(row=0, column=2, sticky='w')
    #     # creating entry boxes
    #     self.entry_product = Entry(self.frame1, width=30)
    #     self.entry_product.grid(row=1, column=0)
    #     self.entry_num_of_products = Entry(self.frame1, width=17)
    #     self.entry_num_of_products.grid(row=1, column=1)
    #     self.entry_price = Entry(self.frame1, width=17)
    #     self.entry_price.grid(row=1, column=2)
    #
    # def init_buttons(self):
    #     create_add_products_buttons = Button(self.frame2, text='Add product', width=22,
    #                                          command=self.click_add_products_button)
    #     create_add_products_buttons.grid(row=0, column=0, sticky='w')
    #
    # send_list = Button(self.frame2, text='Send list', command=self.click_send_list, width=22)
    # send_list.grid(row=0, column=2)
    #
    #     create_delete_buttons = Button(self.frame2, text='Delete product', width=24,
    #                                    command=self.click_delete_button)
    #     create_delete_buttons.grid(row=0, column=1)
    #
    #     add_member = Button(self.frame2, text='Add member', command=self.click_add_member, width=22)
    #     add_member.grid(row=1, column=0)
    #
    #     delete_member = Button(self.frame2, text='Delete member', command=self.click_delete_member, width=24)
    #     delete_member.grid(row=1, column=1)
    #
    #     complete_list = Button(self.frame2, text='Complete a list', command=self.click_complete_list, width=22)
    #     complete_list.grid(row=1, column=2)
    #
    #     back = Button(self.frame2, text='Back', command=self.click_back, width=22)
    #     back.grid(row=2, column=2)
    #
    # def init_products_treeview(self):
    #     style = ttk.Style()
    #     style.theme_use("clam")
    #     style.configure("Treeview", background="blue", foreground="black", rowheight=25, filedbackground="blue")
    #     style.map("Treeview", background=[('selected', 'blue')])
    #
    #     self.add_products_tree = ttk.Treeview(self.root, style="Treeview")
    #     self.add_products_tree['columns'] = ("Product", "Number", "Price")
    #
    #     self.add_products_tree.column("#0", width=0, stretch=NO)
    #     self.add_products_tree.column('Product', anchor=W, width=100)
    #     self.add_products_tree.column('Number', anchor=E, width=50)
    #     self.add_products_tree.column('Price', anchor=E, width=50)
    #
    #     self.add_products_tree.heading("#0", text="", anchor=W)
    #     self.add_products_tree.heading("Product", text="Product", anchor=W)
    #     self.add_products_tree.heading("Number", text="Number", anchor=W)
    #     self.add_products_tree.heading("Price", text="Price per item", anchor=W)
    #     self.add_products_tree.grid(row=2, column=0, columnspan=1, sticky=W + E)
    #
    #     self.add_products_tree.tag_configure('oddrow', background='white')
    #     self.add_products_tree.tag_configure('evenrow', background='lightblue')
    #
    # def get_data_to_Treeview(self):
    #     query = f"SELECT list_id FROM lists WHERE tittle='{self.clicked}' AND owner='{User.current_logged.nickname}'"
    #     list_id = DB().get_data_from_db(query)[0][0]
    #     query = f"SELECT item, count_of_item, prise_per_item FROM items WHERE list_id='{list_id}'"
    #     self.items = DB().get_data_from_db(query)
    #     for item in self.items:
    #         if self.counter % 2 == 0:
    #
    #             self.add_products_tree.insert(parent='', index='end', iid=self.counter, text='Parent',
    #                                           values=(item[0], item[1], item[2]), tags=('evenrow',))
    #         else:
    #             self.add_products_tree.insert(parent='', index='end', iid=self.counter, text='Parent',
    #                                           values=(item[0], item[1], item[2]), tags=('oddrow',))
    #         self.counter += 1
    #
    # def click_add_products_button(self):
    #     if self.name_checker() and self.number_checker() and self.price_checker():
    #         self.list_of_products.append(self.entry_product.get())
    #         self.num_of_products.append(self.entry_num_of_products.get())
    #         self.prise_of_products.append(self.entry_price.get())
    #         self.add_record_to_add_products_tree()
    #         self.init_entry_product()
    #
    # def name_checker(self):
    #     if self.entry_product.get() == '':
    #         message = "You must enter the name of the item."
    #         InfoBoxGUI().info_box(message)
    #     else:
    #         return True
    #
    # def number_checker(self):
    #     try:
    #         int(self.entry_num_of_products.get())
    #     except ValueError as e:
    #         msg = "Number of item must be integer."
    #         InfoBoxGUI().info_box(msg)
    #     else:
    #         return True
    #
    # def price_checker(self):
    #     try:
    #         float(self.entry_price.get())
    #     except (ValueError, TypeError):
    #         msg = "Price must be float \n\n Use dot, not comma."
    #         InfoBoxGUI().info_box(msg)
    #     else:
    #         return True
    #
    # def add_record_to_add_products_tree(self):
    #     query = f"SELECT list_id FROM lists WHERE tittle='{self.clicked}' AND owner='{User.current_logged.nickname}'"
    #     list_id = DB().get_data_from_db(query)[0][0]
    #     query = f"SELECT item, count_of_item, prise_per_item FROM items WHERE list_id='{list_id}'"
    #     for list in (DB().get_data_from_db(query)):
    #         if self.counter % 2 == 0:
    #
    #             self.add_products_tree.insert(parent='', index='end', iid=self.counter, text='Parent',
    #                                           values=(list[0], list[1], list[2]), tags=('evenrow',))
    #         else:
    #             self.add_products_tree.insert(parent='', index='end', iid=self.counter, text='Parent',
    #                                           values=(list[0], list[1], list[2]), tags=('oddrow',))
    #         self.counter += 1
    #
    # def click_next_button(self):
    #     ListCreatorGUI.list_of_products = self.list_of_products
    #     ListCreatorGUI.num_of_product = self.num_of_products
    #     ListCreatorGUI.price_per_item = self.prise_of_products
    #     print(ListCreatorGUI.list_of_products, ListCreatorGUI.num_of_product, ListCreatorGUI.price_per_item)
    #     self.root.withdraw()
    #     ListCreatorGUI.FriendsInserterGUI().start()
    #
# def click_delete_button(self):
#     # TODO: add deleting item from list_of_product
#     items = self.add_products_tree.selection()
#     for record in items:
#         self.add_products_tree.delete(record)
    #
    # def click_add_item(self):
    #     pass
    #
    # def click_add_member(self):
    #     pass
    #
    # def click_delete_item(self):
    #     pass
    #
    # def click_delete_member(self):
    #     pass
    #
    # def click_send_list(self):
    #     MessageManager().send_list(self.clicked, self.items)
    #
    # def click_complete_list(self):
    #     pass
    #
    # def click_back(self):
    #     from GUI.MainMenuGUI import MainMenuGUI
    #     self.root.destroy()
    #     MainMenuGUI().start()
    #
    #
    #
