import tkinter
from tkinter import ttk


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


window = tkinter.Tk()
window.title("TopBike Booking")


frame = tkinter.Frame(window)
frame.pack()


teams_booking = tkinter.LabelFrame(frame, text="Hold")
teams_booking.grid(row=0, column=0, padx=10, pady=10)


bane_booking = tkinter.LabelFrame(frame, text="Bane")
bane_booking.grid(row=0, column=1, padx=10, pady=10)


full_booking = tkinter.LabelFrame(frame, text="Booking")
full_booking.grid(row=0, column=2, padx=10, pady=10)


team_datalist = ttk.Treeview(teams_booking)
team_datalist['columns'] = ("Id", "Erfaring", "Størrelse")
team_datalist.grid(row=0, column=0)
team_datalist.column("#0", width=1)


bane_datalist = ttk.Treeview(bane_booking)
bane_datalist['columns'] = ("Id", "Kapacitet", "Sværhedsgrad")
bane_datalist.grid(row=0, column=0)
bane_datalist.column("#0", width=1)


booking_datalist = ttk.Treeview(full_booking)
booking_datalist['columns'] = ("Id", "Dato", "Hold id", "Bane id")
booking_datalist.grid(row=0, column=0)
booking_datalist.column("#0", width=1)


label1 = tkinter.Label(teams_booking, text="Id")
label1.grid(row=1, column=0)

label2 = tkinter.Label(teams_booking, text="Weight")
label2.grid(row=1, column=1)

label3 = tkinter.Label(teams_booking, text="Destination")
label3.grid(row=1, column=2)

label4 = tkinter.Label(teams_booking, text="Weather")
label4.grid(row=1, column=3)


window.mainloop()