class Node:
    def __init__(self):
        self.data = None
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def append(self):
        data = int(input("Enter data: "))
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
        


if __name__=="__main__":
    obj = LinkList()
    while True:
        print("1 for append: ")
        print("2 insertion at begin: ")
        print("3 Add before: ")
        print("4 add after")
        print("6 deletion at begin: ")
        print("7 deletion at end: ")
        print("8 delete before: ")
        print("9 delete after: ")
        print("10 delete any: ")
        print("2 Traverse: ")
        print("11 length: ")

        print("0 exit")
        n = int(input("Choose: "))

        if n==1:
            obj.append()
        elif n==2:
            obj.insertionAtBegin()
        elif n==3:
            obj.addBefore()
        elif n==4:
            obj.addAfter()
        elif n==5:
            obj.deletionAtBegin()
        elif n==6:
            obj.deletionAtEnd()
        elif n==7:
            obj.deleteBefore()
        elif n==8:
            obj.deleteAfter()
        elif n==9:
            obj.deleteAny()
        elif n==10:
            obj.travese()
        elif n==11:
            obj.lengthOfList()
        elif n==0:
            break
        else:
            print("Enter correct choise")
