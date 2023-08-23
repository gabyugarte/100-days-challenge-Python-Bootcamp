from tkinter import *

def calculate_miles_to_km():
    miles = float(entry.get())
    km = round(miles * 1.609)
    label3.config(text=f"{km}")

#Creating a new window and configurations
window = Tk()
window.title("Mile To Kilometer Converter")
# window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

#Entry
entry = Entry(width=7)
entry.grid(column=1, row=0)

#Labels

label1 = Label(text="Miles")
label1.grid(column=2, row=0)

label2 = Label(text="Is equal to")
label2.grid(column=0, row=1)

label3 = Label(text="0")
label3.grid(column=1, row=1)

label4 = Label(text="km")
label4.grid(column=2, row=1)

#button
button = Button(text="Calculate", command=calculate_miles_to_km)
button.grid(column=1, row=2)


window.mainloop()


