from tkinter import*

window = Tk()
window.geometry('1000x700')
window.config(bg='#ededed')
window.title("My Second GUI")

l1 = Label(window, text="Id")
l1.pack()
l1.grid(row=0, column=0)
l1.config(font=('Monospace', 15))
l1.config(padx=30)
l1.config(pady=20)

l2 = Label(window, text="Weight")
l2.grid(row=0, column=1)
l2.config(font=('Monospace', 15))
l2.config(padx=70)

l3 = Label(window, text="Destination")
l3.grid(row=0, column=2)
l3.config(font=('Monospace', 15))
l3.config(padx=70)

l4 = Label(window, text="Weather")
l4.grid(row=0, column=3)
l4.config(font=('Monospace', 15))
l4.config(padx=80)

e1 = Entry(window, width=4)
e1.grid(row=1, column=0)
e1.config(font=('Monospace', 20))

e2 = Entry(window, width=9)
e2.grid(row=1, column=1)
e2.config(font=('Monospace', 20))

e3 = Entry(window, width=15)
e3.grid(row=1, column=2)
e3.config(font=('Monospace', 20))

e4 = Entry(window, width=11)
e4.grid(row=1, column=3)
e4.config(font=('Monospace', 20))

b1 = Button(window, text="Create")
b1.grid(row=2, column=0)
b1.config(font=('Monospace', 17))

b2 = Button(window, text="Update")
b2.grid(row=2, column=1)
b2.config(font=('Monospace', 17))

b3 = Button(window, text="Delete")
b3.grid(row=2, column=2)
b3.config(font=('Monospace', 17))

b4 = Button(window, text="Clear Entry Boxes")
b4.grid(row=2, column=3)
b4.config(font=('Monospace', 17))

window.mainloop()
