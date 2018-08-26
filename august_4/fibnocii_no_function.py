n=int(input("Enter a number."))
f=[]
first_element=1
second_element=1
f.append(first_element)
f.append(second_element)
for i in range(n-2):
    f.append(f[-1]+f[-2])
print(f)
fname = "Tarun Fibonacci"
train=open(fname,'w')
train.write(str(f))
train.close()

