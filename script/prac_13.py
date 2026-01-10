from tkinter import *

def display():
    print("Button clicked!")

root = Tk()
root.title("Simple GUI")
root.geometry("300x200")
button = Button(root,text="Click Me",fg="blue",bg="lightgrey",font=("Helvetica", 14),command=display)
button.pack()
root.mainloop()