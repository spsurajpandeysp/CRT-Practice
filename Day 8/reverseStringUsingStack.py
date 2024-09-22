import sys

class Stack:
    size = 0
    def __init__(self,size):
        Stack.size = size
        self.stack =[0]*10
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






n = int(input("Enter Size of Stack: "))

st = Stack(n)

s = input("Enter String: ")

for i in s:
    st.push(i)

ans = ""

while(st.isEmpaty()==False):
    ans+=st.pop()

print(ans)






