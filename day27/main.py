# import tkinter => If you want to import an certain class.
# You use -> window = tkinter.Tk()

from tkinter import * 
# If you want to import all classes, you use -> window = Tk(), dont need to call the tkinter module

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
#Add padding to the window
window.config(padx=20, pady=20)

#label
my_label = Label(text="I am a label", font=("Arial", 20, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

#change an argument
my_label["text"] = "New text"
my_label.config(text="New text")

#Button


def button_cliked():
    input_text = input.get()
    my_label.config (text= f' Hello {input_text}')

button = Button(text="Click Me", command=button_cliked)
button.grid(column=1, row=1)
new_button = Button(text="Newbutton", command=button_cliked)
new_button.grid(column=2, row=0)

#Entry

input = Entry(width=10)
input.grid(column=3, row=2)





window.mainloop()
