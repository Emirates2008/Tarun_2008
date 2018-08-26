def Factorial_two(a):
    if(a==0):
        return 1
    else:
        return a*Factorial_two(a-1)

a=int(input("Enter a number."))
print(Factorial_two(a))
