from tkinter import *
from PIL import ImageTk
from tkinter import ttk
import mysql.connector

class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Lifechoices-online | Manage | Update | Remove")
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

        # ====filter frame=====
        self.filter_frame = Frame(self.root, bd=0, relief=RIDGE, bg="white")
        self.filter_frame.place(x=800, y=90, width=1000, height=90)

        self.lbl_contact = Label(self.filter_frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=30, y=15)
        self.email_filter = Entry(self.filter_frame, font=("times new roman", 15, "bold"), bg="lightgray")
        self.email_filter.place(x=30, y=45)

        self.lbl_department = Label(self.filter_frame, text="Department", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=270, y=15)
        self.cmb_department = ttk.Combobox(self.filter_frame, font=("times new roman", 13, "bold"), state='readonly', justify=CENTER)
        self.cmb_department['values'] = ("Select", "All", "Lecture", "Academy", "Studio", "Finance")
        self.cmb_department.place(x=270, y=45, height=28)
        self.cmb_department.current(0)

        self.btn_filter = Button(self.filter_frame, text="FILTER RESULTS", font=("times new roman", 13), bg="#00b0f0", activebackground="#00b0f0", fg="white", activeforeground="white", cursor="hand2").place(x=480, y=41)

        self.lbl_count = Label(self.filter_frame, text="Count Results:", font=("times new roman", 25, "bold"), bg="white", fg="grey").place(x=680, y=40)
        self.lbl_show_count = Label(self.filter_frame, text="0", font=("times new roman", 32, "bold"), bg="white", fg="red").place(x=900, y=31)

        # ======>Treeview frame<======
        self.treeview_frame = Frame(self.root, bd=0, relief=RIDGE, bg="white")
        self.treeview_frame.place(x=800, y=200, width=1000, height=750)

        self.style = ttk.Style()
        self.style.configure("Treeview",
                             background="white",
                             foreground="black",
                             rowheight=35,
                             fieldbackground="white"
                             )
        self.style.map('Treeview',
                       background=[('selected', '#00b0f0')])
        self.my_tree = ttk.Treeview(self.treeview_frame)

        # =====>creating columns<======
        self.my_tree['columns'] = ("Name", "Surname", "Email", "Time-IN", "Time-OUT")

        # =====>layering columns<=======
        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("Name", anchor=W, width=200)
        self.my_tree.column("Surname", anchor=W, width=200)
        self.my_tree.column("Email", anchor=W, width=200)
        self.my_tree.column("Time-IN", anchor=CENTER, width=200)
        self.my_tree.column("Time-OUT", anchor=CENTER, width=200)

        # =====>Tree Headings<======
        self.my_tree.heading("#0", text="", anchor=W)
        self.my_tree.heading("Name", text="Name", anchor=W)
        self.my_tree.heading("Surname", text="Surname", anchor=W)
        self.my_tree.heading("Email", text="Email", anchor=W)
        self.my_tree.heading("Time-IN", text="Time-IN", anchor=CENTER)
        self.my_tree.heading("Time-OUT", text="Time-OUT", anchor=CENTER)




        # =====>Striped rows<====
        self.my_tree.tag_configure('oddrow', background="white")
        self.my_tree.tag_configure('evenrow', background="lightblue")

        # =====Insert data=====
        self.count = 0
        self.get_data = self.mycursor.execute('Select * from attendance')
        for record in self.mycursor:
            if self.count % 2 == 0:
                self.my_tree.insert(parent='', index='end', iid=self.count, text="", values=(record[0], record[1], record[2], record[3], record[4]), tags=('evenrow',))
            else:
                self.my_tree.insert(parent='', index='end', iid=self.count, text="", values=(record[0], record[1], record[2], record[3], record[4]), tags=('oddrow',))
            self.count += 1

        self.my_tree.place(x=0, y=0, height=760)

        # ======>Edit Frame<========
        self.edit_frame = Frame(self.root, bd=0, relief=RIDGE, bg="white")
        self.edit_frame.place(x=100, y=200, width=660, height=750)


root = Tk()
obj = Login_System(root)
root.mainloop()
