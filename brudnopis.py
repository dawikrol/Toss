def init_entry_friends(self):
    # creating labels
    label1 = Label(self.frame3, text='Add your friends:', width=37)
    label1.grid(row=0, column=0, sticky='w')
    label2 = Label(self.frame3, text='List of the friends', width=37)
    label2.grid(row=0, column=1, sticky='e')
    # creating entry boxes
    self.entry_product = Entry(self.frame3, width=37)
    self.entry_product.grid(row=1, column=0)
    # creating listbox
    list_of_friends = Listbox(self.frame3)
    list_of_friends.grid(row=1, column=1, sticky=W + E)
    list_of_friends.config(width=37)
