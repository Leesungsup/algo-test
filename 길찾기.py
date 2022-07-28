from collections import deque
for test_case in range(1,11):
    case,n=map(int,input().split())
    arr1=[100]*100
    arr2=[100]*100
    visited=[0]*100
    k=[]
    c=0
    k=list(map(int,input().split()))
    for i in range(0,n*2,2):
        if arr1[k[i]]==100:
            arr1[k[i]]=k[i+1]
        else:
            arr2[k[i]]=k[i+1]
    #print(arr1)
    #print(arr2)
    q=deque()
    q.append((0,arr1[0]))
    if arr2[0]!=100:
        q.append((0,arr2[0]))
    visited[0]=1
    while q:
        s,v=q.popleft()
        if v==99:
            c=1
            break
        if arr1[v]!=100 and visited[v]==0:
            visited[v]=1
            q.append((v,arr1[v]))
            if arr2[v]!=100:
                q.append((v,arr2[v]))
    print("#{} {}".format(case,c))