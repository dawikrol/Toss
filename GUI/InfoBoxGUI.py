from tkinter import messagebox, Tk


class InfoBoxGUI:

    def __init__(self):
        self.root = Tk()
        self.root.withdraw()

    def error_box(self, error):
        messagebox.showerror('Toss', f'Application error, {error}')
        self.root.mainloop()

    def info_box(self, message):
        messagebox.showinfo('Toss', f'{message}')
        self.root.quit()
        self.root.mainloop()

    def askyesno(self, title, ask):
        response = messagebox.askyesno(title, ask)
        if response == 1:
            return 1
        else:
            return 0





