a=[1,4,9,16,25,35,36,49,64,81,100,121,144]
w=[]
for elements in (a):
    if (elements%2 is 0  and a.index(elements)%2 is 0):
        w.append(elements)
print (w)
        
