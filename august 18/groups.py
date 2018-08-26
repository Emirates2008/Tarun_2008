def groups(a,b):
    groups=[]
    i=0
    while i<len(a):
        groups.append(a[i:i+b])
        i=i+b
    print(groups)

groups([1,2,3,4,5,6,7,8,9,10],3)
