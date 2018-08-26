def charcount(filename):
    return len(open(filename).read())

print(charcount("dups.py"))

