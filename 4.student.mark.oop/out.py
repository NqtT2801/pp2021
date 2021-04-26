#Create List Student
def createListStudent():
    for i in range(numberStudent):
        listStudent.append("s" + str(i))
#Input Student Info
def setStudent():
    for i in range(numberStudent):
        print("---------" + str(i+1) + "st Student" + "---------")
        id_Student = input("Enter Student ID: ")
        name_Student = input("Enter Student Name: ")
        dob_Student = input("Enter Student DoB: ")
        listStudent[i] = Student(id_Student, name_Student, dob_Student)
#Print list
def printStudentList():
    print("\n")
    print("----------The Student List---------- ")
    for i in range(numberStudent):
        print("---------" + str(i + 1) + "st Student" + "---------")
        listStudent[i].getStudentInfo()

#Create List Course
def createListCourse():
    for i in range(numberCourse):
        listCourse.append("s" + str(i))
#Input Course Info
def setCourse():
    for i in range(numberCourse):
        print("---------" + str(i+1) + "st Course" + "---------")
        id_Course = input("Enter Course ID: ")
        name_Course = input("Enter Course Name: ")
        listCourse[i] = Course(id_Course, name_Course)
#Print list
def printCourseList():
    print("\n")
    print("----------The Course List---------- ")
    for i in range(numberCourse):
        print("---------" + str(i + 1) + "st Course" + "---------")
        listCourse[i].getCourseInfo()


#Create List Mark
def createListMark():
    global checkNameStudent
    global checkNameCourse
    checkNameStudent = input("Choose Student: ")
    checkNameCourse = input("Choose Course: ")
    if (ifExistNameStudent(checkNameStudent) and ifExistNameCourse(checkNameCourse)):
        listMark.append("record" + str(index+1))
        print("Index: " + str(index))
        #print("Apeend OK")
    else:
        print("Not exist Student or Course")
#Input Course Info
def setMark():

    global index
    mark = float(input("Mark: "))
    listMark[index] = MarkTable(checkNameStudent, checkNameCourse, floor(mark))
    index += 1

#Print list
def printMarkList():
    print("\n")
    print("----------The Mark List---------- ")
    for i in range(len(listMark)):
        print("---------" + str(i + 1) + "st Record" + "---------")
        listMark[i].getMarkInfo()

#Get Student's Average
def studentAverage():
    nameTemp = input("Student Name you want to get Average: ")
    averageMark(nameTemp)
