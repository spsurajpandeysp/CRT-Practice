class A:
    def __init__(self):
        self.a = 10
        print("Constructor of A")
    def fun(self):
        print("Class A Function: ",self.a)


class B(A):
    def __init__(self):
        self.a = 20
        print("Constructor of b")
    def fun(self):
        print("Class B fun",self.a)




b = B()
b.fun()