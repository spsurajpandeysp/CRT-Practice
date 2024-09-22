class A:
    def fun(self):
        print("Hello")
    def fun(self,a):
        if a<0:
            return a*-1
        return a




b = A()
print(b.fun(-10.2))