import sys
a={"Tarun":[100,100,90,80,70],"Harish":[45,100,97],"Tanush":[50,67,34]}
b=input("Enter student name.  Use a Captial for the first letter only")
for key,value in a.items():
    if (key==b):
        print(value)
        sys.exit(0)

print("This is not a student.")
    
    
