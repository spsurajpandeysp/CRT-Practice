class Test:
    def fun1(self):
        print("No argument")

    def fun1(self,a):
        print("1 argument pass",a)

    def fun1(self,*n):
        for i in n:
            print(i)




t = Test()
t.fun1(3,4,5,6,)