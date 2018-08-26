def isPrime(n):
    k=0
    for i in range(2,n):
        if(n%i==0):
            return 0
        else:
            k=k+1
    if(k==n-2):
        return 1
#a=int(input("enter a number"))
#isPrime(a)
#if(isPrime(a)):
#    print("prime")
#else:
#    print("not prime")
