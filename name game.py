l=['mark','david', 'phil', 'annie', 'maggie', 'hannah', 'gregory', 'susan', 'jake', 'jack', 'jhon', 'cecelia', 'olivia', 'emily', 'charles', 'anne']
a=input("Enter a name in all lowercase")
for i in l:
    if (a==i):
        print("you won")
        winner = 1
        break
    else:
        winner = 0
    
