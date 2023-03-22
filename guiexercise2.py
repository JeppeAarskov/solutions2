from tkinter import*

window = Tk()
window.geometry('1000x700')
window.config(bg='#ededed')
window.title("My Second GUI")

l1 = Label(window, text="Id")
l1.pack()
l1.grid(row=0, column=0)
l1.config(font=('Monospace', 20))

l2 = Label(window, text="Weight")
l2.grid(row=0, column=1)
l2.config(font=('Monospace', 20))

l3 = Label(window, text="Destination")
l3.grid(row=0, column=2)
l3.config(font=('Monospace',20))

l4 =

window.mainloop()
