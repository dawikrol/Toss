from tkinter import *
from tkinter import ttk

from GUI.InfoBoxGUI import InfoBoxGUI
from Model.DB import DB
from Model.User import User


class ListCreatorGUI:

    list_name = ''
    list_of_products = []
    id_list_of_products = ''
    num_of_product = []
    price_per_item = []
    list_of_friends = []

    def __init__(self):
        self.root = Tk()
        self.frame = None
        self.frame2 = None
        self.list_name = None
        self.add_friends = None
        self.list_of_products = []
        self.list_of_friends = []


    def __del__(self):
        self.root.destroy()

    def start(self):
        self.root.title('Create new list')
        Label(self.root, text="Name your list.").grid(row=0, column=0, columnspan=2, padx=50, pady=10)
        self.init_frame()
        self.init_list_name()
        self.init_buttons()
        self.root.mainloop()


    def init_frame(self):
        self.frame = LabelFrame(self.root, padx=10, pady=10)
        self.frame.grid(row=1, column=0)

    def init_list_name(self):
        # TODO: The inscription should disappear after click in the window
        self.list_name = Entry(self.frame, width=35, borderwidth=7)
        self.list_name.insert(1, 'List name')
        self.list_name.grid(row=3, column=0)

    def init_buttons(self):
        create_next_button = Button(self.root, text='Next', padx=15, pady=5,
                                    command=self.click_next_button)
        create_next_button.grid(row=8, column=0, sticky=W+E)

    def click_next_button(self):
        """This module validates the inputs, set a list_name and starts the Add Products GUI"""
        if self.list_name.get() == '':
            message = "The list name field can't be empty"
            InfoBoxGUI().info_box(message)
        list_name = self.list_name.get()
        query = f"SELECT tittle from lists WHERE owner = '{User.current_logged.nickname}'"
        names_of_lists = [list_name[0] for list_name in DB().get_data_from_db(query)]
        if list_name in names_of_lists:
            message = "A list with that name already exist. \n Name the list in a different way."
            InfoBoxGUI().info_box(message)
        else:
            ListCreatorGUI.list_name = self.list_name.get()
            self.root.destroy()
            ListCreatorGUI.ProductsInserterGUI().start()

    class ProductsInserterGUI:

        def __init__(self):
            self.root = Tk()
            style = ttk.Style()
            style.theme_use("clam")
            style.configure("Treeview", background="blue", foreground="black", rowheight=25, filedbackground="blue")
            style.map("Treeview", background=[('selected', 'blue')])
            self.frame1 = None
            self.frame2 = None
            self.frame3 = None
            self.entry_product = None
            self.entry_num_of_products = None
            self.entry_price = None
            self.style = None
            self.add_products_tree = None
            self.style = None
            self.list_of_products = []
            self.num_of_products = []
            self.prise_of_products = []
            self.counter = 0
            self.style = ttk.Style()
            self.style.theme_use("clam")
            style = ttk.Style()
            style.theme_use("clam")
            style.configure("Treeview", background="blue", foreground="black", rowheight=25, filedbackground="blue")
            style.map("Treeview", background=[('selected', 'blue')])


        def __del__(self):
            self.root.destroy()

        def start(self):
            self.root.title('Add products')
            Label(self.root, text="Add products to list:").grid(row=0, column=0, padx=50, pady=10)
            self.init_frame()
            self.init_entry_product()
            self.init_buttons()
            self.init_products_treeview()
            self.root.mainloop()

        def init_frame(self):
            self.frame1 = LabelFrame(self.root, padx=10, pady=10)
            self.frame1.grid(row=1, column=0)
            self.frame2 = LabelFrame(self.root)
            self.frame2.grid(row=3, column=0)
            self.frame3 = LabelFrame(self.root, padx=10, pady=10)
            self.frame3.grid(row=4, column=0)

        def init_entry_product(self):
            # creating labels
            label1 = Label(self.frame1, text='Name of product', width=30)
            label1.grid(row=0, column=0, sticky='w')
            label2 = Label(self.frame1, text='Number of product', width=18, anchor=CENTER)
            label2.grid(row=0, column=1, sticky='w')
            label3 = Label(self.frame1, text='Price per product', width=18, anchor=CENTER)
            label3.grid(row=0, column=2, sticky='w')
            # creating entry boxes
            self.entry_product = Entry(self.frame1, width=30)
            self.entry_product.grid(row=1, column=0)
            self.entry_num_of_products = Entry(self.frame1, width=17)
            self.entry_num_of_products.grid(row=1, column=1)
            self.entry_price = Entry(self.frame1, width=17)
            self.entry_price.grid(row=1, column=2)

        def init_buttons(self):
            create_add_products_buttons = Button(self.frame2, text='Add product', width=22,
                                                 command=self.click_add_products_button)
            create_add_products_buttons.grid(row=0, column=0, sticky='w')

            create_next_buttons = Button(self.frame2, text='Next', width=22,
                                         command=self.click_next_button)
            create_next_buttons.grid(row=0, column=2)

            create_delete_buttons = Button(self.frame2, text='Delete', width=24,
                                           command=self.click_delete_button)
            create_delete_buttons.grid(row=0, column=1)

        def init_products_treeview(self):
            # style nie działa - treeview go nie widzi, zbudowane w innej metodzie (brudnopis) działa. Coś nie tak z klasą.
            style = ttk.Style()
            style.theme_use("clam")
            style.configure("Treeview", background="blue", foreground="black", rowheight=25, filedbackground="blue")
            style.map("Treeview", background=[('selected', 'blue')])

            self.add_products_tree = ttk.Treeview(self.root, style="Treeview")
            self.add_products_tree['columns'] = ("Product", "Number", "Price")

            self.add_products_tree.column("#0", width=0, stretch=NO)
            self.add_products_tree.column('Product', anchor=W, width=100)
            self.add_products_tree.column('Number', anchor=E, width=50)
            self.add_products_tree.column('Price', anchor=E, width=50)

            self.add_products_tree.heading("#0", text="", anchor=W)
            self.add_products_tree.heading("Product", text="Product", anchor=W)
            self.add_products_tree.heading("Number", text="Number", anchor=W)
            self.add_products_tree.heading("Price", text="Price per item", anchor=W)
            self.add_products_tree.grid(row=2, column=0, columnspan=1, sticky=W+E)

            self.add_products_tree.tag_configure('oddrow', background='white')
            self.add_products_tree.tag_configure('evenrow', background='lightblue')

        def click_add_products_button(self):
            if self.name_checker() and self.number_checker() and self.price_checker():
                self.list_of_products.append(self.entry_product.get())
                self.num_of_products.append(self.entry_num_of_products.get())
                self.prise_of_products.append(self.entry_price.get())
                self.add_record_to_add_products_tree()
                self.init_entry_product()

        def add_record_to_add_products_tree(self):
            self.add_products_tree.delete(*self.add_products_tree.get_children())
            for item, number, price in zip(self.list_of_products, self.num_of_products, self.prise_of_products):
                if self.counter % 2 == 0:

                    self.add_products_tree.insert(parent='', index='end', iid=self.counter, text='Parent',
                                              values=(item, number, price), tags=('evenrow',))
                else:
                    self.add_products_tree.insert(parent='', index='end', iid=self.counter, text='Parent',
                                              values=(item, number, price), tags=('oddrow',))
                self.counter += 1

        def name_checker(self):
            if self.entry_product.get() == '':
                message = "You must enter the name of the item."
                InfoBoxGUI().info_box(message)
            if self.entry_product.get() in self.list_of_products:
                message = "The product is already on the list."
                InfoBoxGUI().info_box(message)
            if len(self.entry_product.get()) > 60:
                message = "The name of product is too long."
                InfoBoxGUI().info_box(message)
            else:
                return True

        def number_checker(self):
            try:
                int(self.entry_num_of_products.get())
            except ValueError as e:
                msg = "Number of item must be integer."
                InfoBoxGUI().info_box(msg)
            else:
                return True

        def price_checker(self):
            try:
                float(self.entry_price.get())
            except (ValueError, TypeError):
                msg = "Price must be float \n\n Use dot, not comma."
                InfoBoxGUI().info_box(msg)
            else:
                return True

        def click_next_button(self):
            ListCreatorGUI.list_of_products = self.list_of_products
            ListCreatorGUI.num_of_product = self.num_of_products
            ListCreatorGUI.price_per_item = self.prise_of_products
            self.root.destroy()
            ListCreatorGUI.FriendsInserterGUI().start()

        def click_delete_button(self):
            # TODO: add deleting item from list_of_product
            #items = self.add_products_tree.selection()
            for item in self.add_products_tree.selection():
                item_text = self.add_products_tree.item(item, "text")
                print(item_text)
            # for record in items:
            #     self.add_products_tree.delete(record)

    class FriendsInserterGUI:

        def __init__(self):
            self.root = Tk()
            self.frame = None
            self.entry_friends = None
            self.list_of_friends = []

        def __del__(self):
            self.root.destroy()

        def start(self):
            self.root.title('Add your friends')
            Label(self.root, text="Add your friends to list:").grid(row=0, column=0, columnspan=1, padx=50, pady=10)
            self.init_frame()
            self.init_entry_product()
            self.init_buttons()
            self.init_listbox()
            self.root.mainloop()

        def init_frame(self):
            self.frame = LabelFrame(self.root, padx=10, pady=10)
            self.frame.grid(row=1, column=0)

        def init_entry_product(self):
            self.entry_friends = Entry(self.frame, width=35, borderwidth=7)
            self.entry_friends.insert(1, 'Put nick your friend')
            self.entry_friends.grid(row=0, column=0)

        def init_buttons(self):
            create_add_friends_buttons = Button(self.frame, text='+', padx=4, pady=4,
                                                command=self.click_add_friend_button)
            create_add_friends_buttons.grid(row=0, column=1, sticky='e')
            create_list_buttons = Button(self.root, text='Create a new list!', padx=15, pady=5,
                                         command=self.click_create_list_button)
            create_list_buttons.grid(row=4, column=0, sticky=W + E)

        def init_listbox(self):
            list_of_friends = Listbox(self.root)
            list_of_friends.config(width=26)
            for friend in self.list_of_friends:
                list_of_friends.insert(self.list_of_friends.index(friend), friend)
            list_of_friends.grid(row=2, column=0, columnspan=1, sticky=W + E)

        def click_add_friend_button(self):
            nick = self.entry_friends.get()
            if ListCreatorGUI.FriendsInserterGUI().check_if_friend_exist_in_database(nick):
                self.list_of_friends.append(nick)
                self.init_listbox()
            else:
                InfoBoxGUI().error_box('User with this nickname does not exist!')

        def check_if_friend_exist_in_database(self, nick):
            nicks = [nick[0] for nick in DB().get_data_from_db(query="SELECT nick from users")]
            if nick in nicks and nick != User.current_logged.nickname:
                return True

        def click_create_list_button(self):
            ListCreatorGUI.list_of_friends = self.list_of_friends
            ListCreatorGUI.FriendsInserterGUI().add_list_to_db()
            ListCreatorGUI.FriendsInserterGUI().add_products_to_db()
            ListCreatorGUI.FriendsInserterGUI().add_data_to_relations_table()
            self.root.destroy()
            from GUI.MainMenuGUI import MainMenuGUI
            MainMenuGUI().start()


        def add_data_to_lists_table(self):
            # preparing data to insert to lists table
            str_of_products = ', '.join(ListCreatorGUI.list_of_products)
            str_of_products = str_of_products[:-2]
            # TODO: a part this functionality has been moved to CreateNewListGUI
            #  insert data to lists table
            query = f"INSERT INTO lists VALUES (NULL,'{ListCreatorGUI.list_name}', '{str_of_products}');"
            DB().execute_query(query)

        def add_data_to_relations_table(self):
            # preparing and insert data to relations table
            ListCreatorGUI.list_of_friends.append(User.current_logged.nickname)
            for friend in ListCreatorGUI.list_of_friends:
                try:
                    query = f"SELECT userid FROM users WHERE nick = '{friend}'"
                    user_id = DB().get_data_from_db(query)[0][0]

                    query = f"INSERT INTO relations VALUES (NULL, {user_id}, {int(ListCreatorGUI.id_list_of_products)})"
                    DB().execute_query(query)
                except IndexError as e:
                    error = f"{e} \n\n Probably user '{friend}'  doesn't exists in database "
                    InfoBoxGUI().error_box(error)

        def add_list_to_db(self):
            query = f"INSERT INTO lists VALUES (NULL,'{ListCreatorGUI.list_name}', '{User.current_logged.nickname}');"
            DB().execute_query(query)
            query = f"SELECT list_id FROM lists WHERE tittle = '{ListCreatorGUI.list_name}'"
            ListCreatorGUI.id_list_of_products = DB().get_data_from_db(query)[0][0]

        def add_products_to_db(self):
            for item, num, price in zip(ListCreatorGUI.list_of_products, ListCreatorGUI.num_of_product, ListCreatorGUI.price_per_item):
                query = f"INSERT INTO items VALUES (NULL, {int(ListCreatorGUI.id_list_of_products)}, '{item}', {num}, {price})"
                DB().execute_query(query)






