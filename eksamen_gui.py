import tkinter as tk
from tkinter import ttk
import sqlite3
import eksamen_sql as sql

# region global constants
padx = 8  # Horizontal distance to neighboring objects
pady = 4  # Vertical distance to neighboring objects
rowheight = 24  # rowheight in treeview
treeview_background = "#eeeeee"  # color of background in treeview
treeview_foreground = "black"  # color of foreground in treeview
treeview_selected = "#206030"  # color of selected row in treeview
oddrow = "#dddddd"  # color of odd row in treeview
evenrow = "#cccccc"  # color of even row in treeview
INTERNAL_ERROR_CODE = 0


def enter_data1():  # collects data from the first frame
    Id = teams_entry1.get()
    Erfaring = teams_entry2.get()
    Størrelse = teams_entry3.get()

    print("Id: ", Id, "Erfaring: ", Erfaring, "Størrelse: ", Størrelse)

def enter_data2():  # collects data from the second frame
    Id = bane_entry1.get()
    Kapacitet = bane_entry2.get()
    Sværhedsgrad = bane_entry3.get()

    print("Id: ", Id, "Kapacitet: ", Kapacitet, "Sværhedsgrad: ", Sværhedsgrad)

def enter_data3():  # collects data from the third frame
    Id = booking_entry1.get()
    Dato = booking_entry2.get()
    Hold_id = booking_entry3.get()
    Bane_id = booking_entry4.get()

    print("Id: ", Id, "Dato: ", Dato, "Hold id: ", Hold_id, "Bane id: ", Bane_id)


def clean_text1():  # clears all entries in the first frame
    teams_entry1.delete(0, tk.END)
    teams_entry2.delete(0, tk.END)
    teams_entry3.delete(0, tk.END)


def clean_text2():  # clears all entries in the second frame
    bane_entry1.delete(0, tk.END)
    bane_entry2.delete(0, tk.END)
    bane_entry3.delete(0, tk.END)


def clean_text3():  # clears all entries in the third frame
    booking_entry1.delete(0, tk.END)
    booking_entry2.delete(0, tk.END)
    booking_entry3.delete(0, tk.END)
    booking_entry4.delete(0, tk.END)


conn = sqlite3.connect('eksamen_database.db')
table_create_query = '''CREATE TABLE IF NOT EXISTS TopBike_Data
    (id TEXT, erfaring TEXT, størrelse TEXT, kapacitet TEXT, sværhedsgrad TEXT, dato TEXT, holdid TEXT, baneid TEXT)
'''
conn.execute(table_create_query)
# Insert data

conn.close()

window = tk.Tk()
window.title("TopBike Booking")

frame = tk.Frame(window)
frame.pack()

teams_booking = tk.LabelFrame(frame, text="Hold")
teams_booking.grid(row=0, column=0, padx=10, pady=10)

bane_booking = tk.LabelFrame(frame, text="Bane")
bane_booking.grid(row=0, column=1, padx=10, pady=10)

full_booking = tk.LabelFrame(frame, text="Booking")
full_booking.grid(row=0, column=2, padx=10, pady=10)

teams_widgets = tk.Frame(teams_booking)
teams_widgets.grid(row=1, column=0)

bane_widgets = tk.Frame(bane_booking)
bane_widgets.grid(row=1, column=0)

booking_widgets = tk.Frame(full_booking)
booking_widgets.grid(row=1, column=0)

team_datalist = ttk.Treeview(teams_booking)
team_datalist['columns'] = ("Id", "Erfaring", "Størrelse")
team_datalist.grid(row=0, column=0)
team_datalist.column("#0", width=1)
team_datalist.column("Id", anchor=tk.E, width=40)  # "E" stands for East, meaning Right. Possible anchors are N, NE, E, SE, S, SW, W, NW and CENTER
team_datalist.column("Erfaring", anchor=tk.E, width=80)
team_datalist.column("Størrelse", anchor=tk.W, width=200)
team_datalist.heading("#0", text="", anchor=tk.W)  # Create column headings
team_datalist.heading("Id", text="Id", anchor=tk.CENTER)
team_datalist.heading("Erfaring", text="Weight", anchor=tk.CENTER)
team_datalist.heading("Størrelse", text="Destination", anchor=tk.CENTER)

bane_datalist = ttk.Treeview(bane_booking)
bane_datalist['columns'] = ("Id", "Kapacitet", "Sværhedsgrad")
bane_datalist.grid(row=0, column=0)
bane_datalist.column("#0", width=1)
bane_datalist.column("Id", anchor=tk.E, width=40)  # "E" stands for East, meaning Right. Possible anchors are N, NE, E, SE, S, SW, W, NW and CENTER
bane_datalist.column("Kapacitet", anchor=tk.E, width=80)
bane_datalist.column("Sværhedsgrad", anchor=tk.W, width=200)
bane_datalist.heading("#0", text="", anchor=tk.W)  # Create column headings
bane_datalist.heading("Id", text="Id", anchor=tk.CENTER)
bane_datalist.heading("Kapacitet", text="Kapacitet", anchor=tk.CENTER)
bane_datalist.heading("Sværhedsgrad", text="Sværhedsgrad", anchor=tk.CENTER)

