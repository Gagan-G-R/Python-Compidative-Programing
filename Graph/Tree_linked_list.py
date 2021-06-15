class node():
    def __init__(self,n):
        self.data=n
        self.left=None
        self.right=None

class Tree():
    def __init__(self):
        self.root=None

    def insert(self,num):
        
        if self.root == None:
            self.root =node(num)
        
        else:
            temp = self.root
            while(temp != None):
                print(temp.data)
                if(num > temp.data):
                    temp=temp.right
                else:
                    temp=temp.left
            temp=node(num)
            

    def in_order(self):
        temp = self.root

        def io(temp):
            if temp != None :
                io(temp.left)
                print(temp.data,end="-")
                io(temp.right)
        io(temp)
        print()


    def pre_order(self):
        temp= self.root
        def po(temp):
            if temp != None :
                print(temp.data,end="-")
                po(temp.left)
                po(temp.right)
        po(temp)
        print()


    def post_order(self):
        temp=self.root
        def pto(temp):
            if temp != None :
                pto(temp.left)
                pto(temp.right)
                print(temp.data,end="-")
        pto(temp)
        print()


def main():

    
    my_tree =Tree()
    
    while(True):
        ch = int(input("1:insert\n2:del\n3:Pre-order\n4:In-order\n5:Post-order\n6:Height\nEnter your option : "))
        
        if ch ==1:
            n = int(input("Enter the num to be added : ").strip())
            my_tree.insert(n)
        
        elif ch ==3:
            my_tree.pre_order()

        elif ch ==4:
            my_tree.in_order()

        elif ch ==5:
            my_tree.post_order()
        
        

if __name__ =="__main__":
    main()