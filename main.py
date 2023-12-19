from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


def button_calculate():
    miles_num = miles_entry.get()
    # print(miles_num)
    convert_to_km = float(miles_num) * 1.609344
    # print(convert_to_km)
    km_number["text"] = convert_to_km


# Button
calculate_button = Button(text="calculate", command=button_calculate)
calculate_button.grid(column=1, row=3)


# Label

equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=0, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_number = Label(text="0")
km_number.grid(column=1, row=1)

# Entry
miles_entry = Entry(width=10)
miles_entry.grid(column=1, row=0)



window.mainloop()