booking_datalist = ttk.Treeview(full_booking)
booking_datalist['columns'] = ("Id", "Dato", "Hold id", "Bane id")
booking_datalist.grid(row=0, column=0)
booking_datalist.column("#0", width=1)
booking_datalist.column("Id", anchor=tk.E, width=40)  # "E" stands for East, meaning Right. Possible anchors are N, NE, E, SE, S, SW, W, NW and CENTER
booking_datalist.column("Dato", anchor=tk.E, width=80)
booking_datalist.column("Hold id", anchor=tk.W, width=80)
booking_datalist.column("Bane id", anchor=tk.W, width=100)
booking_datalist.heading("#0", text="", anchor=tk.W)  # Create column headings
booking_datalist.heading("Id", text="Id", anchor=tk.CENTER)
booking_datalist.heading("Dato", text="Dato", anchor=tk.CENTER)
booking_datalist.heading("Hold id", text="Hold id", anchor=tk.CENTER)
booking_datalist.heading("Bane id", text="Bane id", anchor=tk.CENTER)

teams_label1 = tk.Label(teams_widgets, text="Id", anchor=tk.W)
teams_label1.grid(row=0, column=0)

teams_label2 = tk.Label(teams_widgets, text="Erfaring", anchor=tk.W)
teams_label2.grid(row=0, column=1)

teams_label3 = tk.Label(teams_widgets, text="Størrelse", anchor=tk.W)
teams_label3.grid(row=0, column=2)

bane_label1 = tk.Label(bane_widgets, text="Id", anchor=tk.W)
bane_label1.grid(row=0, column=0)

bane_label2 = tk.Label(bane_widgets, text="Kapacitet", anchor=tk.W)
bane_label2.grid(row=0, column=1)

bane_label3 = tk.Label(bane_widgets, text="Sværhedsgrad", anchor=tk.W)
bane_label3.grid(row=0, column=2)

booking_label1 = tk.Label(booking_widgets, text="Id", anchor=tk.W)
booking_label1.grid(row=0, column=0)

booking_label2 = tk.Label(booking_widgets, text="Dato", anchor=tk.W)
booking_label2.grid(row=0, column=1)

booking_label3 = tk.Label(booking_widgets, text="Hold id", anchor=tk.W)
booking_label3.grid(row=0, column=2)

booking_label4 = tk.Label(booking_widgets, text="Bane id", anchor=tk.W)
booking_label4.grid(row=0, column=3)

teams_entry1 = tk.Entry(teams_widgets)
teams_entry1.grid(row=1, column=0)
teams_entry1.config(width=5)

teams_entry2 = tk.Entry(teams_widgets)
teams_entry2.grid(row=1, column=1)
teams_entry2.config(width=12)

teams_entry3 = tk.Entry(teams_widgets)
teams_entry3.grid(row=1, column=2)

bane_entry1 = tk.Entry(bane_widgets)
bane_entry1.grid(row=1, column=0)
bane_entry1.config(width=5)

bane_entry2 = tk.Entry(bane_widgets)
bane_entry2.grid(row=1, column=1)
bane_entry2.config(width=12)

bane_entry3 = tk.Entry(bane_widgets)
bane_entry3.grid(row=1, column=2)

booking_entry1 = tk.Entry(booking_widgets)
booking_entry1.grid(row=1, column=0)
booking_entry1.config(width=5)

booking_entry2 = tk.Entry(booking_widgets)
booking_entry2.grid(row=1, column=1)
booking_entry2.config(width=12)

booking_entry3 = tk.Entry(booking_widgets)
booking_entry3.grid(row=1, column=2)
booking_entry3.config(width=5)

booking_entry4 = tk.Entry(booking_widgets)
booking_entry4.grid(row=1, column=3)
booking_entry4.config(width=5)

teams_button1 = tk.Button(teams_widgets, text="Create", command=enter_data1)
teams_button1.grid(row=2, column=0)
teams_button1.config(font=('Monospace', 10))

teams_button2 = tk.Button(teams_widgets, text="Update")
teams_button2.grid(row=2, column=1)
teams_button2.config(font=('Monospace', 10))

teams_button3 = tk.Button(teams_widgets, text="Delete")
teams_button3.grid(row=2, column=2)
teams_button3.config(font=('Monospace', 10))

teams_button4 = tk.Button(teams_widgets, text="Clear Entry Boxes", command=clean_text1)
teams_button4.grid(row=2, column=3)
teams_button4.config(font=('Monospace', 10))

bane_button1 = tk.Button(bane_widgets, text="Create", command=enter_data2)
bane_button1.grid(row=2, column=0)
bane_button1.config(font=('Monospace', 10))

bane_button2 = tk.Button(bane_widgets, text="Update")
bane_button2.grid(row=2, column=1)
bane_button2.config(font=('Monospace', 10))

bane_button3 = tk.Button(bane_widgets, text="Delete")
bane_button3.grid(row=2, column=2)
bane_button3.config(font=('Monospace', 10))

bane_button4 = tk.Button(bane_widgets, text="Clear Entry Boxes", command=clean_text2)
bane_button4.grid(row=2, column=3)
bane_button4.config(font=('Monospace', 10))

booking_button1 = tk.Button(booking_widgets, text="Create", command=enter_data3)
booking_button1.grid(row=2, column=0)
booking_button1.config(font=('Monospace', 10))

booking_button2 = tk.Button(booking_widgets, text="Update")
booking_button2.grid(row=2, column=1)
booking_button2.config(font=('Monospace', 10))

booking_button3 = tk.Button(booking_widgets, text="Delete")
booking_button3.grid(row=2, column=2)
booking_button3.config(font=('Monospace', 10))

booking_button4 = tk.Button(booking_widgets, text="Clear Entry Boxes", command=clean_text3)
booking_button4.grid(row=2, column=3)
booking_button4.config(font=('Monospace', 10))

for widget in teams_booking.winfo_children():
    widget.grid_configure(padx=10, pady=5)

for widget in bane_booking.winfo_children():
    widget.grid_configure(padx=10, pady=5)

for widget in full_booking.winfo_children():
    widget.grid_configure(padx=10, pady=5)

window.mainloop()
