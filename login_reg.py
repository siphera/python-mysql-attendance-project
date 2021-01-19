from tkinter import *
from PIL import ImageTk

class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Lifechoices-online Login")
        self.root.geometry("1920x1080")
        self.root.config(bg="#fafafa")

        # ====images====
        self.phone_image = ImageTk.PhotoImage(file="images/image.png")
        self.lbl_phone_image = Label(self.root, image=self.phone_image, bg="#00b0f0", bd=0).place(x=0, y=0)

        # =====Login Frame======
        self.login_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        self.login_frame.place(x=750, y=170, width=400, height=600)

        # self.title = Label(self.login_frame, text="Lifechoices-online", font=("Elephant", 23, "bold"), bg="white").place(x=0, y=30, relwidth=1)
        self.logo_image = ImageTk.PhotoImage(file="images/logo1.png")
        self.lbl_logo_image = Label(self.login_frame, image=self.logo_image, bg="black", bd=0).place(x=115, y=40)

        self.lbl_username = Label(self.login_frame, text="Username", font=("Elephant", 15), bg="white", fg="#767171").place(x=50, y=170)
        self.txt_username = Entry(self.login_frame, font=("times new roman", 15), bg="#ECECEC").place(x=50, y=210, width=300)

        self.lbl_pass = Label(self.login_frame, text="Password", font=("Elephant", 15), bg="white", fg="#767171").place(x=50, y=270)
        self.txt_pass = Entry(self.login_frame, font=("times new roman", 15), show="*", bg="#ECECEC").place(x=50, y=310, width=300)

        self.btn_login = Button(self.login_frame, text="Log in", font=("Arial Rounded MT Bold", 15), bg="#00b0f0", activebackground="#00b0f0", fg="white", activeforeground="white", cursor="hand2").place(x=50, y=370, width=300, height=35)

        self.hr = Label(self.login_frame, bg="lightgrey").place(x=50, y=440, width=300, height=2)

        self.lbl_or = Label(self.login_frame, text="OR",bg="white", fg="lightgrey", font=("times new roman", 15, "bold")).place(x=180, y=425)

        self.btn_forgot = Button(self.login_frame, text="Forgot Password?", font=("times new roman", 13), bg="white", fg="#00759E", bd=0, activebackground="white", activeforeground="#00759E").place(x=125, y=480)

        #=======frame 2=========

        # self.register_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        # self.register_frame.place(x=720, y=570, width=350, height=400)

        # self.logo_image = ImageTk.PhotoImage(file="images/logo1.png")
        # self.lbl_logo_image = Label(self.register_frame, image=self.logo_image,bg="black", bd=0).place(x=10, y=0)

        # self.lbl_reg = Label(self.register_frame, text="Don't have an account?", font=("time new roman", 13), bg="white").place(x=40, y=20)
        # self.btn_signup = Button(self.register_frame, text="Sign up", font=("times new roman", 13), bg="white", fg="#00759E",bd=0, activebackground="white", activeforeground="#00759E").place(x=250, y=17)

root = Tk()
obj = Login_System(root)
root.mainloop()
