class Outer:
    def __init__(self):
        print("Outer class cons")

    def outerFun(self):
        print("Outer fun")

    class Inner:
        def __init__(self):
            print("Inner class cons")
        def innerFun(self):
            print("Inner fun:")


outerObj = Outer()
outerObj.outerFun()
innObj = outerObj.Inner()
innObj.innerFun()
# innObj.outerFun()


obj2 = Outer().Inner()


Outer().Inner().innerFun()
