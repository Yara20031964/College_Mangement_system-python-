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
    # if thisFrame != ".!frame5":
    #     destroyFrameWidgets(editStdBar)
    #     editStdBar.destroy()


def backToLogin():
    gridFrame(adminLoginFrame)


def backToMenu():
    forgetFrameWidgets(root)
    gridFrame(menuFrame)


def backToMenuFromEdit():
    gridFrame(menuFrame)
    destroyFrameWidgets(editStdBar)
    editStdBar.destroy()


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

gridFrame(menuFrame)
# - Add Student


def goToAddStd():
    gridFrame(addStudentFrame)
    menuFrame.grid_forget()
    backToMenuBtn = Button(root, text="Back To Menu", command=backToMenu)
    backToMenuBtn.grid(row=0, column=0, sticky=tk.N+tk.W)


addStdButton = Button(menuFrame, width=13,
                      text="Add New Student", command=goToAddStd)
addStdButton.grid(row=1, column=1, padx=4, pady=4)
# - Remove Student


def goToRmStd():
    gridFrame(rmStudentFrame)
    menuFrame.grid_forget()
    backToMenuBtn = Button(root, text="Back To Menu", command=backToMenu)
    backToMenuBtn.grid(row=0, column=0, sticky=tk.N+tk.W)


remStdButton = Button(menuFrame, width=13,
                      command=goToRmStd, text="Remove Student")
remStdButton.grid(row=1, column=2, padx=4, pady=4)
# - Edit Student


def goToEditStd():
    gridFrame(getIdFrame)
    menuFrame.grid_forget()
    backToMenuBtn = Button(root, text="Back To Menu", command=backToMenu)
    backToMenuBtn.grid(row=0, column=0, sticky=tk.N+tk.W)


editStdButton = Button(menuFrame, width=13,
                       text="Edit Student", command=goToEditStd)
editStdButton.grid(row=2, column=1, padx=4, pady=4)
# - Get Student info


def goToGetStdInfo():
    gridFrame(getStudentInfoFrame)
    menuFrame.grid_forget()
    backToMenuBtn = Button(root, text="Back To Menu", command=backToMenu)
    backToMenuBtn.grid(row=0, column=0, sticky=tk.N+tk.W)


getStdButton = Button(menuFrame, width=13,
                      text="Get Student's Info", command=goToGetStdInfo)
getStdButton.grid(row=2, column=2, padx=4, pady=4)
# - Add Course


def goToAddCourse():
    gridFrame(addCourseFrame)
    menuFrame.grid_forget()
    backToMenuBtn = Button(root, text="Back To Menu", command=backToMenu)
    backToMenuBtn.grid(row=0, column=0, sticky=tk.N+tk.W)


addCrsButton = Button(menuFrame, width=13,
                      text="Add New Coruse", command=goToAddCourse)
addCrsButton.grid(row=3, column=1, padx=4, pady=4)
# - Remove Course


def goToRmCourse():
    gridFrame(rmCourseFrame)
    menuFrame.grid_forget()
    backToMenuBtn = Button(root, text="Back To Menu", command=backToMenu)
    backToMenuBtn.grid(row=0, column=0, sticky=tk.N+tk.W)


remCrsButton = Button(menuFrame, width=13,
                      text="Remove Course", command=goToRmCourse)
remCrsButton.grid(row=3, column=2, padx=4, pady=4)
# - Add Post


def goToAddPost():
    gridFrame(addPostFrame)
    menuFrame.grid_forget()
    backToMenuBtn = Button(root, text="Back To Menu", command=backToMenu)
    backToMenuBtn.grid(row=0, column=0, sticky=tk.N+tk.W)


addPostButton = Button(menuFrame, text="Add Post", command=goToAddPost)
addPostButton.grid(row=4, columnspan=3, padx=4, pady=4)
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
stdGpaLabel = Label(addStudentFrame, text="Student GPA: ")
stdGpaLabel.grid(row=3, column=1)
stdGpaEntry = Entry(addStudentFrame)
stdGpaEntry.grid(row=3, column=2)

# - Student level


