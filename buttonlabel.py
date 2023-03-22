from tkinter import*

window = Tk()
window.geometry('700x800')
window.config(bg='#2aa8ff')

def buttonfunction():
    print("Subscribe til MrMasterTop1")

def exitfunction():
    exit()

def click(event):
    entry.config(state=NORMAL)
    entry.delete(0, END)

b = Button(window, text="Du tør ikke klikke", command=buttonfunction)
b.pack()
b.pack(pady=(200,20))
b.config(font=('Monospace',30,'bold'))
b.config(bg='#3fffd3')
b.config(fg='white')
b.config(activebackground='white')
b.config(activeforeground='#3fffd3')

b2 = Button(window, text="Klik for gratis bobux", command=exitfunction)
b2.pack()
b2.pack(pady=(60,0))
b2.config(font=('Monospace',30,'bold'))
b2.config(activebackground='black')
b2.config(activeforeground='white')

entry = Entry(window)
entry.pack()
entry.pack(pady=(100,0))
entry.config(font=('Monospace', 30,))
entry.insert(0, "Skriv for faen")
entry.config(state=DISABLED)
entry.bind("<Button-1>", click)
window.mainloop()