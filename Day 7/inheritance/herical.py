class A:
    def showA(self):
        print("Class a function")



class B(A):
    def showB(self):
        print("Class b function")

class C(A):
    def showC(self):
        print("Class c function")

c = C()
c.showA()

c.showC()


b = B()
b.showA()

b.showB()