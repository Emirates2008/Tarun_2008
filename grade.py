print("Write all grades in precentage, but dont add the precentage sign")
a = int(input("Enter your first grade"))
b = int(input("Enter your second grade"))
c = int(input("Enter your third grade"))
d = int(input("Enter your fourth  grade"))
e = int(input("Enter your fifth grade"))
t = a+b+c+d+e
print("Your total marks are " + str(t))
t1=(t*100)//500
print("You got a total percentage of " + str(t1) + "%.")
if (t1>90):
    print("You have an A grade!")
elif ((t1<90) and (t1>80)):
    print("You have an B grade!")
elif ((t1<80) and (t1>70)):
    print("You have an C grade!")
elif ((t1<70) and (t1>60)):
    print("You have an D grade!")
elif ((t1<60) and (t1>50)):
    print("You have an E grade!")
else :
    print("You have an F grade!")
