from tkinter import*
import tkinter

window = Tk()
window.geometry('350x450')
window.config(bg='#ededed')
window.title("My First GUI")

frame_1 = tkinter.LabelFrame(window, text="Container")
frame_1.grid(row=0, column=0, padx=25, pady=20)
frame_1.config(font=('Monospace',20))
frame_1.config(pady=(60))
frame_1.config(padx=(90))

label_1 = Label(frame_1, text="Id")
label_1.pack(pady=(0,90))
label_1.config(font=('Monospace',30))

e1 = Entry(frame_1, width=5)
e1.pack(pady=(50,0))
e1.config(font=('Monospace',30))

button = Button(window, text="Create")
button.grid(row=0, column=0, pady=50, padx=0)
button.config(font=('Monospace',25))
button.config(bg='#dbdbdb')

window.mainloop()