def dups(a):
    b=[]
    for elements in a:
        if(a.count(elements)>1 and elements not in b):
            b.append(elements)
    return b
a=[1,2,3,4,3,3,2,2]
print(dups(a))
