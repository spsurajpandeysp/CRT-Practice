class TooYoung(Exception):
    def __init__(self,args):
        self.msg = args

class TooOld(Exception):
    def __init__(self,args):
        self.msg = args


age = int(input("Enter user age"))

if age>60:
    raise TooYoung("wait some time w will find best match")

elif age<18:
    raise TooOld(" you are not")
else:
    print("you are ele")