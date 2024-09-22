# local variable

class Test:
    def fun1(self):
        a = 10
        print(a)
    def fun2(self):
        b = 20
        print(b)
        # print(a)  # not accessable in fun 2 function because it is local variable of fun1

t = Test()
t.fun1()
t.fun2()