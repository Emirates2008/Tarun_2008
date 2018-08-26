def cube_square_sec_largest_lst():
    a=[5,3,4,1,6,7,2,8,9,10]
    a.sort()
    b=a[-2]
    c=a[-3]
    h=b*b
    i=b*b*b
    j=c*c
    k=c*c*c    
    return (h,i,j,k)
print(cube_square_sec_largest_lst())
