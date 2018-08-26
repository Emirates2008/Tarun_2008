def groups_of_4(a,b):
    g4=[]
    i=0
    while i<len(a):
        g4.append(a[i:i+b])
        i=i+b
    print(g4)

groups_of_4([1,2,3,4,5,6,7,8,9,10],4)
