import tkinter as tk
from tkinter import messagebox
from tkinter import *
import mysql.connector as my
mycon=my.connect(host='localhost',user='root',password='tiger',database='library')
cur=mycon.cursor()

cur.execute('use library')

def delete_books():
    Book_id=Book_id_entry.get()
    if Book_id: 
            p = "select * from books where Book_id=%s"
            cur.execute(p, (Book_id,))
            if cur.fetchone():
                q="delete from books where Book_id=%s"
                cur.execute(q, (Book_id,))
                mycon.commit()
                messagebox.showinfo("Book Deleted", "Book successfully deleted!")
            else:
                messagebox.showerror("Error", "Book not found.")
    else:
        messagebox.showerror("Error", "Please enter a Book name.")

def deleteBook():
 global Book_id_entry
 window1=Toplevel()
 window1.geometry('1000x1000')
 window1.title("Delete Book")

 Book_id_label = tk.Label(window1, text="Book id:")
 Book_id_label.pack()
 Book_id_entry = tk.Entry(window1)
 Book_id_entry.pack()

 Delete_button = tk.Button(window1, text="Delete Book", command=delete_books)
 Delete_button.pack()

