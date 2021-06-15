a=[]
run =True
while run:
    ch=int(input("1:append Left\n2:Append Right\n3:Pop Left\n4: Pop Right\n5:Display\nEnter your choice:"))
    if ch ==1:
        if len(a)>0:
            a.append(0)
            print(a,len(a))
            for i in range(len(a)-2,-1,-1):
                a[i+1]=a[i]
                print(i)
            print(a)
            a[0]=int(input("Enter the ele to be appended : "))
        else:
            a.append(int(input("Enter the ele to be appended : ")))
    elif ch ==2:
        a.append(int(input("Enter the ele to be appended : ")))
    elif ch ==3:
        print("The element popped is : ",a.pop(0) if len(a)>0 else "The Queue is Empty")
    elif ch ==4:
        print("The element popped is : ",a.pop() if len(a)>0 else "The Queue is Empty")
    elif ch ==5:
        print("The Dequeue is : ",a)
    else:
        print("wrong options")
        run = False