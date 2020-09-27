# def init_entry_friends(self):
#     # creating labels
#     label1 = Label(self.frame3, text='Add your friends:', width=37)
#     label1.grid(row=0, column=0, sticky='w')
#     label2 = Label(self.frame3, text='List of the friends', width=37)
#     label2.grid(row=0, column=1, sticky='e')
#     # creating entry boxes
#     self.entry_product = Entry(self.frame3, width=37)
#     self.entry_product.grid(row=1, column=0)
#     # creating listbox
#     list_of_friends = Listbox(self.frame3)
#     list_of_friends.grid(row=1, column=1, sticky=W + E)
#     list_of_friends.config(width=37)



# from tkinter import *
# from tkinter import ttk
#
# root = Tk()
# style = ttk.Style()
# style.theme_use("clam")
# style.configure("Treeview", background="blue", foreground="black", rowheight=25, filedbackground="blue")
# style.map("Treeview", background=[('selected', 'blue')])
#
# add_products_tree = ttk.Treeview(root)
# add_products_tree['columns'] = ("Product", "Number", "Price")
#
# add_products_tree.column("#0", width=0, stretch=NO)
# add_products_tree.column('Product', anchor=W, width=100)
# add_products_tree.column('Number', anchor=E, width=50)
# add_products_tree.column('Price', anchor=E, width=50)
#
# add_products_tree.heading("#0", text="", anchor=W)
# add_products_tree.heading("Product", text="Product", anchor=W)
# add_products_tree.heading("Number", text="Number", anchor=W)
# add_products_tree.heading("Price", text="Price per item", anchor=W)
# add_products_tree.grid(row=0, column=0, columnspan=1, sticky=W+E)
# add_products_tree.insert(parent='', index='end', iid=0, text='Parent', values=('1', '2', '2'))
# root.mainloop()
from tkinter import Tk, StringVar, OptionMenu


class No:
    def __init__(self):
        self.root = Tk()

    def start(self):

        clicked = StringVar()
        clicked.set('Tak')
        drop = OptionMenu(self.root, clicked, "ta", "da", "ba")
        drop.pack()
        self.root.mainloop()

No().start()

