def Prime():
    a = int(input("Enter a whole number."))
    if is_prime(a):
        print("This number is prime")
    else:
        print("This number is not prime.")
        b = Prime()
        print(b)
