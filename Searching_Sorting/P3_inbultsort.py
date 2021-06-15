a=[(1,5),(2,4),(3,3),(4,2),(5,1)]
print("Before 1st: ",a)
a.sort()
print("After Acc : ",a)
a.sort(reverse=True)
print("After Dcc : ",a)
a.sort()
print("\nBefore 2nd : ",a)

a.sort(key=lambda x:x[1],reverse=False)
print("After Dec : ",a)