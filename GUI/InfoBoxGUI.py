from tkinter import messagebox, Tk


class InfoBoxGUI:

    def __init__(self):
        self.root = Tk()

    def error_box(self, error):
        messagebox.showerror('Application error', error)
        self.root.mainloop()

    def info_box(self, message):
        messagebox.showinfo('Toss', message)
        self.root.mainloop()



