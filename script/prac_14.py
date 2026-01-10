from tkinter import *

def display():
    intput_text = entry.get()
    print(f"Input: {intput_text}")
root = Tk()
root.title("My First Tkinter App")
root.geometry("300x200")
entry = Entry(root, fg="black", bg="white", font=("Arial", 14))
entry.pack(pady=20)
button = Button(root, text="Submit", fg="blue", bg="lightgrey", font=("Helvetica", 14),command=display)
button.pack()
root.mainloop()