from collections import deque
def is_str(str1,str2):
    num1=0
    for i in range(k):
        if str1[i]!=str2[i]:
            num1+=1
    if num1==1:
        return 1
    else:
        return 0
n,k=map(int,input().split())
graph=[]
path=[[0]*(n+1) for _ in range(n+1)]
for i in range(n):
    graph.append(input())
A,B=map(int,input().split())
A-=1
B-=1
for i in range(n):
    for j in range(n):
        if i!=j and is_str(graph[i],graph[j])==1:
            path[i][j]=1
q=deque()
q.append(A)
visited=[-1]*(n+1)
num=0
print(path)
while q:
    a=q.popleft()
    print(a)
    print(visited)
    if a==B:
        num=1
        break
    for j in range(n):
        if path[a][j] == 1 and visited[j] == -1:
            q.append(j)
            visited[j]=a
arr=[]
if num==0:
    print("-1")
else:
    b=B
    while b != A:
        arr.append(b)
        b=visited[b]
    arr.append(A)
    for i in range(len(arr)-1,-1,-1):
        print(arr[i])