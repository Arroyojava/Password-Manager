from tkinter import *

FONT_NAME = 'Calibri'
SIZE = 13
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

email_username_entry = Entry(width=35, font=(FONT_NAME, SIZE))
email_username_entry.grid(column=1, row=2, sticky='w', padx=10, columnspan=2)

password_entry = Entry(width=19, font=(FONT_NAME, SIZE))
password_entry.grid(column=1, row=3, sticky='w', padx=10, )
# Buttons
add_button = Button(text='Add', width=35, font=(FONT_NAME, SIZE))
add_button.grid(column=1, row=4, sticky='w', padx=10, columnspan=2)

gen_password_button = Button(text='Generate Password', font=(FONT_NAME, 12), width=16)
gen_password_button.grid(column=1, row=3, sticky='E', columnspan=2, padx=10)

window.eval('tk::PlaceWindow . Center')
window.mainloop()
