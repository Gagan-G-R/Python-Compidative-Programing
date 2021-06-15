class node():
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList():
    def __init__(self):
        self.head= None

    def disp(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp=temp.nextw

def main():
    
    first = node(1)
    second = node(2)
    third = node(3)

    first.next=second
    second.next=third

    llist=LinkedList()
    llist.head = first

    llist.disp()

if __name__=="__main__":
    main()