def onSelectLvl(value):
    print("selected Level: ", value)


selectedLvl = tk.StringVar(addStudentFrame)
newLvlsArray = [1, 2, 3, 4, 5]
selectedLvl.set("Not set")
newLvlsOptionMenu = OptionMenu(
    addStudentFrame, selectedLvl, *newLvlsArray, command=onSelectLvl)
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
    selected_items = [am.crsCodeByName(avaliableCrssBox.get(
        index)) for index in selected_indices]
    return selected_items
    print("Selected items:", selected_items)


avaliableCrss = am.courses_list
avaliableCrssBox = Listbox(addStudentFrame, selectmode=tk.MULTIPLE)
for option in avaliableCrss:
    avaliableCrssBox.insert(tk.END, option)
avaliableCrssBox.grid(row=6, column=2)
# - Add Std Button


def onAddStdBtn():
    if not stdNameEntry.get().isalpha():
        addStdCaseLabel.config(text="Please Add a valid student's name")
    elif not stdPassEntry.get().isalnum():
        addStdCaseLabel.config(
            text="Please Add a valid student's password ([a-zA-Z0-9])")
    elif not am.validGpaBool(stdGpaEntry.get()):
        addStdCaseLabel.config(
            text="Please Add a valid student's GPA decimal 1.0-4.0")
    elif len(getSelectedCrss()) > 7 or len(getSelectedCrss()) < 3:
        addStdCaseLabel.config(
            text="Please Add 6 courses as a maximum and 3 as a minimum")
    else:
        am.addStd(stdNameEntry.get(), ':'.join(getSelectedCrss()), float(stdGpaEntry.get(
        )), selectedGroup.get(), int(selectedLvl.get()), stdPassEntry.get())


addStdbutton = Button(
    addStudentFrame, text="Get Selected", command=onAddStdBtn)
addStdbutton.grid(row=6, column=3)
addStdCaseLabel = Label(addStudentFrame, text="Level: ")
addStdCaseLabel.grid(row=7, column=1, columnspan=2)

# Remove Student
rmStudentFrame = Frame(root)


def onRmStudent():
    if int(rmStudentEntry.get()) not in am.ids:
        rmStudentCaseLabel.config(text="Invalid Id", fg="red")
    else:
        rmStudentCaseLabel.config(text="Removed", fg="green")
        am.removeStd(int(rmStudentEntry.get()))


rmStudentEntry = Entry(rmStudentFrame, font=("monospace", 10))
rmStudentEntry.grid(row=0, column=1)
rmStudentLabel = Label(rmStudentFrame, font=(
    "monospace", 10), text="Student's Id: ")
rmStudentLabel.grid(row=0, column=0)
rmStudentBtn = Button(
    rmStudentFrame, text="Remove Student", command=onRmStudent)
rmStudentBtn.grid(row=1, column=0, columnspan=2)
rmStudentCaseLabel = Label(rmStudentFrame, font=("monospace", 10))
rmStudentCaseLabel.grid(row=2, column=0, columnspan=2)


# Get all information about student
getStudentInfoFrame = Frame(root)


def onGetInfo():
    if int(getStudentInfoEntry.get()) in am.ids:
        stdId = int(getStudentInfoEntry.get())
        txt = f"Name: {am.getStd(stdId,'n')}\nCourses Enrolled:{am.getStd(stdId,'c')}\nGPA: {am.getStd(stdId,'g')}\nGroup: {am.getStd(stdId,'r')}\nLevel: {am.getStd(stdId,'l')}\nPassword: {am.getStd(stdId,'p')}"
        getStudentInfoLabel.config(text=txt)
    else:
        getStudentInfoLabel.config(text="Invalid Id", fg="red")


getStudentInfoEntry = Entry(getStudentInfoFrame, font=("monospace", 14))
getStudentInfoEntry.grid(row=0, column=0)
getStudentInfoBtn = Button(
    getStudentInfoFrame, command=onGetInfo, text="Get Information", font=("monospace", 12))
getStudentInfoBtn.grid(row=0, column=1)
getStudentInfoLabel = Label(getStudentInfoFrame, font=("monospace", 14))
getStudentInfoLabel.grid(row=1, column=0, rowspan=6)


