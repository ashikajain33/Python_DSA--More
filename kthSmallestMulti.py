
def KthSmallestMultiple(arr,k):
    c=0
    while k>len(arr)-1:
        c+=1
        k-=len(arr)
    ans=1
    while c > 0:
        ans*=arr[k-1]
        c-=1
    return ans
n=int(input("enter array size: "))
arr=[0]*n
for i in range(n):
    arr[i]=int(input("enter the element: "))
print(arr)
k=int(input("enter the value of k: "))
print(KthSmallestMultiple(arr,k))