import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as my
mycon=my.connect(host='localhost',user='root',password='tiger',database='library')
cur=mycon.cursor()

cur.execute('use library')

def view_customer():
    customer_id = customer_id_entry.get()
    if customer_id!='':
        cur.execute("select *  from customer_details where customer_id=%s" %(customer_id))
        for i in cur:
            tree.insert("", END, values=i)
            tree.insert("", END, values="")
    else:
        messagebox.showwarning('Input Error', 'Customer ID is required.')
        
def viewCustomer():
    global tree,customer_id_entry
    window1=Toplevel()
    window1.geometry('1000x1000')
    window1.title("View customer")

    customer_id_label=tk.Label(window1, text='Customer ID')                   
    customer_id_label.pack()
    customer_id_entry = tk.Entry(window1)
    customer_id_entry.pack()

    view_button=tk.Button(window1, text='View Customer', command=view_customer)
    view_button.pack()

    tree = ttk.Treeview(window1)
    tree.place(relx=0.1,rely=0.2,relwidth=0.8)#,relheight=0.6)
    tree.pack(fill=BOTH)
    ttk.Style().configure('Treeview.Heading', foreground='black', background='white', font=('Arial',10),)
    ttk.Style().configure("Treeview",background="#dea5d4",foreground='white')
    #ttk.Style().configure("Treeview",height=8)
    # Define columns
    tree["columns"] = ("customer_id", "name", "address", "pno")

    tree.column("#0", width=0, stretch=NO)
    tree.column("customer_id", anchor=W, width=80)
    tree.column("name", anchor=W, width=120)
    tree.column("address", anchor=W, width=80)
    tree.column("pno", anchor=W, width=80)

    # Define headings
    tree.heading("#0", text="", anchor=W)
    tree.heading("customer_id", text="Customer ID", anchor=W)
    tree.heading("name", text="Name", anchor=W)
    tree.heading("address", text="address", anchor=W)
    tree.heading("pno", text="pno", anchor=W)



