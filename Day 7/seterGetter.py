class Student:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setPercent(self,percent):
        self.percent = percent
    def getPercent(self):
        return self.percent
    

s  = Student()
n = int(input("Enter number of studenbt"))


for i in range(n):
    name= input("Enter name of student: ")
    s.setName(name)
    percent = input("Enter percent: ")
    s.setPercent(percent)

    print(s.getName(),s.getPercent())
    print()