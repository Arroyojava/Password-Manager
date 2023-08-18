from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

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
def save_to_file():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    pyperclip.copy(password)

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning('Oops', 'Fields cannot be left blank!')
    else:
        answer = messagebox.askokcancel('Complete', message=f'Data entered: '
                                                            f'\nWebsite: {website}'
                                                            f'\nEmail/Username: {email}'
                                                            f'\nPassword: {password}'
                                                            f'\nPassword has been saved to Clipboard'
                                                            f'\nIs it ok to save?')
        if answer:
            with open("passwords.txt", "a") as data_file:
                data_file.write(f'{website} | {email} | {password}\n')
            clear_entries()


def clear_entries():
    website_entry.delete(0, END)
    password_entry.delete(0, END)


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
website_entry = Entry(width=35, font=(FONT_NAME, SIZE))
website_entry.grid(column=1, row=1, sticky='w', padx=10, columnspan=2)
website_entry.focus()

email_username_entry = Entry(width=35, font=(FONT_NAME, SIZE))
email_username_entry.grid(column=1, row=2, sticky='w', padx=10, columnspan=2)

password_entry = Entry(width=19, font=(FONT_NAME, SIZE))
password_entry.grid(column=1, row=3, sticky='w', padx=10, )

# Buttons
add_button = Button(text='Add', width=35, font=(FONT_NAME, SIZE), command=save_to_file)
add_button.grid(column=1, row=4, sticky='w', padx=10, columnspan=2)

gen_password_button = Button(text='Generate Password', font=(FONT_NAME, 12), width=16, command=generate_password)
gen_password_button.grid(column=1, row=3, sticky='E', columnspan=2, padx=10)

# Main Loop and Center Window
window.eval('tk::PlaceWindow . Center')
window.mainloop()
