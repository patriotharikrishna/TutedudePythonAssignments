from tkinter import *

window = Tk()
window.geometry('500x500')
window.title('Calculator')

def click(num):
    current = e.get()
    e.delete(0, END)
    e.insert(END, str(current) + str(num))

def clear():
    e.delete(0, END)

def calculate():
    try:
        expression = e.get()
        result = eval(expression)
        e.delete(0, END)
        e.insert(END, str(result))
    except:
        e.delete(0, END)
        e.insert(END, "Error")

e = Entry(window, width=50, borderwidth=5)
e.place(x=10, y=10)

b1 = Button(window, text='1', width=12, bg='light sky blue', command=lambda: click('1'))
b1.place(x=10, y=60)

b2 = Button(window, text='2', width=12, bg='light sky blue', command=lambda: click('2'))
b2.place(x=120, y=60)

b3 = Button(window, text='3', width=12, bg='light sky blue', command=lambda: click('3'))
b3.place(x=230, y=60)

b4 = Button(window, text='4', width=12, bg='light sky blue', command=lambda: click('4'))
b4.place(x=10, y=100)

b5 = Button(window, text='5', width=12, bg='light sky blue', command=lambda: click('5'))
b5.place(x=120, y=100)

b6 = Button(window, text='6', width=12, bg='light sky blue', command=lambda: click('6'))
b6.place(x=230, y=100)

b7 = Button(window, text='7', width=12, bg='light sky blue', command=lambda: click('7'))
b7.place(x=10, y=140)

b8 = Button(window, text='8', width=12, bg='light sky blue', command=lambda: click('8'))
b8.place(x=120, y=140)

b9 = Button(window, text='9', width=12, bg='light sky blue', command=lambda: click('9'))
b9.place(x=230, y=140)

b0 = Button(window, text='0', width=12, bg='light sky blue', command=lambda: click('0'))
b0.place(x=120, y=180)

b_add = Button(window, text='+', width=12, command=lambda: click('+'))
b_add.place(x=380, y=60)

b_sub = Button(window, text='-', width=12, command=lambda: click('-'))
b_sub.place(x=380, y=100)

b_mult = Button(window, text='x ( * )', width=12, command=lambda: click('*'))
b_mult.place(x=380, y=140)

b_div = Button(window, text='/', width=12, command=lambda: click('/'))
b_div.place(x=380, y=180)

b_clear = Button(window, text='Clear', bg='red', width=12, command=clear)
b_clear.place(x=120, y=220)

b_equals = Button(window, text='=', width=12, bg='light green', command=calculate)
b_equals.place(x=380, y=220)

mainloop()