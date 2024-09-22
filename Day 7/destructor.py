## method 1


class Dest:
    def __init__(self):
        print("Const is called: ")
    def __del__(self):
        print("Dest is called: ")

    

t = Dest()


print("Application is end")





# method is called

class Dest:
    def __init__(self):
        print("Const is called: ")
    def __del__(self):
        print("Dest is called: 1")

    

t = Dest()
t1 = Dest()



print("Application is end")