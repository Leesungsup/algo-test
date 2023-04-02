import sys
input=sys.stdin.readline
n,c=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(int(input()))
arr.sort()
left=1
right=arr[n-1]-arr[0]
if c==2:
    print(arr[n-1]-arr[0])
else:
    while left<right:
        mid=(left+right)//2
        count=1
        s=arr[0]
        for i in range(n):
            if arr[i]-s>=mid:
                count+=1
                s=arr[i]
        if count>=c:
            answer=mid
            left=mid+1
        elif count<c:
            right=mid
    print(answer)