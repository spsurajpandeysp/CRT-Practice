
from abc import ABC,abstractmethod

class Bank(ABC):
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
            self.balance-=amount
        else:
            print("Not have sufficent")
    def deposit(self, amount):
        self.balance+=amount

class Current(Bank):
    def withdraw(self,amount):
        if(self.balance>=amount):
            self.balance-=amount
        else:
            print("Not have sufficent")
    def deposit(self, amount):
        self.balance+=amount




cc = Current()
sa = Saving()


b = None

while True:
    print("1 for saving account: ")
    print("2 for current account: ")
    print("3 for exit: ")
    n = int(input("Select number"))

    if n==1:
        while(True):
            print("1 for input Data:")
            print("2 for Display Data:")
            print("3 for Deposit Data:")
            print("4 for Withdraw Data:")
            print("5 for exit")

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
                n = int(input("Enter Amount you wnat to withdraw"))
                sa.withdraw(n)
            elif n==5:
                break
            else:
                print("Enter Correct option")
    elif n==2:
        while(True):
            print("1 for input Data:")
            print("2 for Display Data:")
            print("3 for Deposit Data:")
            print("4 for Withdraw Data:")
            print("5 for exit")

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
                n = int(input("Enter Amount you wnat to withdraw"))
                cc.withdraw(n)
            elif n==5:
                break
            else:
                print("Enter Correct option")

    elif n==3:
        break
    else:
        print("Enter correct choice: ")


    