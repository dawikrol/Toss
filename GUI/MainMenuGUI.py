from tkinter import *
from tkinter import ttk
import GUI.ListCreatorGUI
from GUI.InfoBoxGUI import InfoBoxGUI
from Model.DB import DB
from Model.User import User
from Functionality.MessageManager import MessageManager


class MainMenuGUI:

    '''MainMenuGIU create GUI and give access to main functionalities as: create new list, edit lists and delete lists.
     The current_list_id contain list_id which is currently selected in drop down menu by user.'''
    # TODO: Future functionality: editing user profile: change password, nick, email etc. 

    current_list_id = ''

    def __init__(self):
        self.root = Tk()
        self.frame1 = None
        self.frame2 = None
        self.products_tree = None
        self.counter = 0

        self.name_of_products = []
        self.number_of_products = []
        self.prices_of_products = []

        self.name_of_selected_list = ''
        self.users_lists = []
        self.id_users_lists = []

        self.cost_of_list = 0
        self.members_of_list = ''
        self.cost_per_member = 0

    def start(self):
        self.root.title('Main menu')
        self.root.geometry('540x345')
        self.init_frames()
        self.get_data_to_drop_down_menu()
        if len(self.users_lists) > 0:  # check if the user has any lists to display
            self.init_drop_down_menu()
            self.init_product_treeview()
            self.get_data_to_Treeview(self.users_lists[0])
        else:
            self.init_product_treeview()
        self.init_buttons()
        self.root.mainloop()

    def init_frames(self):
        '''Creates frames that help position GUI elements.
        The frame1 exist in row=0 and contain first object e.g. dropdown menu or entry.
        The frame2 exist in row=2 and contain buttons.
        Between frames in row=1 tree view is located.'''

        self.frame1 = LabelFrame(self.root, padx=3)
        self.frame1.grid(row=0, column=0)
        self.frame2 = LabelFrame(self.root, padx=3)
        self.frame2.grid(row=2, column=0)

    def get_data_to_drop_down_menu(self):
        query = f"SELECT list_id FROM relations WHERE user_id={User.current_logged.user_id}"
        ids_list = DB().get_data_from_db(query)
        for list_id in ids_list:
            query = f"SELECT tittle FROM lists WHERE list_id = {list_id[0]}"
            name_of_list = DB().get_data_from_db(query)[0][0]
            self.users_lists.append(name_of_list)
            self.id_users_lists.append(list_id[0])

    def init_drop_down_menu(self):
        '''Creates drop down menu contain users lists.
        When the user select a list get_data_to_treeview fills the products treeview with the appropriate data.'''
        selected_list = StringVar()
        selected_list.set(self.users_lists[0])
        drop_down_menu = OptionMenu(self.frame1, selected_list, *self.users_lists, command=self.get_data_to_Treeview)
        drop_down_menu.config(width=80)
        drop_down_menu.grid(row=0, column=0)

    def get_data_with_database(self, name_of_selected_list_):
        '''Get data about the selected list and assign them to the appropriate variables.'''
        index = self.users_lists.index(name_of_selected_list_)
        MainMenuGUI.current_list_id = self.id_users_lists[index]
        self.current_list_id = self.id_users_lists[index]
        query = f"SELECT item, count_of_item, prise_per_item FROM items WHERE list_id='{MainMenuGUI.current_list_id}'"
        the_list = DB().get_data_from_db(query)
        self.name_of_products = []
        self.number_of_products = []
        self.prices_of_products = []
        for item in the_list:
            self.name_of_products.append(item[0])
            self.number_of_products.append(item[1])
            self.prices_of_products.append(item[2])

    def get_data_to_Treeview(self, name_of_selected_list_=None):
        if name_of_selected_list_ is not None:  # class is inherited and name_of_selected_list is not always passed on
            self.get_data_with_database(name_of_selected_list_)
        self.products_tree.delete(*self.products_tree.get_children())
        for name, number, price in zip(self.name_of_products, self.number_of_products, self.prices_of_products):
            if self.counter % 2 == 0:

                self.products_tree.insert(parent='', index='end', iid=self.counter, text='Parent',
                                              values=(name, number, price), tags=('evenrow',))
            else:
                self.products_tree.insert(parent='', index='end', iid=self.counter, text='Parent',
                                              values=(name, number, price), tags=('oddrow',))
            self.counter += 1
        self.name_of_selected_list = name_of_selected_list_

    def init_product_treeview(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="blue", foreground="black", rowheight=25, filedbackground="blue")
        style.map("Treeview", background=[('selected', 'blue')])

        self.products_tree = ttk.Treeview(self.root, style="Treeview")
        self.products_tree['columns'] = ("Product", "Number", "Price")

        self.products_tree.column("#0", width=0, stretch=NO)
        self.products_tree.column('Product', anchor=W, width=100)
        self.products_tree.column('Number', anchor=E, width=50)
        self.products_tree.column('Price', anchor=E, width=50)

        self.products_tree.heading("#0", text="", anchor=W)
        self.products_tree.heading("Product", text="Product", anchor=W)
        self.products_tree.heading("Number", text="Number", anchor=W)
        self.products_tree.heading("Price", text="Price per item", anchor=W)
        self.products_tree.grid(row=1, column=0, columnspan=1, sticky=W + E)

        self.products_tree.tag_configure('oddrow', background='white')
        self.products_tree.tag_configure('evenrow', background='lightblue')

    def init_buttons(self):
        delete_list = Button(self.frame2, text='Delete list', padx=12, command=self.click_delete, width=12)
        delete_list.grid(row=0, column=2)
        edit_list = Button(self.frame2, text='Edit list', padx=14, command=self.click_edit_list, width=11)
        edit_list.grid(row=0, column=1)
        create_new_list = Button(self.frame2, text='Create new list', padx=2, command=self.click_create_new_list, width=12)
        create_new_list.grid(row=0, column=0, sticky='W')
        send_list = Button(self.frame2, text='  Send list ', padx=8, command=self.click_send_list, width=11)
        send_list.grid(row=0, column=3)
        log_out = Button(self.frame2, text='   Log out   ', padx=10, command=self.click_log_out, width=10)
        log_out.grid(row=0, column=4)

    def click_log_out(self):
        from GUI.LoginGUI import LoginGUI
        self.root.destroy()
        LoginGUI().start()

    def click_create_new_list(self):
        self.root.destroy()
        GUI.ListCreatorGUI().start()

    def click_send_list(self):
        self.get_cost_of_list()
        self.get_members_of_list()
        self.get_cost_per_member()
        MessageManager(self.current_list_id, self.name_of_selected_list, self.name_of_products,
                                     self.number_of_products, self.prices_of_products, self.cost_of_list,
                                     self.members_of_list, self.cost_per_member)

    def click_edit_list(self):
        self.root.destroy()
        GUI.EditListGUI(self.name_of_selected_list, self.users_lists, self.id_users_lists).start()

    def click_delete(self):
        # TODO: Depending on the service, maybe only the owner should be able to delete the list?
        title = 'Delete list'
        question = 'Are you sure you want to delete the list?'
        if InfoBoxGUI().askyesno(title, question):
            query = f"DELETE FROM relations WHERE list_id={MainMenuGUI.current_list_id}"
            DB().execute_query(query)
            query = f"DELETE FROM items WHERE list_id={MainMenuGUI.current_list_id}"
            DB().execute_query(query)
            query = f"DELETE FROM lists WHERE list_id={MainMenuGUI.current_list_id}"
            DB().execute_query(query)
            self.root.destroy()
            MainMenuGUI().start()

    def get_cost_of_list(self):
        self.cost_of_list = 0
        for num, price in zip(self.number_of_products, self.prices_of_products):
            self.cost_of_list += num * price

    def get_members_of_list(self):
        query = f"SELECT user_id FROM relations WHERE list_id={self.current_list_id}"
        self.members_of_list = DB().get_data_from_db(query)

    def get_cost_per_member(self):
        self.cost_per_member = round(self.cost_of_list / len(self.members_of_list), 2)



