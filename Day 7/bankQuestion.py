class Bank:
    def input(self,name,age,balance):
        self.name=name
        self.age = age
        self.balance = balance

    def display(self):
        print(self.name,self.age,self.balance)
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        self.balance-=amount

class child(Bank):
    def withdraw(self,amount):
        if(self.balance>=amount):
            self.balance-=amount
        else:
            print("Not have sufficent")



b = child()



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
        b.input(name,age,balance)

    elif n==2:
        b.display()

    elif n==3:
        n = int(input("Enter Amount you wnat to deposite:"))
        b.deposit(n)
    elif n==4:
      
        n = int(input("Enter Amount you wnat to withdraw"))
        b.withdraw(n)
    elif n==5:
        break
    else:
        print("Enter Correct option")