from tkinter import *
from PIL import ImageTk
from tkinter import ttk
import mysql.connector

class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Lifechoices-online Login")
        self.root.geometry("1920x1080")
        self.root.resizable(False, False)
        # self.root.config(bg="#fafafa")
        self.mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='Lifechoicesonline', auth_plugin='mysql_native_password')
        self.mycursor = self.mydb.cursor()

        # ======main frame=====
        self.main_frame3 = Frame(self.root, bd=0, relief=RIDGE, bg="white")
        self.main_frame3.place(x=0, y=0, width=1920, height=1080)



        # ====images====
        self.bg_image = ImageTk.PhotoImage(file="images/image.png")
        self.lbl_bg_image = Label(self.main_frame3, image=self.bg_image, bg="#00b0f0", bd=0).place(x=0, y=0)

        self.long_logo_image = ImageTk.PhotoImage(file="images/long_logo.png")
        self.lbl_long_logo_image = Label(self.main_frame3, image=self.long_logo_image, bg="#00b0f0", bd=0).place(x=47, y=40)

        self.filter_frame = Frame(self.root, bd=0, relief=RIDGE, bg="white")
        self.filter_frame.place(x=800, y=80, width=1000, height=90)

        self.treeview_frame = Frame(self.root, bd=0, relief=RIDGE, bg="white")
        self.treeview_frame.place(x=800, y=200, width=1000, height=750)

        self.edit_frame = LabelFrame(self.root, text="Edit Section", bd=0, relief=RIDGE, bg="white")
        self.edit_frame.place(x=100, y=200, width=660, height=750)


root = Tk()
obj = Login_System(root)
root.mainloop()
