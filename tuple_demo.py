a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
v=[]
c=[]
for elements in (a):
    if elements in ['a','e','i','o','u']:
        v.append(elements)
    else:
        c.append(elements)
v=tuple(v)
c=tuple(c)
print(v)
print(c)
