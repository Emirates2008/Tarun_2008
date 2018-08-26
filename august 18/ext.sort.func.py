def ExtSort(a):
    l=[]
    for elements in a:
        f=elements.split(".")
        l.append(f)
    l.sort(key=lambda x:x[1])
    print(l)
    l1=[]
    for element in l:
        l1.append('.'.join(element))
    print(l1)
a=["happy.rtf","abcdefghijklmnopqrstuvwxyz.py", "HiImMickeyMouse.rtf", "Donald T and Kim J U news.txt"]
print(ExtSort(a))
