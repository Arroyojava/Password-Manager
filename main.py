from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

FONT_NAME = 'Calibri'
SIZE = 13


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Function to generate a random password using letters, numbers and symbols
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    symbols_letters = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_letters = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + symbols_letters + numbers_letters
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_to_file(new_data):
    with open('passwords.json', 'w') as data_file:
        json.dump(new_data, data_file, indent=4)


def clear_entries():
    website_entry.delete(0, END)
    password_entry.delete(0, END)


def save_to_json():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'email': email,
            'password': password
        }
    }
    pyperclip.copy(password)

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning('Oops', 'Fields cannot be left blank!')
    else:
        try:
            with open("passwords.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            write_to_file(new_data)

        else:
            data.update(new_data)
            write_to_file(data)

        finally:
            clear_entries()


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()

    try:
        with open('passwords.json', 'r') as data_file:
            entry = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning('Error', 'Not Password File Found!')
    else:
        if website in entry:
            email = entry[website]["email"]
            password = entry[website]["password"]
            messagebox.showinfo(website,
                                f'Email/User: {email}\nPassword: {password}\n'
                                f'Password copied to clipboard!')
            pyperclip.copy(entry[website]["password"])
        else:
            messagebox.showwarning('None Found', f'No details for the {website} exist.')


# ---------------------------- UI SETUP ------------------------------- #
# Window Config
window = Tk()
window.title('Password Manager')
window.config(padx=25, pady=25)

# Canvas / Background
canvas = Canvas(width=325, height=200, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text='Website:', font=(FONT_NAME, SIZE))
website_label.grid(column=0, row=1, sticky='E')

email_username_label = Label(text='Email/Username:', font=(FONT_NAME, SIZE))
email_username_label.grid(column=0, row=2, sticky='E')

password_label = Label(text='Password:', font=(FONT_NAME, SIZE))
password_label.grid(column=0, row=3, sticky='E')

# Entry
website_entry = Entry(width=20, font=(FONT_NAME, SIZE))
website_entry.grid(column=1, row=1, sticky='w', padx=10, columnspan=2)
website_entry.focus()

email_username_entry = Entry(width=35, font=(FONT_NAME, SIZE))
email_username_entry.grid(column=1, row=2, sticky='w', padx=10, columnspan=2)

password_entry = Entry(width=20, font=(FONT_NAME, SIZE))
password_entry.grid(column=1, row=3, sticky='w', padx=10, )

# Buttons
add_button = Button(text='Add', width=35, font=(FONT_NAME, SIZE), command=save_to_json)
add_button.grid(column=1, row=4, sticky='w', padx=10, columnspan=2)

gen_password_button = Button(text='Generate Password', font=(FONT_NAME, 11), width=16, command=generate_password)
gen_password_button.grid(column=1, row=3, sticky='E', columnspan=2, padx=10)

search_button = Button(text='Search', font=(FONT_NAME, 11), width=16, command=find_password)
search_button.grid(column=1, row=1, sticky='E', columnspan=2, padx=10)

# Main Loop and Center Window
window.eval('tk::PlaceWindow . Center')
window.mainloop()
