import tkinter as tk
import pandas as pd
import csv

# File paths for storing data
STUDENTS_FILE = 'studentsT.csv'
student = pd.read_csv('studentsT.csv')
control = pd.read_csv('CoursesT.csv')

# dah m3amol global 3ashan al user mda5al al id bta3oh fi al 2awal ftlam da5l yb2 valid
# wi has5dmo 3ash lama a3adl fi course aw ai haga aw group mslan
ID = 0


def login():
    global ID
    ID = ID_entry.get()

    password = password_entry.get()
    k = 0
    # Check if the username and password match a predefined value
    for i in range(student.shape[0]):
        if (password == student['pass'][i] and int(ID) == student['id'][i]):
            k = 1
            line = i
            message_label.config(
                text=" Logain successfully, Welcome "+student['name'][i], fg="green")
            login_panel.grid_forget()

            # Show the main page with choices
            main_page.grid(row=0, column=0, padx=10, pady=10)
            # print("welcome",student['name'][i])
    if (k == 0):
        message_label.config(text="Invalid username or password", fg="red")


def register_courses():
    # Hide the main page
    main_page.grid_forget()

    # Show page for choice 2
    register_courses_page.grid(row=0, column=0, padx=10, pady=10)

# Function to handle choice 2


def edit_course():
    # Hide the main page
    main_page.grid_forget()

    # Show page for choice 2
    edit_course_page.grid(row=0, column=0, padx=10, pady=10)

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


def validate_group():
    choice = choose_group_entry.get()
    if choice in ['A', 'a', 'B', 'b']:
        ch = choice.upper()
        choose_group1(ID, ch)

    else:
        message_choose.config(text="Invalid group!", fg="red")

# lsa ma7tsh fiha 7aga


def See_news():
    # Hide the main page
    main_page.grid_forget()

    # Show page for choice 2
    See_news_page.grid(row=0, column=0, padx=10, pady=10)


# Create main window
root = tk.Tk()
root.title("Login Page")

# Create labels, entry fields, and button
login_panel = tk.Frame(root)
login_headline = tk.Label(login_panel, text="Welcome to FCI_Community", font=(
    "Arial", 20, "bold"), fg="blue")
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
main_headline = tk.Label(main_page, text="Welcome to Student's service", font=(
    "Arial", 20, "bold"), fg="blue")
main_headline.pack()

register_courses_button = tk.Button(
    main_page, text="Register courses", command=register_courses)
register_courses_button.pack()

edit_course_button = tk.Button(
    main_page, text="Edit courses", command=edit_course)
edit_course_button.pack()

choose_group_button = tk.Button(
    main_page, text="Choose the group", command=choose_group)
choose_group_button.pack()

See_news_button = tk.Button(main_page, text="See news", command=See_news)
See_news_button.pack()


# Create pages for choices
register_courses_page = tk.Frame(root)
register_courses_label = tk.Label(
    register_courses_page, text="Page for Choice 1")
register_courses_label.pack()

edit_course_page = tk.Frame(root)
edit_course_label = tk.Label(edit_course_page, text="Page for Choice 2")
edit_course_label.pack()

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

message_choose = tk.Label(choose_group_page, text="", fg="black")
message_choose.grid(row=4, columnspan=2)

See_news_page = tk.Frame(root)
See_news_label = tk.Label(See_news_page, text="Page for Choice 4")
See_news_label.pack()


login_panel.grid(row=0, column=0, padx=10, pady=10)
root.grid_rowconfigure(0, weight=10)
root.grid_columnconfigure(0, weight=10)
# Run the main event loop
root.mainloop()