# Edit Student
# - Edit Menu's Bar


def gridBar():
    editStdBar.grid(row=0, column=0, sticky=tk.N)


def onUseStdId():
    if int(getIdEntry.get()) not in am.ids:
        getIdErrorLabel.config(text="Id doen's exist")
        getIdErrorLabel.grid(row=1, column=0)
    else:
        global stdIdToEdit
        stdIdToEdit = int(getIdEntry.get())
        gridFrame(editStdFrame)
        gridBar()
        # gridFrame(editStdBar)
        destroyFrameWidgets(getIdFrame)


getIdFrame = Frame(root)
getIdEntry = Entry(getIdFrame)
getIdEntry.grid(row=0, column=1, padx=10)
getIdLabel = Label(getIdFrame, text="Student's ID:")
getIdLabel.grid(row=0, column=0)
getIdBtn = Button(getIdFrame, text="Edit", command=onUseStdId)
getIdBtn.grid(row=1, column=1, columnspan=2)
getIdErrorLabel = Label(getIdFrame, text="", fg="red")


editStdFrame = Frame(root)

editStdBar = Frame(root, height=30,
                   highlightbackground="red", highlightthickness=2)


# editStdBar.grid(row=0, column=0, sticky=tk.N)

editStdContentFrame = Frame(editStdFrame)
editStdContentFrame.grid(row=1, column=0)


def destroyFrameWidgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def forgetFrameWidgets(frame):
    for widget in frame.winfo_children():
        widget.grid_forget()


