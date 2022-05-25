from tkinter import *

def back():
    main.destroy()
    import loading

def bisectionWin():
    main.destroy()
    import bisection

def newtonWin():
    main.destroy()
    import newton

def jacobianWin():
    main.destroy()
    import jacobian

main = Tk()
main.title("Solution Of Non-Linear Equation")
main.iconbitmap('D:/Projects/Solution Of Non-Linear Equation/Python/SONLE/Photos/calculation_icon.ico')
main.geometry('900x500+300+150')
main.maxsize(900, 500)
main.minsize(900, 500)
main.configure(bg='#2D2D2D')
main.overrideredirect(False)
Button(text="Bisection", command=bisectionWin, height=2, width=30, fg='#000000', bg='#676767', font="arial").pack(pady=30)
Button(text="Newton", command=newtonWin, height=2, width=30, fg='#000000', bg='#676767', font="arial").pack(pady=30)
Button(text="Jacobin", command=jacobianWin, height=2, width=30, fg='#000000', bg='#676767', font="arial").pack(pady=30)
Button(text="Back", command=back, height=2, width=15, fg='#000000', bg='#676767', font="arial").pack(pady=30)
