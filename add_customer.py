import tkinter as tk
from tkinter import messagebox
from tkinter import *
import mysql.connector as my
mycon=my.connect(host='localhost',user='root',password='tiger',database='library')
cur=mycon.cursor()

cur.execute('use library')

def add_customer():
    Customer_id = Customer_id_entry.get()
    Customer_name = Customer_name_entry.get()
    Customer_pno = Customer_pno_entry.get()
    Customer_address = Customer_address_entry.get()
    if Customer_name and Customer_id and Customer_pno and Customer_address:
        cur.execute("insert into customer_details(customer_id,name,address,pno)values(%s,%s,%s,%s)",(Customer_id,Customer_name,Customer_address,Customer_pno))
        mycon.commit()
        messagebox.showinfo("added", "sucessfully entered",parent=window1)

    else:
        messagebox.showwarning('Input Error', 'All fields are required.')

def addCustomer():
    global Customer_id_entry,Customer_name_entry,Customer_pno_entry,Customer_address_entry,window1
    window1=Toplevel()
    window1.title("Library Management System")
    window1.minsize(width=400,height=400)
    window1.geometry("600x500")
    canvas1=Canvas(window1)
    canvas1.pack(fill=BOTH, expand=True)
    topFrame=Frame(window1,bg="#a5d0de",bd=5)
    topFrame.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    topLabel=Label(topFrame,text="Add Customer",bg="#dea5d4",fg='white',font=('Fantasy',15))
    topLabel.place(relx=0,rely=0,relwidth=1,relheight=1)
    midFrame=Frame(window1,bg="#a5d0de")
    midFrame.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.8)

    Customer_id_label=tk.Label(midFrame, text='Customer ID',bg="#dea5d4",fg='white')
    Customer_id_label.place(relx=0.05,rely=0.2,relheight=0.08)
    Customer_id_label.pack()
    Customer_id_entry=tk.Entry(midFrame)
    Customer_id_entry.place(relx=0.3,rely=0.2,relwidth=0.62,relheight=0.08)
    Customer_id_entry.pack()

    Customer_name_label= tk.Label(midFrame, text='Name',bg="#dea5d4",fg='white')
    Customer_name_label.place(relx=0.05,rely=0.3,relheight=0.08)
    Customer_name_label.pack()
    Customer_name_entry=tk.Entry(midFrame)
    Customer_name_entry.place(relx=0.3,rely=0.3,relwidth=0.62,relheight=0.08)
    Customer_name_entry.pack()

    Customer_pno_label=tk.Label(midFrame, text='Phone',bg="#dea5d4",fg='white')
    Customer_pno_label.place(relx=0.05,rely=0.4,relheight=0.08)
    Customer_pno_label.pack()
    Customer_pno_entry=tk.Entry(midFrame)
    Customer_pno_entry.place(relx=0.3,rely=0.4,relwidth=0.62,relheight=0.08)
    Customer_pno_entry.pack()

    Customer_address_label=tk.Label(midFrame, text='Address',bg="#dea5d4",fg='white')
    Customer_address_label.place(relx=0.05,rely=0.5,relheight=0.08)
    Customer_address_label.pack()
    Customer_address_entry=tk.Entry(midFrame)
    Customer_address_entry.place(relx=0.3,rely=0.5,relwidth=0.62,relheight=0.08)
    Customer_address_entry.pack()


    add_button=tk.Button(midFrame, text='Add Customer',bg="#dea5d4",fg='white', command=add_customer)
    add_button.place(relx=0.28,rely=0.6,relwidth=0.18,relheight=0.08)
    add_button.pack()


