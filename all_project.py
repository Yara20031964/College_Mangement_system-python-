import pandas as pd
import csv
from pandas import read_csv, DataFrame
from datetime import datetime
# id,name,courses,GPA,Group,level,pass
file = read_csv('./studentsT.csv')
postsFile = read_csv('./news.csv')
# Posts lists
postsStrs = postsFile['post'].tolist()
postsDates = postsFile['date'].tolist()
# Students list
ids = file['id'].tolist()
names = file['name'].tolist()
stdCoursesId = file['courses'].tolist()
gpas = file['GPA'].tolist()
groups = file['Group'].tolist()
levels = file['level'].tolist()
passes = file['pass'].tolist()
# Courses table
courses = read_csv("CoursesT.csv")
courses_list = courses["Course"].tolist()
code_list = courses["Code"].tolist()
ch_list = courses["CH"].tolist()
# Functions
# Id Generator


def idGenerator(arr):
    id = 20230001
    for item in arr:
        if id != int(item):
            return id
        else:
            id += 1
    return id
# Valid Std id
# def validStdId(id):
#     for item in ids:
#         if int(id) == int(item):
#             return True
#     print("blable")
#     raise ValueError("")
# Check course is already avaliable


def validCrss(stdCrss, courses):
    for i in stdCrss.split(":"):
        try:
            courses.index(i)
        except:
            # print("Enter valid courses' codes")
            raise ValueError("")
    return True
# Valid GPA ckecker


def validGPA(gpa):
    if not (gpa <= 4 and gpa >= 0):
        # print("Enter Valid GPA")
        raise ValueError("Type a valid error")
# Valid Group


def validGrp(grp):
    if grp.upper() in "ABC":
        return True
    else:
        raise ValueError("Type a valid group")
# Valid level


def validLvl(lvl):
    if not (lvl <= 5 and lvl >= 1):
        raise ValueError("")


# Valid password
def validPass(str):
    if not str.isalnum():
        raise ValueError("")
# Save file


def saveF():
    dict = {'id': ids,
            'name': names,
            'courses': stdCoursesId,
            'GPA': gpas,
            'Group': groups,
            'level': levels,
            'pass': passes
            }
    dataFrame = DataFrame(dict)
    dataFrame.to_csv('./studentsT.csv', index=False)
# Add student


def addStd(name, coursesId, gpa, group, level, passwd):
    id = int(idGenerator(ids))
    try:
        validCrss(coursesId, code_list)
    except:
        print("Invalid group")
        return
    try:
        validGPA(gpa)
    except:
        print("Invalid GPA, Must be between 0-4")
        return
    try:
        validGrp(group)
    except:
        print("Invalid Group")
        return
    try:
        validLvl(level)
    except:
        print("invalid lvl")
        return
    try:
        validPass(passwd)
    except:
        print("invalid pass")
        return
    # Adding data to each list
    ids.append(id)
    names.append(name)
    stdCoursesId.append(coursesId)
    gpas.append(gpa)
    groups.append(group.upper())
    levels.append(level)
    passes.append(passwd)
    # Saving progress
    saveF()
    print(name, "Added")
# addStd("Mohsen","NVM",3.1,"C",5,"ahmed112")
# Remove Student


def removeStd(id):
    # Getting index
    try:
        ind = ids.index(id)
    except:
        print("Enter a valid id")
        return
    # Remove this index from each list
    ids.pop(ind)
    names.pop(ind)
    stdCoursesId.pop(ind)
    gpas.pop(ind)
    groups.pop(ind)
    levels.pop(ind)
    passes.pop(ind)
    # Saving progress
    saveF()
# removeStd(20230004)
# Get specific data about student


def getStd(id, t="all"):
    ind = ids.index(id)
    if t == 'all':
        arr = [id]
        arr.append(names[ind])
        arr.append(stdCoursesId[ind])
        arr.append(gpas[ind])
        arr.append(groups[ind])
        arr.append(levels[ind])
        arr.append(passes[ind])
        return arr
    elif t == 'n':
        return names[ind]
    elif t == 'c':
        return stdCoursesId[ind]
    elif t == 'g' or t == 'gpa':
        return gpas[ind]
    elif t == 'r' or t == 'grp':
        return groups[ind]
    elif t == 'l':
        return levels[ind]
    elif t == 'p':
        return passes[ind]
# Edit Student info


def editStd(id, t, val):
    # Getting index
    ind = ids.index(id)
    # Edit Courses
    if t == 'c':
        try:
            validCrss(val, code_list)
        except:
            print("Enter a valid Courses' Code")
            return
        stdCoursesId[ind] = val
    # Edit GPA
    elif t == 'g' or t == 'gpa':
        try:
            validGPA(val)
        except:
            print("Enter a valid GPA")
            return
        gpas[ind] = val
    # Edit Group
    elif t == 'r' or t == 'grp':
        try:
            validGrp(val)
        except:
            print("Enter Valid Group")
            return
        groups[ind] = val
    # Edit Level
    elif t == 'l':
        try:
            validLvl(val)
        except:
            print("Enter a valid Level")
            return
        levels[ind] = val
    # Edit Password
    elif t == 'p':
        try:
            validPass(val)
        except:
            print("Enter a valid password")
            return
        passes[ind] = val
    # Saving progress
    saveF()
