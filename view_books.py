import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as my
mycon=my.connect(host='localhost',user='root',password='tiger',database='library')
cur=mycon.cursor()

cur.execute('use library')

def view_book():
    Book_name= Book_name_entry.get()
    if Book_name!='':
        cur.execute("select *  from  books where book_name='%s'" %(Book_name))
        for i in cur:
            tree.insert("", END, values=i)
            tree.insert("", END, values="")
    else:
        messagebox.showwarning('Input Error', 'Book name is required.')

def viewBook():      
    global tree,Book_name_entry
    window1=Toplevel()
    window1.geometry('1000x1000')
    window1.title("View customer")              

    Book_name_label=tk.Label(window1, text='Book Name')                   
    Book_name_label.pack()
    Book_name_entry = tk.Entry(window1)
    Book_name_entry.pack()

    view_button=tk.Button(window1, text='View Book', command=view_book)
    view_button.pack()

    tree = ttk.Treeview(window1)
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




       
