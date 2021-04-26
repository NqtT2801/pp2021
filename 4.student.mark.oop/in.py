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