# Add post


def addPost(postStr):
    thisDate = datetime.today().strftime('%y%m%d')
    print(thisDate)
    postsStrs.append(postStr)
    postsDates.append(thisDate)
    dict = {'date': postsDates,
            'post': postsStrs}
    dataFrame = DataFrame(dict)
    dataFrame.to_csv('./news.csv', index=False)


def crsCodeFound(removed_code, code_list):
    if removed_code in code_list:
        return True
    else:
        return False
# A course code is 3 letters


def validCrsCode(new_code, code_list):
    if len(new_code) > 3 or new_code in code_list or not new_code.isalnum():
        raise ValueError("")
    else:
        return True
# A course code is inavaliable in the courses table


def validCrsName(new_course, courses_list):
    if (new_course in courses_list) or not new_course.isalnum():
        raise ValueError("")
    else:
        return True
# Add course to the courses table
# Takes the Course's Name, Code and Credit hours as Parameters


def addCrs(new_course, new_code, new_ch):
    # new_course = input("Add Course: ")
    # new_code = input("Add the Course's Code: ")
    if not validCrsCode(new_code, code_list):
        # print("Please Enter a Valid Code!!")
        return
    if not (new_ch <= 3 and new_ch >= 0):
        print("Credit hours must be a number between 0-3")
        # raise ValuError("")
        return
    if validCrsName(new_course, courses_list):
        courses_list.append(new_course)
        code_list.append(new_code)
        ch_list.append(new_ch)
        dict = {'Course': courses_list, 'Code': code_list, 'CH': ch_list}
        df = DataFrame(dict)
        df.to_csv('CoursesT.csv', index=False)
    else:
        # print("the Course You are trying to input already exists")
        return
    # return courses_list, code_list,new_course,new_code
# Remove course from the courses table using the Course's Code
# Takes the Courses code as an Parameters


def removeCrsByCode(removed_code):
    # removed_code = input("Enter the code for the course you want to remove: ")
    if crsCodeFound(removed_code, code_list):
        indx_code = code_list.index(removed_code)
        code_list.pop(indx_code)
        courses_list.pop(indx_code)
        ch_list.pop(indx_code)
        dict = {'Course': courses_list, 'Code': code_list, 'CH': ch_list}
        df = DataFrame(dict)
        df.to_csv('CoursesT.csv', index=False)
    else:
        print("Course not Found!!")
        return


    # return courses_list,code_list,ch_list
##############################################################################################################
student = pd.read_csv('studentsT.csv')
control = pd.read_csv('CoursesT.csv')


def Register_course(line):
    valid = False
    c = 0
    t = 0

    while (t == 0):
        h = 0
        ch = 0
        ch1 = 0
        l = student['courses'][line]
        print("There is math1,math2,network, Iman, vim, linux, discrete, neovim")
        ncourse = input("Please select the course that you need:")
        ncourse.lower()
        for j in range(control.shape[0]):
            if (control['Course'][j].lower() == ncourse):
                ch1 = 1
                hour = control['CH'][j]
        words_list = l.split(':')
        for k in words_list:
            if (k.lower() != ncourse):
                ch += 1
        if (ch == len(words_list) and ch1 == 1):
            valid = True
        else:
            False

        if valid == True:
            c += h
            student.loc[line, 'courses'] = l+": "+ncourse
            student.to_csv('studentsT.csv', index=False)
        elif (valid == False):
            print("you may passed this course or invalid course please try again")
        if (c == 18):
            print(
                "The last course that you added will not register bec.you exceed the 18 hour in one semester")
            t = 1
        print("do you want to register another course if you don't want select zero if you want select 1")
        x = input()
        if (int(x) == 0):
            t = 1
        elif (int(x) == 1):
            t = 0
####################################################################################################################


def edit_course(line):
    student = pd.read_csv('studentsT.csv')
    l = student['courses'][line]
    words_list1 = l.split(':')
    ch2 = 0
    ch3 = 0
    # Convert all strings to lowercase using map() function
    lowercase_strings_list = list(map(str.lower, words_list1))
    while ch3 == 0:
        edit = input("please enter the course that you want to drop it: ")
        low = edit.lower()
        for i in lowercase_strings_list:
            if (low != i):
                ch2 += 1
            else:
                lowercase_strings_list.remove(low)
                ch3 = 1
        if (ch2 == len(words_list1)):
            print("The course that you want to drop it not found please try again!")
        if (ch3 == 1):
            string = ""
            for k in lowercase_strings_list:
                if (k == len(words_list1)-1):
                    string += k
                else:
                    string = string + k+": "
            student.loc[line, 'courses'] = string
            student.to_csv('studentsT.csv', index=False)
