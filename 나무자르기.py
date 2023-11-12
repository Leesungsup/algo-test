n,m=map(int,input().split())
arr=list(map(int,input().split()))
left=0
right=max(arr)
while left<=right:
    k=0
    mid=(left+right)//2
    for i in arr:
        if i>=mid:
            k+=(i-mid)
    if k>=m:
        answer=mid
        left=mid+1
    else:
        right=mid-1
print(answer)