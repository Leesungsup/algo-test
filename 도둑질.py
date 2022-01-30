def solution(money):
    dp1 = [0] * len(money)
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])
    for i in range(2, len(money)-1):
        dp1[i] = max(dp1[i-1], money[i]+dp1[i-2])
    dp2 = [0] * len(money)
    dp2[0] = 0
    dp2[1] = money[1]
    for i in range(2, len(money)):
        dp2[i] = max(dp2[i-1], money[i]+dp2[i-2])
    return max(max(dp1), max(dp2))
def solution(money):
    answer = 0
    n=len(money)
    m=-987654321
    visited=[0]*n
    num=0
    for i in range(n):
        if i==0:
            print(visited[-1])
            if visited[-1]==0 and visited[1]==0:
                num+=money[i]
                visited[i]=1
        elif 1<=i and i<=n-2:
            if visited[i]==0 and visited[i-1]==0 and visited[i+1]==0:
                num+=money[i]
                visited[i]=1
        elif i==n-1:
            if visited[i-1]==0 and visited[0]==0:
                num+=money[i]
                visited[i]=1
    m=max(num,m)
    visited=[0]*n
    num=0
    for i in range(1,n):
        if 1<=i and i<=n-2:
            if visited[i]==0 and visited[i-1]==0 and visited[i+1]==0:
                num+=money[i]
                visited[i]=1
        if i==n-1:
            if visited[i-1]==0 and visited[0]==0:
                num+=money[i]
                visited[i]=1
    m=max(num,m)
    print(m)
    return m
solution([1, 2, 3, 1])
