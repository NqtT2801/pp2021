from math import *
from numpy import *
from class import *
import in, out

listStudent = []
listCourse = []
listMark = []

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