import mysql.connector as my
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#from PIL import ImageTK, Image

def saveBook():
    pwd='tiger'
    db='library'
    mycon=my.connect(host='localhost',user='root',password=pwd,database=db)
    cur=mycon.cursor()
    bookid=id.get()
    title=tit.get()
    author=aut.get()
    genre=gen.get()
    publisher=pub.get()
    total=tot.get()
    avl=avail.get()
    try:
        cur.execute("insert into books values({},'{}','{}','{}','{}',{},{})".format(bookid,title,author,genre,publisher,total,avl))
        mycon.commit()
        messagebox.showinfo("Success","Book details added successfully",parent=window1)
    except Exception as s:
        messagebox.showinfo("Error","Error while adding Book details" + str(s))
    cur.close()
    mycon.close()

def addBook():
    global id,tit,aut,gen,pub,tot,avail,window1
    window1=Toplevel()
    window1.title("Library Management System")
    window1.minsize(width=400,height=400)
    window1.geometry("600x500")
    canvas1=Canvas(window1)
    canvas1.pack(fill=BOTH, expand=True)
    topFrame=Frame(window1,bg="#a5d0de",bd=5)
    topFrame.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    topLabel=Label(topFrame,text="Add Books",bg="#dea5d4",fg='white',font=('Fantasy',15))
    topLabel.place(relx=0,rely=0,relwidth=1,relheight=1)
    midFrame=Frame(window1,bg="#a5d0de")
    midFrame.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.8)
    #book id
    lblid=Label(midFrame,text="Book ID:",bg="#dea5d4",fg='white')
    lblid.place(relx=0.05,rely=0.2,relheight=0.08)
    id=Entry(midFrame)
    id.place(relx=0.3,rely=0.2,relwidth=0.62,relheight=0.08)
    #book name
    lblname=Label(midFrame,text="Book Name:",bg="#dea5d4",fg='white')
    lblname.place(relx=0.05,rely=0.30,relheight=0.08)
    tit=Entry(midFrame)
    tit.place(relx=0.3,rely=0.30,relwidth=0.62,relheight=0.08)
    #book author
    lblaut=Label(midFrame,text="Book Author:",bg="#dea5d4",fg='white')
    lblaut.place(relx=0.05,rely=0.40,relheight=0.08)
    aut=Entry(midFrame)
    aut.place(relx=0.3,rely=0.40,relwidth=0.62,relheight=0.08)
    #book publisher
    lblpub=Label(midFrame,text="Book Publisher:",bg="#dea5d4",fg='white')
    lblpub.place(relx=0.05,rely=0.5,relheight=0.08)
    pub=Entry(midFrame)
    pub.place(relx=0.3,rely=0.5,relwidth=0.62,relheight=0.08)
    #book genre
    lblgen=Label(midFrame,text="Book genre:",bg="#dea5d4",fg='white')
    lblgen.place(relx=0.05,rely=0.60,relheight=0.08)
    gen=Entry(midFrame)
    gen.place(relx=0.3,rely=0.60,relwidth=0.62,relheight=0.08)
    #total books
    lbltot=Label(midFrame,text="Total books:",bg="#dea5d4",fg='white')
    lbltot.place(relx=0.05,rely=0.7,relheight=0.08)
    tot=Entry(midFrame)
    tot.place(relx=0.3,rely=0.7,relwidth=0.62,relheight=0.08)
    #available books
    lblavl=Label(midFrame,text="Available books:",bg="#dea5d4",fg='white')
    lblavl.place(relx=0.05,rely=0.8,relheight=0.08)
    avail=Entry(midFrame)
    avail.place(relx=0.3,rely=0.8,relwidth=0.62,relheight=0.08)
    #buttons
    submitbtn=Button(window1,text="Submit",bg="#dea5d4",fg='white',command=saveBook)
    submitbtn.place(relx=0.28,rely=0.9,relwidth=0.18,relheight=0.08)
    quitbtn=Button(window1,text="Quit",bg="#dea5d4",fg='white',command=window1.destroy)
    quitbtn.place(relx=0.53,rely=0.9,relwidth=0.18,relheight=0.08)