def onChgEditingOption(value):
    # - Edit student Content
    print("selected Group: ", value)
    if value == "Group":
        # Forgetting old editing option
        destroyFrameWidgets(editStdContentFrame)
        # - Edit student group

        def onChgGroupBtn():
            if selectedChgGroup.get() in "ABC":
                am.editStd(stdIdToEdit, 'r', selectedChgGroup.get())
                groupChgCaseLabel.config(
                    fg="green", text="Successfully Changed")
            else:
                groupChgCaseLabel.config(fg="red", text="Enter a Valid Group")

        def onChgGroup(value):
            print("selected Group: ", value)

        selectedChgGroup = tk.StringVar(editStdContentFrame)
        groupsArray = ["A", "B", "C"]
        selectedChgGroup.set("Not set")
        groupsChgOptionMenu = OptionMenu(
            editStdContentFrame, selectedChgGroup,
            *groupsArray, command=onChgGroup)
        groupsChgOptionMenu.grid(row=1, column=2)
        groupChgLabel = Label(editStdContentFrame, text="New Group: ")
        groupChgLabel.grid(row=1, column=1)
        groupChgBtn = Button(editStdContentFrame,
                             text="Change", command=onChgGroupBtn)
        groupChgBtn.grid(row=2, columnspan=2, column=1)
        groupChgCaseLabel = Label(editStdContentFrame, text="")
        groupChgCaseLabel.grid(row=3, column=1, columnspan=2)

    elif value == "Level":
        # Forgetting old editing option
        destroyFrameWidgets(editStdContentFrame)
        # - Edit student level

        def onChgLevelBtn():
            if selectedChgLevel.get() in "12345":
                am.editStd(stdIdToEdit, 'l', selectedChgLevel.get())
                levelChgCaseLabel.config(
                    fg="green", text="Successfully Changed")
            else:
                levelChgCaseLabel.config(fg="red", text="Enter a Valid Group")

        def onChgLevel(value):
            print("selected Group: ", value)

        selectedChgLevel = tk.StringVar(editStdContentFrame)
        levelsArray = ["1", "2", "3", "4", "5"]
        selectedChgLevel.set("Not set")
        levelChgOptionMenu = OptionMenu(
            editStdContentFrame, selectedChgLevel,
            *levelsArray, command=onChgLevel)
        levelChgOptionMenu.grid(row=1, column=2)
        levelChgLabel = Label(editStdContentFrame, text="New Level: ")
        levelChgLabel.grid(row=1, column=1)
        levelChgBtn = Button(editStdContentFrame,
                             text="Change", command=onChgLevelBtn)
        levelChgBtn.grid(row=2, columnspan=2, column=1)
        levelChgCaseLabel = Label(editStdContentFrame, text="")
        levelChgCaseLabel.grid(row=3, column=1, columnspan=2)
    elif value == "GPA":
        # Forgetting old editing option
        destroyFrameWidgets(editStdContentFrame)
        # - Edit Student GPA

        def onChgGpaBtn():
            # if stdNewEntry.get().isdecimal():
            if am.validGpaBool(stdNewEntry.get()):
                am.editStd(stdIdToEdit, 'g', stdNewEntry.get())
                gpaChgCaseLabel.config(
                    fg="green", text="Successfully Changed")
            else:
                gpaChgCaseLabel.config(
                    fg="red", text="Enter a Decimal Value [0-4]")
            # else:
            #     gpaChgCaseLabel.config(
            #         fg="red", text="Enter a Decimal Value")
        stdNewLabel = Label(editStdContentFrame, text="Student New GPA: ")
        stdNewLabel.grid(row=1, column=1)
        stdNewEntry = Entry(editStdContentFrame)
        stdNewEntry.grid(row=1, column=2)
        gpaChgBtn = Button(editStdContentFrame,
                           text="Change", command=onChgGpaBtn)
        gpaChgBtn.grid(row=2, columnspan=2, column=1)
        gpaChgCaseLabel = Label(editStdContentFrame, text="")
        gpaChgCaseLabel.grid(row=3, column=1, columnspan=2)
    elif value == "Registered Courses":
        # Destroy old widgets
        destroyFrameWidgets(editStdContentFrame)
        # - Courses

        def getNewSelectedCrss():
            selected_indices = avaliableNewCrssBox.curselection()
            selected_items = [avaliableNewCrssBox.get(
                index) for index in selected_indices]
            selected_itemsCodes = [am.crsCodeByName(i) for i in selected_items]
            am.editStd(stdIdToEdit, 'c', ':'.join(selected_itemsCodes))

            print("Selected items:", ':'.join(selected_itemsCodes))

        avaliableNewCrss = am.avaliableCrss4Std(stdIdToEdit)
        avaliableNewCrssBox = Listbox(
            editStdContentFrame, selectmode=tk.MULTIPLE, font=("monospace", 10), justify=tk.CENTER)
        for option in avaliableNewCrss:
            avaliableNewCrssBox.insert(tk.END, option)
        avaliableNewCrssBox.grid(row=1, column=2, padx=10)
        editCoursesCaseLabel = Label(
            editStdContentFrame, text="", height=3)
        editCoursesCaseLabel.grid(row=3, column=1, columnspan=2, padx=10)
        addCoursesToStdBtn = Button(editStdContentFrame, text="Register Courses",
                                    command=getNewSelectedCrss)
        addCoursesToStdBtn.grid(row=2, column=2, padx=10)
        # Remove courses from student

        def onRmStdCourses():
            selected_indices = stdCoursesBox.curselection()
            selected_items = [stdCoursesBox.get(
                index) for index in selected_indices]
            selected_itemsCodes = [am.crsCodeByName(i) for i in selected_items]
            am.editStd(stdIdToEdit, 'cr', selected_itemsCodes)
        stdCourses = [am.crsNameByCode(i) for i in am.getStd(
            stdIdToEdit, t='c').split(":")]
        stdCoursesBox = Listbox(
            editStdContentFrame, selectmode=tk.MULTIPLE, font=("monospace", 10), justify=tk.CENTER)
        for option in stdCourses:
            stdCoursesBox.insert(tk.END, option)
        stdCoursesBox.grid(row=1, column=3, padx=10)
        rmStdCoursesCaseLabel = Label(
            editStdContentFrame, text="", height=3)
        rmStdCoursesCaseLabel.grid(row=3, column=2, padx=10, columnspan=2)
        rmCoursesToStdBtn = Button(editStdContentFrame, text="Unregister Courses",
                                   command=onRmStdCourses, padx=10)
        rmCoursesToStdBtn.grid(row=2, column=3, padx=10)


