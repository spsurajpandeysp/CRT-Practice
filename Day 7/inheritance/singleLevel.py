class A:
    def showA(self):
        print("Class a function")



class B(A):
    def showB(self):
        print("Class b function")



b = B()
b.showA()
b.showB()