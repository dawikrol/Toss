from tkinter import *

from GUI.InfoBoxGUI import InfoBoxGUI
from Model.DB import DB
from Model.User import User


class CreateNewListGUI:

    list_name = ''
    list_of_products = []
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
            CreateNewListGUI.list_name = self.list_name.get()
            self.root.withdraw()
            CreateNewListGUI.AddProductsGUI().start()

    class AddProductsGUI:

        def __init__(self):
            self.root = Tk()
            self.frame = None
            self.entry_product = None
            self.entry_num_of_products = None
            self.entry_price = None
            self.list_of_products = []

        def __del__(self):
            self.root.destroy()

        def start(self):
            self.root.title('Add products')
            Label(self.root, text="Add products to list:").grid(row=0, column=0, padx=50, pady=10)
            self.init_frame()
            self.init_entry_product()
            self.init_buttons()
            self.init_listbox()
            self.root.mainloop()

        def init_frame(self):
            self.frame = LabelFrame(self.root, padx=10, pady=10)
            self.frame.grid(row=4, column=0, sticky=W+E)

        def init_entry_product(self):
            # TODO: The inscription should disappear after click in the window
            self.entry_product = Entry(self.root, width=35, borderwidth=7)
            self.entry_product.insert(1, 'Add product name')
            self.entry_product.grid(row=2, column=0, sticky=W+E)
            Label(self.frame, text='Number of product:').grid(row=1, column=0, sticky='w', columnspan=1)
            self.entry_num_of_products = Entry(self.frame, width=5, borderwidth=7)
            self.entry_num_of_products.insert(1, '1')
            self.entry_num_of_products.grid(row=1, column=1, sticky='e')
            Label(self.frame, text='Price per product:').grid(row=2, column=0, sticky='w')
            self.entry_price = Entry(self.frame, width=5, borderwidth=7)
            self.entry_price.grid(row=2, column=1, sticky='e')


        def init_buttons(self):
            create_add_products_buttons = Button(self.root, text='Add product', padx=4, pady=4,
                                                 command=self.click_add_products_button)
            create_add_products_buttons.grid(row=5, column=0, sticky=W+E)
            create_next_buttons = Button(self.root, text='Next', padx=15, pady=5,
                                         command=self.click_next_button)
            create_next_buttons.grid(row=7, column=0, sticky=W+E, columnspan=1)

        def init_listbox(self):
            list_of_items = Listbox(self.root)
            list_of_items.config(width=26)
            for item in self.list_of_products:
                list_of_items.insert(self.list_of_products.index(item), item)
            list_of_items.grid(row=6, column=0, columnspan=1, sticky=W+E)

        def click_add_products_button(self):
            self.list_of_products.append(self.entry_product.get())
            self.init_listbox()

        def click_next_button(self):
            CreateNewListGUI.list_of_products = self.list_of_products
            self.root.withdraw()
            CreateNewListGUI.AddFriendsGUI().start()

    class AddFriendsGUI:

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
            if CreateNewListGUI.AddFriendsGUI().check_if_friend_exist_in_database(nick):
                self.list_of_friends.append(nick)
                self.init_listbox()
            else:
                InfoBoxGUI().error_box('User with this nickname does not exist!')

        def check_if_friend_exist_in_database(self, nick):
            nicks = [nick[0] for nick in DB().get_data_from_db(query="SELECT nick from users")]
            if nick in nicks and nick != User.current_logged.nickname:
                return True

        def click_create_list_button(self):
            CreateNewListGUI.list_of_friends = self.list_of_friends
            CreateNewListGUI.AddFriendsGUI().add_data_to_lists_table()
            CreateNewListGUI.AddFriendsGUI().add_data_to_relations_table()
            self.root.withdraw()
            self.root.quit()

        def add_data_to_lists_table(self):
            # preparing data to insert to lists table
            str_of_products = ', '.join(CreateNewListGUI.list_of_products)
            str_of_products = str_of_products[:-2]
            # TODO: a part this functionality has been moved to CreateNewListGUI
            #  insert data to lists table
            query = f"INSERT INTO lists VALUES (NULL,'{CreateNewListGUI.list_name}', '{str_of_products}');"
            DB().execute_query(query)

        def add_data_to_relations_table(self):
            # preparing and insert data to relations table
            CreateNewListGUI.list_of_friends.append(User.current_logged.nickname)
            for friend in CreateNewListGUI.list_of_friends:
                try:
                    query = f"SELECT userid FROM users WHERE nick = '{friend}'"
                    user_id = DB().get_data_from_db(query)[0][0]
                    query = f"SELECT list_id FROM lists WHERE tittle = '{CreateNewListGUI.list_name}'"
                    list_id = DB().get_data_from_db(query)[0][0]
                    query = f"INSERT INTO relations VALUES (NULL, {user_id}, {list_id})"
                    DB().execute_query(query)
                except IndexError as e:
                    error = f"{e} \n\n Probably user '{friend}'  doesn't exists in database "
                    InfoBoxGUI().error_box(error)
        def add_data(self):
            query = f"INSERT INTO lists VALUES (NULL,'{CreateNewListGUI.list_name}', '{User.current_logged.nickname}');"
            DB().execute_query(query)






