def linecount(filename):
    return len(open(filename).readlines())

print(linecount("dups.py"))
