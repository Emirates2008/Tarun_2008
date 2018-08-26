def wordcount(filename):
    return len(open(filename).read().split())

print(wordcount("dups.py"))
