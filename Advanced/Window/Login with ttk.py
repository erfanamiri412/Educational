from tkinter import Tk, ttk, messagebox

class LoginApp:
    def __init__(self,master):
        self.master = master
        self.master.title('Account')
        self.master.geometry('300x300')

        # Creating label for username:
        self.label_username = ttk.Label(master, text = 'Username')
        self.label_username.pack(pady = 10)

        # Creating entry for username:
        self.entry_username = ttk.Entry(master)
        self.entry_username.pack(pady = 10)

        # Creating label for password:
        self.label_password = ttk.Label(master, text = 'Password')
        self.label_password.pack(pady = 10)

        # Creating entry for password:
        self.entry_password = ttk.Entry(master, show = '*')
        self.entry_password.pack(pady = 10)

        # Creating button for enter:
        self.button_login = ttk.Button(master, text = 'Enter', command = self.login)
        self.button_login.pack(pady = 20)

    def login(self):
        username = self.entry_username.get()
        password  = self.entry_password.get()

        # Default username and password:
        if username == 'ali'and password == '123':
            messagebox.showinfo('','Valid data.')
        else:
            messagebox.showerror('','Invalid data!')

if __name__ == '__main__':
    root = Tk()
    app = LoginApp(root)
    root.mainloop()