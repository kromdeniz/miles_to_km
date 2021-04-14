from tkinter import *

window = Tk()
window.title("Miles to KM Converter")
window.minsize(width=200, height=140)
window.config(padx=10,pady=25)

input = Entry(width=2)
input.insert(0, " 0")
input.grid(column=2, row=1)

miles = Label(text="Miles")
miles.grid(column=3, row=1)

is_equal = Label(text="is equal to")
is_equal.grid(column=1 ,row=2)


def calc():
    calc = round(int(input.get())*1.609344,3)
    km.config(text=calc)

km = Label(text="0")
km.grid(column=2, row=2)

km_label = Label(text="Km")
km_label.grid(row=2, column=3)

button = Button(text="Calculate", command=calc)
button.grid(row=3, column=2)






window.mainloop()