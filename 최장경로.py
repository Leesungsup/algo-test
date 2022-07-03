from collections import deque

T=int(input())
def dfs(x,count):
    global sum
    check[x]=0
    if sum<count:
        sum=count
    for i in array[x]:
        if check[i]:
            print(i)
            dfs(i,count+1)
    check[x]=1

for i in range(1,T+1):
    n,m=map(int,input().split())
    array=[[] for _ in range(n+1)]
    for j in range(m):
        a,b=map(int,input().split())
        array[a].append(b)
        array[b].append(a)
    sum=1
    check=[1]*(n+1)
    for j in range(n):
        dfs(j,1)
    print("#{} {}".format(i,sum))
