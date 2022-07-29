T=int(input())
def find(x):
    if arr[x] == x:
        return x
    arr[x] = find(arr[x])
    return arr[x]
def union(x,y):
    x=find(x)
    y=find(y)
    if x==y:
        return
    arr[x]=y
def check(x,y):
    x = find(x) #x와 y의 루트노드를 찾아준다.
    y = find(y)
    if x == y: #루드가 같다면 합칠 필요가 없으니 종료
        return 1
    else:
        return 0

for test_case in range(1,T+1):
    n,m=map(int,input().split())
    arr=[0]*(n+1)
    answer=[]
    for i in range(1,n+1):
        arr[i]=i
    for i in range(m):
        k,a,b=map(int,input().split())
        if k==0:
            union(a,b)
        elif k==1:
            c=check(a,b)
            answer.append(str(c))
    print("#",end="")
    print(test_case,end=" ")
    print(''.join(answer))
