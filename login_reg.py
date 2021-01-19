from tkinter import *
from PIL import ImageTk

class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Lifechoices-online Login")
        self.root.geometry("1920x1080")
        self.root.config(bg="#fafafa")

        # ====images=====
        self.phone_image = ImageTk.PhotoImage(file="images/admin.png")
        self.lbl_phone_image = Label(self.root, image=self.phone_image, bd=0).place(x=200, y=90)

        # =====Login Frame======
        self.login_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        self.login_frame.place(x=720, y=90, width=350, height=460)

        self.title = Label(self.login_frame, text="Lifechoices-online", font=("Elephant", 23, "bold"), bg="white").place(x=0, y=30, relwidth=1)

        self.lbl_username = Label(self.login_frame, text="Username", font=("Elephant", 15), bg="white", fg="#767171").place(x=50, y=100)
        self.txt_username = Entry(self.login_frame, font=("times new roman", 15), bg="#ECECEC").place(x=50, y=140, width=250)

        self.lbl_pass = Label(self.login_frame, text="Password", font=("Elephant", 15), bg="white", fg="#767171").place(x=50, y=200)
        self.txt_pass = Entry(self.login_frame, font=("times new roman", 15), show="*", bg="#ECECEC").place(x=50, y=240, width=250)

        self.btn_login = Button(self.login_frame, text="Log in", font=("Arial Rounded MT Bold", 15), bg="#00b0f0", activebackground="#00b0f0", fg="white", activeforeground="white", cursor="hand2").place(x=50, y=300, width=250, height=35)

        self.hr = Label(self.login_frame, bg="lightgrey").place(x=50, y=370, width=250, height=2)

        self.lbl_or = Label(self.login_frame, text="OR",bg="white", fg="lightgrey", font=("times new roman", 15, "bold")).place(x=150, y=355)

        self.btn_forgot = Button(self.login_frame, text="Forgot Password?", font=("times new roman", 13), bg="white", fg="#00759E",bd=0, activebackground="white", activeforeground="#00759E").place(x=100, y=390)

        #=======frame 2=========
        self.register_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        self.register_frame.place(x=720, y=570, width=350, height=60)

        self.lbl_reg = Label(self.register_frame, text="Don't have an account?", font=("time new roman", 13), bg="white").place(x=40, y=20)
        self.btn_signup = Button(self.register_frame, text="Sign up", font=("times new roman", 13), bg="white", fg="#00759E",bd=0, activebackground="white", activeforeground="#00759E").place(x=250, y=17)


root = Tk()
obj = Login_System(root)
root.mainloop()
