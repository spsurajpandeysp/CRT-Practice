# 100 % abstraction

from abc import ABC,abstractmethod
class Test(ABC):
    @abstractmethod
    def m1(self):
        print("Hello4")

    @abstractmethod
    def m1(self):
        pass




class two(ABC):
    @abstractmethod
    def m1(self):
        pass

    def m2(self):
        print("Hello2")


class two(ABC):
    @abstractmethod
    def __init__():
        print("Cons")
    @abstractmethod
    def m1(self):
        pass

    def m2(self):
        print("Hello2")

class three(two):
    def __init__(self):
        print("hello cons")

    def m1(self):
        print("Hello")
t = three()

t.m1()
t.m2()