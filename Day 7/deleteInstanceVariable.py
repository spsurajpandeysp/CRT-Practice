## delete instance variable

class Python:
    def __init__(self):
        self.a =10
        self.b = 20
        self.c = 30
        self.d = 40


    def func(self):
        del self.d


ob = Python()
print(ob.__dict__)
ob.func()
print(ob.__dict__)
del ob.c
print(ob.__dict__)