from tkinter import *

def close():
    error.destroy()

error = Tk()
error.title("Error")
error.iconbitmap('D:/Projects/Solution Of Non-Linear Equation/Python/SONLE/Photos/calculation_icon.ico')
error.geometry('600x200+450+300')
error.maxsize(600, 200)
error.minsize(600, 200)
error.configure(bg='#2D2D2D')
error.overrideredirect(False)
Label(error, text="F(a) and F(b) must have different signs, please change the interval",
      fg="white", bg='#2D2D2D', font=('Times New Roman', 15)).pack(pady=30)
Button(error, text="Close", command=close, height=2, width=7, fg='#000000', bg='#676767', font="arial").pack(pady=10)
error.mainloop()
