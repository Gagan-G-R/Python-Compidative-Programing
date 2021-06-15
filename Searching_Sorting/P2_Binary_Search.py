def binary_search(a,num):
    min =0
    max = len(a)
    while(min <= max):
        mid = int((min + max)/2)
        if(a[mid] == num):
            return mid
        elif(a[mid]>num):
            max=mid-1
        else:
            min=mid+1
    return -1

a=list(map(int,input("Enter the ele with space seperation : ").strip().split()))
num = int(input("Enter the ele to be found : "))

print("Before: ",a)
a.sort()
print("After : ",a)

result = binary_search(a,num)
if result ==-1:
    print("The element is not found in the array : ")
else:
    print("The ele in found in the array at index position : ",result)