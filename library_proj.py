
#main program
import mysql.connector as my
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from AddBooks import *
from add_customer import *
from IssueBooks import *
from ReturnBooks import *
from view_customer import *
from SearchBooks import *
from delete_books import *
from ViewBooks import *
from SortBooks import *
#from PIL import ImageTK, Image
pwd='tiger'
db='library'
mycon=my.connect(host='localhost',user='root',password=pwd,database=db)
cur=mycon.cursor()
def libraryDB():
    pwd='tiger'
    db='library'
    mycon=my.connect(host='localhost',user='root',password=pwd,database=db)
    cur=mycon.cursor()
    q="create table books(Book_id int(4) primary key,Book_Name varchar(50),Author_Name varchar(50),Genre varchar(20),Publisher varchar(50),Total_Quantity numeric(3),Available_Quantity int(3))"
    r="create table customer_details(customer_id int(4) primary key,name varchar(20),address varchar(50),pno numeric(10))"
    s="create table issue_details(Book_id int(4),customer_id int(4),Quantity_Issued int(1) check(Quantity_issued<=3),Date_of_issue date,Date_of_return date,current_status varchar(10))"
    t="create table login_details(User_Name varchar(50),password varchar(50))"
    cur.execute(q)
    cur.execute(r)
    cur.execute(s)
    cur.execute(t)
    mycon.commit()
    cur.execute("insert into books values(1001,'Alice in Wonderland','Lewis Carroll','Fantasy','Macmillan',100,100)")
    cur.execute("insert into books values(1002,'To kill mocking bird','Harper lee','Novel','Harpercollins publishers',50,50)")
    cur.execute("insert into books values(1003,'Oliver twist','Charles Dickens','Novel','Richard Bentley',50,50)")
    cur.execute("insert into books values(1004,'The Girl in blue','PG Wodehouse','Comedy','Barrie&Jenkins',100,100)")
    cur.execute("insert into books values(1005,'I wish I was an extrovert','Fariyal Mujeeb Khan','Non Fiction','Harpercollins publishers',150,150)")
    cur.execute("insert into login_details values('admin','bookgeek')")
    mycon.commit()
    cur.close()
    mycon.close()

#libraryDB()
window=Tk()
window.title("Library Management System")
window.minsize(width=400,height=400)
window.geometry("600x600")
canvas1=Canvas(window)
canvas1.pack(fill=BOTH, expand=True)
topFrame=Frame(window,bg="#a5d0de",bd=5)
topFrame.place(relx=0.2,rely=0.05,relwidth=0.6,relheight=0.10)
topLabel=Label(topFrame,text="Welcome to World of Books",bg="#dea5d4",fg='white',font=('Fantasy',15))
topLabel.place(relx=0,rely=0,relwidth=1,relheight=1)
#buttons
btn1=Button(window,text="Add Book Details",bg="#dea5d4",fg='white',command=addBook)
btn1.place(relx=0.28,rely=0.18,relwidth=0.45,relheight=0.07)

btn2=Button(window,text="Add Customer Details",bg="#dea5d4",fg='white',command=addCustomer)
btn2.place(relx=0.28,rely=0.25,relwidth=0.45,relheight=0.07)

btn3=Button(window,text="View Book Details",bg="#dea5d4",fg='white',command=viewBook)
btn3.place(relx=0.28,rely=0.32,relwidth=0.45,relheight=0.07)

btn4=Button(window,text="View Customer Details",bg="#dea5d4",fg='white',command=viewCustomer)
btn4.place(relx=0.28,rely=0.39,relwidth=0.45,relheight=0.07)

btn5=Button(window,text="Issue Book",bg="#dea5d4",fg='white',command=issueBook)
btn5.place(relx=0.28,rely=0.46,relwidth=0.45,relheight=0.07)

btn6=Button(window,text="Return Book",bg="#dea5d4",fg='white',command=returnBook)
btn6.place(relx=0.28,rely=0.53,relwidth=0.45,relheight=0.07)

btn7=Button(window,text="Search Book",bg="#dea5d4",fg='white',command=searchBook)
btn7.place(relx=0.28,rely=0.60,relwidth=0.45,relheight=0.07)

btn8=Button(window,text="Delete Book",bg="#dea5d4",fg='white',command=deleteBook)
btn8.place(relx=0.28,rely=0.67,relwidth=0.45,relheight=0.07)

btn9=Button(window,text="Sort Books",bg="#dea5d4",fg='white',command=sortBook)
btn9.place(relx=0.28,rely=0.74,relwidth=0.45,relheight=0.07)

quitbtn=Button(window,text="Quit",bg="#dea5d4",fg='white',command=window.destroy)
quitbtn.place(relx=0.28,rely=0.81,relwidth=0.45,relheight=0.07)

window.mainloop()



