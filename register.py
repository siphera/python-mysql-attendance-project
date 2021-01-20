from tkinter import *
from tkinter import ttk
from PIL import ImageTk

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Lifechoices-online Register")
        self.root.geometry("1920x1080")
        self.root.resizable(False, False)

        self.main_frame2 = Frame(self.root, bd=0, relief=RIDGE, bg="white")
        self.main_frame2.place(x=0, y=0, width=1920, height=1080)

        # ===== background image=====
        self.phone_image = ImageTk.PhotoImage(file="images/image.png")
        self.lbl_phone_image = Label(self.main_frame2, image=self.phone_image, bg="#00b0f0", bd=0).place(x=0, y=0, relwidth=1, relheight=1)

        # ===== side image=====
        self.side_image = ImageTk.PhotoImage(file="images/side3.png")
        self.lbl_side_image = Label(self.main_frame2, image=self.side_image,bg="black", bd=0).place(x=496, y=220, width=282, height=500)

        # =======>reg frame<======
        self.reg_frame = Frame(self.main_frame2, bg="white")
        self.reg_frame.place(x=780, y=220, width=700, height=500)

        self.lbl_title = Label(self.reg_frame, text="REGISTER NEW USER", font=("times new roman", 20, "bold"), bg="white", fg="black").place(x=50, y=30)

        self.lbl_fname = Label(self.reg_frame, text="First name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=100)
        self.txt_fname = Entry(self.reg_frame, font=("times new roman", 15, "bold"), bg="lightgray").place(x=50, y=130, width=250)

        self.lbl_contact = Label(self.reg_frame, text="Contact No.", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=180)
        self.txt_contact = Entry(self.reg_frame, font=("times new roman", 15, "bold"), bg="lightgray").place(x=50, y=210, width=250)

        self.lbl_sname = Label(self.reg_frame, text="Surname", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=380, y=100)
        self.txt_sname = Entry(self.reg_frame, font=("times new roman", 15, "bold"), bg="lightgray").place(x=380, y=130, width=250)

        self.lbl_email = Label(self.reg_frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=380, y=180)
        self.txt_email = Entry(self.reg_frame, font=("times new roman", 15, "bold"), bg="lightgray").place(x=380, y=210, width=250)

        self.lbl_department = Label(self.reg_frame, text="Department", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=285, y=260)
        self.cmb_department = ttk.Combobox(self.reg_frame, font=("times new roman", 13, "bold"), state='readonly', justify=CENTER)
        self.cmb_department['values'] = ("Select", "Lecture", "Academy", "Studio", "Finance")
        self.cmb_department.place(x=210, y=290, width=250)
        self.cmb_department.current(0)

        self.lbl_password = Label(self.reg_frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=340)
        self.txt_password = Entry(self.reg_frame, font=("times new roman", 15, "bold"), bg="lightgray", show="*").place(x=50, y=370, width=250)

        self.lbl_confirm_pword = Label(self.reg_frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=380, y=340)
        self.txt_confirm_pword = Entry(self.reg_frame, font=("times new roman", 15, "bold"), bg="lightgray", show="*").place(x=380, y=370, width=250)



        self.btn_register = Button(self.reg_frame, text="Register", font=("Arial Rounded MT Bold", 15), bg="#00b0f0", activebackground="#00b0f0", fg="white", activeforeground="white", cursor="hand2").place(x=50, y=440, width=250, height=35)



root = Tk()
obj = Register(root)
root.mainloop()
