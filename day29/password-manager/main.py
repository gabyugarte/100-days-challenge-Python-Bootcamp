from tkinter import *
from tkinter import messagebox
import random
import pyperclip 
#pyperclip is a library to copy or paste text into the clipboard.
#In this case we are using it to copy the generated password.

#To reduce the code we can use: from random import choice, randint, shuffle

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project from class5
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    #This code can replace this 👇 using the join() method
    # password = ""
    # for char in password_list:
    #   password += char
    password = "".join(password_list)
    # print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ooops", message="Please, do not leave any of the fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                   f"\nPassword: {password} \nIs it ok to save?")
        
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                #We use delete() method to remove or clear the entry, parameters( 0, END) deletes all
                website_entry.delete(0, END)
                password_entry.delete(0, END)
    
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
password_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_image)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#Entries
website_entry = Entry(width=50)
website_entry.grid(column=1, row=1,columnspan=2)
#To focus the cursor when the user enter to the app, we use a method called focus
website_entry.focus()

email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2)
#We use the method insert to add a placeholder of our info. Parameters, 0
email_entry.insert(0, "gabrielaugartemaco@gmail.com")

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

#buttons
generate_password_button = Button(text="Generate Password", width=14, command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=42, command=save)
add_button.grid(column=1, row=4, columnspan=2)




window.mainloop()