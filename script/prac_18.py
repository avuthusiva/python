from tkinter import *

def display():
    lab.config(text="Selected fuel type: " + fuel.get())

root = Tk()
root.title("Radio Button Example")
root.geometry("300x200")
fuel = StringVar(value="Petrol")
radio_1 = Radiobutton(root, text="Petrol", fg="blue", bg="lightgrey", font=("Helvetica", 12), variable=fuel, value="Petrol")
radio_1.pack(pady=10)
radio_2 = Radiobutton(root, text="Diesel", fg="blue", bg="lightgrey", font=("Helvetica", 12), variable=fuel, value="Diesel")
radio_2.pack(pady=10)
radio_3 = Radiobutton(root, text="Electric", fg="blue", bg="lightgrey", font=("Helvetica", 12), variable=fuel, value="Electric")
radio_3.pack(pady=10)
but = Button(root, text="Submit", fg="blue", bg="lightgrey", font=("Helvetica", 14), command=display)
but.pack(pady=10)
lab = Label(root)
lab.pack()
root.mainloop()