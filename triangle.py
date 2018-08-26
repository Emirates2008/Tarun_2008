print ("Please enter the sides of the triangle in numerical order")
a = float(input("Enter side 1 of triangle."))
b = float(input("Enter side 2 of triangle."))
c = float(input("Enter side 3 of triangle."))
if (a == b == c):
    print ("The triangle is equalateral")
elif (a != b != c):
    print ("The triangle is scalene")
else:
    print ("the triangle is isoceles")
