# from tkinter import *
import tkinter as tk
from tkinter import Tk, Label, Frame, Button
from tkinter import OptionMenu, Listbox, END, Entry, NSEW
import admin as am


# Assigning root window
root = Tk()
root.geometry("800x500")
page = "College system"


# Fast griding the frames
def gridFrame(thisFrame):
    thisFrame.grid(row=0, column=0, padx=10, pady=10)


def checkLogin(user, passwd):
    if user in "ahmed" and passwd in "pass":
        return True
    else:
        return False


def onLogin():
    if checkLogin(usernameEntry.get(), passwordEntry.get()):
        adminLoginFrame.grid_forget()
        gridFrame(menuFrame)
    else:
        loginLabel.config(text="Wrong username or password", fg="red")
        usernameEntry.config(border=1, fg="red")
        passwordEntry.config(border=1, fg="red")


# Admin login menu
adminLoginFrame = Frame(root)
# - Labels
usernameLabel = Label(adminLoginFrame, text="Username: ")
usernameLabel.grid(row=1, column=1)
passwordLabel = Label(adminLoginFrame, text="Password: ")
passwordLabel.grid(row=2, column=1)
# - Entries
usernameEntry = Entry(adminLoginFrame)
usernameEntry.grid(row=1, column=2)
passwordEntry = Entry(adminLoginFrame, show="+")
passwordEntry.grid(row=2, column=2)
# - Label of username and password
loginLabel = Label(adminLoginFrame, text="")
loginLabel.grid(row=3, columnspan=3)
# - Login Button
loginBtn = Button(adminLoginFrame, text="Login", command=onLogin)
loginBtn.grid(row=4, columnspan=3)
# Main Menu

menuFrame = Frame(root)

# - Add Student
addStdButton = Button(menuFrame, width=13,
                      text="Add New Student")
addStdButton.grid(row=1, column=1, padx=4, pady=4)
# - Remove Student
remStdButton = Button(menuFrame, width=13, text="Remove Student")
remStdButton.grid(row=1, column=2, padx=4, pady=4)
# - Edit Student
editStdButton = Button(menuFrame, width=13, text="Edit Student")
editStdButton.grid(row=2, column=1, padx=4, pady=4)
# - Get Student info
getStdButton = Button(menuFrame, width=13, text="Get Student's Info")
getStdButton.grid(row=2, column=2, padx=4, pady=4)
# - Add Course
addCrsButton = Button(menuFrame, width=13, text="Add New Coruse")
addCrsButton.grid(row=3, column=1, padx=4, pady=4)
# - Remove Course
remCrsButton = Button(menuFrame, width=13, text="Add New Course")
remCrsButton.grid(row=3, column=2, padx=4, pady=4)
# - Add Post
addPostButton = Button(menuFrame, text="Add Post")
addPostButton.grid(row=4, columnspan=3, padx=4, pady=4)

# menusOptions = ["bla 1", "bla2"]
# selectedOption = tk.StringVar(menuFrame)
# selectedOption.set(menusOptions[0])
# chooseMenuList = OptionMenu(menuFrame, selectedOption,
#                             *menusOptions)
# chooseMenuList.grid(row=0, column=0, sticky=tk.N)
# menuFrame.grid(row=0, column=0, padx=10, pady=10, sticky=tk.N)

# Add Student Frame
addStudentFrame = Frame(root)

# - Student name text box
stdNameLabel = Label(addStudentFrame, text="Student Name: ")
stdNameLabel.grid(row=1, column=1)
stdNameEntry = Entry(addStudentFrame)
stdNameEntry.grid(row=1, column=2)
# - Student password text box
stdPassLabel = Label(addStudentFrame, text="Student Pass: ")
stdPassLabel.grid(row=2, column=1)
stdPassEntry = Entry(addStudentFrame, show="+")
stdPassEntry.grid(row=2, column=2)

# - Student GPA
stdNewLabel = Label(addStudentFrame, text="Student GPA: ")
stdNewLabel.grid(row=3, column=1)
stdNewEntry = Entry(addStudentFrame)
stdNewEntry.grid(row=3, column=2)

# - Student level


def onSelectNewLvl(value):
    print("selected Level: ", value)


selectedNewLvl = tk.StringVar(addStudentFrame)
newLvlsArray = [1, 2, 3, 4, 5]
selectedNewLvl.set("Not set")
newLvlsOptionMenu = OptionMenu(
    addStudentFrame, selectedNewLvl, *newLvlsArray, command=onSelectNewLvl)
newLvlsOptionMenu.grid(row=4, column=2)
newLvlLabel = Label(addStudentFrame, text="Level: ")
newLvlLabel.grid(row=4, column=1)

# - Student Group option menu


def onSelectGroup(value):
    print("selected Group: ", value)


selectedGroup = tk.StringVar(addStudentFrame)
groupsArray = ["A", "B", "C"]
selectedGroup.set("Not set")
groupsOptionMenu = OptionMenu(
    addStudentFrame, selectedGroup, *groupsArray, command=onSelectGroup)
groupsOptionMenu.grid(row=5, column=2)
groupLabel = Label(addStudentFrame, text="Group: ")
groupLabel.grid(row=5, column=1)


# - Courses

def getSelectedCrss():
    selected_indices = avaliableCrssBox.curselection()
    selected_items = [avaliableCrssBox.get(
        index) for index in selected_indices]
    print("Selected items:", selected_items)


avaliableCrss = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]

avaliableCrssBox = Listbox(addStudentFrame, selectmode=tk.MULTIPLE)
for option in avaliableCrss:
    avaliableCrssBox.insert(tk.END, option)
avaliableCrssBox.grid(row=6, column=2)

button = Button(addStudentFrame, text="Get Selected", command=getSelectedCrss)
button.grid(row=6, column=3)

# Finally the first griding
# gridFrame(adminLoginFrame)
gridFrame(addStudentFrame)
# Griding root window
root.grid_rowconfigure(0, weight=10)
root.grid_columnconfigure(0, weight=10)
root.title(page)
root.mainloop()
