from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import _mysql_connector 


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("New Registration")
        self.root.geometry("1550x800+0+0")


        self.bg=ImageTk.PhotoImage(file=r"C:\Users\priya\Documents\Code\Python\Airline Reservation System\peakpx.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="white")
        frame.place(x=550,y=170,width=450,height=450)

        img1=Image.open(r"C:\Users\priya\Documents\Code\Python\Airline Reservation System\loginpng.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        regimg1=Label(image=self.photoimage1,bg="white",borderwidth=0)
        regimg1.place(x=721,y=175,width=100,height=100)

        get_str=Label(frame,text="New User",font=("Times New Roman",16,"bold"),fg="black",bg="white")
        get_str.place(x=179,y=100)

        # ======LABEL & ENTRIES======

        fname=Label(frame,text="First Name",font=("Times New Roman",8),bg="white")
        fname.place(x=50,y=140)

        self.fname_entry=ttk.Entry(frame,font=("Times New Roman",8))
        self.fname_entry.place(x=45,y=160,width=160)

        laname=Label(frame,text="Last Name",font=("Times New Roman",8),bg="white")
        laname.place(x=50,y=180)

        laname_entry=ttk.Entry(frame,font=("Times New Roman",8))
        laname_entry.place(x=45,y=200,width=160)

        emailid=Label(frame,text="Email ID",font=("Times New Roman",8),bg="white")
        emailid.place(x=50,y=220)

        emailid_entry=ttk.Entry(frame,font=("Times New Roman",8))
        emailid_entry.place(x=45,y=240,width=160)

        contactno=Label(frame,text="Contact Number",font=("Times New Roman",8),bg="white")
        contactno.place(x=50,y=260)

        contactno_entry=ttk.Entry(frame,font=("Times New Roman",8))
        contactno_entry.place(x=45,y=280,width=160)

        passw=Label(frame,text="Password",font=("Times New Roman",8),bg="white")
        passw.place(x=250,y=140)

        passw_entry=ttk.Entry(frame,font=("Times New Roman",8))
        passw_entry.place(x=245,y=160,width=160)

        secq=Label(frame,text="Security Question",font=("Times New Roman",8),bg="white")
        secq.place(x=250,y=180)

        self.combo_security_Q=ttk.Combobox(frame,font=("Times New Roman",8),state="readonly")
        self.combo_security_Q["values"]=("Select one of the following","Your Birthplace","Your Father's Name","Your favourite chocolate")
        self.combo_security_Q.place(x=245,y=200,width=160)
        self.combo_security_Q.current(0)

        secan=Label(frame,text="Security Answer",font=("Times New Roman",8),bg="white")
        secan.place(x=250,y=220)

        secan_entry=ttk.Entry(frame,font=("Times New Roman",8))
        secan_entry.place(x=245,y=240,width=160)

        Country=Label(frame,text="Country",font=("Times New Roman",8),bg="white")
        Country.place(x=250,y=260)

        Country_entry=ttk.Entry(frame,font=("Times New Roman",8))
        Country_entry.place(x=245,y=280,width=160)


        checkbtn=Checkbutton(frame,text="I agree with all T&Cs.",font=("Times New Roman",8,"bold"),bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=155,y=310)

        rebtn=Button(frame,text="Register",font=("Times New Roman",12,"bold"),borderwidth=0,cursor="hand2",fg="black",bg="#83838B")
        rebtn.place(x=171,y=360,width=110,height=50)

        













if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()
