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

'''from tkinter import ttk
import tkinter as tk

# Creating tkinter window
window = tk.Tk()
window.resizable(width=1, height=1)

# Using treeview widget
treev = ttk.Treeview(window, selectmode='browse')

# Calling pack method w.r.to treeview
treev.pack(side='right')

# Constructing vertical scrollbar
# with treeview
verscrlbar = ttk.Scrollbar(window,
                           orient="vertical",
                           command=treev.yview)

# Calling pack method w.r.to verical
# scrollbar
verscrlbar.pack(side='right', fill='x')

# Configuring treeview
treev.configure(xscrollcommand=verscrlbar.set)

# Defining number of columns
treev["columns"] = ("1", "2", "3")

# Defining heading
treev['show'] = 'headings'

# Assigning the width and anchor to  the
# respective columns
treev.column("1", width=90, anchor='c')
treev.column("2", width=90, anchor='se')
treev.column("3", width=90, anchor='se')

# Assigning the heading names to the
# respective columns
treev.heading("1", text="Name")
treev.heading("2", text="Sex")
treev.heading("3", text="Age")

# Inserting the items and their features to the
# columns built
treev.insert("", 'end', text="L1",
             values=("Nidhi", "F", "25"))
treev.insert("", 'end', text="L2",
             values=("Nisha", "F", "23"))
treev.insert("", 'end', text="L3",
             values=("Preeti", "F", "27"))
treev.insert("", 'end', text="L4",
             values=("Rahul", "M", "20"))
treev.insert("", 'end', text="L5",
             values=("Sonu", "F", "18"))
treev.insert("", 'end', text="L6",
             values=("Rohit", "M", "19"))
treev.insert("", 'end', text="L7",
             values=("Geeta", "F", "25"))
treev.insert("", 'end', text="L8",
             values=("Ankit", "M", "22"))
treev.insert("", 'end', text="L10",
             values=("Mukul", "F", "25"))
treev.insert("", 'end', text="L11",
             values=("Mohit", "M", "16"))
treev.insert("", 'end', text="L12",
             values=("Vivek", "M", "22"))
treev.insert("", 'end', text="L13",
             values=("Suman", "F", "30"))

# Calling mainloop
window.mainloop()'''

import tkinter as tk
import tkinter.ttk as ttk


class Application(tk.Frame):
    def __init__(self, root):
        self.root = root
        self.initialize_user_interface()

    def initialize_user_interface(self):
        # Configure the root object for the Application
        self.root.title("Application")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.config(background="green")

        # Define the different GUI widgets
        self.name_label = tk.Label(self.root, text="Name:")
        self.name_entry = tk.Entry(self.root)
        self.name_label.grid(row=0, column=0, sticky=tk.W)
        self.name_entry.grid(row=0, column=1)

        self.idnumber_label = tk.Label(self.root, text="ID:")
        self.idnumber_entry = tk.Entry(self.root)
        self.idnumber_label.grid(row=1, column=0, sticky=tk.W)
        self.idnumber_entry.grid(row=1, column=1)

        self.submit_button = tk.Button(self.root, text="Insert", command=self.insert_data)
        self.submit_button.grid(row=2, column=1, sticky=tk.W)

        self.delete_button = tk.Button(self.root, text="Delete", command=self.delete_data)
        self.delete_button.grid(row=100, column=100)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.grid(row=0, column=3)

        # Set the treeview
        self.tree = ttk.Treeview(self.root, columns=('Name', 'ID'))

        # Set the heading (Attribute Names)
        self.tree.heading('#0', text='Item')
        self.tree.heading('#1', text='Name')
        self.tree.heading('#2', text='ID')

        # Specify attributes of the columns (We want to stretch it!)
        self.tree.column('#0', stretch=tk.YES)
        self.tree.column('#1', stretch=tk.YES)
        self.tree.column('#2', stretch=tk.YES)

        self.tree.grid(row=4, columnspan=4, sticky='nsew')
        self.treeview = self.tree

        self.id = 0
        self.iid = 0

    def insert_data(self):
        self.treeview.insert('', 'end', iid=self.iid, text="Item_" + str(self.id),
                             values=("Name: " + self.name_entry.get(),
                                     self.idnumber_entry.get()))
        self.iid = self.iid + 1
        self.id = self.id + 1

    def delete_data(self):
        row_id = int(self.tree.focus())
        self.treeview.delete(row_id)


app = Application(tk.Tk())
app.root.mainloop()