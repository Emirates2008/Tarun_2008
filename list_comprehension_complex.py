a=[1,4,9,16,25,35,36,49,64,81,100,121,144]
w=[x for x in a if x%2 is 0 and a.index(x)%2 is 0]
print(w)

