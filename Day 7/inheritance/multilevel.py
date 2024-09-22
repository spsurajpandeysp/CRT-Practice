class A:
    def showA(self):
        print("Class a function")



class B(A):
    def showB(self):
        print("Class b function")

class C(B):
    def showC(self):
        print("Class c function")

c = C()
c.showA()
c.showB()
c.showC()