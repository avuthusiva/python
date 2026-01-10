from tkinter import *

def check_display():
    check_lab.config(text=f"Checkbox is {'checked' if check_val.get() else 'unchecked'}")

root = Tk()
root.title("Check box Example")
root.geometry("300x200")
check_val = BooleanVar()
check_but = Checkbutton(root, text="I agree to the terms and conditions", fg="blue", bg="lightgrey", 
                        font=("Helvetica", 12), variable=check_val,command=check_display)
check_but.pack(pady=40)
check_lab = Label(root)
check_lab.pack()
root.mainloop()