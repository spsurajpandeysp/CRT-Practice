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

st = Queue(10)
import sys

while True:
    print("1 for push")
    print("2 for pop")
    print("3 for traverse")
    print("0 for exit")
    n = int(input("Choose option: "))

    if n == 1:
        e = int(input("Enter element: "))
        st.insert(e)
    elif n == 2:
        t = st.delete()
        if t is not None:
            print("DELETE:", t)
    elif n == 3:
        st.traverse()
    elif n == 0:
        sys.exit()
    else:
        print("Enter correct option")
