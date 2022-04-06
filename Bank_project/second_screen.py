from tkinter import *
from Classes.second_screen import login_fail, login_success


class login_screen():
    def __init__(self, master):
        self.label_name = Label(master, text="Username", fg="black")
        self.label_password = Label(master, text="Password", fg="black")
        self.input_name = Entry(master)
        self.input_password = Entry(master, show="*")

        self.label_name.grid(row=0, column=0, sticky=E)
        self.label_password.grid(row=1, column=0, sticky=E)

        self.input_name.grid(row=0, column=1)
        self.input_password.grid(row=1, column=1)

        self.checkbox = Checkbutton(master, text="Remember me")
        self.checkbox.grid(columnspan=2, sticky=W)

        self.login_button = Button(master, text="Login")
        self.login_button.grid(row=1, column=2)

        self.login_button = Button(master, text="Login", command=self.check_login)
        self.login_button.grid(row=1, column=2)


    def check_login(self):
        username = self.input_name.get()
        password = self.input_password.get()

        if username == "" or password == "":
            second_screen = Toplevel()
            login_fail(second_screen)

        elif username != password:
            second_screen = Toplevel()
            login_fail(second_screen)

        elif username == password:
            second_screen = Toplevel()
            login_success(second_screen)