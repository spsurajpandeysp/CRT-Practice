class A:
    def showA(self):
        print("Class a function")



class B(A):
    def showB(self):
        print("Class b function")

class C(A):
    def showC(self):
        print("Class c function")



class D(B,C):
    def showD(self):
        print("Class D function")

d = D()
d.showA()
d.showB()
d.showC()
d.showD()


