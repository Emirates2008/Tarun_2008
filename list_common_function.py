def Common_in_list(a,b):
    return c
a=int(input("How many elements do you want in list a. The elements can be numbers only."))
b=int(input("How many elements do you want in list b. The elements can be numbers only."))
c=[]
d=[]
print("elements for a")
for i in range(a):
    e=int(input("enter element"))
    c.append(i)
print("elements for b")
for x in range(b):
    f=int(input("enter element"))
    d.append(x)
g=[a.union(b)]
print(g)
