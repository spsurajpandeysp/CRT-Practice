import sys

class Stack:
    size = 0
    def __init__(self,size):
        Stack.size = size
        self.stack =[0]*size
        self.top=-1


    def isEmpaty(self):
        if(self.top==-1):
            return True
        
        else:
            return False
        
    def isFull(self):
        if(self.top==Stack.size-1):
            return True
        else:
            return False
        

    


    def push(self,ele):
        if self.isFull():
            print("Stack is full")
        else:
            self.top+=1
            self.stack[self.top]=ele

    def pop(self):
        if self.isEmpaty(): 
            print("Stack is empty")
        else:
            ele = self.stack[self.top]
            del self.stack[self.top]
            self.top-=1
            return ele
    

    def traverse(self):
        if self.isEmpaty(): 
            print("Stack is empty")
        else:
            l = self.stack
            for i in  range(self.top+1):
                print(self.stack[i])

    def peek(self):
        if self.isEmpaty(): 
            print("Stack is empty")
        else:
            return self.stack[self.top]






s = int(input("Enter Size of Stack: "))

st = Stack(s)


while True:
    print("1 for push: ")
    print("2 for pop: ")
    print("3 for traverse: ")
    print("4 for peek: ")
    print("0 for exit")
    n = int(input("Choose option"))

    if n ==1:
        e = int(input("Enter Elememnt: "))
        st.push(e)
    elif n==2:
        t = st.pop()
        if(t!=None):

            print("POP: ",t)
    elif n==3:
        st.traverse()

    elif n==4:
        t = st.peek()
        if(t!=None):
            print("PEEK: ",t)
    elif n==0:
        sys.exit()
    else:
        print("Enter correct option: ")

