from tkinter import*
import tkinter.messagebox
from tkinter import ttk
from PIL import ImageTk
import random
import time
import datetime

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

#import main_page_support
import os.path


def main():
    root = Tk()
    app = Window1(root)

class Window1:
    def __init__(self, master):
        self.master = master
        self.master.title("Restaurant Login System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg = 'powder blue')
        self.frame = Frame(self.master, bg = 'powder blue')
        self.frame.pack()
        
        #====================ALL Image==============================
        #self.comp_logo =PhotoImage(file="image/yotta_logo.png")
        self.bg_img = PhotoImage(file="image/bg_img2.png")

        labbg=Label(master ,image=self.bg_img).pack()

        #======================================================        
        



        self.Username = StringVar()
        self.Password = StringVar()
        self.Branch = StringVar()

        self.lblTitle = Label(self.frame, text = 'Reconciliation Login System', font=('arial',50,'bold'), bg='powder blue',fg='black')
        self.lblTitle.grid(row =0, column= 0, columnspan=2,pady =40)

        #======================================================
        self.LoginFrame1= LabelFrame(self.frame , width=1350,height=1100,font=('arial',20,'bold'),relief='ridge',bg='cadet blue',bd=20)
        self.LoginFrame1.grid(row=1,column=0)

        self.LoginFrame2= LabelFrame(self.frame , width=1000,height=700,font=('arial',20,'bold'),relief='ridge',bg='cadet blue',bd=20)
        self.LoginFrame2.grid(row=2,column=0)

        #===========================Label and Entry===================
        self.lblUsername=Label(self.LoginFrame1, text = 'Username',font=('arial',20,'bold'),bd =22,bg ='cadet blue',fg ='Cornsilk')
        self.lblUsername.grid(row=0, column=0)
        self.txtUsername=Entry(self.LoginFrame1,font=('arial',20,'bold'),textvariable= self.Username)
        self.txtUsername.grid(row=0, column=1)

        self.lblPassword=Label(self.LoginFrame1, text = 'Password',font=('arial',20,'bold'),bg ='cadet blue',fg ='Cornsilk')
        self.lblPassword.grid(row=1, column=0)
        self.txtPassword=Entry(self.LoginFrame1,font=('arial',20,'bold'),show='*', textvariable= self.Password)
        self.txtPassword.grid(row=1, column=1)

        self.lblBranch=Label(self.LoginFrame1, text = 'Branch',font=('arial',20,'bold'),bg ='cadet blue',fg ='Cornsilk')
        self.lblBranch.grid(row=3, column=0)
        self.txtBranch=Entry(self.LoginFrame1,font=('arial',20,'bold'), textvariable= self.Branch)
        self.txtBranch.grid(row=3, column=1)
        
        
        #============================Buttons==========================

        self.btnLogin = Button(self.LoginFrame2, text = 'Login',width = 17,font=('arial',15,'bold'), command =self.Login_System)
        self.btnLogin.grid(row=3,column =0, pady = 20, padx =8)

        self.btnReset = Button(self.LoginFrame2, text = 'Reset',width = 17,font=('arial',15,'bold'), command =self.Rest)
        self.btnReset.grid(row=3,column =1, pady = 20, padx =8)

        self.btnExit = Button(self.LoginFrame2, text = 'Exit',width = 17,font=('arial',15,'bold'), command =self.iExit)
        self.btnExit.grid(row=3,column =2, pady = 20, padx =8)

        



    def Login_System(self):
        user = (self.Username.get())
        pas = (self.Password.get())
        bran = (self.Branch.get())
        
        if (user ==str("Admin") and pas ==str("Admin") and bran == "bank123"):
            self.newWindow = Toplevel(self.master)
            self.app = Window2(self.newWindow)
        else:
            tkinter.messagebox.askyesno("Login Systems","Too Bad, invalid login detail")
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()

    def Rest(self):
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()
        
    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Login System","Confirm If you want to exit")
        if self.iExit > 0:
            self.master.destroy()
        else:
            command = self.new_window
            return
            




    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)

class Window2:
    def __init__(self, master):

        self.master = master
        self.master.title("ATM Management System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg = 'cadet blue')
        self.frame = Frame(self.master, bg = 'powder blue')
        self.frame.pack()
        

        #top.geometry("1038x773+315+133")
        #top.title("Main Page")
        #top.configure(background="#d9d9d9")
        #top.configure(highlightbackground="#6ed8d8")
        #top.configure(highlightcolor="black")
'''
        self.menubar = tk.Menu(master,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        master.configure(menu = self.menubar)

        self.sub_menu = tk.Menu(master,tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu,
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                #command=main_page_support.{},
                font="TkMenuFont",
                foreground="#000000",
                label="Report")
        self.sub_menu.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                #command=main_page_support.{},
                font="TkMenuFont",
                foreground="#000000",
                label="GL")
        self.sub_menu.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                #command=main_page_support.{},
                font="TkMenuFont",
                foreground="#000000",
                label="eJ")
        self.sub_menu.add_separator(
                background="#d9d9d9")
        self.sub_menu.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                #command=main_page_support.{},
                font="TkMenuFont",
                foreground="#000000",
                label="eJFinTxn")
        self.sub_menu.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                #command=main_page_support.{},
                font="TkMenuFont",
                foreground="#000000",
                label="eJNotInGL")
        self.sub_menu.add_separator(
                background="#d9d9d9")
        self.sub_menu.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                #command=main_page_support.{},
                font="TkMenuFont",
                foreground="#000000",
                label="NotInHost")
        self.sub_menu.add_separator(
                background="#d9d9d9")
        self.sub_menu.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                #command=main_page_support.{},
                font="TkMenuFont",
                foreground="#000000",
                label="OTHonUSGLTxn")
        self.sub_menu.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                #command=main_page_support.{},
                font="TkMenuFont",
                foreground="#000000",
                label="USonUSGLTxn")
        self.sub_menu1 = tk.Menu(master,tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu1,
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                #command=main_page_support.{},
                font="TkMenuFont",
                foreground="#000000",
                label="Help")
        self.sub_menu1.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                #command=main_page_support.{},
                font="TkMenuFont",
                foreground="#000000",
                label="Guide")
        self.sub_menu1.add_separator(
                background="#d9d9d9")
        self.sub_menu1.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                #command=main_page_support.{},
                font="TkMenuFont",
                foreground="#000000",
                label="About us")

'''

if __name__ == '__main__':

    main()
