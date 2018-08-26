num = int (input("Enter a number"))
reverse = 0
while(num>0):
    quotient = num//10
    remainder = num % 10
    num = quotient
    reverse = reverse * 10 + remainder
print (reverse)