# - Edit Student Bar
selectedEdit = tk.StringVar(editStdBar)
editOptions = ["Group", "Level", "GPA", "Registered Courses"]
selectedEdit.set("Not set")
editsOptionMenu = OptionMenu(
    editStdBar, selectedEdit, *editOptions, command=onChgEditingOption)
editsOptionMenu.grid(row=0, column=2)
editStdBarLabel = Label(editStdBar, text="Edit Student's:  ")
editStdBarLabel.grid(row=0, column=1)

# Finally the first griding
# Add post frame
addPostFrame = Frame(root)
addPostLabel = Label(addPostFrame, font=("monospace", 14), text="Add Post: ")
addPostLabel.grid(row=1, column=1)
addPostEntry = tk.Text(addPostFrame, padx=20, height=10,
                       width=40, font=("monospace", 14))
addPostEntry.grid(row=1, column=2)


def getData():
    text = addPostEntry.get("1.0", tk.END)
    arr = ["test"]
    arr.append(text)
    print(arr)
    # print(addPostEntry.get("1.0", tk.END))
    # print(type(addPostEntry.get("1.0", tk.END)))


btn = Button(addPostFrame, text="Post", command=getData,
             height=2, width=10, padx=20)
btn.grid(row=1, column=3)


def onClickAddCourseButton():
    newCourseName = courseNameEntry.get()
    newCourseID = courseIdEntry.get()
    if not am.validCrsCodeBool(newCourseID, am.code_list) or not am.validCrsNameBool(newCourseName, am.courses_list):
        addCourseCaseLabel.config(
            fg="red", text="Please add a valid course name and code")
    else:
        am.addCrs(newCourseName, newCourseID, 1)
        addCourseCaseLabel.config(fg="green", text="Course Added")


# Frame for adding a New Course
addCourseFrame = Frame(root)
courseNamelabel = Label(
    addCourseFrame, text="Course Name:", font=("monospace", 12))
courseNamelabel.grid(row=0, column=0)
courseNameEntry = tk.Entry(addCourseFrame)
courseNameEntry.grid(row=0, column=1)
courseIDlabel = Label(addCourseFrame, text="Course ID:",
                      font=("monospace", 12))
courseIDlabel.grid(row=1, column=0, pady=10)
courseIdEntry = tk.Entry(addCourseFrame)
courseIdEntry.grid(row=1, column=1, pady=10)
addCourseButton = Button(addCourseFrame, width=13,
                         text="Add", command=onClickAddCourseButton)
addCourseButton.grid(row=3, column=0, columnspan=2, pady=10)

addCourseCaseLabel = Label(addCourseFrame, text="",
                           font=("monospace", 12))
addCourseCaseLabel.grid(row=4, column=0, pady=10, columnspan=2)


def onClickRemoveCourseButton():
    courseRemoved = selectedCourse.get()
    if courseRemoved == "Unassigned":
        rmCourseCaseLabel.config(
            fg="red", text="Please choose a course to remove")
    else:
        am.removeCrsByCode(am.crsCodeByName(courseRemoved))
        rmCourseCaseLabel.config(fg="green", text="Course Removed")


# Frame for Removing a Course


rmCourseFrame = Frame(root)
coursesList = am.courses_list
selectedCourse = tk.StringVar(rmCourseFrame)
selectedCourse.set("Unassigned")
rmCoursesOptionMenu = OptionMenu(rmCourseFrame, selectedCourse, *coursesList)
rmCoursesOptionMenu.grid(row=0, column=0, )
rmCourseButton = Button(rmCourseFrame, width=13,
                        text="Remove", command=onClickRemoveCourseButton)
rmCourseButton.grid(row=0, column=1, columnspan=2, padx=10)
rmCourseCaseLabel = Label(rmCourseFrame, text="",
                          font=("monospace", 12))
rmCourseCaseLabel.grid(row=4, column=0, pady=10, columnspan=2)


# Griding root window
root.grid_rowconfigure(0, weight=10)
root.grid_columnconfigure(0, weight=10)
root.title(page)
root.mainloop()
