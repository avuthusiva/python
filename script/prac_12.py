from tkinter import *
root = Tk()
root.title("My First Tkinter App")
root.geometry("300x200")
hello = Label(root, text="Hello, Tkinter!",fg="red",bg="yellow",font=("Arial", 16))
hello.pack()
root.mainloop()