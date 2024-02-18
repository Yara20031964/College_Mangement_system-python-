# from tkinter import *
import tkinter as tk
from tkinter import Tk, Label, Frame, Button, ttk
from tkinter import OptionMenu, Listbox, END, Entry, NSEW
import admin as am


# Assigning root window
root = Tk()
root.geometry("800x500")
page = "College system"

style = ttk.Style(root)
style.theme_use('clam')
root.option_add("*font", "sans 12")

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
    forgetFrameWidgets(editStdBar)
    gridFrame(menuFrame)
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

# gridFrame(main_page1)
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
    addStudentFrame, text="Add Student", command=onAddStdBtn)
addStdbutton.grid(row=6, column=3)
addStdCaseLabel = Label(addStudentFrame, text="")
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
        forgetFrameWidgets(getIdFrame)
        gridFrame(editStdFrame)
        gridBar()


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
###############################################################################################################3
import tkinter as tk
import pandas as pd
import csv
from tkinter import scrolledtext

# File paths for storing data
STUDENTS_FILE = 'studentsT.csv'
student = pd.read_csv('studentsT.csv')
control = pd.read_csv('CoursesT.csv')

# dah m3amol global 3ashan al user mda5al al id bta3oh fi al 2awal ftlam da5l yb2 valid
#wi has5dmo 3ash lama a3adl fi course aw ai haga aw group mslan
ID=0
line=0

def student_service():
    # Hide the main page
    main_page1.grid_forget()
    login_panel.grid(row=0, column=0, padx=10, pady=10)
    # Show page for choice 2
def control_service():
    # Hide the main page
    main_page1.grid_forget()
    adminLoginFrame.grid(row=0, column=0, padx=10, pady=10)
    # Show page for choice 2  
    
def login():

    root.title("Login Page")
    global ID
    ID = ID_entry.get()

    password = password_entry.get()
    k = 0
    # Check if the username and password match a predefined value
    for i in range(student.shape[0]):
            if(password==student['pass'][i] and int(ID)==student['id'][i]):
                k=1
                global line
                line=i
                message_label.config(text=" Logain successfully, Welcome "+student['name'][i] ,fg="green")
                login_panel.grid_forget()
    
                # Show the main page with choices
                main_page.grid(row=0, column=0, padx=10, pady=10)
                root.title("Main Page")
    if (k == 0):
     message_label.config(text="Invalid username or password", fg="red")

def register_courses():
    # Hide the main page
    main_page.grid_forget()

    # Show page for choice 2
    register_courses_page.grid(row=0, column=0, padx=10, pady=10)
    root.title("Register page")
def register_courses1():
    ch1=0
    ch=0
    l=student['courses'][line]
    ncourse=register_course_entry.get()
    ncourse.lower()
    for j in range(control.shape[0]):
            if(control['Course'][j].lower()==ncourse):
                ch1=1
    words_list = l.split(':')
    for k in words_list:
        if(k.lower()!=ncourse):
            ch+=1
    if(ch==len(words_list) and ch1==1):
        student.loc[line,'courses']=l+": "+ncourse
        student.to_csv('studentsT.csv',index=False)
        message_register.config(text="the course successfuly registed", fg="green")
    else:
        message_register.config(text="you may passed this course or invalid course please try again", fg="red")
    

# Function to handle choice 2


def edit_course():
    # Hide the main page
    main_page.grid_forget()

    # Show page for choice 2
    edit_course_page.grid(row=0, column=0, padx=10, pady=10)
    root.title("Edit Page")
def valid_edit():
    student=pd.read_csv('studentsT.csv')
    l=student['courses'][line]
    words_list1 = l.split(':')
    ch2=0
    ch3=0
    # Convert all strings to lowercase using map() function
    lowercase_strings_list = list(map(str.lower, words_list1))
    edit=edit_course_entry.get()
    low=edit.lower()
    for i in lowercase_strings_list:
        if(low!=i):
            ch2+=1
        else:
            lowercase_strings_list.remove(low)
            ch3=1
    if(ch2==len(words_list1)):
        message_edit.config(text="The course that you want to drop it not found please try again!", fg="red")

    if(ch3==1):
        string=""
        for k in lowercase_strings_list:
            if(k==len(words_list1)-1):
                string+=k
            else:
                string=string +k+":"
        student.loc[line,'courses']=string
        student.to_csv('studentsT.csv',index=False)
        message_edit.config(text="The course droped successfuly", fg="green") 

