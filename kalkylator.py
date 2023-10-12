from tkinter import *

root = Tk()

root.title('Калькурятор')
entry_ = Entry(root, width=40, borderwidth=10,)
entry_.grid(row=0, column=0, columnspan=3, padx=30, pady=15)

tmp = None

def sum_e():
    global tmp
    if tmp == None:
        tmp = entry_.get()
        entry_.delete(0, END)
    else:
        current = entry_.get()
        entry_.delete(0, END)
        entry_.insert(0, int(tmp) + int(current))
        tmp = None

def sub_e():
    global tmp
    if tmp == None:
        tmp = entry_.get()
        entry_.delete(0, END)
    else:
        current = entry_.get()
        entry_.delete(0, END)
        entry_.insert(0, int(tmp) - int(current))
        tmp = None

def equal():
    global tmp
    current = entry_.get()
    entry_.delete(0, END)
    entry_.insert(0, int(tmp) + int(current))
    tmp = None

def click_handler(x):
    assert type(x) == int
    current = entry_.get()
    entry_.delete(0, END)
    entry_.insert(0, str(current) + str(x))

def clr():
    global tmp
    tmp = None
    entry_.delete(0, END)

button_1 = Button(root, text = '1', pady = 10, command = lambda: click_handler(1))
button_2 = Button(root, text = '2', pady = 10, command = lambda: click_handler(2))
button_3 = Button(root, text = '3', pady = 10, command = lambda: click_handler(3))
button_4 = Button(root, text = '4', pady = 10, command = lambda: click_handler(4))
button_5 = Button(root, text = '5', pady = 10, command = lambda: click_handler(5))
button_6 = Button(root, text = '6', pady = 10, command = lambda: click_handler(6))
button_7 = Button(root, text = '7', pady = 10, command = lambda: click_handler(7))
button_8 = Button(root, text = '8', pady = 10, command = lambda: click_handler(8))
button_9 = Button(root, text = '9', pady = 10, command = lambda: click_handler(9))
button_0 = Button(root, text = '0', pady = 10, command = lambda: click_handler(0))
button_add = Button(root, text = '+', pady = 10, command = sum_e)
button_sub = Button(root, text = '-', pady = 10, command = sub_e)
button_equal = Button(root, text = '=', pady = 10, command = equal)
button_clear = Button(root, text = 'Clear', pady = 10, command = clr)

button_1.grid(row = 1, column = 0, sticky='we')
button_2.grid(row = 1, column = 1, sticky='we')
button_3.grid(row = 1, column = 2, sticky='we')
button_4.grid(row = 2, column = 0, sticky='we')
button_5.grid(row = 2, column = 1, sticky='we')
button_6.grid(row = 2, column = 2, sticky='we')
button_7.grid(row = 3, column = 0, sticky='we')
button_8.grid(row = 3, column = 1, sticky='we')
button_9.grid(row = 3, column = 2, sticky='we')
button_0.grid(row = 4, column = 0, sticky='we')
button_add.grid(row = 5, column = 0, sticky='we')
button_sub.grid(row = 5, column = 1, sticky='we')
button_equal.grid(row = 5, column = 2,sticky = 'we')
button_clear.grid(row = 4, column = 1, columnspan = 2,sticky = 'we')

root.mainloop()