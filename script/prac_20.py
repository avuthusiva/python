from tkinter import *

def display():
    email = entry_1.get()
    password = entry_2.get()
    print(f"Email: {email}, Password: {password}")
    if email and password:
        lab.config(text="Login Successful")
    else:
        lab.config(text="Please enter both email and password")

root = Tk()
root.title("Grid Layout Example")
root.geometry("400x300")
lab_1 = Label(root,text="Email")
lab_1.grid(row=0,column=0,padx=10,pady=10)
entry_1 = Entry(root)
entry_1.grid(row=0,column=1,padx=10,pady=10)
lab_2 = Label(root,text="Password")
lab_2.grid(row=1,column=0,padx=10,pady=10)
entry_2 = Entry(root,show="*")
entry_2.grid(row=1,column=1,padx=10,pady=10)
buttion_1 = Button(root,text="Login",command=display)
buttion_1.grid(row=2,column=1,columnspan=2,pady=20)
lab = Label(root)
lab.grid(row=3,column=0,columnspan=2)
root.mainloop()