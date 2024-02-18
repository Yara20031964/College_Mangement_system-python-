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
# def control_service():
#     # Hide the main page
#     main_page1.grid_forget()
#     login_panel.grid(row=0, column=0, padx=10, pady=10)
#     # Show page for choice 2  
    
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
root = tk.Tk()
root.title("WECOME")


main_page1 = tk.Frame(root)
main_page1_headline = tk.Label(main_page1, text="Welcome to service", font=("Arial", 20, "bold"), fg="blue")
main_page1_headline.pack()

student_service_button = tk.Button(main_page1, text="Register courses", command=student_service)
student_service_button.pack()

# control_service_button = tk.Button(main_page1, text="Edit courses", command=control_service)
# control_service_button.pack()

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

# login_panel.grid(row=0, column=0, padx=10, pady=10)
main_page1.grid(row=0, column=0, padx=10, pady=10)
root.grid_rowconfigure(0, weight=10)
root.grid_columnconfigure(0, weight=10)
# Run the main event loop
root.mainloop()
