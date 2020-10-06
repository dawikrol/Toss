from tkinter import *
from tkinter import ttk

from GUI.CreateNewListGUI import CreateNewListGUI
from GUI.EditListGUI import EditListGUI
from GUI.InfoBoxGUI import InfoBoxGUI
from Model.DB import DB
from Model.User import User


class MainMenuGUI:

    clicked_selected = []
    list_id = ''



    def __init__(self):
        self.root = Tk()
        self.frame1 = None
        self.frame2 = None
        self.add_products_tree = None
        self.counter = 0
        self.clicked = ''
        self.lists = []


    def start(self):
        self.root.title('Main menu')
        Label(self.root).grid(row=0, column=0)
        self.root.geometry('540x500')
        self.get_data_to_drop_down_list()
        self.init_drop_down_list()
        self.init_listbox()
        self.get_data_to_Treeview(self.lists[0])

        self.init_buttons()

        self.root.mainloop()

    def init_drop_down_list(self):
        self.frame1 = LabelFrame(self.root, padx=5)
        self.frame1.grid(row=0, column=0)
        self.get_data_to_drop_down_list()
        clicked = StringVar()
        #clicked.set(self.lists[0])
        drop = OptionMenu(self.frame1, clicked, *self.lists, command=self.get_data_to_Treeview)
        drop.config(width=80)
        drop.grid(row=1, column=0, columnspan=3)
        MainMenuGUI.clicked_selected = clicked.get()

    def get_data_to_drop_down_list(self):
        query = f"SELECT list_id FROM relations WHERE user_id={User.current_logged.user_id}"
        ids_list = DB().get_data_from_db(query)
        for list_id in ids_list:
            query = f"SELECT tittle FROM lists WHERE list_id = {list_id[0]}"
            name_of_list = DB().get_data_from_db(query)[0][0]
            self.lists.append(name_of_list)
        if len(self.lists) > 0:
            pass


    def get_data_to_Treeview(self, clicked):
        self.add_products_tree.delete(*self.add_products_tree.get_children())
        query = f"SELECT list_id FROM lists WHERE tittle='{clicked}' AND owner='{User.current_logged.nickname}'"
        MainMenuGUI.list_id = DB().get_data_from_db(query)[0][0]
        query = f"SELECT item, count_of_item, prise_per_item FROM items WHERE list_id='{MainMenuGUI.list_id}'"
        for list in (DB().get_data_from_db(query)):
            if self.counter % 2 == 0:

                self.add_products_tree.insert(parent='', index='end', iid=self.counter, text='Parent',
                                              values=(list[0], list[1], list[2]), tags=('evenrow',))
            else:
                self.add_products_tree.insert(parent='', index='end', iid=self.counter, text='Parent',
                                              values=(list[0], list[1], list[2]), tags=('oddrow',))
            self.counter += 1
        self.clicked = clicked




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
        from GUI.LoginGUI import LoginGUI
        self.root.destroy()
        LoginGUI().start()


    def click_create_new_list(self):
        self.root.destroy()
        CreateNewListGUI().start()

    def click_my_profile(self):
        pass

    def click_edit_list(self):
        self.root.destroy()
        EditListGUI(self.clicked).start()

    def click_add(self):
        pass

    def click_delete(self):
        title = 'Delete list'
        question = 'Are you sure you want to delete the list?'
        if InfoBoxGUI().askyesno(title, question):
            query = f"DELETE FROM relations WHERE list_id={MainMenuGUI.list_id}"
            DB().execute_query(query)
            # TODO: something is wrong, probably problem is multi deleting 
            query = f"DELETE FROM items WHERE list_id={MainMenuGUI.list_id}"
            DB().execute_query(query)
            query = f"DELETE FROM lists WHERE list_id={MainMenuGUI.list_id}"
            DB().execute_query(query)
            self.root.destroy()
            MainMenuGUI().start()
