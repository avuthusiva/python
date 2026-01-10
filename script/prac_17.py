from tkinter import *

def display():
    selected = []
    if check_1_val.get():
        selected.append("Vanilla")
    if check_2_val.get():
        selected.append("Chocolate")
    if check_3_val.get():
        selected.append("Strawberry")
    lab.config(text="Selected flavors: " + ", ".join(selected) if selected else "No flavors selected")

root = Tk()
root.title("Icecream shop")
root.geometry("400x300")

check_1_val = BooleanVar()
check_2_val = BooleanVar()
check_3_val = BooleanVar()
check_1 = Checkbutton(root, text="Vanilla", fg="blue", bg="lightgrey", font=("Helvetica", 12), variable=check_1_val)
check_1.pack(pady=10)
check_2 = Checkbutton(root, text="Chocolate", fg="blue", bg="lightgrey", font=("Helvetica", 12), variable=check_2_val)
check_2.pack(pady=10)
check_3 = Checkbutton(root, text="Strawberry", fg="blue", bg="lightgrey", font=("Helvetica", 12), variable=check_3_val)
check_3.pack(pady=10)
button = Button(root, text="Submit", fg="blue", bg="lightgrey", font=("Helvetica", 14), command=display)
button.pack(pady=10)
lab = Label(root)
lab.pack()
root.mainloop()