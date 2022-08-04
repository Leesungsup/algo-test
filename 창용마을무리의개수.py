T=int(input())
def find(x):
    if arr[x]==x:
        return x
    arr[x]=find(arr[x])
    return arr[x]
def union(x,y):
    x=find(x)
    y=find(y)
    if x==y:
        return
    arr[x]=y
for test_case in range(1,T+1):
    n,m=map(int,input().split())
    arr=[0]*(n+1)
    for i in range(1,n+1):
        arr[i]=i
    for i in range(m):
        a,b=map(int,input().split())
        union(a,b)
    for i in range(1,n+1):
        find(i)
    d=dict()
    for i in range(1,n+1):
        if arr[i] not in d:
            d[arr[i]]=1
    print(len(d))
    print(arr)
    print("#{} {}".format(test_case,len(d)))
