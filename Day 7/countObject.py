class NewClass:
    count = 0

    def __init__(self):
        NewClass.count+=1
        self.count+=1
    
    @classmethod
    def showCountObject(cl):
        print(cl.count)


t1 = NewClass()
print(NewClass.count)
# print(t1.count)
t2 = NewClass()
print(NewClass.count)
t3 = NewClass()
t4 = NewClass()
# print(t4.count)
NewClass.showCountObject()
