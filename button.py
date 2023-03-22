from tkinter import *
count = 0

def click():
    global count
    count+=1
    label.config(text=count)

window = Tk()
window.geometry("650x600")
window.config(bg="#acf2ff")
button = Button(window,text="Klik hvis du er fuld traktor")
button.pack()
button.pack(pady=(200,20))
button.config(command=click)
button.config(font=('Sans',30,'bold'))
button.config(bg='#5999ff')
button.config(fg='white')
button.config(activeforeground='#5999ff')
button.config(compound='bottom')
button.config(pady=10)
button.config(padx=30)

label = Label(window,text=count)
label.pack()
label.config(font=('Monospace',40))
label.config(bg="#acf2ff")
label.config(fg="blue")
window.mainloop()