# Login Form
#
from tkinter import Tk, Listbox, Button, MULTIPLE, END
from tkinter import Tk, Label, StringVar, OptionMenu
from tkinter import Tk, Label, Entry, Button
from tkinter import ttk
import tkinter as tk


def login():
    username = username_entry.get()
    password = password_entry.get()
    # Add your login logic here
    print(username, password)


window = Tk()
window.geometry("800x500")
window.title("Login Form")
loginFrame = ttk.Frame(window, height=500, width=800)
loginFrame.pack(anchor=tk.CENTER)
# loginFrame.grid(column=0, row=0)
username_label = Label(loginFrame, text="Username:")
password_label = Label(loginFrame, text="Password:")
username_entry = Entry(loginFrame)
password_entry = Entry(loginFrame, show="*")
login_button = Button(loginFrame, text="Login", command=login)

username_label.grid(row=0, column=0, sticky=tk.NSEW)
username_entry.grid(row=0, column=1, sticky=tk.NSEW)
password_label.grid(row=1, column=0, sticky=tk.NSEW)
password_entry.grid(row=1, column=1, sticky=tk.NSEW)
login_button.grid(row=2, columnspan=2)

window.mainloop()


# Option menu
#


def on_select(value):
    print("Selected:", value)


window = Tk()
window.title("Select Box Example")

options = ["Option 1", "Option 2", "Option 3"]

selected_option = StringVar(window)
selected_option.set(options[0])  # Set the default selected option

select_box = OptionMenu(window, selected_option, *options, command=on_select)
select_box.pack()

window.mainloop()

# List Box
#


def get_selected_items():
    selected_indices = listbox.curselection()
    selected_items = [listbox.get(index) for index in selected_indices]
    print("Selected items:", selected_items)


window = Tk()
window.title("Multi-Select Box Example")

options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]

listbox = Listbox(window, selectmode=MULTIPLE)
for option in options:
    listbox.insert(END, option)
listbox.pack()

button = Button(window, text="Get Selected", command=get_selected_items)
button.pack()

window.mainloop()
