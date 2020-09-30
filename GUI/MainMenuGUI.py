from tkinter import *
from tkinter import ttk

from GUI.CreateNewListGUI import CreateNewListGUI
from Model.DB import DB
from Model.User import User


class MainMenuGUI:
    # TODO: OptionMenu doesn't display selected option, OptionMenu must get the selected item, add data to treeview dosen't work

    lists = [1, 2,3]
    clicked_selected = []


    def __init__(self):
        self.root = Tk()
        self.frame1 = None
        self.frame2 =None
        self.add_products_tree = None


    def start(self):
        self.root.title('Main page')
        Label(self.root).grid(row=0, column=0)
        self.root.geometry('540x500')
        self.init_drop_down_list()
        self.init_listbox()
        self.init_buttons()

        self.root.mainloop()

    def init_drop_down_list(self):
        self.frame1 = LabelFrame(self.root, padx=5)
        self.frame1.grid(row=0, column=0)

        self.get_data_to_drop_down_list()
        clicked = StringVar()
        clicked.set(MainMenuGUI.lists[0])
        drop = OptionMenu(self.frame1, clicked, *MainMenuGUI.lists)
        drop.config(width=80)
        drop.grid(row=1, column=0, columnspan=3)
        MainMenuGUI.clicked_selected = clicked.get()
        print(MainMenuGUI.clicked_selected)
        self.get_data_to_drop_down_list()

    def get_data_to_drop_down_list(self):
        query = f"SELECT list_id FROM relations WHERE user_id='Login'"
        ids_list = DB().get_data_from_db(query)
        for list_id in ids_list:
            query = f"SELECT tittle FROM lists WHERE list_id = {list_id[0]}"
            name_of_list = DB().get_data_from_db(query)[0][0]
            MainMenuGUI.lists.append(name_of_list)

    def add_data_to_Treeview(self):
        pass
        query = f"SELECT FROM lists WHERE tittle='{MainMenuGUI.clicked_selected}' AND owner='{User.current_logged.nickname}'"
        print(DB().get_data_from_db(query)[0][0])


    def init_listbox(self):
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
        self.add_products_tree.grid(row=1, column=0, columnspan=1, sticky=W + E)

        self.add_products_tree.tag_configure('oddrow', background='white')
        self.add_products_tree.tag_configure('evenrow', background='lightblue')

    def init_buttons(self):
        self.frame2 = LabelFrame(self.root, padx=5)
        self.frame2.grid(row=2, column=0)
        delete_list = Button(self.frame2, text='Delete list', padx=12, command=self.click_delete, width=12)
        delete_list.grid(row=0, column=2)
        edit_list = Button(self.frame2, text='Edit list', padx=14, command=self.click_edit_list, width=11)
        edit_list.grid(row=0, column=1)
        create_new_list = Button(self.frame2, text='Create new list', padx=2, command=self.click_create_new_list, width=12)
        create_new_list.grid(row=0, column=0, sticky='W')
        my_profile = Button(self.frame2, text='  My profile ', padx=8, command=self.click_my_profile, width=11)
        my_profile.grid(row=0, column=3)
        log_out = Button(self.frame2, text='   Log out   ', padx=10, command=self.click_log_out, width=10)
        log_out.grid(row=0, column=4)

    def click_log_out(self):
        self.root.withdraw()
        self.root.quit()

    def click_create_new_list(self):
        CreateNewListGUI().start()

    def click_my_profile(self):
        pass

    def click_edit_list(self):
        EditListGUI().start()

    def click_add(self):
        pass

    def click_delete(self):
        pass

