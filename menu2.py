from customtkinter import *
import tkinter

set_appearance_mode("Dark")
set_default_color_theme("blue")

def boo():
    print("Hello world!")


window = CTk()
window.geometry("800x500")
adminBtn = CTkButton(master=window, command=boo)
adminBtn.place(rely=2,relx=2,anchor = tkinter.CENTER)
adminBtn.pack()
window.mainloop()

