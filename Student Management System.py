import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

root = tk.Tk()
root.title("Management")


connection = sqlite3.connect('management.db')

TABLE_NAME = "management_table"
STUDENT_ID = "student_id"
STUDENT_NAME = "student_name"
STUDENT_CLASS = "student_class"
STUDENT_ADDRESS = "student_address"
STUDENT_PHONE = "student_phone"

connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + STUDENT_ID +
                   " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                   STUDENT_NAME + " TEXT, " + STUDENT_CLASS + " TEXT, " +
                   STUDENT_ADDRESS + " TEXT, " + STUDENT_PHONE + " INTEGER);")

appLabel = tk.Label(root, text="Student Management System", fg="#06a099", width=35)
appLabel.config(font=("Sylfaen", 30))
appLabel.grid(row=0, columnspan=2, padx=(10,10), pady=(30, 0))

class Student:
    studentName = ""
    className = ""
    phoneNumber = 0
    address = ""

    def __init__(self, studentName, className, phoneNumber, address):
        self.studentName = studentName
        self.className = className
        self.phoneNumber = phoneNumber
        self.address = address

nameLabel = tk.Label(root, text="Enter your name", width=40, anchor='w',
                     font=("Sylfaen", 12)).grid(row=1, column=0, padx=(10,0),
                                                pady=(30, 0))
classLabel = tk.Label(root, text="Enter your Class", width=40, anchor='w',
                        font=("Sylfaen", 12)).grid(row=2, column=0, padx=(10,0))
phoneLabel = tk.Label(root, text="Enter your phone number", width=40, anchor='w',
                      font=("Sylfaen", 12)).grid(row=3, column=0, padx=(10,0))
addressLabel = tk.Label(root, text="Enter your address", width=40, anchor='w',
                        font=("Sylfaen", 12)).grid(row=4, column=0, padx=(10,0))

nameEntry = tk.Entry(root, width = 30)
classEntry = tk.Entry(root, width = 30)
phoneEntry = tk.Entry(root, width = 30)
addressEntry = tk.Entry(root, width = 30)

nameEntry.grid(row=1, column=1, padx=(0,10), pady=(30, 20))
classEntry.grid(row=2, column=1, padx=(0,10), pady = 20)
phoneEntry.grid(row=3, column=1, padx=(0,10), pady = 20)
addressEntry.grid(row=4, column=1, padx=(0,10), pady = 20)

def saveInput():
    global nameEntry, classEntry, phoneEntry, addressEntry  
    global TABLE_NAME, STUDENT_NAME, STUDENT_CLASS, STUDENT_ADDRESS, STUDENT_PHONE
    username = nameEntry.get()
    nameEntry.delete(0, tk.END)
    className = classEntry.get()
    classEntry.delete(0, tk.END)
    phone = int(phoneEntry.get())
    phoneEntry.delete(0, tk.END)
    address = addressEntry.get()
    addressEntry.delete(0, tk.END)

    connection.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + ", " +
                       STUDENT_CLASS + ", " + STUDENT_ADDRESS + ", " +
                       STUDENT_PHONE + " ) VALUES ( '"
                       + username + "', '" + className + "', '" +
                       address + "', " + str(phone) + " ); ")
    connection.commit()
    messagebox.showinfo("Success", "Data Saved Successfully.")

def updateInput():
    global nameEntry, classEntry, phoneEntry, addressEntry  
    # global TABLE_NAME, STUDENT_NAME, STUDENT_CLASS, STUDENT_ADDRESS, STUDENT_PHONE
    username = nameEntry.get()
    nameEntry.delete(0, tk.END)
    className = classEntry.get()
    classEntry.delete(0, tk.END)
    phone = int(phoneEntry.get())
    phoneEntry.delete(0, tk.END)
    address = addressEntry.get()
    addressEntry.delete(0, tk.END)

    connection.execute("UPDATE management_table SET student_name=?,STUDENT_CLASS=?,student_address=? WHERE student_phone=?",(username,className,address,phone))
    connection.commit()
    messagebox.showinfo("Success", "Data Updated Successfully.") 


def deleteInput():
    global phoneEntry 
    phone = int(phoneEntry.get())
    phoneEntry.delete(0, tk.END)

    connection.execute("DELETE FROM management_table WHERE student_phone=?",(phone,))
    connection.commit()
    messagebox.showinfo("Success", "Data Deleted Successfully.")   


def displayResults():
    # root.destroy()
    secondWindow = tk.Tk()

    secondWindow.title("Display results")

    appLabel = tk.Label(secondWindow, text="Student Management System",
                        fg="#06a099", width=40)
    appLabel.config(font=("Sylfaen", 30))
    appLabel.pack()

    tree = ttk.Treeview(secondWindow)
    tree["columns"] = ("one", "two", "three", "four")

    tree.heading("one", text="Student Name")
    tree.heading("two", text="Class Name")
    tree.heading("three", text="Address")
    tree.heading("four", text="Phone Number")

    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
    i = 0

    for row in cursor:
        tree.insert('', i, text="Student " + str(row[0]),
                    values=(row[1], row[2],
                            row[3], row[4]))
        i = i + 1

    tree.pack()
    secondWindow.mainloop()


# def printDetails():
#     for singleItem in list:
#         print("Student name is: %s\nClass name is: %s\nPhone number is: %d\nAddress is: %s" %
#               (singleItem.studentName, singleItem.className, singleItem.phoneNumber, singleItem.address))
#         print("****************************************")

button = tk.Button(root, text="Save Data", command=lambda :saveInput())
# button.grid(row=5, column=0, pady=30)
button.grid(row=5, column=0,pady=0)

button = tk.Button(root, text="Update", command=lambda :updateInput())
button.grid(row=6, column=0, pady=10)

button = tk.Button(root, text="Delete", command=lambda :deleteInput())
button.grid(row=7, column=0, pady=10)

displayButton = tk.Button(root, text="Display result", command=lambda :displayResults())
displayButton.grid(row=5, column=1)

root.mainloop()