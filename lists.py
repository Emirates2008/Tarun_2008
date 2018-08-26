l=[]
l.append(input("enter a name."))
l.append(input("enter a name."))
l.append(input("enter a name."))
l.append(input("enter a name."))
l.append(input("enter a name."))
c = int(input("enter how many times you want to repaet the names in the lists.")) 
l.sort()
l1=l
#print (l1*c)
l1.reverse()
i2=l
i2=i2*c
print (i2)
#list operations
for i in i2:
    print (i)
#indexing
print(i2[len(i2)-1])
i3=len(i2)
print(i2[-3])
