from tkinter import *

root = Tk()

btm = Button(root, text='Click me', activebackground='red')
btm1 = Button(root, text='Click me', activebackground='blue')
btm2 = Button(root, text='Click me',activebackground='green')
btm3 = Button(root, text='Click me',activebackground='orange')
btm4 = Button(root, text='Click me',activebackground='yellow')

btm.grid(row=0, column=0)
btm1.grid(row=0, column=1)
btm2.grid(row=0, column=2)
btm3.grid(row=0, column=3)
btm4.grid(row=0, column=4)


root.mainloop()