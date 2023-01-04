t=int(input())
arr=[]
def dp1(dp,n):
    for i in range(0, n):
        for j in range(0, n):
            if j==i+1:
                dp[i][j] = arr[i] + arr[j]

    for i in range(n-1, -1, -1):
        for j in range(0, n):
            if dp[i][j] == 0 and j>i:
                dp[i][j] = min([dp[i][k]+dp[k+1][j] for k in range(i,j)]) + sum(arr[i:j+1])

    print(dp[0][n-1])

for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    dp=[[-1]*n for _ in range(n)]
    print(arr)
    dp1(dp,n)