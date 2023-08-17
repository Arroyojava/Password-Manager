from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
# Window Config
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

# Canvas / Background
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=0)

window.eval('tk::PlaceWindow . Center')
window.mainloop()
