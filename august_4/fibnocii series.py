def fibnoci(n):
    f_list=[]
    first_element=1
    second_element=1
    f_list.append(first_element)
    f_list.append(second_element)
    for i in range(n-2):
        f_list.append(f_list[-1]+f_list[-2])
    return f_list

train=open("Tarun_Fibnocii.txt",     'w')
train.write(str(fibnoci(int(input("Enter Number")))))
train.close()
