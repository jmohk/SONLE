from tkinter import *

def back():
    about.destroy()
    import loading

about = Tk()
about.title("About")
about.iconbitmap('D:/Projects/Solution Of Non-Linear Equation/Python/SONLE/Photos/calculation_icon.ico')
about.geometry('900x500+300+150')
about.maxsize(900, 500)
about.minsize(900, 500)
about.configure(bg='#2D2D2D')
Label(about, text="Solution Of Non-Linear Equation",
      fg="white", bg="#2D2D2D", font=('Times New Roman', 40)).pack(pady=20)
about.overrideredirect(False)
Label(about, text='This application is developed by:                                                                                                                                  ',
      font=('Helvetica', 10), fg='white', bg='#2D2D2D').pack(pady=20)
Label(about, text='⬤ Yousef Mohamed Abdelkhalek ( 202016394 )',
      font=('Helvetica', 10), fg='white', bg='#2D2D2D').pack(pady=3)
Label(about, text='⬤ Yousef Ashraf Fathy ( 202112187 )',
      font=('Helvetica', 10), fg='white', bg='#2D2D2D').pack(pady=3)
Label(about, text='⬤ Yousef Mohamed Morsy ( 202119783 )',
      font=('Helvetica', 10), fg='white', bg='#2D2D2D').pack(pady=3)
Label(about, text='⬤ Yousef Yaser Antar ( 202123751 )',
      font=('Helvetica', 10), fg='white', bg='#2D2D2D').pack(pady=3)
Label(about, text='This project was developed under the supervision of Dr. Mohamed Abdel Sattar',
      font=('Helvetica', 17), fg='white', bg='#2D2D2D').pack(pady=20)
Button(text="Back", command=back, height=2, width=30, fg='#000000', bg='#676767', font="arial").pack(pady=20)
