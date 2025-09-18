import mysql.connector as my
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date,timedelta
#from PIL import ImageTK, Image
pwd='tiger'
db='library'
mycon=my.connect(host='localhost',user='root',password=pwd,database=db)
cur=mycon.cursor()
def saveIssueBook():
    available=0
    issqty=0
    bid=tit.get()
    custid=aut.get()
    issqty=qty.get()
    available=avail.get()
    if(int(available)>=int(issqty)):
        doi=date.today()
        dor=doi + timedelta(days=10)
        try:
            cur.execute("select * from issue_details where book_id={} and customer_id={}".format(bid,custid))
            res=cur.fetchall()
            print(cur.rowcount)
            if(cur.rowcount==0):
                cur.execute("insert into issue_details values({},{},{},'{}','{}','{}')".format(bid,custid,issqty,doi,dor,'Issued'))
                mycon.commit()
                cur.execute("update books set Available_Quantity=Available_Quantity - {} where book_id={}".format(issqty,bid))
                mycon.commit()
                messagebox.showinfo("Success","Book Issued successdully",parent=window1)
            else:
                messagebox.showinfo("Error","This book is aready issued to this customer",parent=window1)
        except:
            messagebox.showinfo("Error","Error while Issuing Books")
        qty.delete(0,END)
        avail.delete(0,END)
        tit.delete(0,END)
        aut.delete(0,END)
        bookid.set('')
        pub.set('')
    else:
            messagebox.showinfo("Error","Sufficient quantity not available",parent=window1)
            qty.delete(0,END)
# bind the selected value changes
def id_changed(event):
    qty.delete(0,END)
    val=bookid.get()
    a=val.split(":")
    bid=a[0]
    tit.delete(0,END)
    tit.insert(0,bid)
    cur.execute("select Available_Quantity from books where Book_id={}".format(bid))
    for i in cur:
        quant=i[0]
    avail.delete(0,END)
    avail.insert(0,quant)

def custid_changed(event):
    qty.delete(0,END)
    val=pub.get()
    b=val.split(":")
    cid=b[0]
    aut.delete(0,END)
    aut.insert(0,cid)
    
def issueBook():
    global bookid,tit,aut,gen,pub,tot,avail,qty,bklst,cstlst,window1
    bklst=[]
    cstlst=[]
    window1=Toplevel()
    window1.title("Library Managment System")
    window1.minsize(width=400,height=400)
    window1.geometry("600x500")
    canvas1=Canvas(window1)
    canvas1.pack(fill=BOTH, expand=True)
    topFrame=Frame(window1,bg="#a5d0de",bd=5)
    topFrame.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    topLabel=Label(topFrame,text=" Books",bg="#dea5d4",fg='white',font=('Fantasy',15))
    topLabel.place(relx=0,rely=0,relwidth=1,relheight=1)
    midFrame=Frame(window1,bg="#a5d0de")
    midFrame.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.8)
    #get list of books
    booklist="select concat(Book_id,':',Book_Name) from books"
    try:
        cur.execute(booklist)
        for i in cur:
            bklst.append(i[0])
    except Exception as e:
        messagebox.showinfo("Error","Error while Fetching Book details" + str(e))
    #get list of customers
    custlist="select concat(customer_id,':',name) from customer_details"
    try:
        cur.execute(custlist)
        for i in cur:
            cstlst.append(i[0])
    except:
        messagebox.showinfo("Error","Error while Fetching customer details")
    #book id and name
    lblid=Label(midFrame,text="Book:",bg="#dea5d4",fg='white')
    lblid.place(relx=0.05,rely=0.2)
    bookid=ttk.Combobox(midFrame,value=bklst)
    bookid.place(relx=0.3,rely=0.20,relwidth=0.62,relheight=0.08)
    bookid.bind('<<ComboboxSelected>>', id_changed)

    #book id
    lblname=Label(midFrame,text="Book ID:",bg="#dea5d4",fg='white')
    lblname.place(relx=0.05,rely=0.30,relheight=0.08)
    tit=Entry(midFrame,bg="white",fg='black')
    tit.place(relx=0.3,rely=0.30,relwidth=0.62,relheight=0.08)
    tit.bind('<Key>',lambda _:'break')

    #Cust id and name
    lblpub=Label(midFrame,text="Customer:",bg="#dea5d4",fg='white')
    lblpub.place(relx=0.05,rely=0.40,relheight=0.08)
    pub=ttk.Combobox(midFrame,value=cstlst)
    pub.place(relx=0.3,rely=0.40,relwidth=0.62,relheight=0.08)
    pub.bind('<<ComboboxSelected>>', custid_changed)
    #cust id
    lblaut=Label(midFrame,text="Customer ID:",bg="#dea5d4",fg='white')
    lblaut.place(relx=0.05,rely=0.50,relheight=0.08)
    aut=Entry(midFrame,bg="white",fg='black')
    aut.place(relx=0.3,rely=0.50,relwidth=0.62,relheight=0.08)
    aut.bind('<Key>',lambda _:'break')
    #aut.configure(state='disabled')
    #book available
    lblavl=Label(midFrame,text="Quantity available:",bg="#dea5d4",fg='white')
    lblavl.place(relx=0.05,rely=0.60,relheight=0.08)
    #qtyid=tk.StringVar()
    avail=Entry(midFrame,bg="white",fg='black')
    avail.place(relx=0.3,rely=0.60,relwidth=0.62,relheight=0.08)
    avail.bind('<Key>',lambda _:'break')

    #Quantity to be issued
    lbliss=Label(midFrame,text="Quantity to be issued:",bg="#dea5d4",fg='white')
    lbliss.place(relx=0.05,rely=0.7,relheight=0.08)
    qty=Entry(midFrame)
    qty.place(relx=0.3,rely=0.7,relwidth=0.62,relheight=0.08)

    #buttons
    submitbtn=Button(window1,text="Issue",bg="#dea5d4",fg='white',command=saveIssueBook)
    submitbtn.place(relx=0.28,rely=0.9,relwidth=0.18,relheight=0.08)
    quitbtn=Button(window1,text="Quit",bg="#dea5d4",fg='white',command=window1.destroy)
    quitbtn.place(relx=0.53,rely=0.9,relwidth=0.18,relheight=0.08)

#cur.close()
#mycon.close()


