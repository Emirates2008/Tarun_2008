from palindrome import *
b=[]
for i in range(1000,10000):
        b.append(i)

palindrome=[]
for element in b:
        if Areverse(element)==element:
                palindrome.append(element)
#print(palindrome)

palindrome_even=[x for x in palindrome if x%2==0]
print(palindrome_even)
#print(Areverse(100))