# function daad al 3amlha 3ashan hatst5dmha fi choose group


def choose_group1(student_id, group):
    # Check if the student has already chosen a group
    existing_group = get_student_group(student_id)

    if existing_group:
        message_choose.config(
            text=f"Student {student_id} is already part of Group {existing_group}.", fg="green")
    else:
        # Update the student's group in the CSV file
        update_student_group(student_id, group)
        message_choose.config(
            text=f"Student {student_id} has successfully chosen Group {group}.", fg="green")

# function daad al 3amlha 3ashan hatst5dmha fi choose group


def get_student_group(student_id):
    with open(STUDENTS_FILE, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == str(student_id):
                # group information is in the 4th column of the csv file
                return row[4]
    return None


def update_student_group(student_id, group):
    # Update the student's group in the CSV file
    with open(STUDENTS_FILE, 'r', newline='') as file:
        lines = list(csv.reader(file))

    with open(STUDENTS_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in lines:
            if row[0] == str(student_id):
                # group information is in the 4th column of the csv file
                row[4] = group
            writer.writerow(row)

# dih 2t3amlt boso 3aliah htl2o kol sho8la ta7t al bysh8al function dih


def choose_group():
    # Hide the main page
    main_page.grid_forget()
    # Show page for choice 2
    choose_group_page.grid(row=0, column=0, padx=10, pady=10)
    root.title("Choose group Page")

def validate_group():
    choice = choose_group_entry.get()
    if choice in ['A', 'a', 'B', 'b']:
        ch = choice.upper()
        choose_group1(ID, ch)

    else:
        message_choose.config(text="Invalid group!", fg="red")


def See_news():
    # Hide the main page
    main_page.grid_forget()

    # Show page for choice 2
    See_news_page.grid(row=0, column=0, padx=10, pady=10)
    root.title("News Page")
    import csv
    try:
        with open('news.csv', 'r', newline='') as file:
            News = csv.reader(file) 
            for row in News:
                 news_text.insert(tk.END, ', '.join(row)+'\n')
            news_text.config(state=tk.DISABLED)
    except FileNotFoundError:
        news_text.insert(tk.END, "Error: There is NO News.\n")
        news_text.config(state=tk.DISABLED)

def return_to_login():
    register_courses_page.grid_forget() 
    edit_course_page.grid_forget()  
    choose_group_page.grid_forget() 
    See_news_page.grid_forget() 
    # Show the login page
    login_panel.grid(row=0, column=0, padx=10, pady=10)
    

# Create main window
# root = tk.Tk()
# root.title("WECOME")


main_page1 = tk.Frame(root)
main_page1_headline = tk.Label(main_page1, text="Welcome to service", font=("Arial", 20, "bold"), fg="blue")
main_page1_headline.pack()

student_service_button = tk.Button(main_page1, text="Student service", command=student_service)
student_service_button.pack()

control_service_button = tk.Button(main_page1, text="Control service", command=control_service)
control_service_button.pack()

# Create labels, entry fields, and button
login_panel = tk.Frame(root)

login_headline = tk.Label(login_panel, text="Welcome to FCI_Community", font=("Arial", 20, "bold"),fg="blue")
login_headline = tk.Label(login_panel, text="Welcome to FCI_Community", font=("Arial", 20, "bold"), fg="blue")
login_headline.grid(row=0, columnspan=2, pady=10)
ID_label = tk.Label(login_panel, text="ID:")
ID_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
ID_entry = tk.Entry(login_panel)
ID_entry.grid(row=1, column=1, padx=10, pady=5)

password_label = tk.Label(login_panel, text="Password:")
password_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
password_entry = tk.Entry(login_panel, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=5)

login_button = tk.Button(login_panel, text="Login", command=login)
login_button.grid(row=3, column=0, columnspan=2, pady=10)

message_label = tk.Label(login_panel, text="", fg="black")
message_label.grid(row=4, column=0, columnspan=2)


main_page = tk.Frame(root)
main_headline = tk.Label(main_page, text="Welcome to Student's service", font=("Arial", 20, "bold"), fg="blue")
main_headline.pack()

register_courses_button = tk.Button(main_page, text="Register courses", command=register_courses)
register_courses_button.pack()

edit_course_button = tk.Button(main_page, text="Edit courses", command=edit_course)
edit_course_button.pack()

choose_group_button = tk.Button( main_page, text="Choose the group", command=choose_group)
choose_group_button.pack()

See_news_button = tk.Button(main_page, text="See news", command=See_news)
See_news_button.pack()



# Create pages for choices
register_courses_page = tk.Frame(root)
register_course_headline = tk.Label(register_courses_page, text="Please enter the course that you want to register it \n The courses math1,math2,network, Iman, vim, linux, discrete, neovim", font=("Arial", 16, "bold"))
register_course_headline.grid(row=0, columnspan=2, pady=10)

register_course_label = tk.Label(register_courses_page, text="Course:")
register_course_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
register_course_entry = tk.Entry(register_courses_page)
register_course_entry.grid(row=1, column=1, padx=10, pady=5)

register_course_button = tk.Button(register_courses_page, text="Enter", command=register_courses1)
register_course_button.grid(row=3, column=0, columnspan=2, pady=10)

exit_button = tk.Button(register_courses_page, text="Exit", command=return_to_login)
exit_button.grid(row=4,columnspan=2, pady=10)

message_register = tk.Label(register_courses_page, text="", fg="black")
message_register.grid(row=5, columnspan=2)
# register_courses_label = tk.Label(register_courses_page, text="Page for Choice 1")
# register_courses_label.pack()

edit_course_page = tk.Frame(root)
edit_course_headline = tk.Label(edit_course_page, text="Please select the course that you want to edit it ", font=("Arial", 16, "bold"))
edit_course_headline.grid(row=0, columnspan=2, pady=10)

edit_course_label = tk.Label(edit_course_page, text="course Id:")
edit_course_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
edit_course_entry = tk.Entry(edit_course_page)
edit_course_entry.grid(row=1, column=1, padx=10, pady=5)

edit_course_button = tk.Button(edit_course_page, text="Enter", command=valid_edit)
edit_course_button.grid(row=4, column=0, columnspan=2, pady=10)

exit1_button = tk.Button(edit_course_page, text="Exit", command=return_to_login)
exit1_button.grid(row=5,columnspan=2, pady=10)

message_edit = tk.Label(edit_course_page, text="", fg="black")
message_edit.grid(row=6, columnspan=2)

choose_group_page = tk.Frame(root)
choose_group_headline = tk.Label(
    choose_group_page, text="Please select the group that you want A or B", font=("Arial", 16, "bold"))
choose_group_headline.grid(row=0, columnspan=2, pady=10)


choose_group_label = tk.Label(choose_group_page, text="Group:")
choose_group_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
choose_group_entry = tk.Entry(choose_group_page)
choose_group_entry.grid(row=1, column=1, padx=10, pady=5)


choose_group_button = tk.Button(
    choose_group_page, text="Enter", command=validate_group)
choose_group_button.grid(row=3, column=0, columnspan=2, pady=10)

exit2_button = tk.Button(choose_group_page, text="Exit", command=return_to_login)
exit2_button.grid(row=4,columnspan=2, pady=10)

message_choose = tk.Label(choose_group_page, text="", fg="black")
message_choose.grid(row=5, columnspan=2)

See_news_page = tk.Frame(root)
news_text = scrolledtext.ScrolledText(See_news_page, wrap=tk.WORD, width=40, height=10,font=("Arial", 16, "bold"))
news_text.pack(padx=10, pady=10)

exit3_button = tk.Button(See_news_page, text="Exit", command=return_to_login)
exit3_button.pack(pady=10)
# See_news()

main_page1.grid(row=0, column=0, padx=10, pady=10)
# Griding root window
# adminLoginFrame.grid(row=0, column=0, padx=10, pady=10)
root.grid_rowconfigure(0, weight=10)
root.grid_columnconfigure(0, weight=10)
root.title(page)
root.mainloop()
