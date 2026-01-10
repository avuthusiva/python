from tkinter import *

root = Tk()
root.title("Frame Example")
root.geometry("600x400")
frame_1 = Frame(root, bg="lightblue", width=150, height=200,highlightbackground="black", highlightthickness=1)
frame_1.pack(side=LEFT, fill=Y,padx=5,pady=5)
frame_2 = Frame(root, bg="lightgreen", width=150, height=200,highlightbackground="black", highlightthickness=1)
frame_2.pack(side=RIGHT, fill=Y,padx=5,pady=5)
buttion_1 = Button(frame_1, text="Button 1 in Frame 1")
buttion_1.pack(pady=20)
buttion_2 = Button(frame_2, text="Button 2 in Frame 2")
buttion_2.pack(pady=20)
root.mainloop()