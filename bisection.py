from tkinter import *
import numpy as np
import sympy as sp

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
        temp -= 1
        if c1 != c2:
            return True
    return flag

def bisection(user_func, a, b, n):
    fun = sp.sympify(user_func)
    x = sp.Symbol('x')
    a = float(a)
    b = float(b)
    fa = fun.subs(x, a)
    fb = fun.subs(x, b)
    c = (a + b) / 2
    fc = fun.subs(x, c)
    if (fa * fb) > 0:
        import bierror
        return None
    while compare2floats(c, a, n) or compare2floats(c, b, n):
        if np.sign(fc) == np.sign(fa):
            fa = fc
            a = c
            c = (a + b) / 2
            fc = fun.subs(x, c)
        if np.sign(fc) == np.sign(fb):
            fb = fc
            b = c
            c = (a + b) / 2
            fc = fun.subs(x, c)
    t1.config(state="normal")
    t1.insert(INSERT, c)
    t1.config(state="disabled")

def close():
    bi.destroy()

bi = Tk()
bi.title("Bisection")
bi.iconbitmap('D:/Projects/Solution Of Non-Linear Equation/Python/SONLE/Photos/calculation_icon.ico')
bi.geometry('900x500+300+150')
bi.maxsize(900, 500)
bi.minsize(900, 500)
bi.configure(bg='#2D2D2D')
bi.overrideredirect(False)

Label(bi, text="Bisection Method", fg="white", bg='#2D2D2D', font=('Times New Roman', 40)).pack(pady=5)
Label(text="F(x)=", fg="white", bg='#2D2D2D', font=('Courier', 25)).place(x=150, y=75)
function = Text(master=bi, height=1, width=25, bg='#595959', fg="white", font=('Courier', 25))
function.place(x=270, y=75)
Label(text="Interval ", fg="white", bg='#2D2D2D', font=('Courier', 25)).place(x=225, y=150)
int1 = Text(bi, state=NORMAL, height=1, width=4, bg='#595959', fg="white", font=('Courier', 25))
int1.place(x=425, y=150)
int2 = Text(height=1, width=4, bg='#595959', fg="white", font=('Courier', 25))
int2.place(x=550, y=150)
Label(text="Approximate ", fg="white", bg='#2D2D2D', font=('Courier', 25)).place(x=225, y=200)
appr = Text(bi, state=NORMAL, height=1, width=4, bg='#595959', fg="white", font=('Courier', 25))
appr.place(x=485, y=200)
Label(text="X ≈  ", fg="white", bg='#2D2D2D', font=('Courier', 25)).place(x=325, y=265)
t1 = Text(height=1, width=10, bg='#595959', fg="white", font=('Courier', 25), state=DISABLED)
t1.place(x=425, y=265)
b1 = Button(state=NORMAL, text="Clear", height=1, command=lambda: [int1.delete(1.0, END), function.delete(1.0, END),
                                                                   int2.delete(1.0, END), appr.delete(1.0, END),
                                                                   t1.config(state="normal"), t1.delete(1.0, END),
                                                                   t1.config(state="disabled")],
            width=15, fg='#000000', bg='#676767', font="arial")
b1.place(x=250, y=350)
Button(text="Solve", command=lambda: bisection(function.get(1.0, END), int1.get(1.0, END), int2.get(1.0, END),
                                               appr.get(1.0, END)),
       height=1, width=15, fg='#000000', bg='#676767', font="arial").place(x=510, y=350)
Button(text="Close", command=lambda: close(), height=1, width=15, fg='#000000', bg='#676767',
       font="arial").place(x=375, y=420)
