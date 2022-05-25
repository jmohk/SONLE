from tkinter import *
import sympy as sp

def close():
    jac.destroy()

def jacobian(funF, funG, x_node, y_node):
    F = sp.sympify(funF)
    G = sp.sympify(funG)
    x = sp.Symbol('x')
    y = sp.Symbol('y')
    yo = float(x_node)
    xo = float(y_node)
    fx = sp.diff(funF, x)
    fy = sp.diff(funF, y)
    gx = sp.diff(funG, x)
    gy = sp.diff(funG, y)
    m0 = sp.Matrix([[xo], [yo]])
    mj = sp.Matrix([[fx.subs(x, xo).subs(y, yo), fy.subs(y, yo).subs(x, xo)], [gx.subs(x, xo).subs(y, yo),
                                                                               gy.subs(y, yo).subs(x, xo)]])
    mfun = sp.Matrix([[(F.subs(x, xo).subs(y, yo))], [G.subs(x, xo).subs(y, xo)]])
    det = mj.det()
    mji= (1/det)*(sp.Matrix([[gy.subs(x, xo).subs(y, yo), -fy.subs(x, xo).subs(y, yo)], [-gx.subs(x, xo).subs(y, yo),
                                                                                         fx.subs(x, xo).subs(y, yo)]]))
    r = sp.Matrix(m0 - mji * mfun)
    xr.config(state="normal")
    xr.insert(INSERT, r[0, 0])
    xr.config(state="disabled")
    yr.config(state="normal")
    yr.insert(INSERT, r[1, 0])
    yr.config(state="disabled")

jac = Tk()
jac.title("Jacobian")
jac.iconbitmap('D:/Projects/Solution Of Non-Linear Equation/Python/SONLE/Photos/calculation_icon.ico')
jac.geometry('900x500+300+150')
jac.maxsize(900, 500)
jac.minsize(900, 500)
jac.configure(bg='#2D2D2D')
jac.overrideredirect(False)

Label(jac, text="Jacobian Method", fg="white", bg='#2D2D2D', font=('Times New Roman', 40)).pack(pady=5)
Label(text="F(x)=", fg="white", bg='#2D2D2D', font=('Courier', 25)).place(x=150, y=75)
fun_x = Text(master=jac, height=1, width=25, bg='#595959', fg="white", font=('Courier', 25))
fun_x.place(x=270, y=75)
Label(text="G(x)=", fg="white", bg='#2D2D2D', font=('Courier', 25)).place(x=150, y=125)
fun_g = Text(master=jac, height=1, width=25, bg='#595959', fg="white", font=('Courier', 25))
fun_g.place(x=270, y=125)
Label(text="X0=", fg="white", bg='#2D2D2D', font=('Courier', 25)).place(x=225, y=175)
xnode = Text(master=jac, height=1, width=8, bg='#595959', fg="white", font=('Courier', 25))
xnode.place(x=300, y=175)
Label(text="Y0=", fg="white", bg='#2D2D2D', font=('Courier', 25)).place(x=500, y=175)
ynode = Text(master=jac, height=1, width=8, bg='#595959', fg="white", font=('Courier', 25))
ynode.place(x=575, y=175)
Label(jac, text="X ≈ ", fg="white", bg='#2D2D2D', font=('Courier', 25)).place(x=300, y=250)
Label(jac, text="Y ≈ ", fg="white", bg='#2D2D2D', font=('Courier', 25)).place(x=300, y=300)
xr = Text(height=1, width=10, bg='#595959', fg="white", font=('Courier', 25), state="disabled")
xr.place(x=400, y=250)
yr = Text(height=1, width=10, bg='#595959', fg="white", font=('Courier', 25), state="disabled")
yr.place(x=400, y=300)
b1 = Button(state=NORMAL, text="Clear", height=1, command=lambda: [fun_x.delete(1.0, END), fun_g.delete(1.0, END),
                                                                   xr.config(state="normal"), xr.delete(1.0, END),
                                                                   xr.config(state="disabled"),
                                                                   yr.config(state="normal"), yr.delete(1.0, END),
                                                                   yr.config(state="disabled"), xnode.delete(1.0, END),
                                                                   ynode.delete(1.0, END)],
            width=15, fg='#000000', bg='#676767', font="arial")
b1.place(x=250, y=350)
Button(text="Solve", height=1, width=15, fg='#000000', command=lambda: jacobian(fun_x.get(1.0, END),
                                                                                fun_g.get(1.0, END), xnode.get(1.0, END)
                                                                                , ynode.get(1.0, END)),
       bg='#676767', font="arial").place(x=510, y=350)
Button(text="Close", command=lambda: close(), height=1, width=15, fg='#000000', bg='#676767',
       font="arial").place(x=375, y=420)
