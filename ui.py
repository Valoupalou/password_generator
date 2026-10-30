from tkinter import *
from generator import *

root = Tk()

root.title('Password Generator')
root.geometry('500x500')

label_password_length = Label(root, text='Choose the length of your password (16/32/64):')
label_password_length.grid(column=0, row=0)

entry_length = Entry(root, width=2)
entry_length.grid(column=1, row=0)

password_generated = Label(root, text='')
password_generated.grid(column=0, row=1)


def clicked():


    length = int(entry_length.get())

    generator = Generator(length)


    if length != 16 and length != 32 and length != 64:
        password_generated.configure(text='Please choose between 16, 32 or 64')
    else:
        output_password = generator.generating_password()
        password_generated.configure(text=output_password)

button_generating = Button(root, text='Generating', command=clicked)
button_generating.grid(column=2,row=0)

root.mainloop()