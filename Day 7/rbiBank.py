
from abc import ABC,abstractmethod

class Bank(ABC):
    st = 0
    ct = 0
    def input(self,name,age,balance):
        self.name=name
        self.age = age
        self.balance = balance

    def display(self):
        print(self.name,self.age,self.balance)
    @abstractmethod
    def deposit(self,amount):
        pass

    @abstractmethod
    def withdraw(self,amount):
        pass


class Saving(Bank):
    def withdraw(self,amount):
        if(self.balance>=amount):
            if amount<=1000:
                self.balance-=amount
            else:
                print("you can Only withdraw 1000")

        else:
            print("Not have sufficent")
    def deposit(self, amount):
        self.balance+=amount

class Current(Bank):
    def withdraw(self,amount):
        if(self.balance>=amount):
            
            if amount>=1000:
                print("No withdraw more then 100")
            else:
                self.balance-=amount
                
        else:

            print("Not have sufficent")
    def deposit(self, amount):
        self.balance+=amount


class intr1(Saving):
    def getInter(self):
        self.balance+=self.balance*0.04
        print("4 percent interest:",self.balance)
    def setInterest(self,it):
        if it<2:
            print("Enter more then 2")
        else:
            st = it



class intr2(Current):
    def getInter(self):
        self.balance+=self.balance*0.02
        print("2 percent interest:",self.balance)
    def setInterest(self,it):
        if it<4:
            print("Enter more then 2")
        else:
            ct = it

cc = intr2()
sa = intr1()


b = None

while True:
    print("1 for saving account: ")
    print("2 for current account: ")
    print("3 for set interest rate ")
    print("4 for exit: ")
    n = int(input("Select number"))

    if n==1:
        while(True):
            print("1 for input Data:")
            print("2 for Display Data:")
            print("3 for Deposit Data:")
            print("4 for Withdraw Data:")
            print("5 for check interest:")
            print("6 for exit")

            n = int(input("Choose Correct option: "))
            if(n==1):
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                balance = int(input("Enter Balance: "))
                sa.input(name,age,balance)

            elif n==2:
                sa.display()

            elif n==3:
                n = int(input("Enter Amount you wnat to deposite:"))
                sa.deposit(n)
            elif n==4:
                user = input("Enter user name: ")
                if sa.count(user):
                    user = sa.index(user)
                    n = int(input("Enter Amount you wnat to withdraw"))
                    user = sa.index(user)
                    sa[user].withdraw()
                else:
                    print("User is not present: ")
            elif n ==5:
                user = input("Enter user name: ")
                if sa.count(user):
                    user = sa.index(user)
                    sa[user].getInter()
                else:
                    print("User is not present: ")
            elif n==6:
                break
            else:
                print("Enter Correct option")
    elif n==2:
        while(True):
            print("1 for input Data:")
            print("2 for Display Data:")
            print("3 for Deposit Data:")
            print("4 for Withdraw Data:")
            print("5. for get interese")
            print("6 for exit")

            n = int(input("Choose Correct option: "))
            if(n==1):
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                balance = int(input("Enter Balance: "))
                cc.input(name,age,balance)

            elif n==2:
                cc.display()

            elif n==3:
                n = int(input("Enter Amount you wnat to deposite:"))
                cc.deposit(n)
            elif n==4:
                user = input("Enter user name: ")
                if cc.count(user):
                    user = cc.index(user)
                    n = int(input("Enter Amount you wnat to withdraw"))
                    user = cc.index(user)
                    cc[user].withdraw()
                else:
                    print("User is not present: ")
            elif n ==5:
                user = input("Enter user name: ")
                if cc.count(user):
                    user = cc.index(user)
                    cc[user].getInter()
                else:
                    print("User is not present: ")
            elif n==6:
                break
            else:
                print("Enter Correct option")

    elif n==3:
        it = int(input("Enter interest for saving Account:"))
        sa.setInterest(it)
        it = int(input("Enter interest for current Account:"))
        cc.setInterest(it)

    elif n==4:
        break
    else:
        print("Enter correct choice: ")


    