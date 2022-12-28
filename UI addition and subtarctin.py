# Write a fuction to make UI Application to add two number and display result

from tkinter import *

def add():
    result = int(e1.get()) + int(e2.get())
    l3.config(text=result)
 
def subtract():
    result = int(e1.get()) - int(e2.get())
    l3.config(text=result)   
    
root = Tk() 
root.title("Addition")
root.geometry("300x200")

l1 = Label(root, text="Enter First Number")
l2 = Label(root, text="Enter Second Nmmber")
l3 = Label(root, text="Result")

e1 = Entry(root)
e2 = Entry(root)

l1.grid(row=0, column=0)
l2.grid(row=1, column=0)
l3.grid(row=2, column=0)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b1 = Button(root, text="Add", command=add)
b1.grid(row=3, column=0)

b2 = Button(root, text="Subtact", command=subtract)
b2.grid(row=3, column=1)
                                        
root.mainloop()                         