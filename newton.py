from tkinter import *
import sympy as sp

def close():
    new.destroy()

def compare2floats(x, y, zo):
    n = int(zo)
    flag = False
    xs = str(x)
    ys = str(y)
    # print(ys + " " + xs)
    startIndex = xs.find('.') + n
    if len(xs) < startIndex + n or len(ys) < startIndex + n:
        return True
    temp = startIndex
    while temp >= 0:
        c1 = xs[temp]
        c2 = ys[temp]
        #   print(c1 + " " + c2)
        temp -= 1
        if c1 != c2:
            return True
    return flag

def newton(user_func, n):
    fun = sp.sympify(user_func)
    x = sp.Symbol('x')
    f1 = sp.diff(fun, x)
    f2 = sp.diff(f1, x)
    xn = 1
    while (fun.subs(x, xn) * f2.subs(x, xn)) / f1.subs(x, xn) ** 2 > 1 and f1.subs(x, xn) == 0:
        xn += 1
        if xn == 100:
            return None
    xn1 = xn - (fun.subs(x, xn) / f1.subs(x, xn))
    while compare2floats(xn, xn1, n):
        xn = xn1
        xn1 = (xn - (fun.subs(x, xn) / f1.subs(x, xn))).evalf()
    t1.config(state="normal")
    t1.insert(INSERT, xn1)
    t1.config(state="disabled")

new = Tk()
new.title("Newton")
new.iconbitmap('D:/Projects/Solution Of Non-Linear Equation/Python/SONLE/Photos/calculation_icon.ico')
new.geometry('900x500+300+150')
new.maxsize(900, 500)
new.minsize(900, 500)
new.configure(bg='#2D2D2D')
new.overrideredirect(False)

Label(new, text="Newton Method", fg="white", bg='#2D2D2D', font=('Times New Roman', 40)).pack(pady=5)
Label(text="F(x)=", fg="white", bg='#2D2D2D', font=('Courier', 25)).place(x=150, y=75)
function = Text(master=new, height=1, width=25, bg='#595959', fg="white", font=('Courier', 25))
function.place(x=270, y=75)
Label(text="approximate ", fg="white", bg='#2D2D2D', font=('Courier', 25)).place(x=225, y=150)
appr = Text(new, state=NORMAL, height=1, width=2, bg='#595959', fg="white", font=('Courier', 25))
appr.place(x=500, y=150)
Label(text="X ≈  ", fg="white", bg='#2D2D2D', font=('Courier', 25)).place(x=325, y=225)
t1 = Text(height=1, width=10, bg='#595959', fg="white", font=('Courier', 25), state="disabled")
t1.place(x=425, y=225)
b1 = Button(state=NORMAL, text="Clear", height=1, command=lambda: [appr.delete(1.0, END), function.delete(1.0, END),
                                                                   t1.config(state="normal"), t1.delete(1.0, END),
                                                                   t1.config(state="disabled")],
            width=15, fg='#000000', bg='#676767', font="arial")
b1.place(x=250, y=350)
Button(text="Solve", height=1, width=15, fg='#000000', command=lambda: newton(function.get(1.0, END),
                                                                              appr.get(1.0, END)),
       bg='#676767', font="arial").place(x=510, y=350)
Button(text="Close", command=lambda: close(), height=1, width=15, fg='#000000', bg='#676767',
       font="arial").place(x=375, y=420)
