from tkinter import Tk, Entry, Label, Button, messagebox,Toplevel #ERROR!

class Login:
    def __init__(self,window):
        self.window = window
        self.window.title('First GUI')
        self.window.geometry('320x150')
        self.window.config(bg = 'lightgreen')
        x = int((self.window.winfo_screenwidth()-320)/2)
        y = int((self.window.winfo_screenheight()-150)/2)
        self.window.geometry(f'+{x}+{y}')
        self.window.resizable(False,False)
        # self.window.iconbitmap('icon1.ico')
        self.window.bind('<Return>',self.Login)
        self.create_widget()

    def create_widget(self):
        self.user_label = Label(window, text = 'User', font = ('arial', 20, 'bold'), bg = 'lightgreen', fg = 'darkgreen')
        self.user_label.grid(row = 0, column = 0)
#..............................................................................................................................
        self.user_entry = Entry(window, font = ('arial', 20, 'bold'), width = 10)
        self.user_entry.grid(row = 0, column = 1)
        self.user_entry.focus_set()
#..............................................................................................................................
        self.user_label = Label(window, text = 'Password', font = ('arial', 20, 'bold'), bg = 'lightgreen', fg = 'darkgreen')
        self.user_label.grid(row = 1, column = 0)
#..............................................................................................................................
        self.user_entry = Entry(window, font = ('arial', 20, 'bold'), width = 10, show = '*')
        self.user_entry.grid(row = 1, column = 1)
#..............................................................................................................................
        self.button_ok = Button(window, text = 'OK', font = ('arial', 20, 'bold'), bg = 'white', fg = 'darkgreen', padx = 15, command = Login)
        self.button_ok.grid(row = 2, column = 1)
#..............................................................................................................................
        self.status_label = Label(window, font = ('arial', 20, 'bold'), bg = 'lightgreen', fg = 'darkgreen')
        self.status_label.grid(row = 2, column = 0)

    def Login(self, event):
        user = self.user_entry.get()
        password = self.user_entry.get()
        if user == 'ali' and password == '123':
            #status_label.config(text = 'OK', bg = 'lightgreen', fg = 'darkgreen')
            messagebox.showinfo('User and password are correct.')
            self.window.withdraw()
            self.create_dashboard()
        else:
            #status_label.config(text = 'Not OK', bg = 'lightgreen', fg = 'darkgreen')     
            messagebox.showerror('user or password are incorrect!')

    def create_dashboard(self):
        dashboard = Toplevel()

if __name__ == '__main__':
    window = Tk()
    loginapp = Login(window)
    window.mainloop()