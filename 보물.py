def quick(start,end,arr):
    if start>=end:
        return arr
    pivot=start
    left=start+1
    right=end
    while left<=right:
        while left<=end and arr[pivot]>=arr[left]:
            left+=1
        while right>start and arr[pivot]<=arr[right]:
            right-=1
        if left>right:
            arr[pivot],arr[right]=arr[right],arr[pivot]
        else:
            arr[left],arr[right]=arr[right],arr[left]
    quick(start,right-1,arr)
    quick(right+1,end,arr)
    return arr
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a=quick(0,len(a)-1,a)
answer=0
for i in range(len(a)):
    m=-987654321
    for j in range(len(b)):
        if m<b[j]:
            m=b[j]
    b.remove(m)
    answer+=a[i]*m
print(answer)