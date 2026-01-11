from tkinter import *

def get_input():
    val1 = entry.get()
    print(f"Input value: {val1}")
    entry.delete(0, END)

root = Tk()
root.title("Calculator App")
root.geometry("400x500")
entry = Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='ridge', justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
cnt = 1
for i in range(3):
    for j in range(3):
        button = Button(root, text=str(cnt), width=5, height=2, font=('Arial', 18),
                        command=lambda x=cnt: entry.insert(END, str(x)))
        button.grid(row=i+1, column=j, padx=5, pady=5)
        cnt += 1
button_zero = Button(root, text='0', width=5, height=2, font=('Arial', 18),
                     command=lambda: entry.insert(END, '0'))
button_zero.grid(row=4, column=1, padx=5, pady=5)
dot_button = Button(root, text='.', width=5, height=2, font=('Arial', 18),
                    command=lambda: entry.insert(END, '.'))
dot_button.grid(row=4, column=0, padx=5, pady=5)
equal_button = Button(root, text='=', width=5, height=2, font=('Arial', 18),
                      command=get_input)
equal_button.grid(row=4, column=2, padx=5, pady=5)
symbols = ['+', '-', '*', '/']
for i, symbol in enumerate(symbols):
    button = Button(root, text=symbol, width=5, height=2, font=('Arial', 18),
                    command=lambda x=symbol: entry.insert(END, x))
    button.grid(row=i+1, column=3, padx=5, pady=5)

root.mainloop()