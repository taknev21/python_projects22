from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime

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



def main():
    root = Tk()
    app = Window1(root)
    app2 = Window2(root)

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    master = Window1 (root)
    #loginpage_support.init(root, master)
    root.mainloop()
w = None

def create_Login(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    master = Login (w)
    #loginpage_support.init(w, top, *args, **kwargs)
    return (w, master)

def destroy_Login():
    global w
    w.destroy()
    w = None

def new():
    global newroot
    root.withdraw()
    newroot=first(root) 

class Window1:
    def __init__(self, master):
        self.master = master
        self.master.title("Restaurant Login System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg = 'powder blue')
        self.frame = Frame(self.master, bg = 'powder blue')
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.lblTitle = Label(self.frame, text = 'Restaurant Login System', font=('arial',50,'bold'), bg='powder blue',fg='black')
        self.lblTitle.grid(row =0, column= 0, columnspan=2,pady =40)

        #======================================================

        self.LoginFrame1= LabelFrame(self.frame , width=1350,height=750,font=('arial',20,'bold'),relief='ridge',bg='cadet blue',bd=20)
        self.LoginFrame1.grid(row=1,column=0)

        self.LoginFrame2= LabelFrame(self.frame , width=1000,height=750,font=('arial',20,'bold'),relief='ridge',bg='cadet blue',bd=20)
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
        
        
        #============================Buttons==========================

        self.btnLogin = Button(self.LoginFrame2, text = 'Login',width = 17,font=('arial',15,'bold'), command =self.Login_System)
        self.btnLogin.grid(row=3,column =0, pady = 20, padx =8)

        self.btnReset = Button(self.LoginFrame2, text = 'Reset',width = 17,font=('arial',15,'bold'), command =self.Rest)
        self.btnReset.grid(row=3,column =1, pady = 20, padx =8)

        self.btnExit = Button(self.LoginFrame2, text = 'Exit',width = 17,font=('arial',15,'bold'), command =self.iExit)
        self.btnExit.grid(row=3,column =2, pady = 20, padx =8)

        #============================Buttons==========================

    def Login_System(self):
        u = (self.Username.get())
        p = (self.Password.get())
        if (u ==str(12345) and p ==str(12345)):
            root.withdraw()
            self.newWindow = Toplevel(self.master)
            self.app2 = Window2(self.newWindow)
            #root.after(500,new)
            
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
        self.newWindow = Toplevel(self.master1)
        self.app2 = Window2(self.newWindow)

class Window2:
    def __init__(self, master1):
        self.master1 = master1
        self.master1.title("Restaurant Management System")
        self.master1.geometry('1350x750+0+0')
        self.master1.config(bg = 'cadet blue')
        self.frame1 = Frame(self.master1, bg = 'powder blue')
        self.frame1.pack()

if __name__ == '__main__':

    vp_start_gui()
