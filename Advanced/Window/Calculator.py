from tkinter import Tk, Entry, Button, StringVar, ttk
calc = Tk()
op = ''
s = StringVar()

def btnClick(btn):
    global op
    op = op + btn
    if op.find('0') == 0:
        op = op[1:]
    s.set(op)

def equal():
    global op
    try:
        s.set(eval(op))
        op = ''
    except SyntaxError:
        s.set('Error')

def clear():
    global op
    s.set('')
    op = ''

calc.title('Calculator')
calc.geometry('310x250')
x = int((calc.winfo_screenwidth()-150)/2)
y = int((calc.winfo_screenheight()-200)/2)
calc.geometry(f'+{x}+{y}')

entry1 = Entry(calc, textvariable = s, justify = 'right', font = ('arial', 20, 'bold'), borderwidth = 3 )
entry1.grid(columnspan = 4)

btn7 = Button(calc, text = '7', command = lambda : btnClick('7'), padx = 7, font = ('arial', 14, 'bold'), borderwidth = 3)
btn7.grid(column = 0 , row = 1)

btn8 = Button(calc, text = '8', command = lambda : btnClick('8'), padx = 7, font = ('arial', 14, 'bold'), borderwidth = 3)
btn8.grid(column = 1 , row = 1)

btn9 = Button(calc, text = '9', command = lambda : btnClick('9'), padx = 7, font = ('arial', 14, 'bold'), borderwidth = 3)
btn9.grid(column = 2 , row = 1)

btnAdd = Button(calc, text = '+', command = lambda : btnClick('+'), padx = 7, font = ('arial', 14, 'bold'), borderwidth = 3)
btnAdd.grid(column = 3 , row = 1)
#..............................................................................................................................
btn4 = Button(calc, text = '4', command = lambda : btnClick('4'), padx = 7, font = ('arial', 14, 'bold'), borderwidth = 3)
btn4.grid(column = 0 , row = 2)

btn5 = Button(calc, text = '5', command = lambda : btnClick('5'), padx = 7, font = ('arial', 14, 'bold'), borderwidth = 3)
btn5.grid(column = 1 , row = 2)

btn6 = Button(calc, text = '6', command = lambda : btnClick('6'), padx = 7, font = ('arial', 14, 'bold'), borderwidth = 3)
btn6.grid(column = 2 , row = 2)

btnSub = Button(calc, text = '-', command = lambda : btnClick('-'), padx = 7, font = ('arial', 14, 'bold'), borderwidth = 3)
btnSub.grid(column = 3 , row = 2)
#..............................................................................................................................
btn1 = Button(calc, text = '1', command = lambda : btnClick('1'), padx = 7, font = ('arial', 14, 'bold'), borderwidth = 3)
btn1.grid(column = 0 , row = 3)

btn2 = Button(calc, text = '2', command = lambda : btnClick('2'), padx = 7, font = ('arial', 14, 'bold'), borderwidth = 3)
btn2.grid(column = 1 , row = 3)

btn3 = Button(calc, text = '3', command = lambda : btnClick('3'), padx = 7, font = ('arial', 14, 'bold'), borderwidth = 3)
btn3.grid(column = 2 , row = 3)

btnMul = Button(calc, text = 'x', command = lambda : btnClick('x'), padx = 7, font = ('arial', 14, 'bold'), borderwidth = 3)
btnMul.grid(column = 3 , row = 3)
#..............................................................................................................................
btnClear = Button(calc, text = 'C', command = clear, padx = 7, font = ('arial', 14, 'bold'), borderwidth = 3)
btnClear.grid(column = 0 , row = 4)

btn0 = Button(calc, text = '0', command = lambda : btnClick('0'), padx = 7, font = ('arial', 14, 'bold'), borderwidth = 3)
btn0.grid(column = 1 , row = 4)

btnEqual = Button(calc, text = '=', command = equal, padx = 7, font = ('arial', 14, 'bold'), borderwidth = 3)
btnEqual.grid(column = 2 , row = 4)

btnDiv = Button(calc, text = '/', command = lambda : btnClick('/'), padx = 7, font = ('arial', 14, 'bold'), borderwidth = 3)
btnDiv.grid(column = 3 , row = 4)

calc.mainloop()