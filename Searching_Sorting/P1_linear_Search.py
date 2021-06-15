def linear_search(a,n):
    for i in range(len(a)):
        if a[i] == n:
            return i
    return -1 
a=[int(i) for i in input("Enter the ele with space seperation : ").strip().split()]
num = int(input("Enter the ele to be searched : "))
result = linear_search(a,num)
if result == -1:
    print("The ele is not found in the array ")
else:
    print("The ele is found in the array at index ",result)