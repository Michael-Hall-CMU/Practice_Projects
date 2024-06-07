from tkinter import *

MI_TO_KM = 1.60934


def convert_miles_to_km():
    km = round(float(miles_input.get()) * MI_TO_KM, 2)
    kilometer_result.config(text=f"{km}")


window = Tk()
window.title("Miles to Km Converter")
window.maxsize(width=300, height=200)
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result = Label(text="0")
kilometer_result.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=convert_miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
