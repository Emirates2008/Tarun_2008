def Areverse(num):
    '''Tarun and Tanush Reverse program Areverse(num) ---> Reverse of a number'''
    reverse = 0
    while(num>0):
        quotient = num//10
        remainder = num % 10
        num = quotient
        reverse = reverse * 10 + remainder
    return reverse

k=Areverse(123)
print(k)
