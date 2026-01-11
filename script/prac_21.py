from tkinter import *

class Demo:

    def __init__(self,rootone):
        self.frame = Frame(rootone, bg="lightyellow", width=300, height=200, highlightbackground="black", highlightthickness=1)
        self.frame.pack(padx=10, pady=10)

        self.button_1 = Button(self.frame, text="Click Me", command=self.on_click)
        self.button_1.pack(pady=20)

        self.button_2 = Button(self.frame, text="Exit", command=rootone.quit)
        self.button_2.pack(pady=20)

    def on_click(self):
        print("Button clicked!")

root = Tk()
demo = Demo(root)
root.title("Class Example")
root.geometry("400x300")
root.mainloop()