from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector

class User_login_page:
    def __init__(self, master):
        self.root = master
        self.root.title("Lifechoices-online Login")
        self.root.geometry("1920x1080")
        self.root.resizable(False, False)
        # self.root.config(bg="#fafafa")
        self.mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='Lifechoicesonline', auth_plugin='mysql_native_password')
        self.mycursor = self.mydb.cursor()

        #======main frame=====
        self.main_frame1 = Frame(self.root, bd=0, relief=RIDGE, bg="white")
        self.main_frame1.place(x=0, y=0, width=1920, height=1080)

        # ====images====
        self.bg_image = ImageTk.PhotoImage(file="images/image.png")
        self.lbl_bg_image = Label(self.main_frame1, image=self.bg_image, bg="#00b0f0", bd=0).place(x=0, y=0)

        # =====Login Frame======
        self.login_frame = Frame(self.main_frame1, bd=2, relief=RIDGE, bg="white")
        self.login_frame.place(x=759, y=170, width=400, height=600)

        self.logo_image = ImageTk.PhotoImage(file="images/admin.png")
        self.lbl_logo_image = Label(self.login_frame, image=self.logo_image,bg="white", bd=0).place(x=150, y=20)

        self.lbl_admin_txt = Label(self.login_frame, text="ADMIN", bg="white", fg="lightgrey", font=("times new roman", 14, "bold")).place(x=170, y=117)


        self.lbl_username = Label(self.login_frame, text="Username", font=("Elephant", 15), bg="white", fg="#767171").place(x=50, y=170)
        self.txt_username = Entry(self.login_frame, font=("times new roman", 15), bg="#ECECEC")
        self.txt_username.place(x=50, y=210, width=300)

        self.lbl_pass = Label(self.login_frame, text="Password", font=("Elephant", 15), bg="white", fg="#767171").place(x=50, y=270)
        self.txt_pass = Entry(self.login_frame, font=("times new roman", 15), show="*", bg="#ECECEC")
        self.txt_pass.place(x=50, y=310, width=300)

        self.btn_login = Button(self.login_frame, text="Log in", font=("Arial Rounded MT Bold", 15), bg="#00b0f0", activebackground="#00b0f0", fg="white", activeforeground="white", cursor="hand2", command=self.verify).place(x=50, y=370, width=300, height=35)

        self.hr = Label(self.login_frame, bg="lightgrey").place(x=50, y=460, width=300, height=2)

        self.lbl_or = Label(self.login_frame, text="OR",bg="white", fg="lightgrey", font=("times new roman", 15, "bold")).place(x=180, y=445)

        self.btn_user_login = Button(self.login_frame, text="USER LOGIN", font=("times new roman", 13), bg="white", fg="#00759E", bd=0, activebackground="white", activeforeground="#00759E", command=self.back).place(x=135, y=510)


    def verify(self):
        self.email = self.txt_username.get()
        self.password = self.txt_pass.get()

        self.sql = "select * from users where email = %s and password =%s"
        self.mycursor.execute(self.sql, [self.email, self.password])
        self.results = self.mycursor.fetchall()
        if self.results:
            for i in self.results:
                messagebox.showinfo("SUCCESS", "you have logged in successfully")
                break;
        else:
            messagebox.showerror("FAILED", "Login failed please enter correct username and password")

    def back(self):
        self.root.destroy()
        import login_reg


root = Tk()
obj = User_login_page(root)
root.mainloop()
