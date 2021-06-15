a=[]
run =True
while run:
    ch=int(input("1:Appending\n2:Poping\n3:Peak\n4:Display\nEnter your choice:"))
    if ch ==1:
        a.append(int(input("Enter the ele to be appended : ")))
    elif ch ==2:
        print("The element popped is : ",a.pop())
    elif ch ==3:
        print("The ele on top of the stack is :",a[len(a)-1])
    elif ch ==4:
        print("The contents of the stack are : ",a)
    else:
        print("wrong options")
        run = False