import sys
import arithmatic
while True:
    

    print("Enter 1 for armstrong :")
    print("Enter 2 for plindrome :")
    print("Enter 3 for fact :")
    print("Enter 4 for reverse")
    print("Enter 5 for exit :")

    op = int(input("Chose option:"))

    if(op==1):
        print("Enter number for arms: ")
        n = int(input())
        print("arms is:",arithmatic.armstrong(n))
    elif(op==2):
        print("Enter number for check palin: ")
        n = int(input())
        arithmatic.palinNum(n)
    elif(op==3):
        print("Enter number for fact: ")
        n = int(input())
        print("Fact is:",arithmatic.fact(n))
    elif(op==4):
        print("Enter number for rev: ")
        n = int(input())
        print("rev is:",arithmatic.reverse(n))
    elif(op==5):
        sys.exit()
    else:
        print("Chose correct option")
