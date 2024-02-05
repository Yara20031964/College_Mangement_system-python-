from customtkinter import *
import tkinter

set_appearance_mode("Dark")
set_default_color_theme("blue")

def boo():
    print("Hello world!")


window = CTk()
window.geometry("800x500")
adminBtn = CTkButton(master=window, command=boo)
centering = ( rely = 0.5, relx=0.5, anchor = tkinter.CENTER )
# adminBtn.place(rely=0.5,relx=0.5,anchor = tkinter.CENTER)
adminBtn.place(centering)
# adminBtn.pack()
window.mainloop()
