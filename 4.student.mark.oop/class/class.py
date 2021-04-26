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
