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

import tkinter as Tkinter
tk = Tkinter.Tk()
frame1 = Tkinter.Frame(tk, height = 100, width = 100, bg = "WHITE", borderwidth=2)
frame2 = Tkinter.Frame(frame1, height = 100, width = 100, bg = "RED", borderwidth=2)
frame1.pack()
frame2.pack()
label = Tkinter.Label(frame2, text = "Label") #Receive a callback from button here
label.pack()
button = Tkinter.Button(frame1,text="Button") #Send some action to Label here
button.pack()
tk.mainloop()
'''
CREATE TABLE `users` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`name` varchar(60) NOT NULL,
`surname` varchar(60) NOT NULL,
`contact` varchar(60) NOT NULL,
`email` varchar(60) NOT NULL,
`department` varchar(60) NOT NULL,
`password` varchar(60) NOT NULL,
PRIMARY KEY (`email`));
'''