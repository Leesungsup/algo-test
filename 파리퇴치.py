T=int(input())
for i in range(1,T+1):
    n,m=map(int,input().split())
    graph=[]
    ma=0
    for j in range(n):
        graph.append(list(map(int,input().split())))
    for j in range(n):
        for k in range(n):
            sum=0
            for n1 in range(m):
                for n2 in range(m):
                    if 0<=j+n1<n and 0<=k+n2<n:
                        sum+=graph[j+n1][k+n2]
            if ma<sum:
                ma=sum
    print("#{} {}".format(i,ma))
