def unique_and_not_in_list():
    a  = [1,1,3,4,6,6,7,9,10,4]
    c=[]
    d=[]
    for elements in a:
        b=a.count(elements)
        if(b>1):
            d.append(elements)
        else:
            c.append(elements)    
    print(str(c))
    print(str(d))
print(unique_and_not_in_list())
 
