a=int(input("How many numbers do you want in your list? Only ten or less numbers."))
b1=[]
b2=[]
for i in range(a):
    c=int(input("Enter number element."))
    b1.append(c)
for elements in b1:
    if (elements%2==0):
        b2.append(elements)
fname = "Even numbers.txt"
train=open(fname,'w')
train.write(str(b2))
train.close()
