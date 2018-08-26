a=[1,1,2,3,5,8,13,21,34,55,89]
b=[1,2,3,4,5,6,7,8,9,10,11,12,13]
c=a+b
e=[]
for elements in a:
    d=c.count(elements)
    if(d>1 and  elements not in e):
        e.append(elements)
print(e)
        
