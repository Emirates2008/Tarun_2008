classe=[]
a=int(input("how many students do you want?"))
i=0
while(i<a):
    z=[]
    b=input("name of student")
    c=input("grade of student")
    d=input("age of student")
    e=input("teacher of student")
    z.append(b)
    z.append(c)
    z.append(d)
    z.append(e)
    classe.append(z)
    i=i+1

print(classe)