####################################################################################################################


def see_news():
    import csv
    try:
        with open('news.csv', 'r', newline='') as file:
            News = csv.reader(file)

            # Iterate through each row in the CSV file
            for row in News:
                print(', '.join(row))
    except FileNotFoundError:
        print("Error: There is NO News .")

###################################################################################################################


# File paths for storing data
STUDENTS_FILE = 'studentsT.csv'


def choose_group(student_id, group):
    # Check if the student has already chosen a group
    existing_group = get_student_group(student_id)

    if existing_group:
        print(
            f"Student {student_id} is already part of Group {existing_group}.")
    else:
        # Update the student's group in the CSV file
        update_student_group(student_id, group)
        print(f"Student {student_id} has successfully chosen Group {group}.")


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


##################################################################################################################
print("                                         WELCOME")
while True:
    menu1 = '''1.Students service
2.Control service'''
    print(menu1)
    sc = input("Please enter 1 or 2: ")

    if (sc == '1'):
        print('                            Hello to student service')
        k = 0
        while (k == 0):
            id = input('Please enter your id: ')
            p = input('Please enter your password: ')
            for i in range(student.shape[0]):
                if (p == student['pass'][i] and int(id) == student['id'][i]):
                    k = 1
                    line = i
                    print("welcome", student['name'][i])

            if (k == 0):
                print("There is wrong in pass or id please try again")
        while (True):
            menu = '''Select from 1 to 4 to select the option that you want:
            1. Register new courses.
            2. Edit courses.
            3. Choose your group.
            4. See news.
            '''
            print(menu)
            num = input("Please enter your choice: ")
            if ((num) == '1'):
                Register_course(line)
                break
            elif (num == '2'):
                edit_course(line)
                break
            elif (num == '3'):
                while (True):
                    group = input("Please select group A or B: ")
                    up = group.upper()
                    if (up == 'A' or up == 'B'):
                        choose_group(id, up)
                        break
                    else:
                        print("Invalid group, Please try again")
                break
            elif (num == '4'):
                see_news()
                break
            else:
                print("Invalid choice please try again")
        break
###########################################################################
    elif (sc == '2'):
        print('                            Hello to control service')
        conID = 1111
        password = "1234"
        while (True):
            cid = input('Please enter your id: ')
            cp = input('Please enter your password: ')
            if (conID == int(cid) and password == cp):
                break
            else:
                print("There is wrong in pass or id please try again")
        menu2 = '''Select from 1 to 7 the service that you want:
            1. Add student
            2. Remove student
            3. Edit student information
            4. Add courses
            5. Remove courses
            6. See all information of student
            7. post news '''
        print(menu2)
        while (True):
            num1 = input("Please enter the choice: ")
            if (num1 == '1'):
                name = (input("Please enter student's name: "))
                coursesId = input("Please enter courses id: ")
                gpa = float(input("Please enter student's gpa: "))
                group = input("Please enter student's group: ")
                level = int(input("Please enter student's level: "))
                passwd = input("Please enter student's password: ")
                addStd(name, coursesId, gpa, group, level, passwd)
                break
            elif (num1 == '2'):
                id = int(input("PLease enter the id that you want to remove it: "))
                removeStd(id)
                break
            elif (num1 == '3'):
                id = int(input("Please enter student's id: "))
                while (True):
                    print(
                        "Please enter do you to change group or course or Gpa or level or pass: ")
                    menu3 = '''1. If you want to change in group please select 1.
2. If you want to change in course select 2.
3. If you want to change in gpa please select 3.
4. if you want to change in level please select 4.
5. If you want to change in pass please select 5.
                '''
                    print(menu3)
                    num2 = input("Please enter the choice: ")
                    if (num2 == '1'):
                        t = 'r'
                        val = input("Enter the group name: ")
                        editStd(id, t, val)
                        break
                    elif (num2 == '2'):
                        t = 'c'
                        val = input(
                            "Enter the courses name that you want to edit it: ")
                        editStd(id, t, val)
                        break
                    elif (num2 == '3'):
                        t = 'g'
                        val = float(input("Enter the new gpa value : "))
                        editStd(id, t, val)
                        break
                    elif (num2 == '4'):
                        t = 'l'
                        val = int(input("Enter the new level: "))
                        editStd(id, t, val)
                        break
                    elif (num2 == '5'):
                        t = 'p'
                        val = input("Enter the new pass: ")
                        editStd(id, t, val)
                        break
                    else:
                        print("Invalid choice please try again")
                break
            elif (num1 == '5'):
                removed_code = input(
                    "Please enter the code of course that you want to delete it: ")
                removeCrsByCode(removed_code)
                break
            elif (num1 == '7'):
                postStr = input(
                    "please enter new post that you want to publish it")
                addPost(postStr)
                break
        break
    else:
        print("Invalid choice please try again: ")


#####################################################################
