class Emp:
    def __init__(self,eno,name,salary):
        self.eno = eno
        self.name = name
        self.salary = salary

    def getData(self):
        print("E no :",self.eno)
        print("E name :",self.name)
        print("E salary :",self.salary)

class Test:
    def updateInfo(self,e):
        e.salary = e.salary+2000
        e.getData() 


e = Emp(34434,"suraj",22222)

e.getData()

t = Test()
t.updateInfo(e)

