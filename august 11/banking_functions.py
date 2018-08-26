from random import *
#generate account
def generateAccountNumber(bankname):
    alpha="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphalist=list(alpha)
    shuffle(alphalist)
    a=str(randrange(100000,999999))
    print(a)
    onenum=int(a[0:1])
    twonum=int(a[1:2])
    threenum=int(a[2:3])
    fournum=int(a[3:4])
    fivenum=int(a[4:5])
    sixnum=int(a[5:6])
    b=alphalist[onenum]
    c=alphalist[twonum]
    e=alphalist[threenum]
    f=alphalist[fournum]
    g=alphalist[fivenum]
    h=alphalist[sixnum]
    d=b+c+e+f+g+h
    return(bankname+str(d).lower()+str(randrange(1000,9999)))

#getting info to check if account can be made
def Validate_Identity(name,age,phone,country):
    if (age<18):
        print("you are to young to have a bank account with WWB")
        return False
    elif(country is "NorthKorea"):
        print("You are North Korean. TATA Loser!")
        return False
    elif(age>18 and len(str(phone)) is 10):
        return True
#creating account
def Create_Account(name,age,phone,country):
    if(Validate_Identity(name,age,phone,country)):
        account_num=generateAccountNumber("WWB")
        balance_amount=0
        return [str(account_num)+":"+str(name)+":"+str(age)+":"+str(phone)+":"+str(country)+":"+str(balance_amount)]
    else:
        print("Provide Real Identity")
        return None
#Adding account info to a text file
def Input_Account_Creation():
    account_details=Create_Account(input("Your full name."),int(input("Your age.")),int(input("Your phone number.")),input("The country you are from.Use no spaces."))
    train=open("Bank Account.txt",'a')
    train.write(str(account_details)+"\n")
    train.close()
#Display Balance ammount
def display_Balance():
    #f.close()
    f=open("Bank Account.txt",'r')
    for k in f.readlines():
        #print(k)
        Account_details=k[2:len(k)-2].split(":")
        print(Account_details)
        print("balance:"+Account_details[-1][0:len(Account_details[-1])-1])
    f.close()

#making sure that you are not a crook by making you enter your bank account no.
def add_Money():
    acno=input("Enter your Account Number")
    Accounts_list=[]
    f=open("Bank Account.txt",'r')
    for k in f.readlines():
        Account_details=k[2:len(k)-3].split(":")
        Accounts_list.append(Account_details)
    f.close()
    for account in Accounts_list:
        if acno in account:
            print("Valid Account")
            money=int(input("Enter Amount to add to the account"))
            account[-1]=str(int(account[-1][0:len(account[-1])])+money)
            f=open("Bank Account.txt",'w')
    for account in Accounts_list:
        l=[str(account[0])+":"+str(account[1])+":"+str(account[2])+":"+str(account[3])+":"+str(account[4])+":"+str(account[5])]
        f.write(str(l)+"\n")
    f.close()

def Subtract_Money():
    acno=input("Enter your Account Number")
    Accounts_list=[]
    f=open("Bank Account.txt",'r')
    for k in f.readlines():
        Account_details=k[2:len(k)-3].split(":")
        Accounts_list.append(Account_details)
    f.close()
    for account in Accounts_list:
        if acno in account:
            print("Valid Account")
            money=int(input("Enter Amount to subtract to the account"))
            account[-1]=str(int(account[-1][0:len(account[-1])])-money)
    f=open("Bank Account.txt",'w')
    for account in Accounts_list:
        l=[str(account[0])+":"+str(account[1])+":"+str(account[2])+":"+str(account[3])+":"+str(account[4])+":"+str(account[5])]
        f.write(str(l)+"\n")
    f.close()

#for i in range(2):
#    Input_Account_Creation()
display_Balance()
add_Money()
display_Balance()
Subtract_Money()
display_Balance()
