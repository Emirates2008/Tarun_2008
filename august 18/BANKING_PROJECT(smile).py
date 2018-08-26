from banking_functions import *
import sys
while True:
    print("1 to create account.\n")
    print("2 to display balance.\n")
    print("3 to credit money.\n")
    print("4 to debit money.")
    print("5.Exit")
    z=int(input("Please choose an option from above"))
    if(z==1):
        Input_Account_Creation()
    elif(z==2):
        display_Balance()
    elif(z==3):
        add_Money()
    elif(z==4):
        Subtract_Money()
    elif(z==5):
        sys.exit(0);
    else:
        print("wrong choice.")


