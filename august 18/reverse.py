def Areverse(num):
    reverse = 0
    while(num>0):
        quotient = num//10
        remainder = num % 10
        num = quotient
        reverse1 = reverse * 10 + remainder
    return reverse1
