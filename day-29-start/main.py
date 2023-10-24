from tkinter import *
from tkinter import messagebox
from random import randint , choice , shuffle
# import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_pass():

    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    
    pass_input.insert(0, password)
    # pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_pass():
    web = web_input.get()
    name = name_input.get()
    password = pass_input.get()

    if len(web) == 0 or len(password) == 0:
        messagebox.askretrycancel(
            title="Warning", message="Please don't leave any of the feilds empty.")

    else:
        is_ok = messagebox.askokcancel(
            title=web, message=f"These are the details entered: \nEmail: {name} \nPassword: {password} \n\nAre you sure to save? ")

        if is_ok:

            with open("passwords.txt", "a") as pass_file:

                pass_file.write(f"{web} | {name} | {password}\n")

                web_input.delete(0, END)
                pass_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_png)
canvas.grid(column=1, row=0)

website = Label(text="Website:")
website.grid(column=0, row=1)

username = Label(text="Email/Username:")
username.grid(column=0, row=2)

userpass = Label(text="Password:")
userpass.grid(column=0, row=3)

web_input = Entry(width=35)
web_input.grid(column=1, row=1, columnspan=3)
web_input.focus()

name_input = Entry(width=35)
name_input.grid(column=1, row=2, columnspan=3)
name_input.insert(0, "muawan541@gmail.com")

pass_input = Entry(width=21)
pass_input.grid(column=1, row=3)

genrarate_btn = Button(text="Generate Password", command=generate_pass)
genrarate_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=36, command=add_pass)
add_btn.grid(column=1, row=4, columnspan=3)


window.mainloop()
