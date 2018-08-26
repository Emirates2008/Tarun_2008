#function to add a student
def add_students():
    students=[]
    n=int(input("How many Student you want"))
    for i in range(n):
        student=[]
        #append student name
        student.append(input("Enter student name."))
        #append student age
        student.append(int(input("Enter student age.")))
        #append student teacher
        student.append(input("Enter Student's teacher"))
        #append student's info
        students.append(student)
    return students
print(add_students())
