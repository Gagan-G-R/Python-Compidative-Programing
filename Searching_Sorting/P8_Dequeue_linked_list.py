class node():
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_List():
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0
    
    def AppendLeft(self,data):
        temp=node(data)
        if self.head == None:
            self.head = self.tail = temp
        else:
            temp.next=self.head
            self.head=temp
        self.count+=1

    def AppendRight(self,data):
        temp=node(data)
        if self.head == self.tail:
            self.head = self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp
        self.count+=1
    
    def PopLeft(self):
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head=self.head.next
        self.count-=1

    def PopRight(self):
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            temp=self.head
            while(temp.next!=self.tail):
                temp=temp.next
            temp.next =None
            self.tail=temp
        self.count-=1

    def display(self):
        temp = self.head
        while(temp!=None):
            print(temp.data,"->",end=" ")
            temp=temp.next
        print()
    
    def length(self):
        print("The no of elements in the list are : ",self.count)

def main():
    llist=Linked_List()
    endgame=False
    while(not endgame):
        ch = int(input("1:append Left\n2:Append Right\n3:Pop Left\n4:Pop Right \n5:Dispaly\n6:Length\nEnter your option : "))
        if ch == 1:
            data = int(input("Enter the ele value : "))
            llist.AppendLeft(data)
        elif ch ==2:
            data=int(input("Enter the value of the element: "))
            llist.AppendRight(data)
        elif ch ==3:
            llist.PopLeft()
        elif ch ==4:
            llist.PopRight()
        elif ch ==5:
            llist.display()
        elif ch ==6:
            llist.length()
        else:
            print("The option is invalid")
            endgame=True


if __name__ == "__main__":
    main()