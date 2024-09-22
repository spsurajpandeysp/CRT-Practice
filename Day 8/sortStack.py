class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [0] * size
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size - 1

    def push(self, ele):
        if self.is_full():
            print("Stack is full")
        else:
            self.top += 1
            self.stack[self.top] = ele

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            ele = self.stack[self.top]
            self.top -= 1
            return ele

    def traverse(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            for i in range(self.top + 1):
                print(self.stack[i])

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.stack[self.top]

n = int(input("Enter Size of Stack: "))

st = Stack(n)
l = [1, 4, 3, 2, 4, 2, 4]

for i in l:
    if st.is_empty() or st.peek() <= i:
        st.push(i)
    else:
        temp = Stack(n)
        while not st.is_empty() and st.peek() > i:
            temp.push(st.pop())
        st.push(i)
        while not temp.is_empty():
            st.push(temp.pop())

print("Sorted")
st.traverse()
