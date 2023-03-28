import tkinter
from tkinter import ttk

def clean():
    entry1.delete(0, tkinter.END)
    entry2.delete(0, tkinter.END)
    entry3.delete(0, tkinter.END)
    entry4.delete(0, tkinter.END)

def enter_data():
    Id = entry1.get()
    Weight = entry2.get()
    Destination = entry3.get()
    Weather = entry4.get()

    print("Id: ", Id, "Weight: ", Weight, "Destination: ", Destination, "Weather: ", Weather)

window = tkinter.Tk()
window.title("Data Entry")

frame = tkinter.Frame(window)
frame.pack()

user_info = tkinter.LabelFrame(frame, text="Container")
user_info.grid(row=0, column=0, padx=30, pady=30)

label1 = tkinter.Label(user_info, text="Id")
label1.grid(row=0, column=0)

label2 = tkinter.Label(user_info, text="Weight")
label2.grid(row=0, column=1)

label3 = tkinter.Label(user_info, text="Destination")
label3.grid(row=0, column=2)

label4 = tkinter.Label(user_info, text="Weather")
label4.grid(row=0, column=3)

entry1 = tkinter.Entry(user_info)
entry1.grid(row=1, column=0)

entry2 = tkinter.Spinbox(user_info, from_=0, to=5000)
entry2.grid(row=1, column=1)

entry3 = tkinter.ttk.Combobox(user_info, values=["Ohio", "Brazil", "Simons mor"])
entry3.grid(row=1, column=2)

entry4 = tkinter.Entry(user_info)
entry4.grid(row=1, column=3)

button1 = tkinter.Button(user_info, text="Create", command=enter_data)
button1.grid(row=2, column=0)
button1.config(font=('Monospace',10))

button2 = tkinter.Button(user_info, text="Update")
button2.grid(row=2, column=1)
button2.config(font=('Monospace',10))

button3 = tkinter.Button(user_info, text="Delete")
button3.grid(row=2, column=2)
button3.config(font=('Monospace',10))

button4 = tkinter.Button(user_info, text="Clear Entry Boxes", command=clean)
button4.grid(row=2, column=3)
button4.config(font=('Monospace',10))

for widget in user_info.winfo_children():
    widget.grid_configure(padx=10, pady=5)

window.mainloop()