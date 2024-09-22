class Queue:
    def __init__(self, size):
        self.cap = size
        self.front = 0
        self.rear = -1
        self.queue = [0] * self.cap

    def isEmpty(self):
        return self.rear == -1

    def isFull(self):
        return self.rear == self.cap - 1

    def insert(self, val):
        if self.isFull():
            print("Queue is full")
            return
        self.rear += 1
        self.queue[self.rear] = val

    def delete(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        ele = self.queue[self.front]
        for i in range(self.rear):
            self.queue[i] = self.queue[i + 1]
        self.rear -= 1
        return ele

    def traverse(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        for i in range(self.rear + 1):
            print(self.queue[i])



import sys


class Stack:
    cap = 0
    def __init__(self,size):
        Stack.cap = size
        self.stack =[0]*10
        self.top=-1


    def isEmpty(self):
        if(self.top==-1):
            return True
        else:
            return False
        
    def isFull(self):
        if(self.top==Stack.cap-1):
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
        if self.isEmpty(): 
            print("Stack is empty")
        else:
            ele = self.stack[self.top]
            del self.stack[self.top]
            self.top-=1
            return ele
    

    def traverse(self):
        if self.isEmpty(): 
            print("Stack is empty")
        else:
            l = self.stack
            for i in  range(self.top+1):
                print(self.stack[i])

    def peek(self):
        if self.isEmpty(): 
            print("Stack is empty")
        else:
            return self.stack[self.top]






st = Stack(10)

qt = Queue(10*2)

l1 = [4,3,2,1]
l2 = [8,7,6,5]


for i in l1:
    st.push(i)
for i in l2:
    qt.insert(i)

st.traverse()
print()
qt.traverse()

print()

while(st.isEmpty()==False):
    ele = st.pop()
    qt.insert(ele)

for i in range(0,len(l2)):
    ele = qt.delete()
    st.push(ele)

st.traverse()
print()
qt.traverse() 