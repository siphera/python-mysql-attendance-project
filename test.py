'''from tkinter import *
from PIL import Image, ImageTk

# --------------------------------------------------------------------------------------------------------------
# create the window and add size and title to it
window = Tk()
window.geometry("800x500+300+100")
# set size permanently   #or you can use window.resizabld(false, false)
# window.minsize(800, 500)
# window.maxsize(800, 500)
window.title(" RAZ Tech")
# window.iconbitmap("C:\Python\Python Projects\TKINTER/login Sys/lock_v2W_icon.ico")
#
# ---------------------------------------------------------------------------------------------------------------
# first get the picture then save it in pic and set as background
image = Image.open("/home/siphenkosi/Documents/python-projects/lifechoices-online/sunny.jpg")
pic = ImageTk.PhotoImage(image)
# build pic and add it to window
label0 = Label(image=pic)
label0.pack(fill=BOTH, expand='yes')


# -------------------------------------------------------------------------------------------------------------
# functions for the buttons to perform
def login():
    users = {'admin': '1000', 'dev': '2000', 'client': '3000', 'employee': '4000'}
    username = userName.get()
    Pass = password.get()
    if username in users:
        if (users[username] == Pass):
            label4 = Label(window, text=("Welcome " + username), width=25, font=("arial", 40, "bold"))
            label4.place(x=0, y=400)

        else:
            label4 = Label(window, text=("Incorrect Password for " + username), width=25, font=("arial", 40, "bold"))
            label4.place(x=0, y=400)

    else:
        label4 = Label(window, text=(username + " does not exist"), width=25, font=("arial", 40, "bold"))
        label4.place(x=0, y=400)


# ----------------------------------------------------------------------------------------------------------------
# first lable
label1 = Label(window, text=" Login System ", fg="black", font=("new times roman", 40, "bold"))
label1.place(x=200, y=15)

label2 = Label(window, text="User Name :", font=("arial", 16, "bold"))
label2.place(x=110, y=150)

userName = StringVar()
textBox1 = Entry(window, textvar=userName, width=30, font=("arial", 16, "bold"))
textBox1.place(x=290, y=150)

label3 = Label(window, text="Password :", font=("arial", 16, "bold"))
label3.place(x=116, y=250)

password = StringVar()
textBox2 = Entry(window, textvar=password, width=30, font=("arial", 16, "bold"))
textBox2.place(x=290, y=250)

button1 = Button(window, text="   Login   ", fg="black", bg="white", relief="raised", font=("arial", 16, "bold"),
                 command=login)
button1.place(x=335, y=340)

# display window
window.mainloop()'''

from tkinter import *
from tkinter import messagebox
import mysql.connector
import os
import time

#connecting to the database
# db = mysql.connector.connect(host="localhost",user="root",passwd="root",database="techienaman")
# mycur = db.cursor()

def error_destroy():
    err.destroy()

def succ_destroy():
    succ.destroy()
    root1.destroy()

def error():
    global err
    err = Toplevel(root1)
    err.title("Error")
    err.geometry("200x100")
    Label(err,text="All fields are required..",fg="red",font="bold").pack()
    Label(err,text="").pack()
    Button(err,text="Ok",bg="grey",width=8,height=1,command=error_destroy).pack()

def success():
    global succ
    succ = Toplevel(root1)
    succ.title("Success")
    succ.geometry("200x100")
    Label(succ, text="Registration successful...", fg="green", font="bold").pack()
    Label(succ, text="").pack()
    Button(succ, text="Ok", bg="grey", width=8, height=1, command=succ_destroy).pack()

def register_user():
    username_info = username.get()
    password_info = password.get()
    if username_info == "":
        error()
    elif password_info == "":
        error()
    else:
        sql = "insert into login values(%s,%s)"
        t = (username_info, password_info)
        mycur.execute(sql, t)
        db.commit()
        Label(root1, text="").pack()
        time.sleep(0.50)
        success()



def registration():
    global root1
    root1 = Toplevel(root)
    root1.title("Registration Portal")
    root1.geometry("300x250")
    global username
    global password
    Label(root1,text="Register your account",bg="grey",fg="black",font="bold",width=300).pack()
    username = StringVar()
    password = StringVar()
    Label(root1,text="").pack()
    Label(root1,text="Username :",font="bold").pack()
    Entry(root1,textvariable=username).pack()
    Label(root1, text="").pack()
    Label(root1, text="Password :").pack()
    Entry(root1, textvariable=password,show="*").pack()
    Label(root1, text="").pack()
    Button(root1,text="Register",bg="red",command=register_user).pack()

def login():
    global root2
    root2 = Toplevel(root)
    root2.title("Log-In Portal")
    root2.geometry("300x300")
    global username_varify
    global password_varify
    Label(root2, text="Log-In Portal", bg="grey", fg="black", font="bold",width=300).pack()
    username_varify = StringVar()
    password_varify = StringVar()
    Label(root2, text="").pack()
    Label(root2, text="Username :", font="bold").pack()
    Entry(root2, textvariable=username_varify).pack()
    Label(root2, text="").pack()
    Label(root2, text="Password :").pack()
    Entry(root2, textvariable=password_varify, show="*").pack()
    Label(root2, text="").pack()
    Button(root2, text="Log-In", bg="red",command=login_varify).pack()
    Label(root2, text="")

def logg_destroy():
    logg.destroy()
    root2.destroy()

def fail_destroy():
    fail.destroy()

def logged():
    global logg
    logg = Toplevel(root2)
    logg.title("Welcome")
    logg.geometry("200x100")
    Label(logg, text="Welcome {} ".format(username_varify.get()), fg="green", font="bold").pack()
    Label(logg, text="").pack()
    Button(logg, text="Log-Out", bg="grey", width=8, height=1, command=logg_destroy).pack()


def failed():
    global fail
    fail = Toplevel(root2)
    fail.title("Invalid")
    fail.geometry("200x100")
    Label(fail, text="Invalid credentials...", fg="red", font="bold").pack()
    Label(fail, text="").pack()
    Button(fail, text="Ok", bg="grey", width=8, height=1, command=fail_destroy).pack()


def login_varify():
    user_varify = username_varify.get()
    pas_varify = password_varify.get()
    sql = "select * from login where user = %s and password = %s"
    mycur.execute(sql,[(user_varify),(pas_varify)])
    results = mycur.fetchall()
    if results:
        for i in results:
            logged()
            break
    else:
        failed()


def main_screen():
    global root
    root = Tk()
    root.title("Log-IN Portal")
    root.geometry("300x300")
    Label(root,text="Welcome to Log-In Protal",font="bold",bg="grey",fg="black",width=300).pack()
    Label(root,text="").pack()
    Button(root,text="Log-IN",width="8",height="1",bg="red",font="bold",command=login).pack()
    Label(root,text="").pack()
    Button(root, text="Registration",height="1",width="15",bg="red",font="bold",command=registration).pack()
    Label(root,text="").pack()
    Label(root,text="").pack()
    Label(root,text="Developed By Naman Kumar").pack()

main_screen()
root.mainloop()