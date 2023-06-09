from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import _mysql_connector 


def login(self):
            if self.txtuser.get()=="" or self.txtpass.get()=="":
                messagebox.showerror("Error","All fields are required.")
            elif self.txtuser.get()=="mid16_balter" and self.txtpass.get()=="Cherie16**":
                messagebox.showinfo("Success","Welcome to Boardroom Bookings")
            else:
                messagebox.showerror("Invalid","Invalid name and password")


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")


        self.bg=ImageTk.PhotoImage(file=r"C:\Users\priya\Documents\Code\Python\Airline Reservation System\peakpx.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.pack(fill="both", expand = "Yes")

        frame=Frame(self.root,bg="white")
        frame.place(x=550,y=170,width=450,height=350)

        img1=Image.open(r"C:\Users\priya\Documents\Code\Python\Airline Reservation System\loginpng.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="white",borderwidth=0)
        lblimg1.place(x=721,y=175,width=100,height=100)

        get_str=Label(frame,text="User Credentials",font=("Times New Roman",15,"bold"),fg="black",bg="white")
        get_str.place(x=153,y=100)

        username=lbl1=Label(frame,text="Username",font=("Times New Roman",10,"bold"),fg="black",bg="white")
        username.place(x=85,y=130)

        self.txtuser=Entry(frame,font=("Times New Roman",10,"bold"),bg="light grey")
        self.txtuser.place(x=75,y=150,width=300)

        password=lbl2=Label(frame,text="Password",font=("Times New Roman",10,"bold"),fg="black",bg="white")
        password.place(x=85,y=200)

        self.txtpass=Entry(frame,font=("Times New Roman",10,"bold"),bg="light grey")
        self.txtpass.place(x=75,y=220,width=300)

        loginbtn=Button(frame,text="Login",font=("Times New Roman",13,"bold"),bd=3,relief=RIDGE,fg="black",bg="#83838B")
        loginbtn.place(x=165,y=260,width=120,height=35)

        registerbtn=Button(frame,text="New User Registration",font=("Times New Roman",12,"bold"),borderwidth=0,fg="black",bg="white")
        registerbtn.place(x=75,y=315,width=155,height=28)

        forpasbtn=Button(frame,text="Forgot Password",font=("Times New Roman",12,"bold"),borderwidth=0,fg="black",bg="white")
        forpasbtn.place(x=236,y=315,width=140,height=28)



                





if __name__ == "__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()