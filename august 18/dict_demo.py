import sys

b=input("Enter student name.  Use a Captial for the first letter only")
for key,value in a.items():
    if (key==b):
        print(value)
        sys.exit(0)

print("This is not a student.")
    
    