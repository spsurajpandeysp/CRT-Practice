class Node:
    def __init__(self):
        self.data = None
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def append(self,data):
    
        newNode = Node()
        newNode.data=data

        if self.head==None:
            self.head=newNode
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next=newNode
        print("Data inserted succesfully: ")
    def travese(self):
        ptr = self.head

        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next

    def insertionAtBegin(self):
        data = int(input("Enter data: "))
        newNode = Node()
        newNode.data=data

        newNode.next=self.head
        self.head=newNode
        print("DAta at front insert succ:")


    def deletionAtBegin(self):
        if self.head==None:
            print("LinkList is empty:")
        else:
            self.head = self.head.next
            print("DAta is succ deleted at front: ")


    def deletionAtEnd(self):
        if self.head==None:
            print("LinkList is empty:")

        elif self.head.next==None:
            self.head.next=None
            print("Data is succ deleted at end: ")
        else:
            ptr = self.head
            while ptr.next.next is not None:
                ptr = ptr.next
            
            ptr.next = ptr.next.next
            print("Data is succ deleted at end: ")


    def deleteAny(self):
        n = int(input("Enter elemement you want to delete: "))
        prev = None
        ptr = self.head
        while ptr is not None:
            if ptr.data==n:
                if prev==None:
                    self.head = self.head.next
                    return
            prev = ptr
            ptr = ptr.next


    def deleteBefore(self):
        n = int(input("Enter element delete before: "))
        if self.head is None and self.head.data is n:
            print("Not possible to delete: ")

            return 
        prev = None
        ptr = self.head
        while ptr.next is not None:
            if ptr.next.data==n:
                if prev==None:
                    self.head = self.head.next
                    return
                else:
                    prev.next=prev.next.next
            prev = ptr
            ptr = ptr.next
        print("element not present")

    def deleteAfter(self):
        n = int(input("Enter element delete After: "))
        ptr = self.head
        while ptr is not None:
            if ptr.data==n:
                if ptr.next is not None:
                    self.head = self.head.next
                    return
                else:
                    print("Not posible to delete: ")
                    return
            prev = ptr
            ptr = ptr.next


        print("not possible to delete: ")
                

    def lengthOfList(self):
        count = 0
        ptr = self.head
        while ptr is not None:
            count+=1
            ptr=ptr.next


        print("Length of list is: ",count)

    def addBefore(self):
        n = int(input("Enter element which before: "))
        ele  =  int(input("Etner element:"))

        ptr = self.head
        prev = None
        newNode = Node()
        while ptr is not None:
            
            if ptr.data==n:
                break
            prev =ptr
            ptr = ptr.next

        if ptr.data == n:
            if prev==None:
                
                newNode.data = ele
                newNode.next=self.head
                self.head = newNode
            else:
                newNode.next = prev.next
                prev.next=newNode

            print("data added succfully: ")

    def addAfter(self):
        n = int(input("Enter element which before: "))
        ele  =  int(input("Etner element:"))

        ptr = self.head
        newNode = Node()
        while ptr is not None:
            
            if ptr.data==n:
                break
            ptr = ptr.next

        if ptr.data == n:
            newNode.next = ptr.next
            ptr.next = newNode.next

        else:
            print("Element not present")
        


    def peek(self):
        if self.head==None:
            print("Stack is empty: ")
            return


        ptr = self.head

        while ptr.next is not None:
            ptr = ptr.next

        return ptr.data





obj = LinkList()


while True:
    print("1 for push")
    print("2 for pop")
    print("3 for traverse")
    print("0 for exit")
    n = int(input("Choose option: "))

    if n == 1:
        e = int(input("Enter element: "))
        obj.append(e)
    elif n == 2:
        obj.deletionAtBegin()
    elif n == 3:
        obj.travese()
    elif n == 0:
        break
    else:
        print("Enter correct option")

