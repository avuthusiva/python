from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Message Box Example")
root.geometry("400x300")
messagebox.showerror("Error", "This is an error message box")
messagebox.showinfo("Information", "This is an information message box")
messagebox.showwarning("Warning", "This is a warning message box")
ans = messagebox.askquestion("Question", "Do you like Python?")
print("User's answer to the question:", ans)
if ans == 'yes':
    messagebox.showinfo("Response", "Great! Python is awesome.")
else:
    messagebox.showinfo("Response", "Oh no! Maybe give it another try.")
messagebox.askokcancel("Confirmation", "Do you want to proceed?")

root.mainloop()