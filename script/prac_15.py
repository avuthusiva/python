from tkinter import *

def add_numbers():
    num1 = int(entry_1.get())
    num2 = int(entry_2.get())
    result = str(num1 + num2)
    entry_ans.config(text="Result: " + result)
    
root = Tk()
root.title("Adding numbers GUI")
root.geometry("300x250")
entry_1 = Entry(root, fg="black", bg="white", font=("Arial", 14))
entry_1.pack(pady=10)
entry_2 = Entry(root, fg="black", bg="white", font=("Arial", 14))
entry_2.pack(pady=10)
button = Button(root, text="Add", fg="blue", bg="lightgrey", font=("Helvetica", 14),command=add_numbers)
button.pack(pady=10)
entry_ans = Label(root)
entry_ans.pack()
root.mainloop()