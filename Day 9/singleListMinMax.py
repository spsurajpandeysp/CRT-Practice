class Node:
    def __init__(self):
        self.data = None
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def append(self,data):

        newNode = Node()
        newNode.data = data

        if self.head is None:
            self.head = newNode
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = newNode
        print("Data inserted successfully")

    def traverse(self):
        if self.head is None:
            print("List is empty")
            return

        ptr = self.head
        while ptr is not None:
            print(ptr.data, end=" -> ")
            ptr = ptr.next

    def insertionAtBegin(self):
        data = int(input("Enter data: "))
        newNode = Node()
        newNode.data = data

        newNode.next = self.head
        self.head = newNode
        print("Data inserted at the front successfully")

    def deletionAtBegin(self):
        if self.head is None:
            print("LinkedList is empty")
        else:
            self.head = self.head.next
            print("Data deleted from the front")

    def deletionAtEnd(self):
        if self.head is None:
            print("LinkedList is empty")
        else:
            ptr = self.head
            if ptr.next is None:  # Single element case
                self.head = None
            else:
                while ptr.next.next is not None:
                    ptr = ptr.next
                ptr.next = None
            print("Data deleted from the end")

    def deleteAny(self):
        n = int(input("Enter element you want to delete: "))
        prev = None
        ptr = self.head
        while ptr is not None:
            if ptr.data == n:
                if prev is None:
                    self.head = self.head.next
                else:
                    prev.next = ptr.next
                print(f"Element {n} deleted")
                return
            prev = ptr
            ptr = ptr.next
        print(f"Element {n} not found")

    def deleteBefore(self):
        n = int(input("Enter element to delete before: "))
        if self.head is None or self.head.data == n:
            print("Not possible to delete")
            return
        prev = None
        ptr = self.head
        while ptr.next is not None:
            if ptr.next.data == n:
                if prev is None:
                    self.head = self.head.next
                else:
                    prev.next = ptr.next
                print(f"Element before {n} deleted")
                return
            prev = ptr
            ptr = ptr.next
        print("Element not found")

    def deleteAfter(self):
        n = int(input("Enter element to delete after: "))
        ptr = self.head
        while ptr is not None:
            if ptr.data == n:
                if ptr.next is not None:
                    ptr.next = ptr.next.next
                    print(f"Element after {n} deleted")
                    return
                else:
                    print("No element exists after")
                    return
            ptr = ptr.next
        print("Element not found")

    def lengthOfList(self):
        count = 0
        ptr = self.head
        while ptr is not None:
            count += 1
            ptr = ptr.next
        print("Length of list is:", count)

    def addBefore(self):
        n = int(input("Enter element before which to add: "))
        ele = int(input("Enter new element: "))

        ptr = self.head
        prev = None
        newNode = Node()
        newNode.data = ele

        while ptr is not None:
            if ptr.data == n:
                break
            prev = ptr
            ptr = ptr.next

        if ptr is not None and ptr.data == n:
            if prev is None:
                newNode.next = self.head
                self.head = newNode
            else:
                newNode.next = prev.next
                prev.next = newNode
            print(f"Element {ele} added before {n}")
        else:
            print(f"Element {n} not found")

    def addAfter(self):
        n = int(input("Enter element after which to add: "))
        ele = int(input("Enter new element: "))

        ptr = self.head
        newNode = Node()
        newNode.data = ele

        while ptr is not None:
            if ptr.data == n:
                newNode.next = ptr.next
                ptr.next = newNode
                print(f"Element {ele} added after {n}")
                return
            ptr = ptr.next

        print(f"Element {n} not found")


    def minMax(self):
        if self.head==None:
            print("List is empty: ")

        
        mini = self.head.data
        maxi = self.head.data
        ptr = self.head
        ptr = ptr.next
        while ptr is not None:
            maxi = max(maxi,ptr.data)
            mini = min(mini,ptr.data)
            ptr = ptr.next

        print(mini,maxi)



l = [1,2,3,4,5,5]
obj = LinkList()

for i in l:
    obj.append(i)


obj.traverse()
obj.minMax()
