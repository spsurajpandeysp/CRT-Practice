class Student:
    def __init__(self,name,age,percent):
        self.name = name
        self.age = age
        self.percent= percent
    def info(self):
        print("Name :",self.name)
        print("Age :",self.age)
        print("Percent :",self.percent)
    


name = input("Enter Name: ")
age = int(input("Enter age: "))
percent = float(input("Enter Percent: "))

s = Student(name,age,percent)




s.info()