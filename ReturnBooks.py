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
def saveReturnBook():
    issqty=0
    bid=tit.get()
    custid=aut.get()
    curdate=date.today()
    try:
        cur.execute("select Quantity_issued,date_of_return from issue_details where book_id={} and customer_id={}".format(bid,custid))
        res=cur.fetchall()
        print(cur.rowcount)
        if(cur.rowcount!=0):
            for i in res:
                issqty=i[0]
                dor=i[1]
                print (issqty)
                print (dor)
        
            if(curdate>dor):
                status='Returned with fine'
            else:
                status='Returned'
                
            cur.execute("update issue_details set current_status='{}' where  book_id={} and customer_id={}".format(status,bid,custid))
            mycon.commit()
            cur.execute("update books set Available_Quantity=Available_Quantity + {} where book_id={}".format(issqty,bid))
            mycon.commit()
            messagebox.showinfo("Success","Book Returned successdully",parent=window1)
        else:
            messagebox.showinfo("Error","This book is not issued to this customer",parent=window1)
    except Exception as e:
        messagebox.showinfo("Error","Error while Returning Books" +str(e),parent=window1)
    tit.delete(0,END)
    aut.delete(0,END)
    bookid.set('')
    pub.set('')
  
# bind the selected value changes
def id_changed(event):
    val=bookid.get()
    a=val.split(":")
    bid=a[0]
    tit.delete(0,END)
    tit.insert(0,bid)

def custid_changed(event):
    val=pub.get()
    b=val.split(":")
    cid=b[0]
    aut.delete(0,END)
    aut.insert(0,cid)
    
def returnBook():
    global bookid,tit,aut,pub,bklst,cstlst,window1
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
    topLabel=Label(topFrame,text="Return Books",bg="#dea5d4",fg='white',font=('Fantasy',15))
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

    #buttons
    submitbtn=Button(window1,text="Return",bg="#dea5d4",fg='white',command=saveReturnBook)
    submitbtn.place(relx=0.28,rely=0.9,relwidth=0.18,relheight=0.08)
    quitbtn=Button(window1,text="Quit",bg="#dea5d4",fg='white',command=window1.destroy)
    quitbtn.place(relx=0.53,rely=0.9,relwidth=0.18,relheight=0.08)

#cur.close()
#mycon.close()


