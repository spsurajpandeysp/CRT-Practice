class Persion:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.dob =self.DOB(name,age)

    def show(self):
        print(self.name)
        self.dob.show()

    class DOB:
        def __init__(self,name,age):
            self.name = name
            self.age = age
        def show(self):
            print(self.name,self.age)




p = Persion("Suraj",21)
p.show()
p.dob.show()