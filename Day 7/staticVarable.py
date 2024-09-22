# static variable

class Python:
    x = 20 #static variable
    def __init__(self):
        self.y = 10 

m1 = Python()
m2 = Python()
print("m2-->",m1.x,m1.y)
print("M1-->",m2.x,m2.y)
Python.x = 111
m1.y=222
print("m2-->",m1.x,m1.y)
print("M1-->",m2.x,m2.y)

