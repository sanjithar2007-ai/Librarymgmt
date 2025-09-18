import mysql.connector as my
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#from PIL import ImageTK, Image
pwd='tiger'
db='library'
mycon=my.connect(host='localhost',user='root',password=pwd,database=db)
cur=mycon.cursor()

def viewBook():
    #get list of books
    booklist="select * from books"
    ht=0
    try:
        cur.execute(booklist)
        res=cur.fetchall()
        ht=cur.rowcount
        ht=ht*2
    except Exception as e:
        messagebox.showinfo("Error","Error while Fetching Book details" + str(e))
    window1=Toplevel()
    window1.title("Library Managment System")
    window1.minsize(width=400,height=400)
    window1.geometry("600x500")
    canvas1=Canvas(window1,height=ht)
    canvas1.pack(fill=BOTH, expand=True)
    topFrame=Frame(window1,bg="#a5d0de",bd=5)
    topFrame.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.1)
    topLabel=Label(topFrame,text="View Books",bg="#dea5d4",fg='white',font=('Fantasy',15))
    topLabel.place(relx=0,rely=0,relwidth=1,relheight=1)
    midFrame=Frame(window1,bg="#dea5d4")
    midFrame.place(relx=0.1,rely=0.2,relwidth=0.8)#,relheight=0.6)
    tree = ttk.Treeview(midFrame,height=ht)
    tree.place(relx=0.1,rely=0.2,relwidth=0.8)#,relheight=0.6)
    tree.pack(fill=BOTH)
    ttk.Style().configure('Treeview.Heading', foreground='black', background='white', font=('Arial',10),)
    ttk.Style().configure("Treeview",background="#dea5d4",foreground='white')
    #ttk.Style().configure("Treeview",height=8)
    # Define columns
    tree["columns"] = ("Book ID", "Book Name", "Author", "Genre", "Pubisher","Total Quantity","Avaiable Quantity")
    tree.column("#0", width=0, stretch=NO)
    tree.column("Book ID", anchor=W, width=80)
    tree.column("Book Name", anchor=W, width=120)
    tree.column("Author", anchor=W, width=80)
    tree.column("Genre", anchor=W, width=80)
    tree.column("Pubisher", anchor=W, width=80)
    tree.column("Total Quantity", anchor=CENTER, width=80)
    tree.column("Avaiable Quantity", anchor=CENTER, width=80)
    # Define headings
    tree.heading("#0", text="", anchor=W)
    tree.heading("Book ID", text="Book ID", anchor=W)
    tree.heading("Book Name", text="Book Name", anchor=W)
    tree.heading("Author", text="Author", anchor=W)
    tree.heading("Genre", text="Genre", anchor=W)
    tree.heading("Pubisher", text="Pubisher", anchor=W)
    tree.heading("Total Quantity", text="Total Quantity", anchor=CENTER)
    tree.heading("Avaiable Quantity", text="Avaiable Quantity", anchor=CENTER)
    print("success2")
    #get list of books
    booklist="select * from books"
    try:
        cur.execute(booklist)
       
        for i in res:
            tree.insert("", END, values=i)
            tree.insert("", END, values="")
    
    except Exception as e:
        messagebox.showinfo("Error","Error while Fetching Book details" + str(e))
    
    

