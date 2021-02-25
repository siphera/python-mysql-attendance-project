from tkinter import *
from PIL import ImageTk
from tkinter import ttk
import mysql.connector
from duplicity.dup_time import curtime


class Update_page:
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

        self.lbl_or = Label(self.filter_frame, text="OR", bg="white", fg="lightgrey", font=("times new roman", 12, "bold")).place(x=240, y=49)

        self.lbl_department = Label(self.filter_frame, text="Department", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=270, y=15)
        self.cmb_department = ttk.Combobox(self.filter_frame, font=("times new roman", 13, "bold"), state='readonly', justify=CENTER)
        self.cmb_department['values'] = ("Select", "All", "Lecture", "Academy", "Studio", "Finance")
        self.cmb_department.place(x=270, y=45, height=28)
        self.cmb_department.current(0)

        self.btn_filter = Button(self.filter_frame, text="FILTER RESULTS", font=("times new roman", 13), bg="#00b0f0", activebackground="#00b0f0", fg="white", activeforeground="white", cursor="hand2", command=self.filter).place(x=480, y=41)

        self.lbl_count = Label(self.filter_frame, text="Count Results:", font=("times new roman", 25, "bold"), bg="white", fg="grey").place(x=680, y=40)
        self.lbl_show_count = Label(self.filter_frame, text="0", font=("times new roman", 32, "bold"), bg="white", fg="red")
        self.lbl_show_count.place(x=900, y=31)

        # show counter
        self.mycursor.execute('Select COUNT(*) from attendance  where signout IS NULL;')
        for c in self.mycursor:
            self.lbl_show_count.config(text=c)

        # ======>Treeview frame<======_________________________________________________________________________________________________
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
        self.my_tree['columns'] = ("Name", "Surname", "Email", "Department", "Time-IN", "Time-OUT")

        # =====>layering columns<=======
        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("Name", anchor=W, width=150)
        self.my_tree.column("Surname", anchor=W, width=150)
        self.my_tree.column("Email", anchor=W, width=250)
        self.my_tree.column("Department", anchor=W, width=130)
        self.my_tree.column("Time-IN", anchor=CENTER, width=160)
        self.my_tree.column("Time-OUT", anchor=CENTER, width=160)

        # =====>Tree Headings<======
        self.my_tree.heading("#0", text="", anchor=W)
        self.my_tree.heading("Name", text="Name", anchor=W)
        self.my_tree.heading("Surname", text="Surname", anchor=W)
        self.my_tree.heading("Email", text="Email", anchor=W)
        self.my_tree.heading("Department", text="Department", anchor=W)
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
                self.my_tree.insert(parent='', index='end', iid=self.count, text="", values=(record[1], record[2], record[3], record[4], record[5], record[6]), tags=('evenrow',))
            else:
                self.my_tree.insert(parent='', index='end', iid=self.count, text="", values=(record[1], record[2], record[3], record[4], record[5], record[6]), tags=('oddrow',))
            self.count += 1

        self.my_tree.place(x=0, y=0, height=760)
        # >>>>>_____________________________________________________________________________________________________________________________<<<<

        # ======>Edit Frame<========__________________________________________________________________
        self.edit_frame = Frame(self.root, bd=0, relief=RIDGE, bg="white")
        self.edit_frame.place(x=100, y=200, width=660, height=750)

        self.lbl_edit_fname = Label(self.edit_frame, text="Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=100)
        self.txt_edit_fname = Entry(self.edit_frame, font=("times new roman", 15, "bold"), bg="lightgray")
        self.txt_edit_fname.place(x=50, y=130, width=250)

        self.lbl_edit_sname = Label(self.edit_frame, text="Surname", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=380, y=100)
        self.txt_edit_sname = Entry(self.edit_frame, font=("times new roman", 15, "bold"), bg="lightgray")
        self.txt_edit_sname.place(x=350, y=130, width=250)

        self.lbl_edit_email = Label(self.edit_frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=220)
        self.txt_edit_email = Entry(self.edit_frame, font=("times new roman", 15, "bold"), bg="lightgray")
        self.txt_edit_email.place(x=50, y=250, width=250)

        self.lbl_edit_department = Label(self.edit_frame, text="Department", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=380, y=220)
        self.txt_edit_department = Entry(self.edit_frame, font=("times new roman", 15, "bold"), bg="lightgray")
        self.txt_edit_department.place(x=350, y=250, width=250)

        self.lbl_edit_signin = Label(self.edit_frame, text="Sign-in Time", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=330)
        self.txt_edit_signin = Entry(self.edit_frame, font=("times new roman", 15, "bold"), bg="lightgray")
        self.txt_edit_signin.place(x=50, y=360, width=250)

        self.lbl_edit_signout = Label(self.edit_frame, text="Sign-out Time", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=380, y=330)
        self.txt_edit_signout = Entry(self.edit_frame, font=("times new roman", 15, "bold"), bg="lightgray")
        self.txt_edit_signout.place(x=350, y=360, width=250)

        self.btn_edit_signin = Button(self.edit_frame, text="UPDATE SIGN-IN", font=("times new roman", 13), bg="#5C9158", activebackground="#5C9158", fg="white", activeforeground="white", cursor="hand2", command=self.signin)
        self.btn_edit_signin.place(x=50, y=420)
        self.btn_edit_signout = Button(self.edit_frame, text="UPDATE SIGN-OUT", font=("times new roman", 13), bg="#F44B49", activebackground="#F44B49", fg="white", activeforeground="white", cursor="hand2", command=self.signout)
        self.btn_edit_signout.place(x=350, y=420)
        # >>>_______________________________________edit frame__________________________________________________________________________________<<<<<<

        # bind left mouse click to display the records on the side entries
        self.my_tree.bind("<ButtonRelease-1>", self.clicker)

    def insert_records(self):
        for record in self.mycursor:
            if self.count % 2 == 0:
                self.my_tree.insert(parent='', index='end', iid=self.count, text="",
                                    values=(record[1], record[2], record[3], record[4], record[5], record[6]), tags=('evenrow',))
            else:
                self.my_tree.insert(parent='', index='end', iid=self.count, text="",
                                    values=(record[1], record[2], record[3], record[4], record[5], record[6]), tags=('oddrow',))
            self.count += 1

    def filter(self):

        self.my_tree.delete(*self.my_tree.get_children())
        # print(self.cmb_department.get())
        # if self.email_filter
        if len(self.email_filter.get()) > 0:
            self.get_data = self.mycursor.execute('Select * from attendance where email="%s"' % self.email_filter.get())
            self.insert_records()
        elif len(self.email_filter.get()) == 0:
            self.get_data = self.mycursor.execute('Select * from attendance where department="%s"' % self.cmb_department.get())
            self.insert_records()

    def select(self):
        # clear entries
        self.txt_edit_fname.delete(0, END)
        self.txt_edit_sname.delete(0, END)
        self.txt_edit_email.delete(0, END)
        self.txt_edit_department.delete(0, END)
        self.txt_edit_signout.delete(0, END)
        self.txt_edit_signin.delete(0, END)

        self.selected = self.my_tree.focus()        # grab record number
        self.values = self.my_tree.item(self.selected, 'values')        # grab record values

        # output to entry boxes
        self.txt_edit_fname.insert(0, self.values[0])
        self.txt_edit_sname.insert(0, self.values[1])
        self.txt_edit_email.insert(0, self.values[2])
        self.txt_edit_department.insert(0, self.values[3])
        self.txt_edit_signout.insert(0, self.values[5])
        self.txt_edit_signin.insert(0, self.values[4])

    def clicker(self, e):
        self.select()

    def signin(self):
        # get values form entries
        self.fname = str(self.txt_edit_fname.get())
        self.sname = str(self.txt_edit_sname.get())
        self.edit_email = str(self.txt_edit_email.get())
        self.edit_department = str(self.txt_edit_department.get())

        # self.signin_query = "insert into attendance (id, name, surname, email, department, signin) values (%s, %s, %s, %s, %s, %s)"
        # self.val = (self.fname, self.sname, self.edit_email, self.edit_department)
        # self.mycursor.execute(self.signin_query, self.val)
        # self.time = curtime()
        self.mycursor.execute('insert into attendance (name, surname, email, department, signin) values (%s,%s,%s,%s,%s)', (self.fname, self.sname, self.edit_email, self.edit_department, curtime))
        self.mydb.commit()

    def signout(self):
        self.mycursor.execute('update attendance set signout=curtime() where email="%s" order by id desc limit 1' % self.txt_edit_email.get())
        self.mydb.commit()


root = Tk()
obj = Update_page(root)
root.mainloop()
