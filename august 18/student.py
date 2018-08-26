a=[[87,92,100,87,63],[45,42,13,74,100],[56,87,100,92,52],[100,100,100,100,100]]
c=int(input("Enter 0 for math ,1 for science ,2 for art ,3 for gym ,4 for music"))
a.sort(key=lambda car:car[c])
print(a)
