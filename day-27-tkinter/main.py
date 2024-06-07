from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=600, height=500)


# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=1)


# Button
def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)


# Entry
input = Entry(width=10)
input.grid(column=3, row=2)




window.mainloop()
