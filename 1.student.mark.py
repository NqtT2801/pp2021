numberStudent = int(input("Enter number of student: "));
print("Class has:", numberStudent, "student")
studentDict = {}
def inputstudent(id, name, dob):
    studentDict[id] = [name, dob]
for i in range(numberStudent):
    print(i+1, "st Student")
    a = input("Id: ")
    b = input("Name: ")
    c = input('Dob: ')
    inputstudent(a, b, c)
#print(studentDict)

numberCourse = int(input("Enter course number: "))
print(f"There are {numberCourse} courses")
courseDict = {}
def inputCourse(id, name):
    courseDict[id] = name
for i in range(numberCourse):
    print(i+1, "st course")
    a = input("Id: ")
    b = input("Name: ")
    inputCourse(a, b)
#print(courseDict)

idForSum = input("Enter Student'Id to input Mark: ")
while True:
    if idForSum not in studentDict:
        idForSum = input("Wrong, Enter Again Student'Id: ")
    else:
        break

courseSum = input("Name of Course: ")
while True:
        if courseSum not in courseDict.values():
            courseSum = input("Wrong, Again, Name of Course: ")
        else:
            break

markSum = input("Mark: ")
sumDict = {}
def inputMark(idStudent, course, mark):
    sumDict[idStudent] = {course: mark}
inputMark(idForSum, courseSum, markSum)
#print(sumDict)

print("Now you are done with input")
print("Press 1: Show student list")
print("Press 2: Show course list")
print("Press 3: Show Mark")

choice = int(input("Select: "))
if choice == 1:
    print(studentDict)
elif choice == 2:
    print(courseDict)
elif choice == 3:
    print(sumDict)