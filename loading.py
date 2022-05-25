from tkinter import *

def mainWin():
    loading.destroy()
    import main

def aboutWin():
    loading.destroy()
    import about

loading = Tk()
loading.title("Solution Of Non-Linear Equation")
loading.iconbitmap('D:/Projects/Solution Of Non-Linear Equation/Python/SONLE/Photos/calculation_icon.ico')
loading.geometry('900x500+300+150')
loading.maxsize(900, 500)
loading.minsize(900, 500)
loading.configure(bg='#2D2D2D')
loading.overrideredirect(False)
Label(loading, text="Solution Of Non-Linear Equation",
      fg="white", bg='#2D2D2D', font=('Times New Roman', 40)).pack(pady=30)
Button(text="Start", command=mainWin, height=2, width=30, fg='#000000', bg='#676767', font="arial").pack(pady=20)
Button(text="About", command=aboutWin, height=2, width=30, fg='#000000', bg='#676767', font="arial").pack(pady=20)
Button(text="Exit", command=loading.destroy, height=2, width=30, fg='#000000', bg='#676767', font="arial").pack(pady=20)
loading.mainloop()
