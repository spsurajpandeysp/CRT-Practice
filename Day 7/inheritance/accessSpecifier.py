class Test1:


    def __init__(self):
        self.a=10
        self._b=20
        self.__c=30
    

    def show1(self):
        print(self.a,self._b,self.__c)

class Test2(Test1):
    def show2(self):
        print(self.a)
       # print(self._b,self.__c)

    

t = Test2()
t.show1()
t.show2()