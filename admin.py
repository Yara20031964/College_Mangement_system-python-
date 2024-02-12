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
    # getStd(<ID>,<type of information>)
    # n name
    # c courses
    # g gpa
    # r group
    # l level
    # p password
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
    # Same as getStd() But adding the value wants to be changed as a param
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


addPost("WE HAVE FINISHED THE COOOOOOODDDDDEEE")
#
#
#
#
# Marwan's code
#
# Course code valid


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
# Remove course from the courses table


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
        # print("Course not Found!!")
        return
    # return courses_list,code_list,ch_list
