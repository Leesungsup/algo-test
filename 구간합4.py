import sys
input = sys.stdin.readline

n,m=map(int,input().split())
arr=list(map(int,input().split()))
dp = [0] * (n + 1)
for i in range(n):
    dp[i + 1] = dp[i] + arr[i]
for i in range(m):
    a,b=map(int,input().split())
    print(dp[b] - dp[a - 1])



n,m=map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
sum_data = [[0] * (n+1) for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        sum_data[i][j] = sum_data[i][j-1] + sum_data[i-1][j] - sum_data[i-1][j-1] + arr[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    print(sum_data[x2][y2] - sum_data[x1-1][y2] - sum_data[x2][y1-1] + sum_data[x1-1][y1-1])