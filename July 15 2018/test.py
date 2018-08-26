grade = []
for i in range(5):
    grade.append(int(input("enter a student's grade")))
print(grade)
def total_grade(grade):
    total_grade = 0
    for x in grade:
         total_grade = total_grade + x
    return total_grade        
print(total_grade(grade))
