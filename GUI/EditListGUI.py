from tkinter import *
from tkinter import ttk

class EditListGUI:

    def __init__(self):
        self.root = Tk()
        self.root.geometry('540x500')
        self.products_tree = None
        self.buttons_frame = None

    def start(self):
        self.init_list_treeview()
        self.init_buttons()

        self.root.mainloop()


    def init_list_treeview(self):

        self.frame_product_tree = LabelFrame(self.root, padx=5)
        self.frame_product_tree.grid(row=0, column=0)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="blue", foreground="black", rowheight=25, filedbackground="blue")
        style.map("Treeview", background=[('selected', 'blue')])

        self.products_tree = ttk.Treeview(self.frame_product_tree, style="Treeview")
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
        self.buttons_frame = LabelFrame(self.root, padx=5)
        self.buttons_frame.grid(row=0, column=1)

        add_item_to_list = Button(self.buttons_frame, text='Add item', padx=12, command=self.click_add_item, width=12)
        add_item_to_list.grid(row=0, column=0)
        delete_item_to_list = Button(self.buttons_frame, text='Delete item', padx=12, command=self.click_delete_item, width=12)
        add_member = Button(self.buttons_frame, text='Add member', padx=12, command=self.click_add_member, width=12)
        delete_member = Button(self.buttons_frame, text='Delete member', padx=12, command=self.click_delete_member, width=12)
        send_list = Button(self.buttons_frame, text='Send list', padx=12, command=self.click_send_list, width=12)
        complete_list = Button(self.buttons_frame, text='Complete a list', padx=12, command=self.click_complete_list, width=12)
        back = Button(self.buttons_frame, text='Back', padx=12, command=self.click_back, width=12)
        add_item_to_list.grid(row=0, column=0)
        delete_item_to_list.grid(row=1, column=0)
        add_member.grid(row=2, column=0)
        delete_member.grid(row=3, column=0)
        send_list.grid(row=4, column=0)
        complete_list.grid(row=5, column=0)
        back.grid(row=6, column=0)

    def click_add_item(self):
        pass

    def click_add_member(self):
        pass

    def click_delete_item(self):
        pass

    def click_delete_member(self):
        pass

    def click_send_list(self):
        pass

    def click_complete_list(self):
        pass

    def click_back(self):
        pass





