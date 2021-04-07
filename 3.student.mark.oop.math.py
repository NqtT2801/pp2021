from math import *
from numpy import *
listStudent = []
listCourse = []
listMark = []

#stuff function
def numberStudent():
    global numberStudent
    numberStudent = int(input("Enter Number of Student: "))
def numberCourse():
    global numberCourse
    numberCourse = int(input("Enter Number of Course: "))
def numberRecord():
    global numberRecord
    numberRecord = int(input("Enter Number of Record: "))
def ifExistNameStudent(name):
    for student in listStudent:
        if name == student.name:
            return True
def ifExistNameCourse(name):
    for course in listCourse:
        if name == course.name:
            return True
def averageMark(name):
    arrMark = []

    for i in range(len(listMark)):
        if name == listMark[i].studentName:
            arrMark.append(listMark[i].mark)
    arrMarkNp = array(arrMark)
    averageMark = average(arrMarkNp)
    print("Average Mark for " + name + ": " + str(averageMark))
#Class
class Student():
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
    #getter
    def getStudentInfo(self):
        print("ID student : " + self.id)
        print("Name student : " + self.name)
        print("Dob student : " + self.dob)
    #setter
    def setStudentInfo(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

class Course():
    def __init__(self, id, name):
        self.id = id
        self.name = name
    # getter
    def getCourseInfo(self):
        print("ID course: " + self.id)
        print("Name course: " + self.name)
    # setter
    def setCourseInfo(self, id, name):
        self.id = id
        self.name = name

class MarkTable():
    def __init__(self, studentName, courseName, mark):
        self.studentName = studentName
        self.courseName = courseName
        self.mark = mark

    # getter
    def getMarkInfo(self):
        print("Student Name: " + self.studentName)
        print("Course Name: " + self.courseName)
        print("Mark: " + str(self.mark))
    # setter
    def setMarkInfo(self, studentName, courseName, mark):
        self.studentName = studentName
        self.courseName = courseName
        self.mark = mark

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

#Main
index = 0
numberStudent()
createListStudent()
setStudent()
printStudentList()

print("\n")
numberCourse()
createListCourse()
setCourse()
printCourseList()

print("\n")
numberRecord()
for i in range(numberRecord):
    createListMark()
    setMark()
printMarkList()
studentAverage()



